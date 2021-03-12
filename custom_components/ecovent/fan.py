import logging

from homeassistant.components.fan import (
    SUPPORT_SET_SPEED,
    FanEntity,
    SPEED_OFF,
    SPEED_LOW,
    SPEED_MEDIUM,
    SPEED_HIGH,
    DOMAIN
    )

from homeassistant.const import (
    ATTR_ENTITY_ID
    )

import homeassistant.helpers.config_validation as cv

from . import ECOVENT_DEVICES

import voluptuous as vol

_LOGGER = logging.getLogger(__name__)


ATTR_AIRFLOW_VENT = "ventilation"
ATTR_AIRFLOW_HEATREC = "heat_recovery"
ATTR_AIRFLOW_AIRSUPP = "air_supply"
ATTR_FAN_AIRFLOW = "airflow"
ATTR_FAN_AIRFLOW_LIST = "airflow_list"

ECOVENT_FAN_DEVICES = 'ecovent_fan_devices'

SERVICE_SET_AIRFLOW = "ecovent_set_airflow"

AIRFLOW_MODES = [
    ATTR_AIRFLOW_VENT, ATTR_AIRFLOW_HEATREC, ATTR_AIRFLOW_AIRSUPP
]

SPEED_LIST = [
    SPEED_OFF, SPEED_LOW, SPEED_MEDIUM, SPEED_HIGH
]

SPEED_TO_INT = {
    SPEED_LOW: 1,
    SPEED_MEDIUM: 2,
    SPEED_HIGH: 3,
}

AIRFLOW_TO_INT = {
    ATTR_AIRFLOW_VENT: 0,
    ATTR_AIRFLOW_HEATREC: 1,
    ATTR_AIRFLOW_AIRSUPP: 2,
}

SET_AIRFLOW_SCHEMA = vol.Schema(
    {
        vol.Required(ATTR_ENTITY_ID): cv.entity_id,
        vol.Required(ATTR_FAN_AIRFLOW, default=[]):
            vol.All(cv.ensure_list, [vol.In(AIRFLOW_MODES)])
    }
)

async def async_setup_platform(
        hass, config, async_add_entities, discovery_info=None):
    """ Set up the Ecovent fan """
    if ECOVENT_FAN_DEVICES not in hass.data:
        hass.data[ECOVENT_FAN_DEVICES] = []

    for device in hass.data[ECOVENT_DEVICES]:
        hass.data[ECOVENT_FAN_DEVICES].append(EcoventFan(device))

    async_add_entities(hass.data[ECOVENT_FAN_DEVICES])

    def service_handle(service):
        """Handle the Ecovent fan set airflow service"""
        entity_id = service.data[ATTR_ENTITY_ID]
        fan_device = next(
                (fan for fan in hass.data[ECOVENT_FAN_DEVICES] if fan.entity_id == entity_id),
            None,
        )

        airflow = AIRFLOW_TO_INT[service.data.get(ATTR_FAN_AIRFLOW)[0]]
        fan_device.set_airflow(airflow)

    hass.services.async_register(
        DOMAIN, SERVICE_SET_AIRFLOW, service_handle, schema=SET_AIRFLOW_SCHEMA
    )

class EcoventFan(FanEntity):

    def __init__(self, fan):
        """Initialize the fan device."""
        self._fan = fan
        self._name = fan.name
        self._host = fan.host
        self._port = fan.port

        """Perform inital update of device status"""
        self._fan.update()

        self._fan_state = self._fan.state
        self._fan_speed = self._fan.speed
        self._fan_airflow = self._fan.airflow

    @property
    def name(self):
        """Return the name of the fan"""
        return self._fan.name

    @property
    def state(self):
        """Return the state of the fan state"""
        return self._fan.state

    @property
    def speed(self):
        """Return the fan speed"""
        return self._fan.speed

    @property
    def should_poll(self):
        """Enable polling of the device."""
        return True

    @property
    def supported_features(self):
        """Return supported features."""
        return SUPPORT_SET_SPEED

    @property
    def speed_list(self):
        """List of available fan speeds"""
        return SPEED_LIST

    @property
    def is_on(self):
        """If the fan currently is on or off"""
        if self._fan.state is not None:
            return self._fan.state
        return None

    @property
    def device_state_attributes(self):
        """Return device specific state attributes."""
        return {
            ATTR_FAN_AIRFLOW: self._fan_airflow,
            ATTR_FAN_AIRFLOW_LIST: AIRFLOW_MODES,
        }

    async def async_update(self) -> None:
        """ Get latest data from fan object"""
        self._fan.update()
        self._fan_airflow = self._fan.airflow

    async def async_turn_on(
        self,
        speed: str = None,
        percentage: str = None,
        preset_mode: str = None,
        ) -> None:

        """Turn fan on"""
        if speed is None:
            speed = self._fan.speed    

        if speed == SPEED_OFF:
            await self.async_turn_off()
        else:
            await self.async_set_speed(speed)
            self._fan.set_state_on()

    async def async_turn_off(self) -> None:
        """Turn fan off"""
        self._fan.set_state_off()

    async def async_set_speed(self, speed: str) -> None:
        """Set the speed of the fan."""
        fan_speed = SPEED_TO_INT[speed]
        self._fan.set_speed(fan_speed)

    def set_airflow(self, airflow: int) -> None:
        self._fan.set_airflow(airflow)

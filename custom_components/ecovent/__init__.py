"""Support for Ecovent Fam"""
import logging

import voluptuous as vol

from homeassistant.const import CONF_NAME, CONF_IP_ADDRESS, CONF_PORT, CONF_DEVICES
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.discovery import async_load_platform

_LOGGER = logging.getLogger(__name__)

DOMAIN = 'ecovent'
ECOVENT_DEVICES = 'ecovent_devices'

CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        vol.Required(CONF_DEVICES, default=[]): vol.All(cv.ensure_list, [dict]),
    })
},extra=vol.ALLOW_EXTRA)

async def async_setup(hass, config):
    """Set up the Ecovent Fan component."""
    from ecovent import Fan

    if ECOVENT_DEVICES not in hass.data:
        hass.data[ECOVENT_DEVICES] = []

    conf = config[DOMAIN]
    conf_devices = config[DOMAIN].get(CONF_DEVICES)
    for device in conf_devices:
        name = device.get(CONF_NAME)
        ip_address = device.get(CONF_IP_ADDRESS)

        if device.get(CONF_PORT) is None:
            port = 4000
        else:
            port = device.get(CONF_PORT)

        fan = Fan(ip_address, name, port)
        hass.data[ECOVENT_DEVICES].append(fan)

    hass.async_create_task(
        async_load_platform(hass, 'fan', DOMAIN, {CONF_NAME: DOMAIN}, config)
    )

    return True

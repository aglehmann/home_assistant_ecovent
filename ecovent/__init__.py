"""Support for Ecovent Fam"""
import logging

import voluptuous as vol

from homeassistant.const import CONF_NAME, CONF_IP_ADDRESS, CONF_PORT
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.discovery import async_load_platform

_LOGGER = logging.getLogger(__name__)

DOMAIN = 'ecovent'

CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        vol.Required(CONF_NAME): cv.string,
        vol.Required(CONF_IP_ADDRESS): cv.string,
        vol.Optional(CONF_PORT, default=4000): cv.port,
    }),
}, extra=vol.ALLOW_EXTRA)


async def async_setup(hass, config):
    """Set up the Ecovent Fan component."""
    from ecovent import Fan

    conf = config[DOMAIN]

    name = conf.get(CONF_NAME)
    ip_address = conf.get(CONF_IP_ADDRESS)
    port = conf.get(CONF_PORT)

    fan = Fan(ip_address, name, port)

    hass.data[DOMAIN] = fan

    hass.async_create_task(
        async_load_platform(hass, 'fan', DOMAIN, {CONF_NAME: DOMAIN}, config)
    )

    return True

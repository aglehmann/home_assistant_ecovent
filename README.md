# EcoVent Home Assistant Integration

[![HACS Badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/aglehmann/home_assistant_ecovent)

Home Assistant custom component for heat recovery ventilation units.
See below sections for details about 'supported' ventilation units.

## Installation

### HACS

The recommended way of installing this component is using the [Home Assistant Community Store](https://hacs.xyz).
To install the integration follow these steps:

1. Go to the HACS Settings and add the custom repository `aglehmann/home_assistant_ecovent` with category "Integration".
2. Open the "Integrations" tab and search for "EcoVent".
3. Follow the instructions on the page to set the integration up.

### Manual installation

Copy the contents of the [custom_components](custom_components) folder to the `custom_components` folder in your Home Assistant config directory.
You may need to create the `custom_components` folder if this is the first integration you're installing.
It should look something like this:

```
├── custom_components
│   └── ecovent
│       ├── __init__.py
│       ├── fan.py
│       ├── manifest.json
│       └── services.yaml
```

Follow the instructions in the [info.md](info.md) file for the configuration and usage documentation.

## Tested fans

This component has only been tested on two [Twinfresh Expert RW1-50](http://vents-us.com/item/5262/VENTS_TwinFresh_Expert_RW1-50-2_Wi-Fi/) which are configured as master/slave.

There are fans from Blauberg and Flexit that are identical and should work, but I have not verified that.

- [Single room ventilator Roomie Dual](https://www.flexit.no/en/products/single_room_ventilator/single_room_ventilator_roomie_dual/single_room_ventilator_roomie_dual/)
- [Blauberg VENTO Expert A50-1 W](https://blaubergventilatoren.de/en/product/vento-expert-a50-1-w)

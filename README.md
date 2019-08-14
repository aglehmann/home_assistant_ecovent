# Ecovent
Home Assistant custom component for heat recovery ventilation units.
See below sections for details about the ventilation unit.

## Installation
Copy the the entire ecovent folder with contents and place it under 'custom_components'.
It should look something like this:
```
├── custom_components
│   └── ecovent
│       ├── __init__.py
│       ├── fan.py
│       ├── manifest.json
│       └── services.yaml
```

Add the following to your `configuration.yaml`
```
ecovent:
  name: "The name of your fan"
  ip_address: 192.168.10.45
```

Reload Home Assistant

## Tested fans 
This component has only been tested on a single [Twinfresh Expert RW1-50](http://vents-us.com/item/5262/VENTS_TwinFresh_Expert_RW1-50-2_Wi-Fi/)

There are fans from Blauberg and Flexit that are identical and should work, but I have not verified that.
- [Single room ventilator Roomie Dual](https://www.flexit.no/en/products/single_room_ventilator/single_room_ventilator_roomie_dual/single_room_ventilator_roomie_dual/)
- [Blauberg VENTO Expert A50-1 W](https://blaubergventilatoren.de/en/product/vento-expert-a50-1-w)

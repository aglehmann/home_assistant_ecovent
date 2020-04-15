# Ecovent
Home Assistant custom component for heat recovery ventilation units.
See below sections for details about 'supported' ventilation units.

## Installation
### Fan component
Copy the the entire `ecovent` folder with contents and place it under `custom_components`.

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
  devices: 
    - name: "Basement fan"
      ip_address: 192.168.10.45

    - name: "Living room fan"
      ip_address: 192.168.10.23
```

Reload Home Assistant

### Service
The ecovent component also adds a service to control airflow modes.

Service name: `fan.ecovent_set_airflow`

This service takes to following input and allowed values:
```
entity_id: "your fan entity id"
airflow: "airflow mode"

Allowed airflow values are:
- 'ventilation'
- 'heat_recovery'
- 'air_supply'
```

Example service call yaml:
```
entity_id: fan.basement_fan
airflow: ventilation 
```

The 'airflow mode' is shown as a state attribute on the fan component and can be used in automations.

## Tested fans 
This component has only been tested on two [Twinfresh Expert RW1-50](http://vents-us.com/item/5262/VENTS_TwinFresh_Expert_RW1-50-2_Wi-Fi/) which are configured as master/slave.

There are fans from Blauberg and Flexit that are identical and should work, but I have not verified that.
- [Single room ventilator Roomie Dual](https://www.flexit.no/en/products/single_room_ventilator/single_room_ventilator_roomie_dual/single_room_ventilator_roomie_dual/)
- [Blauberg VENTO Expert A50-1 W](https://blaubergventilatoren.de/en/product/vento-expert-a50-1-w)

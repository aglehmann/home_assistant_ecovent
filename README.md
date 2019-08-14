# Ecovent
Home Assistant custom component for heat recovery fans

## Installation
Copy the the entire folder with contents and place it under 'custom_components'

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

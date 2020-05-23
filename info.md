# EcoVent

## Configuration

Add the following to your `configuration.yaml`

```yaml
ecovent:
  devices:
    - name: "Basement fan"
      ip_address: 192.168.10.45

    - name: "Living room fan"
      ip_address: 192.168.10.23
```

Reload Home Assistant

## Usage

### Services

The ecovent component also adds a service to control airflow modes.

Service name: `fan.ecovent_set_airflow`

This service accepts the following input values:

```yaml
entity_id: "your fan entity id"
airflow: "airflow mode"

Allowed airflow values are:
  - "ventilation"
  - "heat_recovery"
  - "air_supply"
```

Example service call yaml:

```yaml
entity_id: fan.basement_fan
airflow: ventilation
```

The 'airflow mode' is shown as a state attribute on the fan component and can be used in automations.

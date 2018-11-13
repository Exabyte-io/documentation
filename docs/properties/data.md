# Data

## JSON Schemas

We provide below an example of **JSON schema** [[1](#links)], a vocabulary that allows to validate JSON-based documents containing structured data, and to annotate them with descriptions. The JSON document being validated or described is called the **instance**.

The reader is referred to the documentation linked in Refs. [[2](#links)] and [[3](#links)] for an explanation of the keywords included in this example.

```json
{
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "total energy schema",
    "allOf": [
        {
            "allOf": [
                {
                    "type": "object",
                    "properties": {
                        "value": {
                            "type": "number"
                        }
                    },
                    "required": [
                        "value"
                    ]
                }
            ],
            "properties": {
                "name": {
                    "type": "string"
                },
                "units": {
                    "enum": [
                        "eV"
                    ]
                }
            },
            "required": [
                "name",
                "units"
            ]
        }
    ],
    "properties": {
        "name": {
            "enum": [
                "total_energy"
            ]
        }
    }
}
```

The "Exabyte Data Convention", introduced [in this page](../data-structured/schemas.md), contains a list of available schemas applicable to each property.

## JSON Example

Below is an example of [total energy](scalar/energies.md) instance from a calculation, which can be validated by the above schema. It consists in a scalar numerical **value**, which is expressed in **units** of electronVolts (eV).

```json
{
    "name": "total_energy",
    "value": -123.43573079,
    "units": "eV"
}
```

## Links

1. [JSON Schema, Website](http://json-schema.org/)
2. [JSON Schema Core Documentation, Website](https://json-schema.org/latest/json-schema-core.html)
3. [JSON Schema Validation Documentation, Website](https://json-schema.org/latest/json-schema-validation.html)

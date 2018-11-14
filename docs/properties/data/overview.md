# Properties Data

We make use of the "Exabyte Data Convention", introduced [in this page](../../data-structured/convention.md), to structure the information related to properties using the JSON formalism.

## JSON Schemas and Representations

We provide below an example of [**JSON schema**](../../data-structured/convention.md) for a material property. The reader is referred to the documentation linked in Refs. [[1](#links)] and [[2](#links)] for an explanation of the keywords included here. 

Attached as a separate tab is also an example of [total energy](../scalar/energies.md) JSON representation from a calculation, which can be validated by this schema. It consists in a scalar numerical **value**, which is expressed in **units** of electronVolts (eV).

```tab="Schema"
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

```tab="Example"
{
    "name": "total_energy",
    "value": -123.43573079,
    "units": "eV"
}
```

## Primitive Schema Types

Primitive schema types are defined as parent schemas that are used for constructing the JSON representations of materials properties. Primitive types are abstract and do not have physical meaning, but can hold the properties data. 

We provide a list of available primitive schema types [in this page](primitive.md).

## List of Schemas

[In this section](list.md), we offer a full list of schemas and example representations relevant for properties, which constitute a subset of those available under the general [Exabyte Data Convention](../../data-structured/convention.md).

## Links

1. [JSON Schema Core Documentation, Website](https://json-schema.org/latest/json-schema-core.html)

2. [JSON Schema Validation Documentation, Website](https://json-schema.org/latest/json-schema-validation.html)

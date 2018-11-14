# Properties Data

We make use of the data convention, introduced [in this page](../../data-structured/convention.md), to organize the information related to properties.

## JSON Schemas and Examples

We provide below an example of a [**JSON schema**](../../data-structured/convention.md) for a material property. The reader is referred to the JSON external documentation [^1] [^2] for the explanation of the primitive types and schema keywords. 

Also listed below, is an example of a JSON representation of the [total energy](../scalar/energies.md), which can validated by the schema. It consists in a scalar numerical **value**, which is expressed in **units** of electronVolts (eV).

```json tab="Schema"
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

```json tab="Example"
{
    "name": "total_energy",
    "value": -123.43573079,
    "units": "eV"
}
```

## Primitive Schema Types

In addition to the default primitive types for JSON Schemas, we construct additional types types used for constructing the representations of numeric properties specifically. Primitive types are abstract and do not have physical meaning, but can hold the data. We provide a list of available primitive schema types [in this page](primitive.md).

## List of Schemas

[In this section](list.md), we offer a full list of schemas and examples relevant for properties.

## Links

[^1]: [JSON Schema Core Documentation, Website](https://json-schema.org/latest/json-schema-core.html)

[^2]: [JSON Schema Validation Documentation, Website](https://json-schema.org/latest/json-schema-validation.html)

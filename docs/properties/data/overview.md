# Properties Data

We make use of the data convention, introduced [in this page](../../data-structured/convention.md), to organize the information related to properties.

## [JSON Schemas and Examples](../../data-structured/convention.md)

We provide below an example of a [**JSON schema**](../../data-structured/convention.md) for a material property. The reader is referred to the JSON external documentation [^1] [^2] for the explanation of the primitive types and schema keywords. 

Also listed below, is an example of a JSON representation of the [total energy](../../properties-directory/scalar/total-energy.md), which can validated by the schema. It consists in a scalar numerical **value**, which is expressed in **units** of electronVolts (eV).

<details markdown="1">
  <summary>
    Data Convention
  </summary> 

```json tab="Schema"
{!schema/material/properties/primary/total_energy.json!}
```

```json tab="Example"
{!example/material/properties/primary/total_energy.json!}
```

</details> 

## [Primitive Schema Types](primitive.md)

In addition to the default primitive types for JSON Schemas, we construct additional types types used for constructing the representations of numeric properties specifically. Primitive types are abstract and do not have physical meaning, but can hold the data. We provide a list of available primitive schema types [in this page](primitive.md).

## [List of Schemas](list.md)

[In this section](list.md), we offer a full list of schemas and examples relevant for properties. The properties relevant for each element in the Periodic Table are also listed [separately](periodic-table.md).

## Links

[^1]: [JSON Schema Core Documentation, Website](https://json-schema.org/latest/json-schema-core.html)

[^2]: [JSON Schema Validation Documentation, Website](https://json-schema.org/latest/json-schema-validation.html)

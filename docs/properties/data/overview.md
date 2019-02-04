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
{!schema/properties_directory/scalar/total_energy.json!}
```

```json tab="Example"
{!example/properties_directory/scalar/total_energy.json!}
```

</details> 

## [Core Schema Types](core.md)

In addition to the default primitive types for JSON Schemas, we construct additional types used for constructing the representations of properties. The core schemas are classified into primitive and abstract. The primitive schemas are derived from the default JSON primitives and do not have physical meaning. The abstract schemas outline the data structure of an abstract concept (e.g. a point) and are derived from the primitive schemas. We provide a list of available schema types [in this page](core.md).

## [List of Schemas](list.md)

[In this section](list.md), we offer a full list of schemas and examples relevant for properties. The properties relevant for each element in the Periodic Table are also listed [separately](periodic-table.md).

## Links

[^1]: [JSON Schema Core Documentation, Website](https://json-schema.org/latest/json-schema-core.html)

[^2]: [JSON Schema Validation Documentation, Website](https://json-schema.org/latest/json-schema-validation.html)

# Exabyte Data Convention

Our approach towards storing and organizing structured data is based on the **Exabyte Data Convention (EDC)**. We specifically use this convention to store the data and information associated with the [entities](../entities-general/overview.md) present across our platform, and with their corresponding [permissions](../entities-general/permissions.md). This is done with the aim of facilitating both the access and collaboration with regards to such entities.

The fundamental practices which lie at the core of the EDC are further elucidated in the following sections. 

## JSON Representations

We make use of the **JSON format** [^1] [^2] for storing **structured data** in the database of our platform. This structured data might for example be relevant for storing information about the [entities](../entities-general/data.md) present in the [account-owned collections](../accounts/collections.md), and for storing their respective [properties](../properties/data/overview.md).

### Example

The example included in the expandable section below shows a possible **JSON representation**, describing a material sample of silicon. Its detailed explanation can be found [here](../materials/data.md).

<details markdown="1">
  <summary>
    JSON representation
  </summary> 

```json 
{!example/material.json!}
```
</details>

## JSON Schemas

Different **schemas** are available on our platform for describing the structured data associated with the different [entities](../entities-general/data.md) and their respective [Properties](../properties/data/overview.md).
 
In computer science, a schema [^3] is a general concept referring to how structured data can be **stored** and **organized** within a database. 

**JSON schemas** [^4] [^5] in particular consist in a vocabulary that allows to **validate** JSON-based documents containing structured data, and to annotate them with **descriptions**. The JSON document being validated or described is then called the corresponding **instance**.

## Links

[^1]: [JSON specifications, Website](https://www.json.org/)

[^2]: [Wikipedia JSON, Website](https://en.wikipedia.org/wiki/JSON)

[^3]: [Introduction to Structured Data, Website](https://developers.google.com/search/docs/guides/intro-structured-data)

[^4]: [JSON Schema, Website](http://json-schema.org/)

[^5]: [Wikipedia JSON Schema, Website](https://en.wikipedia.org/wiki/JSON#Schema_and_metadata)

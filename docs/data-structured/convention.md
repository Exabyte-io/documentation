# Exabyte Data Convention

Our approach towards storing and organizing structured data is based on the **Exabyte Data Convention (EDC)**. We specifically use this convention to store the data and information associated with the [entities](../entities-general/overview.md) present across our platform, and with their corresponding [permissions](../entities-general/permissions.md). This is done with the aim of facilitating both the access and collaboration with regards to such entities.

The fundamental practices which lie at the core of the EDC are further elucidated in the following sections. 

## JSON Representations

We make use of the **JSON format** [[1,2](#links)] for storing **structured data** in the database of our platform. This structured data might for example be relevant for storing information about the [entities](../entities-general/data.md) present in the [account-owned collections](../accounts/collections.md), and for storing their respective [properties](../properties/data/overview.md).

### Example

The example included in the expandable section below shows a possible **JSON representation**, describing a material sample of silicon. Its detailed explanation can be found [here](../materials/data.md).


<details markdown="1">
  <summary>
     Expand to view
  </summary> 

```json
{
    "name" : "Silicon FCC",
    "basis" : {
        "units" : "crystal",
        "elements" : [
            {
                "id" : 1,
                "value" : "Si"
            },
            {
                "id" : 2,
                "value" : "Si"
            }
        ],
        "coordinates" : [
            {
                "id" : 1,
                "value" : [
                    0,
                    0,
                    0
                ]
            },
            {
                "id" : 2,
                "value" : [
                    0.25,
                    0.25,
                    0.25
                ]
            }
        ]
    },
    "lattice" : {
        "a" : 3.867,
        "c" : 3.867,
        "b" : 3.867,
        "units" : {
            "length" : "angstrom",
            "angle" : "degree"
        },
        "alpha" : 60,
        "type" : "FCC",
        "beta" : 60,
        "gamma" : 60,
        "vectors" : {
            "a" : [
                3.34892,
                0,
                1.9335
            ],
            "b" : [
                1.116307,
                3.157392,
                1.9335
            ],
            "c" : [
                0,
                0,
                3.867
            ],
            "alat" : 1,
            "units" : "angstrom"
        }
    },
    "formula" : "Si",
    "unitCellFormula" : "Si2",
    "tags" : [
        "silicon"
    ],
    "derivedProperties" : [
        {
            "units" : "angstrom^3",
            "name" : "volume",
            "value" : 40.88909038874689
        }
    ],
    "exabyteId" : "e3nJ9g7tLaARSA25g",
    "createdAt" : "2016-10-27T07:35:53.740Z",
    "updatedAt" : "2017-08-12T09:22:19.468Z",
    "hash" : "fa78cb87eb5c25d1661a8ba5c0654d24",
    "scaledHash" : "a4b8b020e89ff7c1c1c7b7bcf19de84e"
}
```

  </details>


## JSON Schemas

Different **schemas** are available on our platform for describing the structured data associated with the different [entities](../entities-general/data.md) and their respective [Properties](../properties/data/overview.md).
 
In computer science, a schema [[3](#links)] is a general concept referring to how structured data can be **stored** and **organized** within a database. 

**JSON schemas** [[4,5](#links)] in particular consist in a vocabulary that allows to **validate** JSON-based documents containing structured data, and to annotate them with **descriptions**. The JSON document being validated or described is then called the corresponding **instance**.

## Links

1. [JSON specifications, Website](https://www.json.org/)

2. [Wikipedia JSON, Website](https://en.wikipedia.org/wiki/JSON)

3. [Introduction to Structured Data, Website](https://developers.google.com/search/docs/guides/intro-structured-data)

4. [JSON Schema, Website](http://json-schema.org/)

5. [Wikipedia JSON Schema, Website](https://en.wikipedia.org/wiki/JSON#Schema_and_metadata)

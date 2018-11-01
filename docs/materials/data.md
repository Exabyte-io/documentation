# Structured Representation of Materials

We present an example of our approach towards storing structured data for materials. The aspects presented herein complement the [general introduction](/entities-general/data.md).

# Example Representation

In the expandable section below, the user can find an example JSON representation of a face-centered cubic Silicon: 

<details>
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


# Explanation of Keywords

| Keyword    |  Short Description      | Details        | 
| :-------- |:----------- |:------------- |
| basis   | Crystal [basis](/materials-designer/source-editor/basis.md) with explicit identification per atom  | The information about the atomic type and coordinates |
| lattice | Crystal [lattice](/materials-designer/source-editor/lattice.md) in both Bravais and vector notations  | Crystal lattice parameters - lattice constants and angles. Components of the corresponding lattice vectors are also included. |
| derivedProperties | [descriptive properties](/data-structured/overview.md#by-relation-to-workflow) derived from lattice/basis (only one example shown above) | Additional properties of the crystal structure under investigation as explained in the section ensuing the present table. |
| hash | Hash string calculated by the [Bank Mapping Function](bank.md)  |   Structure-based hash string for the primitive standard representation of this material, calculated when checking this material against existing entries within the Materials Bank |
| scaledHash | As above, but for the lattice axis scaled to 1.0 (i.e. to identify same structures under different uniform pressure) | This hash string is calculated by scaling all the dimensions of the primitive unit cell representation of the material by the $a$ lattice constant |

# Derived Properties

As seen above, we use the crystal **lattice** and **basis** JSON objects as the main [identifying properties](/data-structured/overview.md#by-relation-to-uniqueness). Based upon them, we calculate the **derivedProperties**, that may include such information as:
 
 - the unit cell volume, 
 - density, 
 - chemical formula, 
 - and a large number of other possibilities. 
 
 For every material imported/uploaded to our platform, we pre-calculate a set of such descriptors, and store them inside this "derivedProperties" section. This information can be further used during data analysis or the construction of statistical predictive models.

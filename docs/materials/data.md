# Structure-based approach

We consider **Structure-based** atomistic approach, where the information about the atomistic arrangement is known *a priori*. 

# Example Representation

Below is an example JSON representation a of FCC Silicon. We use lattice and basis as the key identifiers and derive multiple other properties from them:

```json
{
    "name" : "Silicon FCC",
    // crystal basis with explicit identification per atom
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
    // crystal lattice in both Bravais and vector notations
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
    // extra properties derived from lattice/basis (only one example property shown)
    "derivedProperties" : [
        {
            "units" : "angstrom^3",
            "name" : "volume",
            "value" : 40.88909038874689
        }
    ],
    // global id of this material inside Exabyte Database
    "exabyteId" : "e3nJ9g7tLaARSA25g",
    "createdAt" : "2016-10-27T07:35:53.740Z",
    "updatedAt" : "2017-08-12T09:22:19.468Z",
    // structure-based hash string for the primitive standard representation of this material
    "hash" : "fa78cb87eb5c25d1661a8ba5c0654d24",
    // as above, but for the primitive axis scaled to 1.0 (ie. to identify material under uniform pressure)
    "scaledHash" : "a4b8b020e89ff7c1c1c7b7bcf19de84e"
}
```

> Note: JSON does not support inclusion of inline commentaries, we only left them above for clarity.

# Properties

As seen above we use crystal **lattice** and **basis** and the main identifying properties. Based upon them we calculate **derivedProperties**, that may include unit cell volume, density, chemical formula, and a large number of other possibilities. For every material imported/uploaded to our platform we pre-calculate a set of descriptors and store them inside derivedProperties.

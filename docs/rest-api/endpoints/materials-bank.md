## Materials-bank

Materials-bank is central storage of the materials and their calculated characteristics. We keep bank items unique based on descriptive properties. `materials-bank` endpoint is accessible at [https://platform.exabyte.io/api/v1/materials-bank](https://platform.exabyte.io/api/v1/materials-bank). The following actions are supported on `materials-bank` endpoint:

### List

`GET` HTTP method is used to retrieve a list of materials-bank items.

<details>
    <summary>List all materials-bank items:</summary>
```bash
curl -X GET https://platform.exabyte.io/api/v1/materials-bank -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```
```bash
{
  "data": [
    {
      "_id": "hXFvhjYWfR2fmDFJ9",
      "access": {
        "level": 0,
        "type": 0
      },
      "basis": {
        "coordinates": [
          {
            "id": 1,
            "value": [
              0,
              0,
              0
            ]
          },
          {
            "id": 2,
            "value": [
              0.75,
              0.75,
              0.75
            ]
          }
        ],
        "elements": [
          {
            "id": 1,
            "value": "Al"
          },
          {
            "id": 2,
            "value": "P"
          }
        ],
        "name": "basis",
        "units": "crystal"
      },
      "createdAt": "2016-09-28T19:36:56.976Z",
      "derivedProperties": {
        "symmetry": {
          "spaceGroup": "F-43m"
        }
      },
      "elements": [
        "Al",
        "P"
      ],
      "formula": "PAl",
      "hash": "193f3d40f8413c8922e36f8fa354dbd3",
      "lattice": {
        "a": 3.89411623995381,
        "alpha": 59.99999999999999,
        "b": 3.89411623995381,
        "beta": 59.99999999999999,
        "c": 3.89411623995381,
        "gamma": 59.99999999999999,
        "type": "FCC",
        "units": {
          "angle": "degree",
          "length": "angstrom"
        },
        "vectors": {
          "a": [
            3.89411623995381,
            0,
            0
          ],
          "alat": 1,
          "b": [
            1.9470581199769055,
            3.3724035890895383,
            0
          ],
          "c": [
            1.9470581199769055,
            1.1241345296965128,
            3.179532595657418
          ],
          "name": "lattice vectors",
          "units": "angstrom"
        }
      },
      "nElements": 2,
      "nSites": 2,
      "name": "Al1 P1",
      "owners": [
        {
          "_id": "qSTp6ZtWCDsqQgKCk",
          "name": "mghaverty",
          "type": 0
        }
      ],
      "unitCellFormula": "PAl",
      "updatedAt": "2016-09-28T19:38:14.902Z"
    },
    {
      "_id": "hXFvhjYWfR2fmDFJ9",
      "access": {
        "level": 0,
        "type": 0
      },
      "basis": {
        "coordinates": [
          {
            "id": 1,
            "value": [
              0,
              0,
              0
            ]
          },
          {
            "id": 2,
            "value": [
              0.75,
              0.75,
              0.75
            ]
          }
        ],
        "elements": [
          {
            "id": 1,
            "value": "Al"
          },
          {
            "id": 2,
            "value": "P"
          }
        ],
        "name": "basis",
        "units": "crystal"
      },
      "createdAt": "2016-09-28T19:36:56.976Z",
      "derivedProperties": {
        "symmetry": {
          "spaceGroup": "F-43m"
        }
      },
      "elements": [
        "Al",
        "P"
      ],
      "formula": "PAl",
      "hash": "193f3d40f8413c8922e36f8fa354dbd3",
      "lattice": {
        "a": 3.89411623995381,
        "alpha": 59.99999999999999,
        "b": 3.89411623995381,
        "beta": 59.99999999999999,
        "c": 3.89411623995381,
        "gamma": 59.99999999999999,
        "type": "FCC",
        "units": {
          "angle": "degree",
          "length": "angstrom"
        },
        "vectors": {
          "a": [
            3.89411623995381,
            0,
            0
          ],
          "alat": 1,
          "b": [
            1.9470581199769055,
            3.3724035890895383,
            0
          ],
          "c": [
            1.9470581199769055,
            1.1241345296965128,
            3.179532595657418
          ],
          "name": "lattice vectors",
          "units": "angstrom"
        }
      },
      "nElements": 2,
      "nSites": 2,
      "name": "Al1 P1",
      "owners": [
        {
          "_id": "qSTp6ZtWCDsqQgKCk",
          "name": "mghaverty",
          "type": 0
        }
      ],
      "unitCellFormula": "PAl",
      "updatedAt": "2016-09-28T19:38:14.902Z"
    },
    ...
  ]
  "status": "success"
}
```
</details>

!!! tip "Number of Returned Results"
    The number of returned results are limited to 20 by default ([Results Pagination](../query-structure/#results-pagination)).

<details>
    <summary>Get material-bank item by ID:</summary>
```bash
curl -X GET https://platform.exabyte.io/api/v1/materials-bank/hXFvhjYWfR2fmDFJ9 -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```
```bash
{
  "data": {
    "_id": "hXFvhjYWfR2fmDFJ9",
    "access": {
      "level": 0,
      "type": 0
    },
    "basis": {
      "coordinates": [
        {
          "id": 1,
          "value": [
            0,
            0,
            0
          ]
        },
        {
          "id": 2,
          "value": [
            0.75,
            0.75,
            0.75
          ]
        }
      ],
      "elements": [
        {
          "id": 1,
          "value": "Al"
        },
        {
          "id": 2,
          "value": "P"
        }
      ],
      "name": "basis",
      "units": "crystal"
    },
    "createdAt": "2016-09-28T19:36:56.976Z",
    "derivedProperties": {
      "symmetry": {
        "spaceGroup": "F-43m"
      }
    },
    "elements": [
      "Al",
      "P"
    ],
    "formula": "PAl",
    "hash": "193f3d40f8413c8922e36f8fa354dbd3",
    "lattice": {
      "a": 3.89411623995381,
      "alpha": 59.99999999999999,
      "b": 3.89411623995381,
      "beta": 59.99999999999999,
      "c": 3.89411623995381,
      "gamma": 59.99999999999999,
      "type": "FCC",
      "units": {
        "angle": "degree",
        "length": "angstrom"
      },
      "vectors": {
        "a": [
          3.89411623995381,
          0,
          0
        ],
        "alat": 1,
        "b": [
          1.9470581199769055,
          3.3724035890895383,
          0
        ],
        "c": [
          1.9470581199769055,
          1.1241345296965128,
          3.179532595657418
        ],
        "name": "lattice vectors",
        "units": "angstrom"
      }
    },
    "nElements": 2,
    "nSites": 2,
    "name": "Al1 P1",
    "owners": [
      {
        "_id": "qSTp6ZtWCDsqQgKCk",
        "name": "mghaverty",
        "type": 0
      }
    ],
    "unitCellFormula": "PAl",
    "updatedAt": "2016-09-28T19:38:14.902Z"
  },
  "status": "success"
}
```
</details>

<details>
    <summary>Get material-bank by formula. The original query before encoding is `query={'formula': 'SiGe'}`:</summary>
```bash
curl -X GET https://platform.exabyte.io/api/v1/materials-bank?query%3D%7B%27formula%27%3A+%27SiGe%27%7D -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```
```bash
{
  "data": {
    "_id": "hXFvhjYWfR2fmDFJ9",
    "access": {
      "level": 0,
      "type": 0
    },
    "basis": {
      "coordinates": [
        {
          "id": 1,
          "value": [
            0,
            0,
            0
          ]
        },
        {
          "id": 2,
          "value": [
            0.75,
            0.75,
            0.75
          ]
        }
      ],
      "elements": [
        {
          "id": 1,
          "value": "Al"
        },
        {
          "id": 2,
          "value": "P"
        }
      ],
      "name": "basis",
      "units": "crystal"
    },
    "createdAt": "2016-09-28T19:36:56.976Z",
    "derivedProperties": {
      "symmetry": {
        "spaceGroup": "F-43m"
      }
    },
    "elements": [
      "Al",
      "P"
    ],
    "formula": "PAl",
    "hash": "193f3d40f8413c8922e36f8fa354dbd3",
    "lattice": {
      "a": 3.89411623995381,
      "alpha": 59.99999999999999,
      "b": 3.89411623995381,
      "beta": 59.99999999999999,
      "c": 3.89411623995381,
      "gamma": 59.99999999999999,
      "type": "FCC",
      "units": {
        "angle": "degree",
        "length": "angstrom"
      },
      "vectors": {
        "a": [
          3.89411623995381,
          0,
          0
        ],
        "alat": 1,
        "b": [
          1.9470581199769055,
          3.3724035890895383,
          0
        ],
        "c": [
          1.9470581199769055,
          1.1241345296965128,
          3.179532595657418
        ],
        "name": "lattice vectors",
        "units": "angstrom"
      }
    },
    "nElements": 2,
    "nSites": 2,
    "name": "Al1 P1",
    "owners": [
      {
        "_id": "qSTp6ZtWCDsqQgKCk",
        "name": "mghaverty",
        "type": 0
      }
    ],
    "unitCellFormula": "PAl",
    "updatedAt": "2016-09-28T19:38:14.902Z"
  },
  "status": "success"
}
```
</details>

The returned materials do not contain material's characteristics by default, as we store characteristics inside a separate collection. Although characteristics can be queried separately via `characteristics` endpoint, you can use `includeCharacteristics` parameter to get material's characteristics with one call to the REST API.

<details>
    <summary>Get material-bank item with characteristics:</summary>
```bash
curl -X GET https://platform.exabyte.io/api/v1/materials-bank/KuAsBRwofzGfHPWiT?includeCharacteristics=true -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```
```bash
{
  "data": {
    "_id": "hXFvhjYWfR2fmDFJ9",
    "access": {
      "level": 0,
      "type": 0
    },
    "basis": {
      "coordinates": [
        {
          "id": 1,
          "value": [
            0,
            0,
            0
          ]
        },
        {
          "id": 2,
          "value": [
            0.75,
            0.75,
            0.75
          ]
        }
      ],
      "elements": [
        {
          "id": 1,
          "value": "Al"
        },
        {
          "id": 2,
          "value": "P"
        }
      ],
      "name": "basis",
      "units": "crystal"
    },
    "characteristics": [
      {
        "_id": "SrYEjcjKqR5ntFrD4",
        "access": {
          "level": 10,
          "type": 0
        },
        "data": {
          "name": "band_gaps",
          "values": [
            {
              "kpointConduction": [
                0,
                0,
                0
              ],
              "kpointValence": [
                0,
                0,
                0
              ],
              "type": "direct",
              "units": "eV",
              "value": 3.0728999999999997
            },
            {
              "kpointConduction": [
                0.42857143,
                0.42857143,
                0
              ],
              "kpointValence": [
                0,
                0,
                0
              ],
              "type": "indirect",
              "units": "eV",
              "value": 1.7463999999999995
            }
          ]
        },
        "exabyteId": "hXFvhjYWfR2fmDFJ9",
        "owner": {
          "_id": "qSTp6ZtWCDsqQgKCk",
          "name": "mghaverty",
          "type": 0
        },
        "source": {
          "info": {
            "_id": "3e8RFbHmZ8gop3F32",
            "_project": {
              "_id": "sHJEAwXe9S8jrmxGP",
              "access": {
                "level": 10,
                "type": 0
              },
              "goldName": "mghaverty",
              "name": "mghaverty",
              "owner": {
                "_id": "qSTp6ZtWCDsqQgKCk",
                "name": "mghaverty",
                "type": 0
              },
              "slug": "mghaverty"
            },
            "model": {
              "method": {
                "subtype": "us",
                "type": "pseudo",
                "workflow": {
                  "app": "vasp"
                }
              },
              "subtype": "GGA",
              "type": "DFT"
            },
            "owner": {
              "_id": "qSTp6ZtWCDsqQgKCk",
              "name": "mghaverty",
              "type": 0
            },
            "title": "AlP Density of States"
          },
          "type": "exabyte"
        }
      }
    ],
    "createdAt": "2016-09-28T19:36:56.976Z",
    "derivedProperties": {
      "symmetry": {
        "spaceGroup": "F-43m"
      }
    },
    "elements": [
      "Al",
      "P"
    ],
    "formula": "PAl",
    "hash": "193f3d40f8413c8922e36f8fa354dbd3",
    "lattice": {
      "a": 3.89411623995381,
      "alpha": 59.99999999999999,
      "b": 3.89411623995381,
      "beta": 59.99999999999999,
      "c": 3.89411623995381,
      "gamma": 59.99999999999999,
      "type": "FCC",
      "units": {
        "angle": "degree",
        "length": "angstrom"
      },
      "vectors": {
        "a": [
          3.89411623995381,
          0,
          0
        ],
        "alat": 1,
        "b": [
          1.9470581199769055,
          3.3724035890895383,
          0
        ],
        "c": [
          1.9470581199769055,
          1.1241345296965128,
          3.179532595657418
        ],
        "name": "lattice vectors",
        "units": "angstrom"
      }
    },
    "nElements": 2,
    "nSites": 2,
    "name": "Al1 P1",
    "owners": [
      {
        "_id": "qSTp6ZtWCDsqQgKCk",
        "name": "mghaverty",
        "type": 0
      }
    ],
    "unitCellFormula": "PAl",
    "updatedAt": "2016-09-28T19:38:14.902Z"
  },
  "status": "success"
}
```
</details>

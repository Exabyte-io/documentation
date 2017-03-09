<!-- by MM -->

## Materials

Materials are accessible via `materials` endpoint. Materials are not unique. There could be situation, when different users have identical materials. All materials are stored inside materials collection while a copy of unique materials are stored inside a separate collection called materials-bank. `materials` endpoint is accessible at [https://platform.exabyte.io/api/v1/materials](https://platform.exabyte.io/api/v1/materials). The following actions are supported on `materials` endpoint:

### List

`GET` HTTP method is used to retrieve a list of materials.

<details>
  <summary>List all materials:</summary>
```bash
curl -X GET https://platform.exabyte.io/api/v1/materials -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```
```bash
{
  "data": [
    {
      "_id": "KuAsBRwofzGfHPWiT",
      "access": {
        "level": 20,
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
              0.25,
              0.25,
              0.25
            ]
          }
        ],
        "elements": [
          {
            "id": 1,
            "value": "Si"
          },
          {
            "id": 2,
            "value": "Ge"
          }
        ],
        "name": "basis",
        "units": "crystal"
      },
      "createdAt": "2016-10-29T03:44:21.162Z",
      "derivedProperties": {
        "symmetry": {
          "spaceGroup": "F-43m"
        }
      },
      "editable": false,
      "elements": [
        "Si",
        "Ge"
      ],
      "exabyteId": "tnnXu2d3pkWf9Ypc3",
      "formula": "SiGe",
      "hash": "72ac9a1f4b487390c88673c2358c8930",
      "lattice": {
        "a": 3.867,
        "alpha": 60,
        "b": 3.867,
        "beta": 60,
        "c": 3.867,
        "gamma": 60,
        "type": "FCC",
        "units": {
          "angle": "degree",
          "length": "angstrom"
        },
        "vectors": {
          "a": [
            3.867,
            0,
            0
          ],
          "alat": 1,
          "b": [
            1.9335000000000004,
            3.3489202364344242,
            0
          ],
          "c": [
            1.9335000000000004,
            1.1163067454781415,
            3.1573922784475164
          ],
          "name": "lattice vectors",
          "units": "angstrom"
        }
      },
      "mainDep": {
        "_dependentsById": {}
      },
      "nElements": 2,
      "nSites": 2,
      "name": "Silicon FCC",
      "owner": {
        "_id": "jnLJpf9vJKYtFoQxc",
        "name": "exadmin",
        "type": 0
      },
      "tags": [],
      "unitCellFormula": "SiGe",
      "updatedAt": "2016-10-29T03:44:40.994Z"
    },
    {
      "_id": "KuAsBRwofzGfHPWiT",
      "access": {
        "level": 20,
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
              0.25,
              0.25,
              0.25
            ]
          }
        ],
        "elements": [
          {
            "id": 1,
            "value": "Si"
          },
          {
            "id": 2,
            "value": "Ge"
          }
        ],
        "name": "basis",
        "units": "crystal"
      },
      "createdAt": "2016-10-29T03:44:21.162Z",
      "derivedProperties": {
        "symmetry": {
          "spaceGroup": "F-43m"
        }
      },
      "editable": false,
      "elements": [
        "Si",
        "Ge"
      ],
      "exabyteId": "tnnXu2d3pkWf9Ypc3",
      "formula": "SiGe",
      "hash": "72ac9a1f4b487390c88673c2358c8930",
      "lattice": {
        "a": 3.867,
        "alpha": 60,
        "b": 3.867,
        "beta": 60,
        "c": 3.867,
        "gamma": 60,
        "type": "FCC",
        "units": {
          "angle": "degree",
          "length": "angstrom"
        },
        "vectors": {
          "a": [
            3.867,
            0,
            0
          ],
          "alat": 1,
          "b": [
            1.9335000000000004,
            3.3489202364344242,
            0
          ],
          "c": [
            1.9335000000000004,
            1.1163067454781415,
            3.1573922784475164
          ],
          "name": "lattice vectors",
          "units": "angstrom"
        }
      },
      "mainDep": {
        "_dependentsById": {}
      },
      "nElements": 2,
      "nSites": 2,
      "name": "Silicon FCC",
      "owner": {
        "_id": "jnLJpf9vJKYtFoQxc",
        "name": "exadmin",
        "type": 0
      },
      "tags": [],
      "unitCellFormula": "SiGe",
      "updatedAt": "2016-10-29T03:44:40.994Z"
    },
    ...
  ],
  "status": "success"
}
```
</details>

!!! tip "Number of Returned Results"
    The number of returned results are limited to 20 by default ([Results Pagination](../query-structure/#results-pagination)).

<details>
    <summary>Get material by ID:</summary>
```bash
curl -X GET https://platform.exabyte.io/api/v1/materials/KuAsBRwofzGfHPWiT -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```
```bash
{
  "data": {
    "_id": "KuAsBRwofzGfHPWiT",
    "access": {
      "level": 20,
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
            0.25,
            0.25,
            0.25
          ]
        }
      ],
      "elements": [
        {
          "id": 1,
          "value": "Si"
        },
        {
          "id": 2,
          "value": "Ge"
        }
      ],
      "name": "basis",
      "units": "crystal"
    },
    "createdAt": "2016-10-29T03:44:21.162Z",
    "derivedProperties": {
      "symmetry": {
        "spaceGroup": "F-43m"
      }
    },
    "editable": false,
    "elements": [
      "Si",
      "Ge"
    ],
    "exabyteId": "tnnXu2d3pkWf9Ypc3",
    "formula": "SiGe",
    "hash": "72ac9a1f4b487390c88673c2358c8930",
    "lattice": {
      "a": 3.867,
      "alpha": 60,
      "b": 3.867,
      "beta": 60,
      "c": 3.867,
      "gamma": 60,
      "type": "FCC",
      "units": {
        "angle": "degree",
        "length": "angstrom"
      },
      "vectors": {
        "a": [
          3.867,
          0,
          0
        ],
        "alat": 1,
        "b": [
          1.9335000000000004,
          3.3489202364344242,
          0
        ],
        "c": [
          1.9335000000000004,
          1.1163067454781415,
          3.1573922784475164
        ],
        "name": "lattice vectors",
        "units": "angstrom"
      }
    },
    "mainDep": {
      "_dependentsById": {}
    },
    "nElements": 2,
    "nSites": 2,
    "name": "Silicon FCC",
    "owner": {
      "_id": "jnLJpf9vJKYtFoQxc",
      "name": "exadmin",
      "type": 0
    },
    "tags": [],
    "unitCellFormula": "SiGe",
    "updatedAt": "2016-10-29T03:44:40.994Z"
  },
  "status": "success"
}
```
</details>

<details>
    <summary>Get material by formula. The original query before encoding is `query={'formula': 'SiGe'}`:</summary>
```bash
curl -X GET https://platform.exabyte.io/api/v1/materials?query%3D%7B%27formula%27%3A+%27SiGe%27%7D -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```
```bash
{
  "data": [
    {
      "_id": "KuAsBRwofzGfHPWiT",
      "access": {
        "level": 20,
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
              0.25,
              0.25,
              0.25
            ]
          }
        ],
        "elements": [
          {
            "id": 1,
            "value": "Si"
          },
          {
            "id": 2,
            "value": "Ge"
          }
        ],
        "name": "basis",
        "units": "crystal"
      },
      "createdAt": "2016-10-29T03:44:21.162Z",
      "derivedProperties": {
        "symmetry": {
          "spaceGroup": "F-43m"
        }
      },
      "editable": false,
      "elements": [
        "Si",
        "Ge"
      ],
      "exabyteId": "tnnXu2d3pkWf9Ypc3",
      "formula": "SiGe",
      "hash": "72ac9a1f4b487390c88673c2358c8930",
      "lattice": {
        "a": 3.867,
        "alpha": 60,
        "b": 3.867,
        "beta": 60,
        "c": 3.867,
        "gamma": 60,
        "type": "FCC",
        "units": {
          "angle": "degree",
          "length": "angstrom"
        },
        "vectors": {
          "a": [
            3.867,
            0,
            0
          ],
          "alat": 1,
          "b": [
            1.9335000000000004,
            3.3489202364344242,
            0
          ],
          "c": [
            1.9335000000000004,
            1.1163067454781415,
            3.1573922784475164
          ],
          "name": "lattice vectors",
          "units": "angstrom"
        }
      },
      "mainDep": {
        "_dependentsById": {}
      },
      "nElements": 2,
      "nSites": 2,
      "name": "Silicon FCC",
      "owner": {
        "_id": "jnLJpf9vJKYtFoQxc",
        "name": "exadmin",
        "type": 0
      },
      "tags": [],
      "unitCellFormula": "SiGe",
      "updatedAt": "2016-10-29T03:44:40.994Z"
    },
    ...
  ],
  "status": "success"
}
```
</details>

<details>
    <summary>Get material by a property. The original query before encoding is `query={'derivedProperties.symmetry.spaceGroup': 'F-43m'}`:</summary>
```bash
curl -X GET https://platform.exabyte.io/api/v1/materials?query%3D%7B%27derivedProperties.symmetry.spaceGroup%27%3A+%27F-43m%27%7D -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```
```bash
{
  "data": [
    {
      "_id": "KuAsBRwofzGfHPWiT",
      "access": {
        "level": 20,
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
              0.25,
              0.25,
              0.25
            ]
          }
        ],
        "elements": [
          {
            "id": 1,
            "value": "Si"
          },
          {
            "id": 2,
            "value": "Ge"
          }
        ],
        "name": "basis",
        "units": "crystal"
      },
      "createdAt": "2016-10-29T03:44:21.162Z",
      "derivedProperties": {
        "symmetry": {
          "spaceGroup": "F-43m"
        }
      },
      "editable": false,
      "elements": [
        "Si",
        "Ge"
      ],
      "exabyteId": "tnnXu2d3pkWf9Ypc3",
      "formula": "SiGe",
      "hash": "72ac9a1f4b487390c88673c2358c8930",
      "lattice": {
        "a": 3.867,
        "alpha": 60,
        "b": 3.867,
        "beta": 60,
        "c": 3.867,
        "gamma": 60,
        "type": "FCC",
        "units": {
          "angle": "degree",
          "length": "angstrom"
        },
        "vectors": {
          "a": [
            3.867,
            0,
            0
          ],
          "alat": 1,
          "b": [
            1.9335000000000004,
            3.3489202364344242,
            0
          ],
          "c": [
            1.9335000000000004,
            1.1163067454781415,
            3.1573922784475164
          ],
          "name": "lattice vectors",
          "units": "angstrom"
        }
      },
      "mainDep": {
        "_dependentsById": {}
      },
      "nElements": 2,
      "nSites": 2,
      "name": "Silicon FCC",
      "owner": {
        "_id": "jnLJpf9vJKYtFoQxc",
        "name": "exadmin",
        "type": 0
      },
      "tags": [],
      "unitCellFormula": "SiGe",
      "updatedAt": "2016-10-29T03:44:40.994Z"
    },
    ...
  ],
  "status": "success"
}

```
</details>

The returned materials do not contain material's characteristics by default, as we store characteristics inside a separate collection. Although characteristics can be queried separately via `characteristics` endpoint, you can use `includeCharacteristics` parameter to get material's characteristics with one call to the REST API.

<details>
    <summary>Get material with characteristics:</summary>
```bash
curl -X GET https://platform.exabyte.io/api/v1/materials/KuAsBRwofzGfHPWiT?includeCharacteristics=true -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```
```bash
{
  "data": {
    "_id": "KuAsBRwofzGfHPWiT",
    "access": {
      "level": 20,
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
            0.25,
            0.25,
            0.25
          ]
        }
      ],
      "elements": [
        {
          "id": 1,
          "value": "Si"
        },
        {
          "id": 2,
          "value": "Ge"
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
        "exabyteId": "tnnXu2d3pkWf9Ypc3",
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
    "createdAt": "2016-10-29T03:44:21.162Z",
    "derivedProperties": {
      "symmetry": {
        "spaceGroup": "F-43m"
      }
    },
    "editable": false,
    "elements": [
      "Si",
      "Ge"
    ],
    "exabyteId": "tnnXu2d3pkWf9Ypc3",
    "formula": "SiGe",
    "hash": "72ac9a1f4b487390c88673c2358c8930",
    "lattice": {
      "a": 3.867,
      "alpha": 60,
      "b": 3.867,
      "beta": 60,
      "c": 3.867,
      "gamma": 60,
      "type": "FCC",
      "units": {
        "angle": "degree",
        "length": "angstrom"
      },
      "vectors": {
        "a": [
          3.867,
          0,
          0
        ],
        "alat": 1,
        "b": [
          1.9335000000000004,
          3.3489202364344242,
          0
        ],
        "c": [
          1.9335000000000004,
          1.1163067454781415,
          3.1573922784475164
        ],
        "name": "lattice vectors",
        "units": "angstrom"
      }
    },
    "mainDep": {
      "_dependentsById": {}
    },
    "nElements": 2,
    "nSites": 2,
    "name": "Silicon FCC",
    "owner": {
      "_id": "jnLJpf9vJKYtFoQxc",
      "name": "exadmin",
      "type": 0
    },
    "tags": [],
    "unitCellFormula": "SiGe",
    "updatedAt": "2016-10-29T03:44:40.994Z"
  },
  "status": "success"
}
```
</details>

### Create

`POST` HTTP method is used to create a new material. New material is passed in JSON format inside body.

<details>
    <summary>Create a new material:</summary>
```bash
curl -X POST https://platform.exabyte.io/api/v1/materials -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ" -d '
{
  "access": {
    "level": 20,
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
          0.25,
          0.25,
          0.25
        ]
      }
    ],
    "elements": [
      {
        "id": 1,
        "value": "Si"
      },
      {
        "id": 2,
        "value": "Ge"
      }
    ],
    "name": "basis",
    "units": "crystal"
  },
  "lattice": {
    "a": 3.867,
    "alpha": 60,
    "b": 3.867,
    "beta": 60,
    "c": 3.867,
    "gamma": 60,
    "type": "FCC",
    "units": {
      "angle": "degree",
      "length": "angstrom"
    }
  },
  "name": "Silicon FCC",
  "tags": []
}'
```
```bash
{
  "status": "success",
  "data": {
    "_id": "ZPjWNWWmt8hnWAm6e",
    "access": {
      "level": 20,
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
            0.25,
            0.25,
            0.25
          ]
        }
      ],
      "elements": [
        {
          "id": 1,
          "value": "Si"
        },
        {
          "id": 2,
          "value": "Ge"
        }
      ],
      "name": "basis",
      "units": "crystal"
    },
    "lattice": {
      "a": 3.867,
      "alpha": 60,
      "b": 3.867,
      "beta": 60,
      "c": 3.867,
      "gamma": 60,
      "type": "FCC",
      "units": {
        "angle": "degree",
        "length": "angstrom"
      },
      "vectors": {
        "a": [
          3.34892,
          0,
          1.9335
        ],
        "b": [
          1.116307,
          3.157392,
          1.9335
        ],
        "c": [
          0,
          0,
          3.867
        ],
        "name": "lattice vectors",
        "alat": 1,
        "units": "angstrom"
      }
    },
    "name": "Silicon FCC",
    "tags": [],
    "owner": {
      "_id": "jnLJpf9vJKYtFoQxc",
      "name": "exadmin",
      "type": 0
    },
    "derivedProperties": {
      "symmetry": {
        "spaceGroup": "F-43m"
      }
    },
    "exabyteId": "CmYpGiuTZQdcaCdRp",
    "hash": "72ac9a1f4b487390c88673c2358c8930",
    "formula": "SiGe",
    "unitCellFormula": "SiGe",
    "nSites": 2,
    "elements": [
      "Si",
      "Ge"
    ],
    "nElements": 2,
    "editable": true,
    "createdAt": "2017-03-09T14:17:12.061Z"
  }
}
```
</details>

### Delete

`DELETE` HTTP method is used to delete a material with a given ID.

<details>
    <summary>Delete a material:</summary>
```bash
curl -X DELETE https://platform.exabyte.io/api/v1/materials/ZPjWNWWmt8hnWAm6e"
```
```bash
{
  "status": "success",
  "data": {
    "message": "Material ZPjWNWWmt8hnWAm6e successfully deleted"
  }
}
```
</details>


### Update

`PATCH` HTTP method is used to update an existing material. New material's properties are passed in JSON inside body.

<details>
    <summary>Create a new material:</summary>
```bash
curl -X PATCH https://platform.exabyte.io/api/v1/materials/KuAsBRwofzGfHPWiT -d '{"name": "Silicon FCC"}'
```
```bash
{
  "_id": "KuAsBRwofzGfHPWiT",
  "access": {
    "level": 20,
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
          0.25,
          0.25,
          0.25
        ]
      }
    ],
    "elements": [
      {
        "id": 1,
        "value": "Si"
      },
      {
        "id": 2,
        "value": "Ge"
      }
    ],
    "name": "basis",
    "units": "crystal"
  },
  "createdAt": "2016-10-29T03:44:21.162Z",
  "derivedProperties": {
    "symmetry": {
      "spaceGroup": "F-43m"
    }
  },
  "editable": false,
  "elements": [
    "Si",
    "Ge"
  ],
  "exabyteId": "tnnXu2d3pkWf9Ypc3",
  "formula": "SiGe",
  "hash": "72ac9a1f4b487390c88673c2358c8930",
  "lattice": {
    "a": 3.867,
    "alpha": 60,
    "b": 3.867,
    "beta": 60,
    "c": 3.867,
    "gamma": 60,
    "type": "FCC",
    "units": {
      "angle": "degree",
      "length": "angstrom"
    },
    "vectors": {
      "a": [
        3.867,
        0,
        0
      ],
      "alat": 1,
      "b": [
        1.9335000000000004,
        3.3489202364344242,
        0
      ],
      "c": [
        1.9335000000000004,
        1.1163067454781415,
        3.1573922784475164
      ],
      "name": "lattice vectors",
      "units": "angstrom"
    }
  },
  "mainDep": {
    "_dependentsById": {}
  },
  "nElements": 2,
  "nSites": 2,
  "name": "Silicon FCC",
  "owner": {
    "_id": "jnLJpf9vJKYtFoQxc",
    "name": "exadmin",
    "type": 0
  },
  "tags": [],
  "unitCellFormula": "SiGe",
  "updatedAt": "2016-10-29T03:44:40.994Z"
}
```
</details>


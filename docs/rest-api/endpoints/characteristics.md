## Characteristics

Every material can be characterized according to its many physical properties. Characteristic data contains parameters that reflect on physical properties of materials. `characteristics` endpoint is accessible at [https://platform.exabyte.io/api/v1/characteristics](https://platform.exabyte.io/api/v1/characteristics). The following actions are supported on `characteristics` endpoint:


### List

`GET` HTTP method is used to retrieve a list of characteristics.

<details>
    <summary>List all characteristics:</summary>
```bash
curl -X GET https://platform.exabyte.io/api/v1/characteristics -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```
```bash
{
  "data": [
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
    },
    {
      "_id": "AstEjcowqR5ntFrD4",
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
    <summary>Get characteristic by ID:</summary>
```bash
curl -X GET https://platform.exabyte.io/api/v1/characteristics/SrYEjcjKqR5ntFrD4 -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```
```bash
{
  "data": {
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
  },
  "status": "success"
}
```
</details>

<details>
    <summary>Get characteristic by a property. The original query before encoding is `query={'data.name': 'band_gaps'}`</summary>
```bash
curl -X GET https://platform.exabyte.io/api/v1/characteristics?query=query%3D%7B%27data.name%27%3A+%27band_gaps%27%7D -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```
```bash
{
  "data": [
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
    },
    ...
  ]
  "status": "success"
}
```
</details>

<!-- by MM -->

## Materials

Materials are accessible via `materials` endpoint. Materials are not unique. There could be situation, when different users have identical materials. All materials are stored inside materials collection while a copy of unique materials are stored inside a separate collection called materials-bank. `materials` endpoint is accessible at [https://platform.exabyte.io/api/v1/materials](https://platform.exabyte.io/api/v1/materials). The following actions are supported on `materials` endpoint:

!!! tip "REST API Test Framework"
    Please visit our [REST API Test Framework](https://docs.exabyte.io/api/#!/Materials/get_materials) to test the queries in this page and see the results. Resuls are not shwown here for simiplicity.

### List

`GET` HTTP method is used to retrieve a list of materials.

* List all materials:

```bash
curl -X GET https://platform.exabyte.io/api/v1/materials -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```

!!! tip "Number of Returned Results"
    The number of returned results are limited to 20 by default ([Results Pagination](../query-structure/#results-pagination)).

* Get material by ID:

```bash
curl -X GET https://platform.exabyte.io/api/v1/materials/KuAsBRwofzGfHPWiT -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```

* Get material by formula:

```bash
curl -X GET https://platform.exabyte.io/api/v1/materials?query%3D%7B%27formula%27%3A+%27SiGe%27%7D -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```

!!! tip "Query Parameter"
    The query parameter before encoding is `query={"formula': "SiGe"}`.

* Get material by a property:

```bash
curl -X GET https://platform.exabyte.io/api/v1/materials?query%3D%7B%27derivedProperties.symmetry.spaceGroup%27%3A+%27F-43m%27%7D -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```

!!! tip "Query Parameter"
    The query parameter before encoding is `query={"derivedProperties.symmetry.spaceGroup": "F-43m"}`.

The returned materials do not contain material's characteristics by default, as we store characteristics inside a separate collection. Although characteristics can be queried separately via `characteristics` endpoint, you can use `includeCharacteristics` parameter to get material's characteristics with one call to the REST API.

* Get material with characteristics:

```bash
curl -X GET https://platform.exabyte.io/api/v1/materials/KuAsBRwofzGfHPWiT?includeCharacteristics=true -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```

### Create

`POST` HTTP method is used to create a new material. New material is passed in JSON format inside body.

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

### Delete

`DELETE` HTTP method is used to delete a material with a given ID.

```bash
curl -X DELETE https://platform.exabyte.io/api/v1/materials/ZPjWNWWmt8hnWAm6e"
```
```json
{
  "status": "success",
  "data": {
    "message": "Material ZPjWNWWmt8hnWAm6e successfully deleted"
  }
}
```

### Update

`PATCH` HTTP method is used to update an existing material. New material's properties are passed in JSON inside body.

```bash
curl -X PATCH https://platform.exabyte.io/api/v1/materials/KuAsBRwofzGfHPWiT -d '{"name": "Silicon FCC"}'
```

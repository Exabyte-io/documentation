## Materials-bank

Materials-bank is central storage of the materials and their calculated characteristics. We keep bank items unique based on descriptive properties. `materials-bank` endpoint is accessible at [https://platform.exabyte.io/api/v1/materials-bank](https://platform.exabyte.io/api/v1/materials-bank). The following actions are supported on `materials-bank` endpoint:

!!! tip "REST API Test Framework"
    Please visit our [REST API Test Framework](https://docs.exabyte.io/api/#!/Materials_Bank/get_materials_bank) to test the queries in this page and see the results. Resuls are not shwown here for simiplicity.

### List

`GET` HTTP method is used to retrieve a list of materials-bank items.

* List all materials-bank items:

```bash
curl -X GET https://platform.exabyte.io/api/v1/materials-bank -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```

!!! tip "Number of Returned Results"
    The number of returned results are limited to 20 by default ([Results Pagination](../query-structure/#results-pagination)).

* Get material-bank item by ID:

```bash
curl -X GET https://platform.exabyte.io/api/v1/materials-bank/hXFvhjYWfR2fmDFJ9 -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```

* Get material-bank by formula:

```bash
curl -X GET https://platform.exabyte.io/api/v1/materials-bank?query%3D%7B%27formula%27%3A+%27SiGe%27%7D -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```

!!! tip "Query Parameter"
    The query parameter before encoding is `query={"formula': "SiGe"}`.

The returned materials do not contain material's characteristics by default, as we store characteristics inside a separate collection. Although characteristics can be queried separately via `characteristics` endpoint, you can use `includeCharacteristics` parameter to get material's characteristics with one call to the REST API.

* Get material-bank item with characteristics:
```bash
curl -X GET https://platform.exabyte.io/api/v1/materials-bank/KuAsBRwofzGfHPWiT?includeCharacteristics=true -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```

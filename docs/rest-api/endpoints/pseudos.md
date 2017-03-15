## Pseudos

`pseudos` endpoint is accessible at [https://platform.exabyte.io/api/v1/pseudos](https://platform.exabyte.io/api/v1/pseudos). The following actions are supported on `pseudos` endpoint:

!!! tip "REST API Test Framework"
    Please visit our [REST API Test Framework](https://docs.exabyte.io/api/#!/Pseudos/get_pseudos) to test the queries in this page and see the results. Resuls are not shwown here for simiplicity.

### List
`GET` HTTP method is used to retrieve a list of pseudos.

* List all pseudos:

```bash
curl -X GET https://platform.exabyte.io/api/v1/pseudos -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```

!!! tip "Number of Returned Results"
    The number of returned results is limited to 20 by default ([Results Pagination](../query-structure/#results-pagination)).

* Get pseudo by ID:

```bash
curl -X GET https://platform.exabyte.io/api/v1/pseudos/58b6b850fe450029c339a559 -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```

* Get pseudo by a property:
```bash
curl -X GET https://platform.exabyte.io/api/v1/pseudos?query%3D%7B%22type%22%3A+%22paw%22%7D -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```


!!! tip "Query Parameter"
    The query parameter before encoding is `query={"type": "paw"}`.

## Create

`POST` HTTP method is used to create a new pseudo (upload a UPF file).

```bash
curl -X POST https://platform.exabyte.io/api/v1/pseudos?approximation=gga&functional=pbe&method=us&application=espresso -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ" -F "pseudoFile=@/path/to/your/upfFile.UPF"
```

### Delete

`DELETE` HTTP method is used to delete an existing pseudos with a given ID.

```bash
curl -X DELETE https://platform.exabyte.io/api/v1/pseudos/RhCFP2WuehvG4hCLp
```
```json
{
  "status": "success",
  "data": {
    "message": "Pseudo RhCFP2WuehvG4hCLp successfully deleted"
  }
}
```

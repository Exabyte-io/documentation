# Workflows

`workflows` endpoint is accessible at [https://platform.exabyte.io/api/v1/workflows](https://platform.exabyte.io/api/v1/workflows). The following actions are supported on `workflows` endpoint:

!!! tip "REST API Test Framework"
    Please visit our [REST API Test Framework](https://docs.exabyte.io/api/#!/Workflows/get_workflows) to test the queries in this page and see the results. Resuls are not shwown here for simiplicity.

## List

`GET` HTTP method is used to retrieve a list of workflows

* List all workflows:

```bash
curl -X GET https://platform.exabyte.io/api/v1/workflows -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```

!!! tip "Number of Returned Results"
    The number of returned results is limited to 20 by default ([Results Pagination](../query-structure/#results-pagination)).

* Get workflow by ID:

```bash
curl -X GET https://platform.exabyte.io/api/v1/workflows/3JCRoje9bbbAMzydb -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```

* Get workflow by a property:

```bash
curl -X GET https://platform.exabyte.io/api/v1/workflows?query%3D%7B%22name%22%3A+%22Total+Energy%22%7D -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```

!!! tip "Query Parameter"
    The query parameter before encoding is `query={"name": "Total Energy"}`.

## Create

`POST` HTTP method is used to create a new workflow. Workflow properties should be passed in JSON format inside body.

```bash
curl -X POST https://platform.exabyte.io/api/v1/workflows -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ" -d
'
{
    // JSON data source...
}
'
```

## Delete

`DELETE` HTTP method is used to delete a workflow with a given id.

```bash
curl -X DELETE https://platform.exabyte.io/api/v1/workflows/SxiKuakDhSQaCAnTC
```
```json
{
  "status": "success",
  "data": {
    "message": "Workflow SxiKuakDhSQaCAnTC successfully deleted"
  }
}
```

## Update

`PATCH` HTTP method is used to update an existing workflow with a given ID.

```bash
curl -X PATCH https://platform.exabyte.io/api/v1/workflows/RhCFP2WuehvG4hCLp -d '{"name": "Total Energy 2"}'
```

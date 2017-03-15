# Jobs

`jobs` endpoint is accessible at [https://platform.exabyte.io/api/v1/jobs](https://platform.exabyte.io/api/v1/jobs). The following actions are supported on `jobs` endpoint:

!!! tip "REST API Test Framework"
    Please visit our [REST API Test Framework](https://docs.exabyte.io/api/#!/Jobs/get_jobs) to test the queries in this page and see the results. Resuls are not shwown here for simiplicity.

### List

`GET` HTTP method is used to retrieve a list of jobs.

* List all jobs:

```bash
curl -X GET https://platform.exabyte.io/api/v1/jobs -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```

!!! tip "Number of Returned Results"
    The number of returned results is limited to 20 by default ([Results Pagination](../query-structure/#results-pagination)).

* Get job by ID:

```bash
curl -X GET https://platform.exabyte.io/api/v1/jobs/RhCFP2WuehvG4hCLp -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```

* Get job by property:

```bash
curl -X GET https://platform.exabyte.io/api/v1/jobs?query%3D%7B%22status%22%3A+%22finished%22%7D -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```

!!! tip "Query Parameter"
    The query parameter before encoding is `query={"status": "finished"}`.

### Create

`POST` HTTP method is used to create a new job. Job parameters are passed in JSON format inside body.

```bash
curl -X POST https://platform.exabyte.io/api/v1/jobs -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ" -d '
{
  "_material": {
    "_id": "gyfPHZk56QAxRpAqv"
  },
  "compute": {
    "cluster": {
      "fqdn": "AWS-cluster-001"
    },
    "nodes": 1,
    "notify": "n",
    "ppn": 1,
    "queue": "D",
    "timeLimit": "01:00:00"
  },
  "model": {
    "method": {
      "data": {
        "pseudo": [
          {
            "_id": "58947f5efe450067c9c92e24"
          }
        ]
      },
      "precision": {
        "kpoints": {
          "shift": {
            "x": 0,
            "y": 0,
            "z": 0
          },
          "value": {
            "x": 2,
            "y": 2,
            "z": 2
          }
        }
      },
      "workflow": {
        "_id": "7GSofzPcxZryR8YiL"
      }
    }
  },
  "title": "New Job Feb 15th 2017, 18:32 PM"
}
'
```

### Delete

`DELETE` HTTP method is used to delete a job with a given ID.

```bash
curl -X DELETE https://platform.exabyte.io/api/v1/jobs/HmeWjp69jHYkZYMkh
```
```json
{
  "status": "success",
  "data": {
    "message": "Job HmeWjp69jHYkZYMkh successfully deleted"
  }
}
```

### Update

`PATCH` HTTP method is used to update an existing job.

```bash
curl -X PATCH https://platform.exabyte.io/api/v1/jobs/RhCFP2WuehvG4hCLp -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ" -d '{"title": "New Job Feb 15th 2017, 18:32 PM"}'
```

### Job Submission

`POST` HTTP method with `submit` URL paramater are used to submit a job with a given.

```bash
curl -X POST https://platform.exabyte.io/api/v1/jobs/RhCFP2WuehvG4hCLp?submit=true -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```

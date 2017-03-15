## Workflows

`workflows` endpoint is accessible at [https://platform.exabyte.io/api/v1/workflows](https://platform.exabyte.io/api/v1/workflows). The following actions are supported on `workflows` endpoint:

!!! tip "REST API Test Framework"
    Please visit our [REST API Test Framework](https://docs.exabyte.io/api/#!/Workflows/get_workflows) to test the queries in this page and see the results. Resuls are not shwown here for simiplicity.

### List

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

### Create

`POST` HTTP method is used to create a new workflow. Workflow properties should be passed in JSON format inside body.

```bash
curl -X POST https://platform.exabyte.io/api/v1/workflows -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ" -d
'
{
  "app": "vasp",
  "ignore": false,
  "name": "Total Energy",
  "units": [
    {
      "execution": {
        "app": {
          "exec": "vasp",
          "name": "vasp",
          "summary": "VASP",
          "version": "5.3.5"
        },
        "input": [
          {
            "content": "ISMEAR = 0\nSIGMA  = 0.05\nLWAVE  = .FALSE.\nLCHARG = .FALSE.",
            "name": "INCAR"
          },
          {
            "content": "Automatic mesh\n0\nGamma\n  1  1  1\n  0.  0.  0.",
            "name": "KPOINTS"
          },
          {
            "content": "Diamond FCC Si\n5.43\n0.000000000 0.500000000 0.500000000\n0.500000000 0.000000000 0.500000000\n0.500000000 0.500000000 0.000000000\nSi\n2\nDirect\n0.000000000 0.000000000 0.000000000 Si\n0.250000000 0.250000000 0.250000000 Si",
            "name": "POSCAR"
          }
        ]
      },
      "flowchartId": "vasp",
      "head": true,
      "monitors": [
        {
          "name": "standard_output"
        },
        {
          "name": "electronic"
        }
      ],
      "name": "vasp",
      "postProcessors": [
        {
          "kwargs": [
            {
              "key": "source",
              "value": "INCAR"
            },
            {
              "key": "destination",
              "value": "INCAR.vasp"
            }
          ],
          "name": "copy_file",
          "type": "command"
        },
        {
          "kwargs": [
            {
              "key": "source",
              "value": "KPOINTS"
            },
            {
              "key": "destination",
              "value": "KPOINTS.vasp"
            }
          ],
          "name": "copy_file",
          "type": "command"
        },
        {
          "kwargs": [
            {
              "key": "source",
              "value": "POSCAR"
            },
            {
              "key": "destination",
              "value": "POSCAR.vasp"
            }
          ],
          "name": "copy_file",
          "type": "command"
        },
        {
          "kwargs": [
            {
              "key": "source",
              "value": "OSZICAR"
            },
            {
              "key": "destination",
              "value": "OSZICAR.vasp"
            }
          ],
          "name": "copy_file",
          "type": "command"
        },
        {
          "kwargs": [
            {
              "key": "source",
              "value": "OUTCAR"
            },
            {
              "key": "destination",
              "value": "OUTCAR.vasp"
            }
          ],
          "name": "copy_file",
          "type": "command"
        },
        {
          "kwargs": [
            {
              "key": "source",
              "value": "XDATCAR"
            },
            {
              "key": "destination",
              "value": "XDATCAR.vasp"
            }
          ],
          "name": "copy_file",
          "type": "command"
        },
        {
          "kwargs": [
            {
              "key": "source",
              "value": "vasprun.xml"
            },
            {
              "key": "destination",
              "value": "vasprun.xml.vasp"
            }
          ],
          "name": "copy_file",
          "type": "command"
        },
        {
          "kwargs": [
            {
              "key": "source",
              "value": "DOSCAR"
            },
            {
              "key": "destination",
              "value": "DOSCAR.vasp"
            }
          ],
          "name": "copy_file",
          "type": "command"
        },
        {
          "kwargs": [
            {
              "key": "source",
              "value": "PROCAR"
            },
            {
              "key": "destination",
              "value": "PROCAR.vasp"
            }
          ],
          "name": "copy_file",
          "type": "command"
        },
        {
          "kwargs": [
            {
              "key": "source",
              "value": "IBZKPT"
            },
            {
              "key": "destination",
              "value": "IBZKPT.vasp"
            }
          ],
          "name": "copy_file",
          "type": "command"
        }
      ],
      "preProcessors": [],
      "results": [
        {
          "name": "total_energy"
        },
        {
          "name": "fermi_energy"
        },
        {
          "name": "pressure"
        },
        {
          "name": "atomic_forces"
        },
        {
          "name": "total_forces"
        },
        {
          "name": "stress_tensor"
        },
        {
          "name": "total_energy_contributions"
        }
      ],
      "status": "idle",
      "type": "execution"
    }
  ]
}
'
```

### Delete

`DELETE` HTTP method is used to delete a workflow with a given.

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

### Update

`PATCH` HTTP method is used to update an existing workflow with a given ID.

```bash
curl -X PATCH https://platform.exabyte.io/api/v1/workflows/RhCFP2WuehvG4hCLp -d '{"name": "Total Energy 2"}'
```

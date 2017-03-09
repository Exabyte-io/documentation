## Workflows

`workflows` endpoint is accessible at [https://platform.exabyte.io/api/v1/workflows](https://platform.exabyte.io/api/v1/workflows). The following actions are supported on `workflows` endpoint:

### List

`GET` HTTP method is used to retrieve a list of workflows

<details>
    <summary>List all workflows:</summary>
```bash
curl -X GET https://platform.exabyte.io/api/v1/workflows -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```
```bash
{
  "status": "success",
  "data": [
    {
      "_id": "3JCRoje9bbbAMzydb",
      "name": "Total Energy",
      "app": "vasp",
      "units": [
        {
          "type": "execution",
          "name": "vasp",
          "status": "idle",
          "head": true,
          "flowchartId": "vasp",
          "execution": {
            "app": {
              "name": "vasp",
              "version": "5.3.5",
              "summary": "VASP",
              "exec": "vasp"
            },
            "input": [
              {
                "name": "INCAR",
                "content": "ISMEAR = 0\nSIGMA  = 0.05\nLWAVE  = .FALSE.\nLCHARG = .FALSE."
              },
              {
                "name": "KPOINTS",
                "content": "Automatic mesh\n0\nGamma\n  1  1  1\n  0.  0.  0."
              },
              {
                "name": "POSCAR",
                "content": "Diamond FCC Si\n5.43\n0.000000000 0.500000000 0.500000000\n0.500000000 0.000000000 0.500000000\n0.500000000 0.500000000 0.000000000\nSi\n2\nDirect\n0.000000000 0.000000000 0.000000000 Si\n0.250000000 0.250000000 0.250000000 Si"
              }
            ]
          },
          "monitors": [
            {
              "name": "standard_output"
            },
            {
              "name": "electronic"
            }
          ],
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
          "postProcessors": [
            {
              "type": "command",
              "name": "copy_file",
              "kwargs": [
                {
                  "key": "source",
                  "value": "INCAR"
                },
                {
                  "key": "destination",
                  "value": "INCAR.vasp"
                }
              ]
            },
            {
              "type": "command",
              "name": "copy_file",
              "kwargs": [
                {
                  "key": "source",
                  "value": "KPOINTS"
                },
                {
                  "key": "destination",
                  "value": "KPOINTS.vasp"
                }
              ]
            },
            {
              "type": "command",
              "name": "copy_file",
              "kwargs": [
                {
                  "key": "source",
                  "value": "POSCAR"
                },
                {
                  "key": "destination",
                  "value": "POSCAR.vasp"
                }
              ]
            },
            {
              "type": "command",
              "name": "copy_file",
              "kwargs": [
                {
                  "key": "source",
                  "value": "OSZICAR"
                },
                {
                  "key": "destination",
                  "value": "OSZICAR.vasp"
                }
              ]
            },
            {
              "type": "command",
              "name": "copy_file",
              "kwargs": [
                {
                  "key": "source",
                  "value": "OUTCAR"
                },
                {
                  "key": "destination",
                  "value": "OUTCAR.vasp"
                }
              ]
            },
            {
              "type": "command",
              "name": "copy_file",
              "kwargs": [
                {
                  "key": "source",
                  "value": "XDATCAR"
                },
                {
                  "key": "destination",
                  "value": "XDATCAR.vasp"
                }
              ]
            },
            {
              "type": "command",
              "name": "copy_file",
              "kwargs": [
                {
                  "key": "source",
                  "value": "vasprun.xml"
                },
                {
                  "key": "destination",
                  "value": "vasprun.xml.vasp"
                }
              ]
            },
            {
              "type": "command",
              "name": "copy_file",
              "kwargs": [
                {
                  "key": "source",
                  "value": "DOSCAR"
                },
                {
                  "key": "destination",
                  "value": "DOSCAR.vasp"
                }
              ]
            },
            {
              "type": "command",
              "name": "copy_file",
              "kwargs": [
                {
                  "key": "source",
                  "value": "PROCAR"
                },
                {
                  "key": "destination",
                  "value": "PROCAR.vasp"
                }
              ]
            },
            {
              "type": "command",
              "name": "copy_file",
              "kwargs": [
                {
                  "key": "source",
                  "value": "IBZKPT"
                },
                {
                  "key": "destination",
                  "value": "IBZKPT.vasp"
                }
              ]
            }
          ],
          "preProcessors": []
        }
      ],
      "ignore": false
    },
  ]
}
```
</details>

!!! tip "Number of Returned Results"
    The number of returned results are limited to 20 by default ([Results Pagination](../query-structure/#results-pagination)).

<details>
    <summary>Get workflow by ID:</summary>
```bash
curl -X GET https://platform.exabyte.io/api/v1/workflows/3JCRoje9bbbAMzydb -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```
```bash
{
  "status": "success",
  "data": {
    "_id": "3JCRoje9bbbAMzydb",
    "name": "Total Energy",
    "app": "vasp",
    "units": [
      {
        "type": "execution",
        "name": "vasp",
        "status": "idle",
        "head": true,
        "flowchartId": "vasp",
        "execution": {
          "app": {
            "name": "vasp",
            "version": "5.3.5",
            "summary": "VASP",
            "exec": "vasp"
          },
          "input": [
            {
              "name": "INCAR",
              "content": "ISMEAR = 0\nSIGMA  = 0.05\nLWAVE  = .FALSE.\nLCHARG = .FALSE."
            },
            {
              "name": "KPOINTS",
              "content": "Automatic mesh\n0\nGamma\n  1  1  1\n  0.  0.  0."
            },
            {
              "name": "POSCAR",
              "content": "Diamond FCC Si\n5.43\n0.000000000 0.500000000 0.500000000\n0.500000000 0.000000000 0.500000000\n0.500000000 0.500000000 0.000000000\nSi\n2\nDirect\n0.000000000 0.000000000 0.000000000 Si\n0.250000000 0.250000000 0.250000000 Si"
            }
          ]
        },
        "monitors": [
          {
            "name": "standard_output"
          },
          {
            "name": "electronic"
          }
        ],
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
        "postProcessors": [
          {
            "type": "command",
            "name": "copy_file",
            "kwargs": [
              {
                "key": "source",
                "value": "INCAR"
              },
              {
                "key": "destination",
                "value": "INCAR.vasp"
              }
            ]
          },
          {
            "type": "command",
            "name": "copy_file",
            "kwargs": [
              {
                "key": "source",
                "value": "KPOINTS"
              },
              {
                "key": "destination",
                "value": "KPOINTS.vasp"
              }
            ]
          },
          {
            "type": "command",
            "name": "copy_file",
            "kwargs": [
              {
                "key": "source",
                "value": "POSCAR"
              },
              {
                "key": "destination",
                "value": "POSCAR.vasp"
              }
            ]
          },
          {
            "type": "command",
            "name": "copy_file",
            "kwargs": [
              {
                "key": "source",
                "value": "OSZICAR"
              },
              {
                "key": "destination",
                "value": "OSZICAR.vasp"
              }
            ]
          },
          {
            "type": "command",
            "name": "copy_file",
            "kwargs": [
              {
                "key": "source",
                "value": "OUTCAR"
              },
              {
                "key": "destination",
                "value": "OUTCAR.vasp"
              }
            ]
          },
          {
            "type": "command",
            "name": "copy_file",
            "kwargs": [
              {
                "key": "source",
                "value": "XDATCAR"
              },
              {
                "key": "destination",
                "value": "XDATCAR.vasp"
              }
            ]
          },
          {
            "type": "command",
            "name": "copy_file",
            "kwargs": [
              {
                "key": "source",
                "value": "vasprun.xml"
              },
              {
                "key": "destination",
                "value": "vasprun.xml.vasp"
              }
            ]
          },
          {
            "type": "command",
            "name": "copy_file",
            "kwargs": [
              {
                "key": "source",
                "value": "DOSCAR"
              },
              {
                "key": "destination",
                "value": "DOSCAR.vasp"
              }
            ]
          },
          {
            "type": "command",
            "name": "copy_file",
            "kwargs": [
              {
                "key": "source",
                "value": "PROCAR"
              },
              {
                "key": "destination",
                "value": "PROCAR.vasp"
              }
            ]
          },
          {
            "type": "command",
            "name": "copy_file",
            "kwargs": [
              {
                "key": "source",
                "value": "IBZKPT"
              },
              {
                "key": "destination",
                "value": "IBZKPT.vasp"
              }
            ]
          }
        ],
        "preProcessors": []
      }
    ],
    "ignore": false
  }
}
```
</details>

<details>
    <summary>Get workflow by a property. The original query before encoding is `query={"name": "Total Energy"}`</summary>
```bash
curl -X GET https://platform.exabyte.io/api/v1/workflows?query%3D%7B%22name%22%3A+%22Total+Energy%22%7D -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```
```bash
{
  "status": "success",
  "data": [
    {
      "_id": "3JCRoje9bbbAMzydb",
      "name": "Total Energy",
      "app": "vasp",
      "units": [
        {
          "type": "execution",
          "name": "vasp",
          "status": "idle",
          "head": true,
          "flowchartId": "vasp",
          "execution": {
            "app": {
              "name": "vasp",
              "version": "5.3.5",
              "summary": "VASP",
              "exec": "vasp"
            },
            "input": [
              {
                "name": "INCAR",
                "content": "ISMEAR = 0\nSIGMA  = 0.05\nLWAVE  = .FALSE.\nLCHARG = .FALSE."
              },
              {
                "name": "KPOINTS",
                "content": "Automatic mesh\n0\nGamma\n  1  1  1\n  0.  0.  0."
              },
              {
                "name": "POSCAR",
                "content": "Diamond FCC Si\n5.43\n0.000000000 0.500000000 0.500000000\n0.500000000 0.000000000 0.500000000\n0.500000000 0.500000000 0.000000000\nSi\n2\nDirect\n0.000000000 0.000000000 0.000000000 Si\n0.250000000 0.250000000 0.250000000 Si"
              }
            ]
          },
          "monitors": [
            {
              "name": "standard_output"
            },
            {
              "name": "electronic"
            }
          ],
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
          "postProcessors": [
            {
              "type": "command",
              "name": "copy_file",
              "kwargs": [
                {
                  "key": "source",
                  "value": "INCAR"
                },
                {
                  "key": "destination",
                  "value": "INCAR.vasp"
                }
              ]
            },
            {
              "type": "command",
              "name": "copy_file",
              "kwargs": [
                {
                  "key": "source",
                  "value": "KPOINTS"
                },
                {
                  "key": "destination",
                  "value": "KPOINTS.vasp"
                }
              ]
            },
            {
              "type": "command",
              "name": "copy_file",
              "kwargs": [
                {
                  "key": "source",
                  "value": "POSCAR"
                },
                {
                  "key": "destination",
                  "value": "POSCAR.vasp"
                }
              ]
            },
            {
              "type": "command",
              "name": "copy_file",
              "kwargs": [
                {
                  "key": "source",
                  "value": "OSZICAR"
                },
                {
                  "key": "destination",
                  "value": "OSZICAR.vasp"
                }
              ]
            },
            {
              "type": "command",
              "name": "copy_file",
              "kwargs": [
                {
                  "key": "source",
                  "value": "OUTCAR"
                },
                {
                  "key": "destination",
                  "value": "OUTCAR.vasp"
                }
              ]
            },
            {
              "type": "command",
              "name": "copy_file",
              "kwargs": [
                {
                  "key": "source",
                  "value": "XDATCAR"
                },
                {
                  "key": "destination",
                  "value": "XDATCAR.vasp"
                }
              ]
            },
            {
              "type": "command",
              "name": "copy_file",
              "kwargs": [
                {
                  "key": "source",
                  "value": "vasprun.xml"
                },
                {
                  "key": "destination",
                  "value": "vasprun.xml.vasp"
                }
              ]
            },
            {
              "type": "command",
              "name": "copy_file",
              "kwargs": [
                {
                  "key": "source",
                  "value": "DOSCAR"
                },
                {
                  "key": "destination",
                  "value": "DOSCAR.vasp"
                }
              ]
            },
            {
              "type": "command",
              "name": "copy_file",
              "kwargs": [
                {
                  "key": "source",
                  "value": "PROCAR"
                },
                {
                  "key": "destination",
                  "value": "PROCAR.vasp"
                }
              ]
            },
            {
              "type": "command",
              "name": "copy_file",
              "kwargs": [
                {
                  "key": "source",
                  "value": "IBZKPT"
                },
                {
                  "key": "destination",
                  "value": "IBZKPT.vasp"
                }
              ]
            }
          ],
          "preProcessors": []
        }
      ],
      "ignore": false
    },
  ]
}
```
</details>

### Create

`POST` HTTP method is used to create a new workflow. Workflow properties should be passed in JSON format inside body.

<details>
    <summary>Create a new workflow:</summary>
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
```bash
{
  "data": {
    "_id": "SxiKuakDhSQaCAnTC",
    "app": "vasp",
    "ignore": false,
    "name": "Total Energy",
    "owner": {
      "_id": "jnLJpf9vJKYtFoQxc",
      "name": "exadmin",
      "type": 0
    },
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
  },
  "status": "success"
}
```
</details>

### Delete

`DELETE` HTTP method is used to delete a workflow with a given.

<details>
    <summary>Delete a workflow:</summary>
```bash
curl -X DELETE https://platform.exabyte.io/api/v1/workflows/SxiKuakDhSQaCAnTC
```
```bash
{
  "status": "success",
  "data": {
    "message": "Workflow SxiKuakDhSQaCAnTC successfully deleted"
  }
}
```
</details>

### Update

`PATCH` HTTP method is used to update an existing workflow with a given ID.

<details>
    <summary>Update a workflow:</summary>
```bash
curl -X PATCH https://platform.exabyte.io/api/v1/workflows/RhCFP2WuehvG4hCLp -d '{"name": "Total Energy 2"}'
```
```bash
{
      "_id": "3JCRoje9bbbAMzydb",
      "name": "Total Energy 2",
      "owner": {
           "type": 1,
           "name": "demo",
           "_id": "DKJRd2svSD2j3n94E",
      },
      "app": "vasp",
      "units": [
        {
          "type": "execution",
          "name": "vasp",
          "status": "idle",
          "head": true,
          "flowchartId": "vasp",
          "execution": {
            "app": {
              "name": "vasp",
              "version": "5.3.5",
              "summary": "VASP",
              "exec": "vasp"
            },
            "input": [
              {
                "name": "INCAR",
                "content": "ISMEAR = 0\nSIGMA  = 0.05\nLWAVE  = .FALSE.\nLCHARG = .FALSE."
              },
              {
                "name": "KPOINTS",
                "content": "Automatic mesh\n0\nGamma\n  1  1  1\n  0.  0.  0."
              },
              {
                "name": "POSCAR",
                "content": "Diamond FCC Si\n5.43\n0.000000000 0.500000000 0.500000000\n0.500000000 0.000000000 0.500000000\n0.500000000 0.500000000 0.000000000\nSi\n2\nDirect\n0.000000000 0.000000000 0.000000000 Si\n0.250000000 0.250000000 0.250000000 Si"
              }
            ]
          },
          "monitors": [
            {
              "name": "standard_output"
            },
            {
              "name": "electronic"
            }
          ],
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
          "postProcessors": [
            {
              "type": "command",
              "name": "copy_file",
              "kwargs": [
                {
                  "key": "source",
                  "value": "INCAR"
                },
                {
                  "key": "destination",
                  "value": "INCAR.vasp"
                }
              ]
            },
            {
              "type": "command",
              "name": "copy_file",
              "kwargs": [
                {
                  "key": "source",
                  "value": "KPOINTS"
                },
                {
                  "key": "destination",
                  "value": "KPOINTS.vasp"
                }
              ]
            },
            {
              "type": "command",
              "name": "copy_file",
              "kwargs": [
                {
                  "key": "source",
                  "value": "POSCAR"
                },
                {
                  "key": "destination",
                  "value": "POSCAR.vasp"
                }
              ]
            },
            {
              "type": "command",
              "name": "copy_file",
              "kwargs": [
                {
                  "key": "source",
                  "value": "OSZICAR"
                },
                {
                  "key": "destination",
                  "value": "OSZICAR.vasp"
                }
              ]
            },
            {
              "type": "command",
              "name": "copy_file",
              "kwargs": [
                {
                  "key": "source",
                  "value": "OUTCAR"
                },
                {
                  "key": "destination",
                  "value": "OUTCAR.vasp"
                }
              ]
            },
            {
              "type": "command",
              "name": "copy_file",
              "kwargs": [
                {
                  "key": "source",
                  "value": "XDATCAR"
                },
                {
                  "key": "destination",
                  "value": "XDATCAR.vasp"
                }
              ]
            },
            {
              "type": "command",
              "name": "copy_file",
              "kwargs": [
                {
                  "key": "source",
                  "value": "vasprun.xml"
                },
                {
                  "key": "destination",
                  "value": "vasprun.xml.vasp"
                }
              ]
            },
            {
              "type": "command",
              "name": "copy_file",
              "kwargs": [
                {
                  "key": "source",
                  "value": "DOSCAR"
                },
                {
                  "key": "destination",
                  "value": "DOSCAR.vasp"
                }
              ]
            },
            {
              "type": "command",
              "name": "copy_file",
              "kwargs": [
                {
                  "key": "source",
                  "value": "PROCAR"
                },
                {
                  "key": "destination",
                  "value": "PROCAR.vasp"
                }
              ]
            },
            {
              "type": "command",
              "name": "copy_file",
              "kwargs": [
                {
                  "key": "source",
                  "value": "IBZKPT"
                },
                {
                  "key": "destination",
                  "value": "IBZKPT.vasp"
                }
              ]
            }
          ],
          "preProcessors": []
        }
      ],
      "ignore": false
    }
```
</details>

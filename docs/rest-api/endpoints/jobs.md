# Jobs

`jobs` endpoint is accessible at [https://platform.exabyte.io/api/v1/jobs](https://platform.exabyte.io/api/v1/jobs). The following actions are supported on `jobs` endpoint:

### List

`GET` HTTP method is used to retrieve a list of jobs.

<details>
    <summary>List all jobs:</summary>
```bash
curl -X GET https://platform.exabyte.io/api/v1/jobs -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```
```bash
{
  "data": [
    {
      "_id": "RhCFP2WuehvG4hCLp",
      "_material": {
        "_id": "gyfPHZk56QAxRpAqv",
        "exabyteId": "ixAXcDT9DJcCP4GrY",
        "name": "Silicon FCC"
      },
      "_project": {
        "_id": "Wk8F7azNhP3R5j6GG",
        "access": {
          "level": 10,
          "type": 0
        },
        "goldName": "exadmin",
        "name": "exadmin",
        "owner": {
          "_id": "k8uubJNniCHuydoNF",
          "name": "exadmin",
          "type": 0
        },
        "slug": "exadmin"
      },
      "compute": {
        "arguments": {},
        "cluster": {
          "fqdn": "master-vagrant-cluster-001.exabyte.io",
          "jid": "2.master-vagrant-cluster-001.exabyte.io"
        },
        "email": "admin@exabyte.io",
        "nodes": 1,
        "notify": "n",
        "ppn": 1,
        "queue": "D",
        "timeLimit": "01:00:00"
      },
      "createdAt": "2017-02-15T15:03:02.032Z",
      "creator": {
        "_id": "k8uubJNniCHuydoNF",
        "username": "exadmin"
      },
      "friendlySlugs": {
        "titleSlug": {
          "base": "new-job-feb-15th-2017-18-32-pm",
          "index": 0
        }
      },
      "model": {
        "accuracy": 200,
        "method": {
          "data": {
            "pseudo": [
              {
                "_id": "58947f5efe450067c9c92e24",
                "access": {
                  "level": 0,
                  "type": 0
                },
                "apps": [
                  "espresso"
                ],
                "characteristics": [
                  {
                    "name": "total_energy",
                    "units": "eV",
                    "value": -130.568347569
                  },
                  {
                    "name": "zero_point_energy",
                    "units": "eV",
                    "value": -0.04545053892
                  }
                ],
                "element": "Si",
                "exchangeCorrelation": {
                  "approximation": "gga",
                  "functional": "pbe"
                },
                "filename": "si_pbe_gbrv_1.0.upf",
                "path": "/export/share/pseudo/si/gga/pbe/gbrv/1.0/us/si_pbe_gbrv_1.0.upf",
                "source": "gbrv",
                "textHeading": "0                   Version Number\n  Si                   Element\n   US                  Ultrasoft pseudopotential\n    T                  Nonlinear Core Correction\nSLA  PW   PBE  PBE     PBE  Exchange-Correlation functional\n    4.00000000000      Z valence\n   -9.19868380872      Total energy\n    0.00000    0.00000 Suggested cutoff for wfc and rho\n    2                  Max angular momentum component\n  899                  Number of points in mesh\n    2    6             Number of Wavefunctions, Number of Projectors\n Wavefunctions         nl  l   occ\n                       3S  0  2.00\n                       3P  1  2.00",
                "type": "us",
                "version": "1.0"
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
            },
            "kppra": 16
          },
          "subtype": "us",
          "type": "pseudo",
          "workflow": {
            "_id": "7GSofzPcxZryR8YiL",
            "app": "espresso",
            "ignore": false,
            "name": "Total Energy",
            "units": [
              {
                "execution": {
                  "app": {
                    "exec": "pw.x",
                    "flavor": "pw_scf",
                    "name": "espresso",
                    "summary": "Quantum Espresso",
                    "version": "5.4.0"
                  },
                  "input": [
                    {
                      "content": "&CONTROL\n    calculation= 'scf'\n    title= ''\n    verbosity= 'low'\n    restart_mode= 'from_scratch'\n    wf_collect= .true.\n    tstress= .true.\n    tprnfor= .true.\n    outdir= '$OUTPUT_DIR/'\n    wfcdir= '$OUTPUT_DIR/'\n    prefix= '__prefix__'\n    pseudo_dir= '$PSEUDO_DIR'\n/\n&SYSTEM\n    ibrav=0\n    nat=2\n    ntyp=1\n    ecutwfc= 40\n    ecutrho= 200\n    occupations= 'smearing'\n    degauss= 0.005\n/\n&ELECTRONS\n    diagonalization= 'david'\n    diago_david_ndim= 4\n    diago_full_acc= .true.\n    mixing_beta= 0.3\n    startingwfc='atomic+random'\n/\n&IONS\n/\n&CELL\n/\nATOMIC_SPECIES\nSi 28.0855 si_pbe_gbrv_1.0.upf\nCELL_PARAMETERS angstrom\n3.867000000 0.000000000 0.000000000\n1.933500000 3.348920236 0.000000000\n1.933500000 1.116306745 3.157392278\nATOMIC_POSITIONS crystal\nSi 0.000000000 0.000000000 0.000000000\nSi 0.250000000 0.250000000 0.250000000\nK_POINTS automatic\n2 2 2 0 0 0",
                      "name": "pw_scf.in"
                    }
                  ]
                },
                "flowchartId": "pw-scf",
                "head": true,
                "monitors": [
                  {
                    "data": [
                      1.4026394168011649,
                      0.5946081794827971,
                      0.006968158142486594,
                      0.000969405970227804,
                      0.00003891229578738975,
                      0.000007347076826989673
                    ],
                    "name": "electronic",
                    "units": "eV"
                  },
                  {
                    "name": "standard_output"
                  }
                ],
                "name": "pw_scf",
                "postProcessors": [],
                "preProcessors": [],
                "results": [
                  {
                    "name": "total_energy",
                    "units": "eV",
                    "value": -258.62939528928314
                  },
                  {
                    "ewald": {
                      "name": "ewald",
                      "value": -226.941256604257
                    },
                    "exchangeCorrelation": {
                      "name": "exchange_correlation",
                      "value": -118.06522851215864
                    },
                    "harrisFoulkes": {
                      "name": "harris_foulkes",
                      "value": -258.62938957489007
                    },
                    "hartree": {
                      "name": "hartree",
                      "value": 17.723393566555778
                    },
                    "name": "total_energy_contributions",
                    "oneElectron": {
                      "name": "one_electron",
                      "value": 68.65369626057674
                    },
                    "smearing": {
                      "name": "smearing",
                      "value": 0
                    },
                    "units": "eV"
                  },
                  {
                    "name": "pressure",
                    "units": "kbar",
                    "value": 73.71
                  },
                  {
                    "name": "fermi_energy",
                    "units": "eV",
                    "value": 6.607916337990446
                  },
                  {
                    "name": "atomic_forces",
                    "units": "eV",
                    "value": [
                      [
                        0,
                        0,
                        -0.00000116
                      ],
                      [
                        0,
                        0,
                        0.00000116
                      ]
                    ]
                  },
                  {
                    "name": "total_forces",
                    "units": "eV",
                    "value": 0.000002
                  },
                  {
                    "name": "stress_tensor",
                    "units": "kbar",
                    "value": [
                      [
                        0.00050111,
                        0,
                        0
                      ],
                      [
                        0,
                        0.00050111,
                        0
                      ],
                      [
                        0,
                        0,
                        0.00050096
                      ]
                    ]
                  }
                ],
                "status": "complete",
                "type": "execution"
              }
            ]
          }
        },
        "subsubtype": "PBE",
        "subtype": "GGA",
        "type": "DFT"
      },
      "owner": {
        "_id": "k8uubJNniCHuydoNF",
        "name": "exadmin",
        "type": 0
      },
      "status": "finished",
      "statusTrack": [
        {
          "status": "pre-submission",
          "trackedAt": 1487170982035
        },
        {
          "status": "submitted",
          "trackedAt": 1487170985238
        },
        {
          "status": "active",
          "trackedAt": 1487170989234
        },
        {
          "status": "finished",
          "trackedAt": 1487170992492
        }
      ],
      "title": "New Job Feb 15th 2017, 18:32 PM",
      "titleSlug": "new-job-feb-15th-2017-18-32-pm",
      "updatedAt": "2017-02-15T15:03:12.587Z",
      "version": "0.1.1"
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
    <summary>Get job by ID:</summary>
```bash
curl -X GET https://platform.exabyte.io/api/v1/jobs/RhCFP2WuehvG4hCLp -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```
```bash
{
  "data": {
    "_id": "RhCFP2WuehvG4hCLp",
    "_material": {
      "_id": "gyfPHZk56QAxRpAqv",
      "exabyteId": "ixAXcDT9DJcCP4GrY",
      "name": "Silicon FCC"
    },
    "_project": {
      "_id": "Wk8F7azNhP3R5j6GG",
      "access": {
        "level": 10,
        "type": 0
      },
      "goldName": "exadmin",
      "name": "exadmin",
      "owner": {
        "_id": "k8uubJNniCHuydoNF",
        "name": "exadmin",
        "type": 0
      },
      "slug": "exadmin"
    },
    "compute": {
      "arguments": {},
      "cluster": {
        "fqdn": "master-vagrant-cluster-001.exabyte.io",
        "jid": "2.master-vagrant-cluster-001.exabyte.io"
      },
      "email": "admin@exabyte.io",
      "nodes": 1,
      "notify": "n",
      "ppn": 1,
      "queue": "D",
      "timeLimit": "01:00:00"
    },
    "createdAt": "2017-02-15T15:03:02.032Z",
    "creator": {
      "_id": "k8uubJNniCHuydoNF",
      "username": "exadmin"
    },
    "friendlySlugs": {
      "titleSlug": {
        "base": "new-job-feb-15th-2017-18-32-pm",
        "index": 0
      }
    },
    "model": {
      "accuracy": 200,
      "method": {
        "data": {
          "pseudo": [
            {
              "_id": "58947f5efe450067c9c92e24",
              "access": {
                "level": 0,
                "type": 0
              },
              "apps": [
                "espresso"
              ],
              "characteristics": [
                {
                  "name": "total_energy",
                  "units": "eV",
                  "value": -130.568347569
                },
                {
                  "name": "zero_point_energy",
                  "units": "eV",
                  "value": -0.04545053892
                }
              ],
              "element": "Si",
              "exchangeCorrelation": {
                "approximation": "gga",
                "functional": "pbe"
              },
              "filename": "si_pbe_gbrv_1.0.upf",
              "path": "/export/share/pseudo/si/gga/pbe/gbrv/1.0/us/si_pbe_gbrv_1.0.upf",
              "source": "gbrv",
              "textHeading": "0                   Version Number\n  Si                   Element\n   US                  Ultrasoft pseudopotential\n    T                  Nonlinear Core Correction\nSLA  PW   PBE  PBE     PBE  Exchange-Correlation functional\n    4.00000000000      Z valence\n   -9.19868380872      Total energy\n    0.00000    0.00000 Suggested cutoff for wfc and rho\n    2                  Max angular momentum component\n  899                  Number of points in mesh\n    2    6             Number of Wavefunctions, Number of Projectors\n Wavefunctions         nl  l   occ\n                       3S  0  2.00\n                       3P  1  2.00",
              "type": "us",
              "version": "1.0"
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
          },
          "kppra": 16
        },
        "subtype": "us",
        "type": "pseudo",
        "workflow": {
          "_id": "7GSofzPcxZryR8YiL",
          "app": "espresso",
          "ignore": false,
          "name": "Total Energy",
          "units": [
            {
              "execution": {
                "app": {
                  "exec": "pw.x",
                  "flavor": "pw_scf",
                  "name": "espresso",
                  "summary": "Quantum Espresso",
                  "version": "5.4.0"
                },
                "input": [
                  {
                    "content": "&CONTROL\n    calculation= 'scf'\n    title= ''\n    verbosity= 'low'\n    restart_mode= 'from_scratch'\n    wf_collect= .true.\n    tstress= .true.\n    tprnfor= .true.\n    outdir= '$OUTPUT_DIR/'\n    wfcdir= '$OUTPUT_DIR/'\n    prefix= '__prefix__'\n    pseudo_dir= '$PSEUDO_DIR'\n/\n&SYSTEM\n    ibrav=0\n    nat=2\n    ntyp=1\n    ecutwfc= 40\n    ecutrho= 200\n    occupations= 'smearing'\n    degauss= 0.005\n/\n&ELECTRONS\n    diagonalization= 'david'\n    diago_david_ndim= 4\n    diago_full_acc= .true.\n    mixing_beta= 0.3\n    startingwfc='atomic+random'\n/\n&IONS\n/\n&CELL\n/\nATOMIC_SPECIES\nSi 28.0855 si_pbe_gbrv_1.0.upf\nCELL_PARAMETERS angstrom\n3.867000000 0.000000000 0.000000000\n1.933500000 3.348920236 0.000000000\n1.933500000 1.116306745 3.157392278\nATOMIC_POSITIONS crystal\nSi 0.000000000 0.000000000 0.000000000\nSi 0.250000000 0.250000000 0.250000000\nK_POINTS automatic\n2 2 2 0 0 0",
                    "name": "pw_scf.in"
                  }
                ]
              },
              "flowchartId": "pw-scf",
              "head": true,
              "monitors": [
                {
                  "data": [
                    1.4026394168011649,
                    0.5946081794827971,
                    0.006968158142486594,
                    0.000969405970227804,
                    0.00003891229578738975,
                    0.000007347076826989673
                  ],
                  "name": "electronic",
                  "units": "eV"
                },
                {
                  "name": "standard_output"
                }
              ],
              "name": "pw_scf",
              "postProcessors": [],
              "preProcessors": [],
              "results": [
                {
                  "name": "total_energy",
                  "units": "eV",
                  "value": -258.62939528928314
                },
                {
                  "ewald": {
                    "name": "ewald",
                    "value": -226.941256604257
                  },
                  "exchangeCorrelation": {
                    "name": "exchange_correlation",
                    "value": -118.06522851215864
                  },
                  "harrisFoulkes": {
                    "name": "harris_foulkes",
                    "value": -258.62938957489007
                  },
                  "hartree": {
                    "name": "hartree",
                    "value": 17.723393566555778
                  },
                  "name": "total_energy_contributions",
                  "oneElectron": {
                    "name": "one_electron",
                    "value": 68.65369626057674
                  },
                  "smearing": {
                    "name": "smearing",
                    "value": 0
                  },
                  "units": "eV"
                },
                {
                  "name": "pressure",
                  "units": "kbar",
                  "value": 73.71
                },
                {
                  "name": "fermi_energy",
                  "units": "eV",
                  "value": 6.607916337990446
                },
                {
                  "name": "atomic_forces",
                  "units": "eV",
                  "value": [
                    [
                      0,
                      0,
                      -0.00000116
                    ],
                    [
                      0,
                      0,
                      0.00000116
                    ]
                  ]
                },
                {
                  "name": "total_forces",
                  "units": "eV",
                  "value": 0.000002
                },
                {
                  "name": "stress_tensor",
                  "units": "kbar",
                  "value": [
                    [
                      0.00050111,
                      0,
                      0
                    ],
                    [
                      0,
                      0.00050111,
                      0
                    ],
                    [
                      0,
                      0,
                      0.00050096
                    ]
                  ]
                }
              ],
              "status": "complete",
              "type": "execution"
            }
          ]
        }
      },
      "subsubtype": "PBE",
      "subtype": "GGA",
      "type": "DFT"
    },
    "owner": {
      "_id": "k8uubJNniCHuydoNF",
      "name": "exadmin",
      "type": 0
    },
    "status": "finished",
    "statusTrack": [
      {
        "status": "pre-submission",
        "trackedAt": 1487170982035
      },
      {
        "status": "submitted",
        "trackedAt": 1487170985238
      },
      {
        "status": "active",
        "trackedAt": 1487170989234
      },
      {
        "status": "finished",
        "trackedAt": 1487170992492
      }
    ],
    "title": "New Job Feb 15th 2017, 18:32 PM",
    "titleSlug": "new-job-feb-15th-2017-18-32-pm",
    "updatedAt": "2017-02-15T15:03:12.587Z",
    "version": "0.1.1"
  },
  "status": "success"
}
```
</details>

<details>
    <summary>get job by property. The original query before encoding is `query={"status": "finished"}`</summary>
```bash
curl -X GET https://platform.exabyte.io/api/v1/jobs?query%3D%7B%22status%22%3A+%22finished%22%7D -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```
```bash
{
  "data": [
    {
      "_id": "RhCFP2WuehvG4hCLp",
      "_material": {
        "_id": "gyfPHZk56QAxRpAqv",
        "exabyteId": "ixAXcDT9DJcCP4GrY",
        "name": "Silicon FCC"
      },
      "_project": {
        "_id": "Wk8F7azNhP3R5j6GG",
        "access": {
          "level": 10,
          "type": 0
        },
        "goldName": "exadmin",
        "name": "exadmin",
        "owner": {
          "_id": "k8uubJNniCHuydoNF",
          "name": "exadmin",
          "type": 0
        },
        "slug": "exadmin"
      },
      "compute": {
        "arguments": {},
        "cluster": {
          "fqdn": "master-vagrant-cluster-001.exabyte.io",
          "jid": "2.master-vagrant-cluster-001.exabyte.io"
        },
        "email": "admin@exabyte.io",
        "nodes": 1,
        "notify": "n",
        "ppn": 1,
        "queue": "D",
        "timeLimit": "01:00:00"
      },
      "createdAt": "2017-02-15T15:03:02.032Z",
      "creator": {
        "_id": "k8uubJNniCHuydoNF",
        "username": "exadmin"
      },
      "friendlySlugs": {
        "titleSlug": {
          "base": "new-job-feb-15th-2017-18-32-pm",
          "index": 0
        }
      },
      "model": {
        "accuracy": 200,
        "method": {
          "data": {
            "pseudo": [
              {
                "_id": "58947f5efe450067c9c92e24",
                "access": {
                  "level": 0,
                  "type": 0
                },
                "apps": [
                  "espresso"
                ],
                "characteristics": [
                  {
                    "name": "total_energy",
                    "units": "eV",
                    "value": -130.568347569
                  },
                  {
                    "name": "zero_point_energy",
                    "units": "eV",
                    "value": -0.04545053892
                  }
                ],
                "element": "Si",
                "exchangeCorrelation": {
                  "approximation": "gga",
                  "functional": "pbe"
                },
                "filename": "si_pbe_gbrv_1.0.upf",
                "path": "/export/share/pseudo/si/gga/pbe/gbrv/1.0/us/si_pbe_gbrv_1.0.upf",
                "source": "gbrv",
                "textHeading": "0                   Version Number\n  Si                   Element\n   US                  Ultrasoft pseudopotential\n    T                  Nonlinear Core Correction\nSLA  PW   PBE  PBE     PBE  Exchange-Correlation functional\n    4.00000000000      Z valence\n   -9.19868380872      Total energy\n    0.00000    0.00000 Suggested cutoff for wfc and rho\n    2                  Max angular momentum component\n  899                  Number of points in mesh\n    2    6             Number of Wavefunctions, Number of Projectors\n Wavefunctions         nl  l   occ\n                       3S  0  2.00\n                       3P  1  2.00",
                "type": "us",
                "version": "1.0"
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
            },
            "kppra": 16
          },
          "subtype": "us",
          "type": "pseudo",
          "workflow": {
            "_id": "7GSofzPcxZryR8YiL",
            "app": "espresso",
            "ignore": false,
            "name": "Total Energy",
            "units": [
              {
                "execution": {
                  "app": {
                    "exec": "pw.x",
                    "flavor": "pw_scf",
                    "name": "espresso",
                    "summary": "Quantum Espresso",
                    "version": "5.4.0"
                  },
                  "input": [
                    {
                      "content": "&CONTROL\n    calculation= 'scf'\n    title= ''\n    verbosity= 'low'\n    restart_mode= 'from_scratch'\n    wf_collect= .true.\n    tstress= .true.\n    tprnfor= .true.\n    outdir= '$OUTPUT_DIR/'\n    wfcdir= '$OUTPUT_DIR/'\n    prefix= '__prefix__'\n    pseudo_dir= '$PSEUDO_DIR'\n/\n&SYSTEM\n    ibrav=0\n    nat=2\n    ntyp=1\n    ecutwfc= 40\n    ecutrho= 200\n    occupations= 'smearing'\n    degauss= 0.005\n/\n&ELECTRONS\n    diagonalization= 'david'\n    diago_david_ndim= 4\n    diago_full_acc= .true.\n    mixing_beta= 0.3\n    startingwfc='atomic+random'\n/\n&IONS\n/\n&CELL\n/\nATOMIC_SPECIES\nSi 28.0855 si_pbe_gbrv_1.0.upf\nCELL_PARAMETERS angstrom\n3.867000000 0.000000000 0.000000000\n1.933500000 3.348920236 0.000000000\n1.933500000 1.116306745 3.157392278\nATOMIC_POSITIONS crystal\nSi 0.000000000 0.000000000 0.000000000\nSi 0.250000000 0.250000000 0.250000000\nK_POINTS automatic\n2 2 2 0 0 0",
                      "name": "pw_scf.in"
                    }
                  ]
                },
                "flowchartId": "pw-scf",
                "head": true,
                "monitors": [
                  {
                    "data": [
                      1.4026394168011649,
                      0.5946081794827971,
                      0.006968158142486594,
                      0.000969405970227804,
                      0.00003891229578738975,
                      0.000007347076826989673
                    ],
                    "name": "electronic",
                    "units": "eV"
                  },
                  {
                    "name": "standard_output"
                  }
                ],
                "name": "pw_scf",
                "postProcessors": [],
                "preProcessors": [],
                "results": [
                  {
                    "name": "total_energy",
                    "units": "eV",
                    "value": -258.62939528928314
                  },
                  {
                    "ewald": {
                      "name": "ewald",
                      "value": -226.941256604257
                    },
                    "exchangeCorrelation": {
                      "name": "exchange_correlation",
                      "value": -118.06522851215864
                    },
                    "harrisFoulkes": {
                      "name": "harris_foulkes",
                      "value": -258.62938957489007
                    },
                    "hartree": {
                      "name": "hartree",
                      "value": 17.723393566555778
                    },
                    "name": "total_energy_contributions",
                    "oneElectron": {
                      "name": "one_electron",
                      "value": 68.65369626057674
                    },
                    "smearing": {
                      "name": "smearing",
                      "value": 0
                    },
                    "units": "eV"
                  },
                  {
                    "name": "pressure",
                    "units": "kbar",
                    "value": 73.71
                  },
                  {
                    "name": "fermi_energy",
                    "units": "eV",
                    "value": 6.607916337990446
                  },
                  {
                    "name": "atomic_forces",
                    "units": "eV",
                    "value": [
                      [
                        0,
                        0,
                        -0.00000116
                      ],
                      [
                        0,
                        0,
                        0.00000116
                      ]
                    ]
                  },
                  {
                    "name": "total_forces",
                    "units": "eV",
                    "value": 0.000002
                  },
                  {
                    "name": "stress_tensor",
                    "units": "kbar",
                    "value": [
                      [
                        0.00050111,
                        0,
                        0
                      ],
                      [
                        0,
                        0.00050111,
                        0
                      ],
                      [
                        0,
                        0,
                        0.00050096
                      ]
                    ]
                  }
                ],
                "status": "complete",
                "type": "execution"
              }
            ]
          }
        },
        "subsubtype": "PBE",
        "subtype": "GGA",
        "type": "DFT"
      },
      "owner": {
        "_id": "k8uubJNniCHuydoNF",
        "name": "exadmin",
        "type": 0
      },
      "status": "finished",
      "statusTrack": [
        {
          "status": "pre-submission",
          "trackedAt": 1487170982035
        },
        {
          "status": "submitted",
          "trackedAt": 1487170985238
        },
        {
          "status": "active",
          "trackedAt": 1487170989234
        },
        {
          "status": "finished",
          "trackedAt": 1487170992492
        }
      ],
      "title": "New Job Feb 15th 2017, 18:32 PM",
      "titleSlug": "new-job-feb-15th-2017-18-32-pm",
      "updatedAt": "2017-02-15T15:03:12.587Z",
      "version": "0.1.1"
    },
    ...
  ]
  "status": "success"
}
```
</details>


### Create

`POST` HTTP method is used to create a new job. Job parameters are passed in JSON format inside body.

<details>
    <summary>Create a new job:</summary>
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
```bash
{
  "data": {
    "_id": "HmeWjp69jHYkZYMkh",
    "_material": {
      "_id": "fusSBAHTGcnEqnEb2",
      "exabyteId": "KAtZXknJJRBYce5xp",
      "name": "Silicon FCC - supercell"
    },
    "_project": {
      "_id": "cYFTeEgfj5X6PNCxK",
      "access": {
        "level": 10,
        "type": 0
      },
      "goldName": "exadmin",
      "name": "exadmin",
      "owner": {
        "_id": "jnLJpf9vJKYtFoQxc",
        "name": "exadmin",
        "type": 0
      },
      "slug": "exadmin"
    },
    "compute": {
      "arguments": {},
      "cluster": {
        "fqdn": "AWS-cluster-001"
      },
      "nodes": 1,
      "notify": "n",
      "ppn": 1,
      "queue": "D",
      "timeLimit": "01:00:00"
    },
    "createdAt": "2017-03-09T14:33:47.995Z",
    "creator": {
      "_id": "jnLJpf9vJKYtFoQxc",
      "username": "exadmin"
    },
    "friendlySlugs": {
      "titleSlug": {
        "base": "new-job-feb-15th-2017-18-32-pm",
        "index": 0
      }
    },
    "model": {
      "accuracy": 200,
      "method": {
        "data": {
          "pseudo": [
            {
              "_id": "5759584013ce4c5848a6048a",
              "access": {
                "level": 0,
                "type": 0
              },
              "apps": [
                "espresso"
              ],
              "characteristics": [
                {
                  "name": "total_energy",
                  "units": "eV",
                  "value": -4022.12794602
                },
                {
                  "name": "zero_point_energy",
                  "units": "eV",
                  "value": -0.0021813732
                }
              ],
              "element": "Ag",
              "exchangeCorrelation": {
                "approximation": "gga",
                "functional": "pbe"
              },
              "filename": "ag_pbe_gbrv_1.4.upf",
              "path": "/export/share/pseudo/ag/gga/pbe/gbrv/1.4/us/ag_pbe_gbrv_1.4.upf",
              "source": "gbrv",
              "textHeading": "0                   Version Number\n  Ag                   Element\n   US                  Ultrasoft pseudopotential\n    T                  Nonlinear Core Correction\n SLA  PW   PBX  PBC    PBE  Exchange-Correlation functional\n   19.00000000000      Z valence\n -295.21248450600      Total energy\n    0.00000    0.00000 Suggested cutoff for wfc and rho\n    2                  Max angular momentum component\n  887                  Number of points in mesh\n    5    6             Number of Wavefunctions, Number of Projectors\n Wavefunctions         nl  l   occ\n                       4S  0  2.00\n                       4P  1  6.00\n                       4D  2 10.00\n                       5S  0  0.50\n                       5P  1  0.00",
              "type": "us",
              "version": "1.4"
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
          },
          "kppra": 16
        },
        "subtype": "us",
        "type": "pseudo",
        "workflow": {
          "_id": "8HFZ7zjrkeRjYsGvW",
          "app": "espresso",
          "ignore": false,
          "name": "Total Energy",
          "units": [
            {
              "execution": {
                "app": {
                  "exec": "pw.x",
                  "flavor": "pw_scf",
                  "name": "espresso",
                  "summary": "Quantum Espresso",
                  "version": "5.4.0"
                },
                "input": [
                  {
                    "content": "&CONTROL\n    calculation= 'scf'\n    title= ''\n    verbosity= 'low'\n    restart_mode= 'from_scratch'\n    wf_collect= .true.\n    tstress= .true.\n    tprnfor= .true.\n    outdir= '$OUTPUT_DIR/'\n    wfcdir= '$OUTPUT_DIR/'\n    prefix= '__prefix__'\n    pseudo_dir= '$PSEUDO_DIR'\n/\n&SYSTEM\n    ibrav=0\n    nat=16\n    ntyp=1\n    ecutwfc= 40\n    ecutrho= 200\n    occupations= 'smearing'\n    degauss= 0.005\n/\n&ELECTRONS\n    diagonalization= 'david'\n    diago_david_ndim= 4\n    diago_full_acc= .true.\n    mixing_beta= 0.3\n    startingwfc='atomic+random'\n/\n&IONS\n/\n&CELL\n/\nATOMIC_SPECIES\nSi 28.0855 \nCELL_PARAMETERS angstrom\n6.697840000 0.000000000 3.867000000\n2.232613000 6.314785000 3.867000000\n0.000000000 0.000000000 7.734000000\nATOMIC_POSITIONS crystal\nSi 0.000000000 0.000000000 0.000000000\nSi 0.000000000 0.000000000 0.500000000\nSi 0.000000000 0.500000000 0.000000000\nSi 0.000000000 0.500000000 0.500000000\nSi 0.500000000 0.000000000 0.000000000\nSi 0.500000000 0.000000000 0.500000000\nSi 0.500000000 0.500000000 0.000000000\nSi 0.500000000 0.500000000 0.500000000\nSi 0.125000000 0.125000000 0.125000000\nSi 0.125000000 0.125000000 0.625000000\nSi 0.125000000 0.625000000 0.125000000\nSi 0.125000000 0.625000000 0.625000000\nSi 0.625000000 0.125000000 0.125000000\nSi 0.625000000 0.125000000 0.625000000\nSi 0.625000000 0.625000000 0.125000000\nSi 0.625000000 0.625000000 0.625000000\nK_POINTS automatic\n1 1 1 0 0 0",
                    "name": "pw_scf.in"
                  }
                ]
              },
              "flowchartId": "pw-scf",
              "head": true,
              "monitors": [
                {
                  "name": "electronic"
                },
                {
                  "name": "standard_output"
                }
              ],
              "name": "pw_scf",
              "postProcessors": [],
              "preProcessors": [],
              "results": [
                {
                  "name": "total_energy"
                },
                {
                  "name": "total_energy_contributions"
                },
                {
                  "name": "pressure"
                },
                {
                  "name": "fermi_energy"
                },
                {
                  "name": "atomic_forces"
                },
                {
                  "name": "total_forces"
                },
                {
                  "name": "stress_tensor"
                }
              ],
              "status": "idle",
              "type": "execution"
            }
          ]
        }
      },
      "subsubtype": "PBE",
      "subtype": "GGA",
      "type": "DFT"
    },
    "owner": {
      "_id": "jnLJpf9vJKYtFoQxc",
      "name": "exadmin",
      "type": 0
    },
    "status": "pre-submission",
    "title": "New Job Feb 15th 2017, 18:32 PM",
    "titleSlug": "new-job-feb-15th-2017-18-32-pm",
    "version": "0.1.1"
  },
  "status": "success"
}
```
</details>

### Delete

`DELETE` HTTP method is used to delete a job with a given ID.

<details>
    <summary>Delete a job with a given ID:</summary>
```bash
curl -X DELETE https://platform.exabyte.io/api/v1/jobs/HmeWjp69jHYkZYMkh
```
```bash
{
  "status": "success",
  "data": {
    "message": "Job HmeWjp69jHYkZYMkh successfully deleted"
  }
}
```
</details>

### Update

`PATCH` HTTP method is used to update an existing job.

<details>
    <summary>Update a job:</summary>
```bash
curl -X PATCH https://platform.exabyte.io/api/v1/jobs/RhCFP2WuehvG4hCLp -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ" -d '{"title": "New Job Feb 15th 2017, 18:32 PM"}'
```
```bash
{
  "data": {
    "_id": "RhCFP2WuehvG4hCLp",
    "_material": {
      "_id": "gyfPHZk56QAxRpAqv",
      "exabyteId": "ixAXcDT9DJcCP4GrY",
      "name": "Silicon FCC"
    },
    "_project": {
      "_id": "Wk8F7azNhP3R5j6GG",
      "access": {
        "level": 10,
        "type": 0
      },
      "goldName": "exadmin",
      "name": "exadmin",
      "owner": {
        "_id": "k8uubJNniCHuydoNF",
        "name": "exadmin",
        "type": 0
      },
      "slug": "exadmin"
    },
    "compute": {
      "arguments": {},
      "cluster": {
        "fqdn": "master-vagrant-cluster-001.exabyte.io",
        "jid": "2.master-vagrant-cluster-001.exabyte.io"
      },
      "email": "admin@exabyte.io",
      "nodes": 1,
      "notify": "n",
      "ppn": 1,
      "queue": "D",
      "timeLimit": "01:00:00"
    },
    "createdAt": "2017-02-15T15:03:02.032Z",
    "creator": {
      "_id": "k8uubJNniCHuydoNF",
      "username": "exadmin"
    },
    "friendlySlugs": {
      "titleSlug": {
        "base": "new-job-feb-15th-2017-18-32-pm",
        "index": 0
      }
    },
    "model": {
      "accuracy": 200,
      "method": {
        "data": {
          "pseudo": [
            {
              "_id": "58947f5efe450067c9c92e24",
              "access": {
                "level": 0,
                "type": 0
              },
              "apps": [
                "espresso"
              ],
              "characteristics": [
                {
                  "name": "total_energy",
                  "units": "eV",
                  "value": -130.568347569
                },
                {
                  "name": "zero_point_energy",
                  "units": "eV",
                  "value": -0.04545053892
                }
              ],
              "element": "Si",
              "exchangeCorrelation": {
                "approximation": "gga",
                "functional": "pbe"
              },
              "filename": "si_pbe_gbrv_1.0.upf",
              "path": "/export/share/pseudo/si/gga/pbe/gbrv/1.0/us/si_pbe_gbrv_1.0.upf",
              "source": "gbrv",
              "textHeading": "0                   Version Number\n  Si                   Element\n   US                  Ultrasoft pseudopotential\n    T                  Nonlinear Core Correction\nSLA  PW   PBE  PBE     PBE  Exchange-Correlation functional\n    4.00000000000      Z valence\n   -9.19868380872      Total energy\n    0.00000    0.00000 Suggested cutoff for wfc and rho\n    2                  Max angular momentum component\n  899                  Number of points in mesh\n    2    6             Number of Wavefunctions, Number of Projectors\n Wavefunctions         nl  l   occ\n                       3S  0  2.00\n                       3P  1  2.00",
              "type": "us",
              "version": "1.0"
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
          },
          "kppra": 16
        },
        "subtype": "us",
        "type": "pseudo",
        "workflow": {
          "_id": "7GSofzPcxZryR8YiL",
          "app": "espresso",
          "ignore": false,
          "name": "Total Energy",
          "units": [
            {
              "execution": {
                "app": {
                  "exec": "pw.x",
                  "flavor": "pw_scf",
                  "name": "espresso",
                  "summary": "Quantum Espresso",
                  "version": "5.4.0"
                },
                "input": [
                  {
                    "content": "&CONTROL\n    calculation= 'scf'\n    title= ''\n    verbosity= 'low'\n    restart_mode= 'from_scratch'\n    wf_collect= .true.\n    tstress= .true.\n    tprnfor= .true.\n    outdir= '$OUTPUT_DIR/'\n    wfcdir= '$OUTPUT_DIR/'\n    prefix= '__prefix__'\n    pseudo_dir= '$PSEUDO_DIR'\n/\n&SYSTEM\n    ibrav=0\n    nat=2\n    ntyp=1\n    ecutwfc= 40\n    ecutrho= 200\n    occupations= 'smearing'\n    degauss= 0.005\n/\n&ELECTRONS\n    diagonalization= 'david'\n    diago_david_ndim= 4\n    diago_full_acc= .true.\n    mixing_beta= 0.3\n    startingwfc='atomic+random'\n/\n&IONS\n/\n&CELL\n/\nATOMIC_SPECIES\nSi 28.0855 si_pbe_gbrv_1.0.upf\nCELL_PARAMETERS angstrom\n3.867000000 0.000000000 0.000000000\n1.933500000 3.348920236 0.000000000\n1.933500000 1.116306745 3.157392278\nATOMIC_POSITIONS crystal\nSi 0.000000000 0.000000000 0.000000000\nSi 0.250000000 0.250000000 0.250000000\nK_POINTS automatic\n2 2 2 0 0 0",
                    "name": "pw_scf.in"
                  }
                ]
              },
              "flowchartId": "pw-scf",
              "head": true,
              "monitors": [
                {
                  "data": [
                    1.4026394168011649,
                    0.5946081794827971,
                    0.006968158142486594,
                    0.000969405970227804,
                    0.00003891229578738975,
                    0.000007347076826989673
                  ],
                  "name": "electronic",
                  "units": "eV"
                },
                {
                  "name": "standard_output"
                }
              ],
              "name": "pw_scf",
              "postProcessors": [],
              "preProcessors": [],
              "results": [
                {
                  "name": "total_energy",
                  "units": "eV",
                  "value": -258.62939528928314
                },
                {
                  "ewald": {
                    "name": "ewald",
                    "value": -226.941256604257
                  },
                  "exchangeCorrelation": {
                    "name": "exchange_correlation",
                    "value": -118.06522851215864
                  },
                  "harrisFoulkes": {
                    "name": "harris_foulkes",
                    "value": -258.62938957489007
                  },
                  "hartree": {
                    "name": "hartree",
                    "value": 17.723393566555778
                  },
                  "name": "total_energy_contributions",
                  "oneElectron": {
                    "name": "one_electron",
                    "value": 68.65369626057674
                  },
                  "smearing": {
                    "name": "smearing",
                    "value": 0
                  },
                  "units": "eV"
                },
                {
                  "name": "pressure",
                  "units": "kbar",
                  "value": 73.71
                },
                {
                  "name": "fermi_energy",
                  "units": "eV",
                  "value": 6.607916337990446
                },
                {
                  "name": "atomic_forces",
                  "units": "eV",
                  "value": [
                    [
                      0,
                      0,
                      -0.00000116
                    ],
                    [
                      0,
                      0,
                      0.00000116
                    ]
                  ]
                },
                {
                  "name": "total_forces",
                  "units": "eV",
                  "value": 0.000002
                },
                {
                  "name": "stress_tensor",
                  "units": "kbar",
                  "value": [
                    [
                      0.00050111,
                      0,
                      0
                    ],
                    [
                      0,
                      0.00050111,
                      0
                    ],
                    [
                      0,
                      0,
                      0.00050096
                    ]
                  ]
                }
              ],
              "status": "complete",
              "type": "execution"
            }
          ]
        }
      },
      "subsubtype": "PBE",
      "subtype": "GGA",
      "type": "DFT"
    },
    "owner": {
      "_id": "k8uubJNniCHuydoNF",
      "name": "exadmin",
      "type": 0
    },
    "status": "finished",
    "statusTrack": [
      {
        "status": "pre-submission",
        "trackedAt": 1487170982035
      },
      {
        "status": "submitted",
        "trackedAt": 1487170985238
      },
      {
        "status": "active",
        "trackedAt": 1487170989234
      },
      {
        "status": "finished",
        "trackedAt": 1487170992492
      }
    ],
    "title": "New Job Feb 15th 2017, 18:32 PM",
    "titleSlug": "new-job-feb-15th-2017-18-32-pm",
    "updatedAt": "2017-02-15T15:03:12.587Z",
    "version": "0.1.1"
  },
  "status": "success"
}
```
</details>

### Job Submission

`POST` HTTP method with `submit` URL paramater are used to submit a job with a given.

<details>
    <summary>Submit a job:</summary>
```bash
curl -X POST https://platform.exabyte.io/api/v1/jobs/RhCFP2WuehvG4hCLp?submit=true -H "X-Auth-Token: f2KpRW7KeN9aPmjSZ" -H "X-User-Id: fbdpsNf4oHiX79vMJ"
```
```bash

```
</details>

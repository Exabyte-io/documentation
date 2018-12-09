In order to organize and store the information about workflows we employ [Exabyte Data Convention](../data-structured/overview.md) as explained elsewhere in this documentation.

# Example Representation

Below is an example JSON representation a of a workflow. It contains five *subworkflows*, each of which contains a number of *units* in turn. The workflow demonstrates implements a many-body (GW) calculation of an electronic band gap with VASP:

```json
{
    "name": "Single-shot G0W0 Band Gap",
    "subworkflows": [
        {
            "_id": "17b7404f8f8dbecb7278c4f8",
            // information about the application (or simulation engine) used in this subworkflow (SW)
            "app": {
                "build": "Default",
                "name": "vasp",
                "summary": "VASP",
                "version": "5.3.5"
            },
            // whether to omit storing the resulting properties in database (eg. during prototyping)
            "isDraft": false,
            // model used inside this SW
            "model": {
                "method": {
                    "subtype": "us",
                    "type": "pseudopotential"
                },
                "subtype": "gga",
                "type": "dft"
            },
            // SW name
            "name": "SCF",
            // materials properties extracted in this SW
            "properties": [
                "total_energy",
                "total_energy_contributions",
                "pressure",
                "fermi_energy",
                "atomic_forces",
                "total_force",
                "stress_tensor",
                "band_gaps",
                "fermi_energy"
            ],
            // units that constitute this SW
            "units": [
                {
                    "name": "vasp",
                    "execution": {
                        "app": {
                            "build": "Default",
                            "exec": "vasp",
                            "flavor": "vasp",
                            "name": "vasp",
                            "summary": "VASP",
                            "version": "5.3.5"
                        },
                        // contains the input files/templates for simulation engine
                        "input": [
                            {
                                // input file name (will be stored under it in filesystem)
                                "name": "KPOINTS",
                                // Jinja template to be used for producing the input in Workflow Designer
                                "content": "Automatic mesh\n0\nGamma\n  {% for d in kgrid.dimensions %}{{ d/2 }} {% endfor %}\n  {% for s in kgrid.shifts %}{{s}} {% endfor %}\n",
                                // Final input file content after render in Workflow Designer
                                //     May still contain template variables to be rendered at runtime
                                "rendered": "Automatic mesh\n0\nGamma\n  5 5 5 \n  0 0 0 \n"
                            },
                            {
                                "content": "ISMEAR = 0\nSIGMA  = 0.05\n",
                                "isManuallyChanged": false,
                                "name": "INCAR",
                                "rendered": "ISMEAR = 0\nSIGMA  = 0.05\n"
                            },
                            {
                                "content": "{{ POSCAR }}",
                                "isManuallyChanged": false,
                                "name": "POSCAR",
                                "rendered": "Silicon FCC\n1.0\n   3.348920000\t   0.000000000\t   1.933500000\n   1.116307000\t   3.157392000\t   1.933500000\n   0.000000000\t   0.000000000\t   3.867000000\nSi\n2\ndirect\n   0.000000000    0.000000000    0.000000000 Si\n   0.250000000    0.250000000    0.250000000 Si"
                            }
                        ]
                    },
                    // Important settings for this unit (k-point grid)
                    "important": {
                        "kgrid": {
                            "dimensions": [
                                10,
                                10,
                                10
                            ],
                            "shifts": [
                                0,
                                0,
                                0
                            ]
                        }
                    },
                    "monitors": [
                        {
                            "name": "standard_output"
                        },
                        {
                            "name": "convergence_electronic"
                        }
                    ],
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
                            "name": "total_force"
                        },
                        {
                            "name": "stress_tensor"
                        }
                    ],
                    "status": "idle",
                    "type": "execution"
                }
            ]
        },
        {
            "_id": "e230f0ee0ed5074211c47715",
            "app": {
                "build": "Default",
                "name": "shell",
                "summary": "Shell Script",
                "version": "4.2.46"
            },
            "model": {
                "method": {
                    "subtype": "unknown",
                    "type": "unknown"
                },
                "subtype": "unknown",
                "type": "unknown"
            },
            "name": "Grep NBANDS",
            "properties": [],
            "units": [
                {
                    "execution": {
                        "app": {
                            "build": "Default",
                            "exec": "sh",
                            "flavor": "sh",
                            "name": "shell",
                            "summary": "Shell Script",
                            "version": "4.2.46"
                        },
                        "input": [
                            {
                                "content": "#!/bin/bash\n\n# grep the maximum number of plane-wave allowed for the basis set with chosen ENCUT \ngrep \"maximum and minimum number of plane-waves\" OUTCAR | tail -1 | awk '{print $10}' ",
                                "isManuallyChanged": false,
                                "name": "script.sh",
                                "rendered": "#!/bin/bash\n\n# grep the maximum number of plane-wave allowed for the basis set with chosen ENCUT \ngrep \"maximum and minimum number of plane-waves\" OUTCAR | tail -1 | awk '{print $10}' "
                            }
                        ]
                    },
                    "important": {},
                    "monitors": [
                        {
                            "name": "standard_output"
                        }
                    ],
                    "name": "shell",
                    "postProcessors": [],
                    "preProcessors": [],
                    "results": [],
                    "status": "idle",
                    "type": "execution"
                }
            ]
        },
        {
            "_id": "52ff2b4d94c26a3787c4ef8d",
            "app": {
                "build": "Default",
                "name": "vasp",
                "summary": "VASP",
                "version": "5.3.5"
            },
            "model": {
                "method": {
                    "subtype": "us",
                    "type": "pseudopotential"
                },
                "subtype": "gga",
                "type": "dft"
            },
            "name": "SCF many bands",
            "properties": [],
            "units": [
                {
                    "execution": {
                        "app": {
                            "build": "Default",
                            "exec": "vasp",
                            "flavor": "vasp_nscf",
                            "name": "vasp",
                            "summary": "VASP",
                            "version": "5.3.5"
                        },
                        "input": [
                            {
                                "content": "ISMEAR = 0\nSIGMA = 0.05\nNBANDS = {%raw%} {{shell.stdout}} {%endraw%} \nALGO = EXACT # does exact diagonalization of Kohn-Sham Hamiltonian \nNELM = 1 # 1 electronic step is enough\nLOPTICS = .TRUE. # long-wave limit q->0 to write WAVEDER file  \n",
                                "isManuallyChanged": false,
                                "name": "INCAR",
                                "rendered": "ISMEAR = 0\nSIGMA = 0.05\nNBANDS =  {{shell.stdout}}  \nALGO = EXACT # does exact diagonalization of Kohn-Sham Hamiltonian \nNELM = 1 # 1 electronic step is enough\nLOPTICS = .TRUE. # long-wave limit q->0 to write WAVEDER file  \n"
                            },
                            {
                                "content": "Automatic mesh\n0\nGamma\n  {% for d in kgrid.dimensions %}{{d/2}} {% endfor %}\n  {% for s in kgrid.shifts %}{{s}} {% endfor %}\n",
                                "isManuallyChanged": false,
                                "name": "KPOINTS",
                                "rendered": "Automatic mesh\n0\nGamma\n  5 5 5 \n  0 0 0 \n"
                            },
                            {
                                "content": "{{ POSCAR }}",
                                "isManuallyChanged": false,
                                "name": "POSCAR",
                                "rendered": "Silicon FCC\n1.0\n   3.348920000\t   0.000000000\t   1.933500000\n   1.116307000\t   3.157392000\t   1.933500000\n   0.000000000\t   0.000000000\t   3.867000000\nSi\n2\ndirect\n   0.000000000    0.000000000    0.000000000 Si\n   0.250000000    0.250000000    0.250000000 Si"
                            }
                        ]
                    },
                    "important": {
                        "kgrid": {
                            "dimensions": [
                                10,
                                10,
                                10
                            ],
                            "shifts": [
                                0,
                                0,
                                0
                            ]
                        },
                        "kpath": [
                            {
                                "point": "Г",
                                "steps": 10
                            },
                            {
                                "point": "X",
                                "steps": 10
                            }
                        ]
                    },
                    "monitors": [
                        {
                            "name": "standard_output"
                        },
                        {
                            "name": "convergence_electronic"
                        }
                    ],
                    "name": "vasp_nscf",
                    "postProcessors": [],
                    "preProcessors": [],
                    "results": [
                        {
                            "name": "band_gaps"
                        },
                        {
                            "name": "fermi_energy"
                        }
                    ],
                    "status": "idle",
                    "type": "execution"
                }
            ]
        },
        {
            "_id": "b053d1575dffe7e1a7ba6fac",
            "app": {
                "build": "Default",
                "name": "shell",
                "summary": "Shell Script",
                "version": "4.2.46"
            },
            "model": {
                "method": {
                    "subtype": "us",
                    "type": "pseudopotential"
                },
                "subtype": "gga",
                "type": "dft"
            },
            "name": "extract NBANDS",
            "properties": [],
            "units": [
                {
                    "execution": {
                        "app": {
                            "build": "Default",
                            "exec": "sh",
                            "flavor": "sh",
                            "name": "shell",
                            "summary": "Shell Script",
                            "version": "4.2.46"
                        },
                        "input": [
                            {
                                "content": "#!/bin/bash\n\n# PUT YOUR CODE BELOW\ngrep NBANDS OUTCAR| tail -1 | awk '{print $15}' ",
                                "isManuallyChanged": false,
                                "name": "script.sh",
                                "rendered": "#!/bin/bash\n\n# PUT YOUR CODE BELOW\ngrep NBANDS OUTCAR| tail -1 | awk '{print $15}' "
                            }
                        ]
                    },
                    "important": {},
                    "monitors": [
                        {
                            "name": "standard_output"
                        }
                    ],
                    "name": "sh",
                    "postProcessors": [],
                    "preProcessors": [],
                    "results": [],
                    "status": "idle",
                    "type": "execution"
                }
            ]
        },
        {
            "_id": "4039e61d74ebf977036459de",
            "app": {
                "build": "Default",
                "name": "vasp",
                "summary": "VASP",
                "version": "5.3.5"
            },
            "model": {
                "method": {
                    "subtype": "us",
                    "type": "pseudopotential"
                },
                "subtype": "gga",
                "type": "dft"
            },
            "name": "G0W0 step",
            "properties": [],
            "units": [
                {
                    "execution": {
                        "app": {
                            "build": "Default",
                            "exec": "vasp",
                            "flavor": "vasp",
                            "name": "vasp",
                            "summary": "VASP",
                            "version": "5.3.5"
                        },
                        "input": [
                            {
                                "content": "ISMEAR = 0\nSIGMA  = 0.05\nLORBIT = 11\nALGO = GW0 ; NELM = 1 ! one-shot GW calculation, ie G0W0\nNOMEGA = 100 \n",
                                "isManuallyChanged": false,
                                "name": "INCAR",
                                "rendered": "ISMEAR = 0\nSIGMA  = 0.05\nLORBIT = 11\nALGO = GW0 ; NELM = 1 ! one-shot GW calculation, ie G0W0\nNOMEGA = 100 \n"
                            },
                            {
                                "content": "Automatic mesh\n0\nGamma\n  {% for d in kgrid.dimensions %}{{d/2}} {% endfor %}\n  {% for s in kgrid.shifts %}{{s}} {% endfor %}\n",
                                "isManuallyChanged": false,
                                "name": "KPOINTS",
                                "rendered": "Automatic mesh\n0\nGamma\n  5 5 5 \n  0 0 0 \n"
                            },
                            {
                                "content": "{{ POSCAR }}",
                                "isManuallyChanged": false,
                                "name": "POSCAR",
                                "rendered": "Silicon FCC\n1.0\n   3.348920000\t   0.000000000\t   1.933500000\n   1.116307000\t   3.157392000\t   1.933500000\n   0.000000000\t   0.000000000\t   3.867000000\nSi\n2\ndirect\n   0.000000000    0.000000000    0.000000000 Si\n   0.250000000    0.250000000    0.250000000 Si"
                            }
                        ]
                    },
                    "important": {},
                    "monitors": [
                        {
                            "name": "standard_output"
                        },
                        {
                            "name": "convergence_electronic"
                        }
                    ],
                    "name": "vasp",
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
                            "name": "band_gaps"
                        }
                    ],
                    "status": "idle",
                    "type": "execution"
                }
            ]
        }
    ],
    // container for workflow (top-level) units
    //  each member is a subworkflow in the current document
    "units": [
        {
            "type": "subworkflow"
        },
        {
            "type": "subworkflow"
        },
        {
            "type": "subworkflow"
        },
        {
            "type": "subworkflow"
        },
        {
            "type": "subworkflow"
        }
    ],
    // global id of this material inside Exabyte Database
    "exabyteId": "QTCfaBWmpZsgH9HsN",
    "createdAt": "2017-10-11T03:22:10.376Z",
    "updatedAt": "2017-10-13T15:09:51.009Z"
}
```

> Note: JSON does not support inclusion of inline commentaries, we only left them above for clarity.

# Notes

There are a few notable points to emphasize from the example above.

## Nested data

We use top-level workflow as a "container" and separate the details of each individual section of calculation inside a subworkflow.

## Execution Units 

For physics-based modeling engines the execution unit is the main one. It contains the information about the input parameters and runtime environment for the specific simulation engine.

## Templating

We allow for using Jinja templates [1](#links) inside the input to individual units. This way we can decouple material-specific information from workflow-specific. The latter lets us apply a workflow for multiple materials at the same time without having to adjust it extensively. More inside [units](units.md) section.

## Properties

"properties" section serves as an aggregator of all the properties that are extracted at each level (workflow/subworkflow). "results" key serves the same purpose for unit.  

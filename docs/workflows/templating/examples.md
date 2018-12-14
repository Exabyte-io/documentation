# Templating Examples

The present page contains examples of [templates](overview.md), implemented under the [Jinja templating language](engine.md), for automating the generation of input scripts for the [simulation engines](../../software-directory/overview.md) currently supported on our platform.

## Quantum ESPRESSO Example

For example, the input file template shown in the expandable section below, for a basic [Quantum ESPRESSO](../../software-directory/modeling/quantum-espresso.md) "self-consistent field" total-energy computation, contains data that will be different for different materials, such as the number of atoms (under the "nat" flag). 

### Template

<details markdown="1">
  <summary>
     Expand to view
  </summary> 

```jinja2
&CONTROL
    calculation = 'scf'
    title = ''
    verbosity = 'low'
    restart_mode = '{{ input.RESTART_MODE }}'
    wf_collect = .true.
    tstress = .true.
    tprnfor = .true.
    outdir = {% raw %}'{{ JOB_WORK_DIR }}/outdir'{% endraw %}
    wfcdir = {% raw %}'{{ JOB_WORK_DIR }}/outdir'{% endraw %}
    prefix = '__prefix__'
    pseudo_dir = {% raw %}'{{ JOB_WORK_DIR }}/pseudo'{% endraw %}
/
&SYSTEM
    ibrav = {{ input.IBRAV }}
    nat = {{ input.NAT }}
    ntyp = {{ input.NTYP }}
    ecutwfc = {{ cutoffs.wavefunction }}
    ecutrho = {{ cutoffs.density }}
    occupations = 'smearing'
    degauss = 0.005
/
&ELECTRONS
    diagonalization = 'david'
    diago_david_ndim = 4
    diago_full_acc = .true.
    mixing_beta = 0.3
    startingwfc = 'atomic+random'
/
&IONS
/
&CELL
/
ATOMIC_SPECIES
{{ input.ATOMIC_SPECIES }}
ATOMIC_POSITIONS crystal
{{ input.ATOMIC_POSITIONS }}
CELL_PARAMETERS angstrom
{{ input.CELL_PARAMETERS }}
K_POINTS automatic
{% for d in kgrid.dimensions %}{{d}} {% endfor %}{% for s in kgrid.shifts %}{{s}} {% endfor %}
```

</details>

### Context

<details markdown="1">
  <summary>
     Expand to view
  </summary> 

```jinja2
{
    "kgridExtraData": {
        "materialHash": "a665723ef7429caef6ca89385fe25bae"
    },
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
        ],
        "KPPRA": 2000,
        "preferKPPRA": false
    },
    "inputExtraData": {
        "materialHash": "a665723ef7429caef6ca89385fe25bae"
    },
    "input": {
        "IBRAV": 0,
        "RESTART_MODE": "from_scratch",
        "NAT": 2,
        "NTYP": 1,
        "ATOMIC_POSITIONS": "Si 0.000000000 0.000000000 0.000000000\nSi 0.250000000 0.250000000 0.250000000",
        "CELL_PARAMETERS": "3.348920236 0.000000000 1.933500000\n1.116306745 3.157392278 1.933500000\n0.000000000 0.000000000 3.867000000",
        "ATOMIC_SPECIES": "Si 28.0855 si_pbe_gbrv_1.0.upf"
    },
    "isInputEdited": false,
    "cutoffsExtraData": {
        "materialHash": "a665723ef7429caef6ca89385fe25bae"
    },
    "cutoffs": {
        "wavefunction": 40,
        "density": 200
    }
}
```

</details>

### Rendered Output

#### Design-time

For Silicon FCC as a default material, the resulting text of the unit input, as rendered at Design-time from the above template and associated context, will be as shown in the following expandable section.

<details markdown="1">
  <summary>
     Expand to view
  </summary> 

```fortran
&CONTROL
    calculation = 'scf'
    title = ''
    verbosity = 'low'
    restart_mode = 'from_scratch'
    wf_collect = .true.
    tstress = .true.
    tprnfor = .true.
    outdir = '{{ JOB_WORK_DIR }}/outdir'
    wfcdir = '{{ JOB_WORK_DIR }}/outdir'
    prefix = '__prefix__'
    pseudo_dir = '{{ JOB_WORK_DIR }}/pseudo'
/
&SYSTEM
    ibrav = 0
    nat = 2
    ntyp = 1
    ecutwfc = 40
    ecutrho = 200
    occupations = 'smearing'
    degauss = 0.005
/
&ELECTRONS
    diagonalization = 'david'
    diago_david_ndim = 4
    diago_full_acc = .true.
    mixing_beta = 0.3
    startingwfc = 'atomic+random'
/
&IONS
/
&CELL
/
ATOMIC_SPECIES
Si 28.0855 si_pbe_gbrv_1.0.upf
ATOMIC_POSITIONS crystal
Si 0.000000000 0.000000000 0.000000000
Si 0.250000000 0.250000000 0.250000000
CELL_PARAMETERS angstrom
3.348920236 0.000000000 1.933500000
1.116306745 3.157392278 1.933500000
0.000000000 0.000000000 3.867000000
K_POINTS automatic
10 10 10 0 0 0 
```

</details>

#### Execution Time

In the rendered text of the unit above, there are still namelist flags that are not resolved, such as `{{JOB_WORK_DIR}}`. These are only rendered during the ensuing Execution-time, as explained [here](exabyte-conventions.md#"raw"-syntax-for-execution-variables-in-web-context).

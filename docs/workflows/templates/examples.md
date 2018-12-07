# Templating

We allow for using **Jinja templates** [^1] inside the input to individual [units](../components/units.md). This way we can decouple material-specific information from workflow-specific. The latter lets us apply a workflow for multiple materials at the same time, without having to adjust it extensively.

## Design-time Render

Input templates are first rendered during the [job design](../../jobs-designer/overview.md), where multiple materials can be selected within a single job design session.

For example, the input file template shown below for a basic [Quantum ESPRESSO](../../software/modeling/quantum-espresso.md) computation contains data that will be different for different materials, such as the number of atoms (under the "nat" flag).


## Template
```jinja
&CONTROL
    calculation = 'scf'
    title = ''
    verbosity = 'low'
    restart_mode = '{{ RESTART_MODE }}'
    wf_collect = .true.
    tstress = .true.
    tprnfor = .true.
    outdir = '{{ JOB_WORK_DIR }}/outdir'
    wfcdir = '{{ JOB_WORK_DIR }}/outdir'
    prefix = '__prefix__'
    pseudo_dir = '{{ JOB_WORK_DIR }}/pseudo'
/
&SYSTEM
    ibrav = {{ IBRAV }}
    nat = {{ NAT }}
    ntyp = {{ NTYP }}
    ecutwfc = {{ ECUTWFC }}
    ecutrho = {{ ECUTRHO }}
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
{{ ATOMIC_SPECIES }}
ATOMIC_POSITIONS crystal
{{ ATOMIC_POSITIONS }}
CELL_PARAMETERS angstrom
{{ CELL_PARAMETERS }}
K_POINTS automatic
{% for d in kgrid.dimensions %}{{d}} {% endfor %}{% for s in kgrid.shifts %}{{s}} {% endfor %}
```

For Silicon FCC as a default material, the resulting rendered text of the unit input, using the above template, will be the following.


## Rendered
```fortran
&CONTROL
    calculation = 'scf'
    title = ''
    verbosity = 'low'
    restart_mode = 'from_scratch'
    wf_collect = .true.
    tstress = .true.
    tprnfor = .true.
    outdir = '{{JOB_WORK_DIR}}/outdir'
    wfcdir = '{{JOB_WORK_DIR}}/outdir'
    prefix = '__prefix__'
    pseudo_dir = '{{JOB_WORK_DIR}}/pseudo'
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
3.348920000 0.000000000 1.933500000
1.116307000 3.157392000 1.933500000
0.000000000 0.000000000 3.867000000
K_POINTS automatic
10 10 10 0 0 0 
```

## Include Context (template data in Workflow Designer)

## Run-time Render

In the rendered text of the unit above there are still namelist flags that are not resolved, such as `{{JOB_WORK_DIR}}`. These are system-level [Environment Variables](../../jobs-cli/batch-scripts/directives.md#environment-variables) that will be resolved during the runtime. Thus, the job work directory will be automatically assigned based on the account and job/workflow information at the time of job execution.

## Editing Input

There are two ways to edit the input of an individual unit: either by editing the template inside the workflow (in this case **all** jobs created with this workflow will inherit the changes), or by editing the template or preview during job creation (in this case only one job, or multiple jobs created from the modified one, will have their input changed).

## Links

[^1]: [Jinja templating engine](http://jinja.pocoo.org/)

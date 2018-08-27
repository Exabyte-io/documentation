# Unit input templates

Unit input templates allow input text scripts to be entered automatically, and to be subsequently fed to the simulation engine being employed as part of the present unit calculation. The original input script templates, as well as their final preview appearances, can be inspected at the bottom of the [Unit Editor interface](../unit-editor.md) page for the elementary unit under consideration. The typical appearance of an input template within the Unit Editor interface, for the specific example of a "pw_scf" self-consistent field total ground-state energy unit calculation using the pw.x executable of the Quantum ESPRESSO DFT simulation package, is depicted on the left-hand side in the image below:

![](/images/input-template.png)

The reader is referred to the Quantum ESPRESSO-specific [documentation page](/applications/quantum-espresso.md), and to its official online documentation page pertaining specifically to the pw.x executable code [[1](#links)], for a detailed description of the meaning of the various input commands displayed in the above image example of input script template. The equivalent documentation for VASP can be accessed [here](/applications/vasp.md).

# Template Data

By clicking on the `Template Data` button to the right of the unit input template, under the "Template" tab at the bottom of the Unit Editor interface, the user can inspect the corresponding JSON representation from which the  input data necessary to assemble the template is directly extracted. The templates themselves are built starting from this JSON data using the Jinja2 template engine [[2](#links)]. 

The user can notice that some scripting commands are allowed as part of the template syntax, such as the "for" loop contained in the final line of the template for defining the size of the grid of k-points employed as part of the current "pw_scf" computation, according to the specific format of Quantum ESPRESSO input scripts [[1](#links)].

The JSON data representation interface can be exited at any time to return to the previous view by clicking on the three-dotted button at its top-right corner.


# Example JSON Representation

The example of a JSON data structure, containing the input data for the template of a "pw_scf" unit computation on silicon with Quantum ESPRESSO, is shown in the expandable section below. 

## JSON source

<details>
  <summary>
     "Expand to view": ...
  </summary> 

```json
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


# Example Unit Input Template

An example of Jinja2-generated input template based upon the above JSON source data, and referring to the same "pw_scf" unit calculation, can be viewed in the expandable section below:

<details>
  <summary>
     "Expand to view": ...
  </summary> 

```Jinja2
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


# Preview of input script

By clicking on the "Preview" tab next to "Template" at the bottom of the Unit Editor interface, the user can subsequently visualize a complete preview of the corresponding input script, in its final form that will be fed directly to the simulation engine to perform the associated unit computation. 

An example of Quantum ESPRESSO "pw_scf" input script, resulting from the above-mentioned JSON data structure and Jinja2 template for performing an scf ground-state total energy calculation on crystalline silicon, is displayed in the expandable section below:

<details>
  <summary>
     "Expand to view": ...
  </summary> 

```Jinja2
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

# Selecting different materials

Furthermore, if multiple material structures are present within the same subworkflow, they can each be selected from the list of radio buttons on the right-hand side of the "Preview" tab page in order to review their corresponding input scripts in turn. The appearance of such radio buttons, when silicon is the only material being considered in the subworkflow calculation, is highlighted as an example in the image below:

![](/images/input-preview.png)

# Links

1. [Input file description of the pw.x code](https://www.quantum-espresso.org/Doc/INPUT_PW.html)

2. [Jinja2 templating engine](http://jinja.pocoo.org/)





<!-- TODO by MH -->

[**Setup of combinatorial materials described here**](../materials/combinatorial-sets.md)

**Input file display in the online GUI**

Input files contain template placeholders in place of the elements that are replaced and/or in place of the parameters that define lattice type.  These are pseudo files which will be further processed by Exabyte.io software and can not be run directly by the software tool (quantum espresso) in this case.


!!! warning "Special sections of input files"
    Please note that all variables ($something) & placeholders ({{something}}) are important in Exabyte.io functionality.
    If altered the calculation result will give unexpected results if they do not fail completely.

<details>
<summary>**Example pw_scf.in file**</summary>
```
&CONTROL
    calculation= 'scf'
    title= ''
    verbosity= 'low'
    restart_mode= 'from_scratch'
    wf_collect= .true.
    tstress= .true.
    tprnfor= .true.
    outdir= '$OUTPUT_DIR/'
    wfcdir= '$OUTPUT_DIR/'
    prefix= '__prefix__'
    pseudo_dir= '$PSEUDO_DIR'
/
&SYSTEM
    ibrav={{ IBRAV }}
    nat={{ NAT }}
    ntyp={{ NTYP }}
    ecutwfc= 40
    ecutrho= 200
    occupations= 'smearing'
    degauss= 0.005
    celldm(1)={{ CELLDM(1) }}
    celldm(2)={{ CELLDM(2) }}
    celldm(3)={{ CELLDM(3) }}
    celldm(4)={{ CELLDM(4) }}
    celldm(5)={{ CELLDM(5) }}
    celldm(6)={{ CELLDM(6) }}
/
&ELECTRONS
    diagonalization= 'david'
    diago_david_ndim= 4
    diago_full_acc= .true.
    mixing_beta= 0.3
/
&IONS
/
&CELL
/
ATOMIC_SPECIES
As 74.92159 as_pbe_gbrv_1.0.upf
P 30.973762 p_pbe_gbrv_1.5.upf
Si 28.0855 si_pbe_gbrv_1.0.upf
ATOMIC_POSITIONS crystal
Si 0 0 0
Si/P/As 0.25 0.25 0.25
K_POINTS automatic
1 1 1 0 0 0
```
</details>
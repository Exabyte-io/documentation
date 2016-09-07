<!-- by MH -->

Combinatorial sets are used to study a wide variety of modifications to a base crystal structure through atomic substituion of elements at particular atomic positions.  To this end it is possible to specify what elements are substituted for each element in a structure and specify a different substituion rule for each position in the atomic structure as well.

To activate this automated capability, go to the `Create Job` webpage.  On this page near the upper right corner of the three dimensional window showing the visual representation of the atoms you will see a box called `Activate Comibinatorial`.  If you click on this button new functionality will appear on your screen that may not be immediately self-explanatory.  To get more information to read on how to set up the combinatorics, click on the `i` information button.  The contents of that page are also displayed below as well.

# Overview
This feature lets users create multiple jobs at the same time using a combinatorial set of materials and input templates for workflows.

The combinatorial part is reflected in 2 input fields: `basis` and `lattice basis`
Any input line that has element characters separated by slashes is triggering the generation of the set.

**Basis**
<details>
<summary>**1st scenario - input**</summary>
```
Si/Ge/As 0.0 0.0 0.0
Si/Ge    0.5 0.5 0.0
```
</details>

In case slashes are used the elements are changed all at once, eg. in the above case there will be 3 total basises created
<details>
<summary>**Case 1 - executed structure**</summary>
```
Si 0.0 0.0 0.0
Si 0.5 0.5 0.0
```
</details>
<details>
<summary>**Case 2 - executed structure**</summary>
```
Ge 0.0 0.0 0.0
Ge 0.5 0.5 0.0
```
</details>
<details>
<summary>**Case 3 - executed structure**</summary>
```
As 0.0 0.0 0.0
Ge 0.5 0.5 0.0
```
</details>

<details>
<summary>**2nd scenario - input**</summary>
```
Si,Ge,As 0.0 0.0 0.0
Si,Ge    0.5 0.5 0.0
```
</details>
In case commas are used the elements are changed one at a time, eg. in the above case there will be 6 total basises created
<details>
<summary>**Case 1 - executed structure**</summary>
```
Si 0.0 0.0 0.0
Si 0.5 0.5 0.0
```
</details>
<details>
<summary>**Case 2 - executed structure**</summary>
```
Si 0.0 0.0 0.0
Ge 0.5 0.5 0.0
```
</details>
<details>
<summary>**Case 3 - executed structure**</summary>
```
Ge 0.0 0.0 0.0
Si 0.5 0.5 0.0
```
</details>
<details>
<summary>**Case 4 - executed structure**</summary>
```
Si 0.0 0.0 0.0
Si 0.5 0.5 0.0
```
</details>
<details>
<summary>**Case 5 - executed structure**</summary>
```
As 0.0 0.0 0.0
Si 0.5 0.5 0.0
```
</details>
<details>
<summary>**Case 6 - executed structure**</summary>
```
As 0.0 0.0 0.0
Ge 0.5 0.5 0.0
```
</details>

**Lattice**

Multiple lattices could also be selected at the same time from UI: for example BCC, FCC, SC. For each of them a new material will be created.

When multiple lattices selection is used, the Basis input units should be automatically converted to "crystal".

**Input file display in the online GUI**

Input files are containing a template placeholder in place of the elements that are replaced and/or in place of the parameters that define lattice type
<details>
<summary>**Example pw_scf.in file**</summary>
```
&CONTROL
    calculation='scf'
    title=''
    verbosity='low'
    restart_mode='from_scratch'
    wf_collect=.true.
    tstress=.true.
    tprnfor=.true.
    outdir='$OUTPUT_DIR/'
    wfcdir='$OUTPUT_DIR/'
    prefix='__prefix__'
    pseudo_dir='$PSEUDO_DIR'
/
&SYSTEM
    ibrav={{ IBRAV }}
    nat=2
    ntyp={{ NTYP }}
    ecutwfc=40
    ecutrho=200
    occupations='smearing'
    degauss=0.005
    celldm(1)=9.448580823160363
/
&ELECTRONS
    diagonalization='david'
    diago_david_ndim=4
    diago_full_acc=.true.
    mixing_beta=0.3
/
&IONS
/
&CELL
/
ATOMIC_SPECIES
Si 28.0855 si_pbe_gbrv_1.0.upf
ATOMIC_POSITIONS crystal
{{ ELEMENT_0 }} 0.0 0.0 0.0
{{ ELEMENT_1 }} 0.5 0.5 0.5
K_POINTS automatic
2 2 2 0 0 0
```
</details>

**Job Names**

If the original job name text is JOB_NAME, then at the end of the creation process there should be multiple jobs with chemical formula prepended to the job name:
JOB_NAME_Si2
JOB_NAME_SiGe
JOB_NAME_SiAs



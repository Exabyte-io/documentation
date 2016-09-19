<!-- TODO by MH For all of the characteristic properties: explain how we assert fidelity -->
Currently we support the characteristic property simulations [**here**](../materials/characteristic-properties)

# Core Properties

## [Electronic wave functions](../materials/characteristic-properties#electronic-wave-functions)

## [Electronic energies](../materials/characteristic-properties#electronic-energies)

Both electronic energies and wave functions are calculated concurrently in  [first simulation tutorial](../tutorials/first-simulation.md) and by the example files below:

**VASP**: requires the standard INCAR, KPOINTS, POTCAR, & POSCAR files
<details>
<summary>**Example INCAR file**</summary>
```
SYSTEM =  Silicon-FCC
LWAVE  = .TRUE.
LCHARG  = .TRUE.
ISMEAR =    0
SIGMA  = 0.1
```
</details>
<details>
<summary>**Example KPOINTS file**</summary>
```
Automatic mesh
0
Gamma
  1  1  1
  0.  0.  0.
```
</details>
<details>
<summary>**Example POSCAR file**</summary>
```
Silicon FCC
1.0
   5.000000000     0.000000000     0.000000000
   2.500000000     4.330127019     0.000000000
   2.500000000     1.443375673     4.082482905
Si
2
direct
   0.000000000    0.000000000    0.000000000 Si
   0.250000000    0.250000000    0.250000000 Si
```
</details>

**Quantum Espresso**: requires the standard *.in and *.upf files only
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
    ibrav=2
    nat=2
    ntyp=1
    ecutwfc= 40
    ecutrho= 200
    occupations= 'smearing'
    degauss= 0.005
    celldm(1)=9.448580823160363
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
Si 28.0855 si_pbe_gbrv_1.0.upf
ATOMIC_POSITIONS crystal
Si 0 0 0
Si 0.25 0.25 0.25
K_POINTS automatic
1 1 1 0 0 0
```
</details>

<hr>

# [Principal Properties](../materials/characteristic-properties#principal-properties)
Total Energy, Entropy, Fermi energy, Atomic forces, Stress tensor, Average pressure, and Charge density are all usually calculated concurrently as shown in the example below:

**VASP**: requires the standard INCAR, KPOINTS, POTCAR, & POSCAR files
<details>
<summary>**Example INCAR file**</summary>
```
SYSTEM =  Silicon-FCC
LWAVE  = .TRUE.
LCHARG  = .TRUE.
ISMEAR =    0
SIGMA  = 0.1
```
</details>
<details>
<summary>**Example KPOINTS file**</summary>
```
Automatic mesh
0
Gamma
  1  1  1
  0.  0.  0.
```
</details>
<details>
<summary>**Example POSCAR file**</summary>
```
Silicon FCC
1.0
   5.000000000     0.000000000     0.000000000
   2.500000000     4.330127019     0.000000000
   2.500000000     1.443375673     4.082482905
Si
2
direct
   0.000000000    0.000000000    0.000000000 Si
   0.250000000    0.250000000    0.250000000 Si
```
</details>

### Quantum Espresso
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
    ibrav=2
    nat=2
    ntyp=1
    ecutwfc= 40
    ecutrho= 200
    occupations= 'smearing'
    degauss= 0.005
    celldm(1)=9.448580823160363
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
Si 28.0855 si_pbe_gbrv_1.0.upf
ATOMIC_POSITIONS crystal
Si 0 0 0
Si 0.25 0.25 0.25
K_POINTS automatic
1 1 1 0 0 0
```
</details>

<hr>

# [Derived Properties](../materials/characteristic-properties#derived-properties)
## [Electronic Properties](../materials/characteristic-properties#electronic-properties)

### [Band Structure](../materials/characteristic-properties#band-structure)
Please see the [band structure tutorial](../tutorials/band-structure.md) for more details.

**VASP**: requires the standard INCAR, KPOINTS, POTCAR, & POSCAR files

!!! Note "POTCAR's"
    POTCAR's provided are the [PAW database of potentials from vasp](http://cms.mpi.univie.ac.at/vasp/vasp/PAW_potentials.html)

<details>
<summary>**Example INCAR file**</summary>
```
SYSTEM =  Silicon-FCC
LWAVE  = .TRUE.
LCHARG  = .TRUE.
ISMEAR =    0
SIGMA  = 0.1
```
</details>
<details>
<summary>**Example KPOINTS file**</summary>
```
Automatic mesh
0
Gamma
  1  1  1
  0.  0.  0.
```
</details>
<details>
<summary>**Example POSCAR file**</summary>
```
Silicon FCC
1.0
   5.000000000     0.000000000     0.000000000
   2.500000000     4.330127019     0.000000000
   2.500000000     1.443375673     4.082482905
Si
2
direct
   0.000000000    0.000000000    0.000000000 Si
   0.250000000    0.250000000    0.250000000 Si
```
</details>
<details>
<summary>**Example second step INCAR file**</summary>
```
System = fcc Si
ICHARG = 11
ISMEAR = 0;
SIGMA = 0.1;
LORBIT=11
```
</details>
<details>
<summary>**Example second step KPOINTS file**</summary>
```
kpoints path
3
reciprocal
0.0  0.0  0.0   1
0.0  0.0  0.5   1
0.0  0.5  0.5   1
```
</details>
<details>
<summary>**Example second step POSCAR file**</summary>
```
Silicon FCC
1.0
   5.000000000     0.000000000     0.000000000
   2.500000000     4.330127019     0.000000000
   2.500000000     1.443375673     4.082482905
Si
2
direct
   0.000000000    0.000000000    0.000000000 Si
   0.250000000    0.250000000    0.250000000 Si
```
</details>

### Quantum Espresso
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
    ibrav=2
    nat=2
    ntyp=1
    ecutwfc= 40
    ecutrho= 200
    occupations= 'smearing'
    degauss= 0.005
    celldm(1)=9.448580823160363
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
Si 28.0855 si_pbe_gbrv_1.0.upf
ATOMIC_POSITIONS crystal
Si 0 0 0
Si 0.25 0.25 0.25
K_POINTS automatic
1 1 1 0 0 0
```
</details>
<details>
<summary>**Example pw_bands.in file**</summary>
```
&CONTROL
    calculation= 'bands'
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
    ibrav=2
    nat=2
    ntyp=1
    ecutwfc= 40
    ecutrho= 200
    occupations= 'smearing'
    degauss= 0.005
    celldm(1)=9.448580823160363
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
Si 28.0855 si_pbe_gbrv_1.0.upf
ATOMIC_POSITIONS crystal
Si 0 0 0
Si 0.25 0.25 0.25
K_POINTS crystal_b
3
0.50000000  0.50000000  0.50000000  10
0.00000000  0.00000000  0.00000000  10
0.50000000  0.00000000  0.50000000  10
```
</details>
<details>
<summary>**Example bands.in file**</summary>
```
&BANDS
    prefix= '__prefix__'
    outdir= '$OUTPUT_DIR'
    filband= '$JOB_WORK_DIR/bands.dat'
    no_overlap= .true.
/
```
</details>

### [Band Gap](../materials/characteristic-properties#band-gap)
Please see the [band gap tutorial](../tutorials/band-gap.md) for more details and the input files for Band Structure above.

### [Density of States and Partial DOS](../materials/characteristic-properties#sensity-of-states-and-partial-dos)
Please see the [density of states tutorial](../tutorials/density-of-states.md) for more details.
### VASP
VASP calculates the density of states for every simulation so see the example input files for Total energy
<!--To Do, get partial DOS running for VASP -->
### Quantum Espresso
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
    ibrav=2
    nat=2
    ntyp=1
    ecutwfc= 40
    ecutrho= 200
    occupations= 'smearing'
    degauss= 0.005
    celldm(1)=9.448580823160363
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
Si 28.0855 si_pbe_gbrv_1.0.upf
ATOMIC_POSITIONS crystal
Si 0 0 0
Si 0.25 0.25 0.25
K_POINTS automatic
1 1 1 0 0 0
```
</details>
<details>
<summary>**Example pw_bands.in file**</summary>
```
&CONTROL
    calculation= 'bands'
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
    ibrav=2
    nat=2
    ntyp=1
    ecutwfc= 40
    ecutrho= 200
    occupations= 'smearing'
    degauss= 0.005
    celldm(1)=9.448580823160363
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
Si 28.0855 si_pbe_gbrv_1.0.upf
ATOMIC_POSITIONS crystal
Si 0 0 0
Si 0.25 0.25 0.25
K_POINTS crystal_b
3
0.50000000  0.50000000  0.50000000  10
0.00000000  0.00000000  0.00000000  10
0.50000000  0.00000000  0.50000000  10
```
</details>
<details>
<summary>**Example bands.in file**</summary>
```
&BANDS
    prefix= '__prefix__'
    outdir= '$OUTPUT_DIR'
    filband= '$JOB_WORK_DIR/bands.dat'
    no_overlap= .true.
/
```
</details>
<details>
<summary>**Example pw_nscf.in file**</summary>
```
&CONTROL
    calculation= 'nscf'
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
    ibrav=2
    nat=2
    ntyp=1
    ecutwfc= 40
    ecutrho= 200
    occupations= 'smearing'
    degauss= 0.005
    celldm(1)=9.448580823160363
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
Si 28.0855 si_pbe_gbrv_1.0.upf
ATOMIC_POSITIONS crystal
Si 0 0 0
Si 0.25 0.25 0.25
K_POINTS automatic
1 1 1 0 0 0
```
</details>
<details>
<summary>**Example projwfc.in file**</summary>
```
&PROJWFC
    prefix= '__prefix__'
    outdir= '$OUTPUT_DIR/'
    degauss= 0.01
/
```
</details>

### [Fermi surface](../materials/characteristic-properties#fermi-surface)
Please see the [Fermi surface tutorial](../tutorials/fermi-surface.md) for more details.

<hr>

## [Chemistry Properties](../materials/characteristic-properties#chemical-properties)

### [Formation energy at 0K](../materials/characteristic-properties#formation-energy-at-0K)
Please see the [formation energy tutorial](../tutorials/formation-energy.md) for more details.  A formation energy calculation is simply a total energy calculation following a k-point convergence study and a relaxation calculation

<hr>

## [Vibrational Properties](../materials/characteristic-properties#vibrational-properties)

### [Zero Point Energy](../materials/characteristic-properties#zero-point-energy)
Please see the [zero point enegry tutorial](../tutorials/zero-point-energy.md) for more details.

**VASP**

<details>
<summary>**Example INCAR file**</summary>
```
IBRION = 5
LWAVE = .FALSE.
LCHARG = .FALSE.
ISMEAR = 1
SIGMA = 0.1
```
</details>
<details>
<summary>**Example KPOINTS file**</summary>
```
Automatic mesh
0
Gamma
  1  1  1
  0.  0.  0.
```
</details>
<details>
<summary>**Example POSCAR file**</summary>
```
Silicon FCC
1.0
   5.000000000     0.000000000     0.000000000
   2.500000000     4.330127019     0.000000000
   2.500000000     1.443375673     4.082482905
Si
2
direct
   0.000000000    0.000000000    0.000000000 Si
   0.250000000    0.250000000    0.250000000 Si
```
</details>

**Quantum Espresso**

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
    ibrav=2
    nat=2
    ntyp=1
    ecutwfc= 40
    ecutrho= 200
    occupations= 'smearing'
    degauss= 0.005
    celldm(1)=9.448580823160363
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
Si 28.0855 si_pbe_gbrv_1.0.upf
ATOMIC_POSITIONS crystal
Si 0 0 0
Si 0.25 0.25 0.25
K_POINTS automatic
1 1 1 0 0 0
```
</details>
<details>
<summary>**Example ph.in file**</summary>
```
&INPUTPH
    tr2_ph= 1.0d-12
    asr= .true.
    prefix='__prefix__'
    outdir='$OUTPUT_DIR/'
/
0.0 0.0 0.0
```
</details>

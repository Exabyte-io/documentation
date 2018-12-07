<!-- TODO: recycle or remove on cleanup -->

This page contains explanation about the characteristic properties of materials and the corresponding simulation input parameters.

# Core Properties

## Electronic energies and wave functions

Both electronic energies and wave functions are calculated concurrently. One can consult [getting started](../tutorials/dft/band-structure.md) to learn more. Example input files are given below.

#### VASP

Vienna ab-initio simulation package requires the standard INCAR, KPOINTS, POTCAR, & POSCAR files.

!!! Note "POTCAR files"
    POTCARs used are from the PAW database of potentials ([link](http://cms.mpi.univie.ac.at/vasp/vasp/PAW_potentials.html)) at version 5.3.5 (default)

<details markdown="1">
<summary>**INCAR**</summary>
```
SYSTEM =  Silicon-FCC
LWAVE  = .TRUE.
LCHARG  = .TRUE.
ISMEAR =    0
SIGMA  = 0.1
```
</details>

<details markdown="1">
<summary>**KPOINTS**</summary>
```
Automatic mesh
0
Gamma
  1  1  1
  0.  0.  0.
```
</details>

<details markdown="1">
<summary>**POSCAR**</summary>
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

#### Quantum Espresso

Quantum ESPRESSO ("QE" or "espresso") requires the input file and pseudopotentials.

!!! Note "UPF pseudopotentials"
    Default pseudopotentials for QE are from the GBRV database ([link](https://www.physics.rutgers.edu/gbrv/)) at version 1.5 (default)

<details markdown="1">
<summary>**pw_scf.in**</summary>
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

# Principal Properties

We classify Total Energy, Entropy, Fermi energy, Atomic forces, Stress tensor, Average pressure, and Charge density as the [Principal Properties](../materials/characteristic-properties#principal-properties). All these are all usually calculated concurrently as shown in the example below.

### VASP

<details markdown="1">
<summary>**INCAR**</summary>
```
SYSTEM =  Silicon-FCC
LWAVE  = .TRUE.
LCHARG  = .TRUE.
ISMEAR =    0
SIGMA  = 0.1
```
</details>
<details markdown="1">
<summary>**KPOINTS**</summary>
```
Automatic mesh
0
Gamma
  1  1  1
  0.  0.  0.
```
</details>
<details markdown="1">
<summary>**POSCAR**</summary>
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

<details markdown="1">
<summary>**pw_scf.in**</summary>
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

# Derived Properties

## Electronic Properties

### [Band Structure](../materials/characteristic-properties#band-structure)
Please see the [band structure tutorial](../tutorials/dft/band-structure.md) for more details.

#### VASP

<details markdown="1">
<summary>**INCAR**</summary>
```
SYSTEM =  Silicon-FCC
LWAVE  = .TRUE.
LCHARG  = .TRUE.
ISMEAR =    0
SIGMA  = 0.1
```
</details>

<details markdown="1">
<summary>**KPOINTS**</summary>
```
Automatic mesh
0
Gamma
  1  1  1
  0.  0.  0.
```
</details>

<details markdown="1">
<summary>**POSCAR**</summary>
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

<details markdown="1">
<summary>**second step INCAR**</summary>
```
System = fcc Si
ICHARG = 11
ISMEAR = 0;
SIGMA = 0.1;
LORBIT=11
```
</details>

<details markdown="1">
<summary>**second step KPOINTS**</summary>
```
kpoints path
3
reciprocal
0.0  0.0  0.0   1
0.0  0.0  0.5   1
0.0  0.5  0.5   1
```
</details>

<details markdown="1">
<summary>**second step POSCAR**</summary>
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

#### Quantum Espresso

<details markdown="1">
<summary>**pw_scf.in**</summary>
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

<details markdown="1">
<summary>**pw_bands.in**</summary>
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

<details markdown="1">
<summary>**bands.in**</summary>
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
Please see the [band gap tutorial](../tutorials/dft/band-gap.md) for more details and the input files for Band Structure above.

### [Density of States and Partial DOS](../materials/characteristic-properties#sensity-of-states-and-partial-dos)
Please see the [density of states tutorial](../tutorials/dft/density-of-states.md) for more details.

#### VASP

VASP calculates the density of states for every simulation so see the example input files for Total energy


<details markdown="1">
<summary>**INCAR**</summary>
```
SYSTEM =  Silicon-FCC
LWAVE  = .FALSE.
LCHARG  = .FALSE.
ISMEAR =    0
SIGMA  = 0.05
LORBIT=11
```
</details>

<details markdown="1">
<summary>**KPOINTS**</summary>
```
Automatic mesh
0
Gamma
  2 2 2
  0.  0.  0.
```
</details>
<details markdown="1">
<summary>**POSCAR**</summary>
```
Cubic Diamond Si
5.43
0.0 0.5 0.5
0.5 0.0 0.5
0.5 0.5 0.0
Si
2
Direct
0.0 0.0 0.0 Si
0.25 0.25 0.25 Si
```
</details>

#### Quantum Espresso

<details markdown="1">
<summary>**pw_scf.in**</summary>
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
<details markdown="1">
<summary>**pw_bands.in**</summary>
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
<details markdown="1">
<summary>**bands.in**</summary>
```
&BANDS
    prefix= '__prefix__'
    outdir= '$OUTPUT_DIR'
    filband= '$JOB_WORK_DIR/bands.dat'
    no_overlap= .true.
/
```
</details>
<details markdown="1">
<summary>**pw_nscf.in**</summary>
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
<details markdown="1">
<summary>**projwfc.in**</summary>
```
&PROJWFC
    prefix= '__prefix__'
    outdir= '$OUTPUT_DIR/'
    degauss= 0.01
/
```
</details>

### [Fermi surface](../materials/characteristic-properties#fermi-surface)
Please see the [Fermi surface tutorial](../tutorials/dft/fermi-surface.md) for more details.

<hr>

### [Formation energy](../materials/characteristic-properties#formation-energy-at-0K)
Please see the [formation energy tutorial](../tutorials/formation-energy.md) for more details.  A formation energy calculation is simply a total energy calculation following a k-point convergence study and a relaxation calculation

<hr>

## [Vibrational Properties](../materials/characteristic-properties#vibrational-properties)

### [Zero Point Energy](../materials/characteristic-properties#zero-point-energy)
Please see the [zero point enegry tutorial](../tutorials/dft/zero-point-energy.md) for more details.

#### VASP

<details markdown="1">
<summary>**INCAR**</summary>
```
IBRION = 5
LWAVE = .FALSE.
LCHARG = .FALSE.
ISMEAR = 1
SIGMA = 0.1
```
</details>

<details markdown="1">
<summary>**KPOINTS**</summary>
```
Automatic mesh
0
Gamma
  1  1  1
  0.  0.  0.
```
</details>

<details markdown="1">
<summary>**POSCAR**</summary>
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

#### Quantum Espresso

<details markdown="1">
<summary>**pw_scf.in**</summary>
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

<details markdown="1">
<summary>**ph.in**</summary>
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

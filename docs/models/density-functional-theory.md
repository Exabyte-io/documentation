<!-- by MH -->

We currently support Density Functional Theory in the planewave pseudopotential approximation as implemented in Quantum ESPRESSO and VASP simulation packages. Both have similar inputs but structure their inputs in a distinctive way through different input files. Quantum Espresso also breaks its execution workflow up into seperate executables but Exabyte.io makes this difference transparent to the user.  However, especially for more advanced users it is critical to understand the input file options to customize your work.  We've provided a few references and examples below with links back to the application information pages for more details.

# Input File Primer/Examples:

<hr>

## VASP Input Files:

### INCAR
Control file of algorithm and methodology setting. A comprehensive list of available parameters is available at http://cms.mpi.univie.ac.at/wiki/index.php/Category:INCAR

<details>
<summary>**Example INCAR file**</summary>
```
System = diamond Si
ISTART = 0         Job type: 0 = new,  1 = continuation,  2 = same cutoff
ISMEAR = 0         Electronic State Broadening: 4 = tetrahedron, 1 = Fermi, 0 = Gaussian
SIGMA = 0.1        Size of smearing of electronic states in eV
LWAVE = .FALSE.    Do not output the wavefunctions file WAVECAR
LCHARG = .FALSE.   Do not output the charge density file CHGCAR
```
</details>

### KPOINTS
Information about the k-points used in the calculation.  Full explanation of available settings available at http://cms.mpi.univie.ac.at/vasp/vasp/KPOINTS_file.html

<details>
<summary>**Example KPOINTS file**</summary>
```
k-points file with gamma point only
 0
Gamma
 1 1 1
 0  0  0
```
</details>

### POSCAR
The structure of the supercell/material and information on relaxation constraints.  Full explanation of available settings available at http://cms.mpi.univie.ac.at/vasp/vasp/POSCAR_file.html

<details>
<summary>**Example POSCAR file**</summary>
```
cubic diamond Si
   5.5
 0.0    0.5     0.5
 0.5    0.0     0.5
 0.5    0.5     0.0
  Si
  2
Direct
 -0.125 -0.125 -0.125 Si
  0.125  0.125  0.125 Si
```
</details>

### POTCAR
Pseudopotential input file.  Instructions onc creating the POTCAR file http://cms.mpi.univie.ac.at/vasp/vasp/POTCAR_file.html

<hr>

## Quantum Espresso Input Files:
As mentioned above, quantum espresso breaks its execution up into multiple executables in contrast to VASP.  On this page we will just focus on the pw.x executable input files (http://www.quantum-espresso.org/wp-content/uploads/Doc/INPUT_PW.html) as the input settings for other executables can be quite advanced and is explained in depth on the quantum espresso website at http://www.quantum-espresso.org/users-manual/input-data-description/
### *.in
Summary input file that combines similar functionality to INCAR, KPOINTS, & POSCAR in vasp
<details>
<summary>**pw_scf.in file structure**</summary>
```
&CONTROL
  ...
/
&SYSTEM
 ...
/
&ELECTRONS
...
/
[ &IONS
  ...
 / ]
[ &CELL
  ...
 / ]
ATOMIC_SPECIES
 X  Mass_X  PseudoPot_X
 Y  Mass_Y  PseudoPot_Y
 Z  Mass_Z  PseudoPot_Z
ATOMIC_POSITIONS { alat | bohr | crystal | angstrom | crystal_sg }
  X 0.0  0.0  0.0  {if_pos(1) if_pos(2) if_pos(3)}
  Y 0.5  0.0  0.0
  Z O.0  0.2  0.2
K_POINTS { tpiba | automatic | crystal | gamma | tpiba_b | crystal_b | tpiba_c | crystal_c }
if (gamma)
   nothing to read
if (automatic)
   nk1, nk2, nk3, k1, k2, k3
if (not automatic)
   nks
   xk_x, xk_y, xk_z,  wk
[ CELL_PARAMETERS { alat | bohr | angstrom }
   v1(1) v1(2) v1(3)
   v2(1) v2(2) v2(3)
   v3(1) v3(2) v3(3) ]
[ OCCUPATIONS
   f_inp1(1)  f_inp1(2)  f_inp1(3) ... f_inp1(10)
   f_inp1(11) f_inp1(12) ... f_inp1(nbnd)
 [ f_inp2(1)  f_inp2(2)  f_inp2(3) ... f_inp2(10)
   f_inp2(11) f_inp2(12) ... f_inp2(nbnd) ] ]
[ CONSTRAINTS
   nconstr  { constr_tol }
   constr_type(.)   constr(1,.)   constr(2,.) [ constr(3,.)   constr(4,.) ] { constr_target(.) } ]
[ ATOMIC_FORCES
   label_1 Fx(1) Fy(1) Fz(1)
   .....
   label_n Fx(n) Fy(n) Fz(n) ]
```
</details>
<details>
<summary>**pw_scf.in Example file**</summary>
```
 &control
    prefix='silicon',
    pseudo_dir='directory_where_pp-files_are_kept'
    outdir = 'temporary_directory_for_large_files',
 /
 &system
    ibrav =  2,
    celldm(1) = 10.2,
    nat =  2,
    ntyp = 1,
    ecutwfc = 12.0
 /
 &electrons
 /
ATOMIC_SPECIES
 Si  28.086  Si.vbc.UPF
ATOMIC_POSITIONS
 Si 0.00 0.00 0.00
 Si 0.25 0.25 0.25
K_POINTS
   2
   0.25 0.25 0.75 3.0
   0.25 0.25 0.25 1.0
```
</details>
### *.upf
Pseudopotential input file.  List of pseudopotentials currently available on the Quantum Espresso website http://www.quantum-espresso.org/pseudopotentials/

<hr>

# Convergence and Relaxation
In most cases to have a reasonable level of confidence that a result can be trusted the total energy should not increase significantly when the k-point density is increassed.  This search for the appropriate density of k-points is called [k-point convergence](convergence-algorithms.md).

It is often desirable to obtain [relaxed structures](structural-relaxation.md) to ensure that your system is in the lowest total energy state configuration possible before computing your property.

<hr>

# Additional resources
There are many well developed Density Functional Theory reviews on the web and below we list a few that we find the most helpful:
1. P. Hohenberg and W. Kohn, Phys. Rev. 136, B864 1964, http://journals.aps.org/pr/abstract/10.1103/PhysRev.136.B864

2. W. Kohn and L. J. Sham, Phys. Rev. 140, A1133 1965, http://journals.aps.org/pr/abstract/10.1103/PhysRev.140.A1133

3. J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77, 3865, http://journals.aps.org/prl/abstract/10.1103/PhysRevLett.77.3865



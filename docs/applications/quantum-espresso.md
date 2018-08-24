# The Quantum ESPRESSO code

Quantum ESPRESSO (QE) is a software suite for ab-initio quantum methods performing general electronic-structure calculations and materials modeling. It is distributed for free under the GNU General Public License. Quantum ESPRESSO is based on Density Functional Theory, plane wave basis sets, and pseudopotentials (both norm-conserving and ultrasoft). 

The core plane wave DFT functions of QE are provided by the PWscf (Plane-Wave Self-Consistent Field) component. Further components are included in the distribution package, such as the Ph module for performing phonon calculations via the density functional perturbation theory and linear response theoretical formalisms.

Complete information and documentation about the QE software package can be found in its corresponding website [[1](#links)]. 



# Input File Examples

<hr>

Quantum ESPRESSO breaks its execution up into multiple executables, in contrast to VASP.  On this page, we will focus on the pw.x executable input [[2](#links)], as the input settings for other executables can be quite advanced and is explained in depth on the "Resources" page of the Quantum ESPRESSO website [[3](#links)].

### pw.in

Summary input file that combines similar functionality to INCAR, KPOINTS, & POSCAR in VASP:

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

### Pseudopotential files

The files with ".upf" extension represent the pseudopotential input files.  The list of pseudopotentials currently available on the Quantum Espresso website can be found [here](http://www.quantum-espresso.org/pseudopotentials/). Exabyte in particular supports [gbrv potentials from Rutgers](https://www.physics.rutgers.edu/gbrv/).

<hr>

# Links

1. [Official Quantum ESPRESSO website](https://www.quantum-espresso.org/)
2. [Input file description of the pw.x code](https://www.quantum-espresso.org/Doc/INPUT_PW.html)
3. [Quantum ESPRESSO package-specific documentation](https://www.quantum-espresso.org/resources/users-manual/specific-documentation)
4. [Official Quantum ESPRESSO GitHub repository](https://github.com/QEF/q-e/tags)
5. [Calculation of Phonon Dispersions on the Grid Using Quantum ESPRESSO](http://users.ictp.it/~pub_off/lectures/lns024/10-giannozzi/10-giannozzi.pdf)

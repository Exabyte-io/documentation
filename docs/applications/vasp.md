# Vienna Ab initio Simulation Package

The Vienna Ab initio Simulation Package, better known as VASP, is a package for performing ab-initio electronic structure calculations and molecular dynamics, using either Vanderbilt ultra-soft pseudopotentials or the projector-augmented wave (PAW) method, together with a plane wave basis set. 

The underlying theoretical model is Density Functional Theory (DFT), but the code also allows for the use of post-DFT corrections, such as hybrid functionals mixing DFT and Hartree–Fock exchange, many-body perturbation theory (the GW method), and dynamical electronic correlations within the Random Phase Approximation (RPA).

Complete information and documentation about the VASP code can be found in its corresponding website [[1](#links)]. 


# Input File Examples

A comprehensive list of available VASP input parameters is available in Refs. [[2-3](#links)].


<hr>

### INCAR

Control file of algorithm and methodology setting: 

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

Information about the k-points used in the calculation:  

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

The structure of the crystal cell and information about relaxation constraints:  

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

Pseudopotential input file. 

<hr>


# Links

1. [Official VASP website](https://www.vasp.at/)
2. [Official VASP Documentation Manual, pdf copy](http://cms.mpi.univie.ac.at/vasp/vasp.pdf)
3. [Official VASP Documentation Manual, online version](http://cms.mpi.univie.ac.at/vasp/vasp/vasp.html)


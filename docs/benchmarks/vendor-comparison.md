# Cloud vendors performance comparison

> Date: 2016/09

Exabyte.io utilizes multiple cloud vendors resources to provide users with a large scale computing infrastructure. Since Each cloud provider uses a specific type of resources, applications performance vary on different cloud vendors. For the sake of simplicity, a short VASP calculation utilizing 1 CPU with the following characteristics was used to compare the performance of four cloud providers, AWS, Rackspace, SoftLayer and Microsoft Azure.

## Model and Method

Plane-wave Pseudopotential Density Functional Theory formalism as implemented in Vienna Ab-initio Simulation Package (VASP) at version 5.3.5 with a corresponding set of atomic pseudo-potentials was employed in this run.

## Inputs

<details markdown="1">
  <summary>**INCAR**</summary>

```fortran
SYSTEM = Si
!!
NWRITE = 2
IALGO = 48
NELM = 13
ENMAX = 140 eV
IALGO = -1
NELMIN = 3
NELMDL = 7
NSIM = 4
LREAL = .TRUE.
BMIX = 2.5
ISYM = 0
EDIFF = 1E-4
LWAVE = .FALSE.
LCHARG = .FALSE.
!!
NSW = 0
POTIM = 5.00
TEBEG = 423
!!
ISMEAR = 1
SIGMA = 0.1
EMIN = -15
EMAX = 0
```
</details>

<details markdown="1">
  <summary>**POSCAR**</summary>

```text
Silicon8
1.0
5.468728 0.000000 0.000000
0.000000 5.468728 0.000000
0.000000 0.000000 5.468728
Si
8
direct
0.250000 0.250000 0.250000 Si
0.750000 0.750000 0.250000 Si
0.500000 0.500000 0.000000 Si
0.000000 0.500000 0.500000 Si
0.250000 0.750000 0.750000 Si
0.000000 0.000000 0.000000 Si
0.750000 0.250000 0.750000 Si
0.500000 0.000000 0.500000 Si
```
</details>

<details markdown="1">
  <summary>**KPOINTS**</summary>

```text
Automatic mesh
0
Gamma
  8  8  8
  0.  0.  0.
```
</details>

## Results

|Provider  |CPU                                      |Memory (GB) |Disk (GB) |Bandwidth (Gbps) |Runtime (sec)|
|:---------|:---------------------------------------:|:---------:|:-------:|:--------------:|:---------------:|
|AWS       |36 core, Intel Xeon E5-2666-v3, 2.90GHz |60         |10       |10              |37.8             |
|Azure     |16 core, Intel Xeon E5-2673-v3, 2.40GHz |32         |256      |10              |43.5             |
|Rackspace |32 core, Intel Xeon E5-2680-v2, 2.80GHz |60         |50       |5               |49               |
|Softlayer |32 core, Intel Xeon E5-2650-v0, 2.00GHz |64         |25       |1               |89.5             |

> NOTE: no Infiband hardware was available on Azure at the time
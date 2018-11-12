# Total Energy Contributions

The Total Energy of a Material, introduced [in this page](energies.md), is itself comprised of several **Energy Contributions**. They can be computed as part of any [Workflow](/workflows/overview.md) involving at least one basic "self-consistent field" (scf) energy calculation, and are returned as a list of scalar quantities.

## Types of Contributions

Specific types of energy contributions are commonly encountered in [DFT](/models/dft/overview.md) computations. The types of contributions included in the final results depend specifically on the modeling [application](/software/applications.md) employed, between [Quantum Espresso](/software/modeling/quantum-espresso.md) (QE) and [VASP](/software/modeling/vasp.md), as explained in what follows.

The reader is referred to the links presented at the bottom of the page for a theoretical review of the energy contributions presented herein.

## Contributions Computed by Both QE and VASP

The following contributions displayed in the image below are computed and returned to the user under the [Results Tab](../../jobs/ui/results-tab.md) of [Job Viewer](../../jobs/ui/viewer.md), for the cases of both VASP and QE calculations. In all instances, the results are returned in units of eV. 

![Common Contributions](/images/common-contributions.png "Common Contributions")

## Contributions Computed Only by QE

Two additional energy contributions can be evaluated with QE-based Workflows: the "One-electron" and "Harris-Foulkes" contributions. They are both returned as values expressed in eV, in a similar format to the other properties listed in the above image. 


# Links

1. [Wikipedia Ewald summation, Website](https://en.wikipedia.org/wiki/Ewald_summation)

2. [Wikipedia Hartree–Fock method, Website](https://en.wikipedia.org/wiki/Hartree%E2%80%93Fock_method)

3. [Introduction to Density Functional Theory and Exchange-Correlation Energy Functionals, Website](https://www.uio.no/studier/emner/matnat/fys/FYS4411/v11/undervisningsmateriale/Lecture_notes_and_literature/jones.pdf)

4. [Wikipedia Harris functional, Website](https://en.wikipedia.org/wiki/Harris_functional)

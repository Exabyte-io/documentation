# Total Energy Contributions

The Total Energy of a Material, introduced [in this page](total-energy.md), is itself comprised of several **Energy Contributions**. They can be computed as part of any [Workflow](../../workflows/overview.md) involving at least one basic "self-consistent field" (scf) energy calculation using [DFT](../../models/dft/overview.md), and they are returned as a list of [Scalar, Characteristic and Auxiliary](../../properties/classification/general.md) quantities.

## Types of Contributions

Specific types of energy contributions are commonly encountered in [DFT](../../models/dft/overview.md) computations. The types included in the final results depend specifically on the modeling [application](../../software/applications.md) employed, as explained in what follows.

The reader is referred to the links presented at the bottom of the page for a theoretical review of the energy contributions presented herein.

## Contributions Computed by all Applications

The following contributions, displayed in the image below, are computed and returned to the user under the [Results Tab](../../jobs/ui/results-tab.md) of [Job Viewer](../../jobs/ui/viewer.md), for the cases of both [VASP](../../software/modeling/vasp.md) and [Quantum ESPRESSO](../../software/modeling/quantum-espresso.md) calculations. In all instances, the results are returned in units of eV. 

![Common Contributions](/images/Properties/common-contributions.png "Common Contributions")

## Contributions Computed Only by Quantum ESPRESSO

Two additional energy contributions can be evaluated with Quantum ESPRESSO-based Workflows: the "One-electron" and "Harris-Foulkes" contributions. They are both returned as values expressed in eV, in a similar format to the other properties listed in the above image. 

## Links

[^1]: [Wikipedia Ewald summation, Website](https://en.wikipedia.org/wiki/Ewald_summation)

[^2]: [Wikipedia Hartree–Fock method, Website](https://en.wikipedia.org/wiki/Hartree%E2%80%93Fock_method)

[^3]: [Introduction to Density Functional Theory and Exchange-Correlation Energy Functionals, Website](https://www.uio.no/studier/emner/matnat/fys/FYS4411/v11/undervisningsmateriale/Lecture_notes_and_literature/jones.pdf)

[^4]: [Wikipedia Harris functional, Website](https://en.wikipedia.org/wiki/Harris_functional)

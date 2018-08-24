# Overview of the Density Functional Theory Model
 
The Exabyte platform currently supports two widely used first-principles quantum computational engines, namely the [Quantum ESPRESSO](/applications/quantum-espresso.md) and [VASP](/applications/vasp.md) simulation packages. Both of these based on the plane-waves pseudopotential formulation of the Density Functional Theory (DFT) [[1](#links)] theoretical model, for calculating approximate solutions to Schrodinger's Equations and associated physical properties in relatively complex crystalline materials. The reader who wishes to revise the fundamental theoretical framework underlying DFT is referred to the introductory literature on the subject [[2,3](#links)]. 

Both of these codes have similar inputs, but at the same time structure them in a rather distinctive way through different input files. Quantum Espresso also breaks its execution workflow up into separate executables, and we make this difference transparent to the user in our general description of the [Workflows Designer interface](/workflow-designer/subworkflow-editor/intro.md).  However, especially for more advanced users, it is critical to understand the input file options and to be able to customize the work.  In this spirit, we have provided a few references and examples in the applications' corresponding pages, accessible [here](/applications/quantum-espresso.md) and [here](/applications/vasp.md) respectively, with links in them referring back to the applications' original websites for more details.

Some important theoretical concepts in DFT, within the context of the way DFT is implemented in the various codes made available on the Exabyte platform, are outlined in the following sections of this page:

# Approximation Subtype to the Exchange-Correlation functional

New subworkflows are by default based on the **Generalized Gradient Approximation** (GGA) for the Exchange-Correlation part of the total energy functional of the crystal being studied. This choice in general represents the most accurate approximation in Density Functional Theory for modeling all the complex exchange and correlation effects between the electrons in periodic crystals. 

# Flavors of Exchange-Correlation functional

The particular flavor of GGA implemented in the Exabyte Platform is the one due to **Perdew, Burke and Ernzerhof** (PBE) [[4](#links)], which is well-entrenched in the computational material science community and has proven through the times to constitute one of the most efficient and reliable approximations to the Exchange-Correlation functional.  

# Links

Additional resourceful general references on DFT and associated concepts, beyond those outlined below, are contained in this [page](references.md), to be referred to at the reader's discretion.

1. [Wikipedia Density Functional Theory, Website](https://en.wikipedia.org/wiki/Density_functional_theory)
2. R.M. Martin: "Electronic Structure: Basic Theory and Practical Methods"; Cambridge University Press (2008)
3. [Introductory notes on Density Functional Theory, Gabriele Mogni](https://docs.wixstatic.com/ugd/02c77e_67682e5712b14fbaa8acc70d2021dd29.pdf)
4. [J.P. Perdew, K. Burke, M. Ernzerhof: "Generalized Gradient Approximation Made Simple"; Phys. Rev. Lett. 77, 3865 (1996)](https://users.wfu.edu/natalie/s11phy752/lecturenote/PhysRevLett.77.3865.pdf)



# Overview of Density Functional Theory
 
The Exabyte platform supports several widely used first-principles quantum computational engines, all based on the plane-waves pseudopotential formulation of the Density Functional Theory (DFT) [[1](#links)] theoretical model for calculating approximate solutions to Schrodinger's Equations and associated physical properties in relatively complex crystalline materials. The reader who wishes to revise the fundamental theoretical framework underlying DFT is referred to the introductory literature on the subject [[2,3](#links)]. 

Some important theoretical concepts in DFT, within the context of the way DFT is implemented in the various codes made available on the Exabyte platform, are outlined in the following sections of this page, and in [this other page](/models/dft/density-functional-theory.md).   


# Approximations to the Exchange-Correlation functional

New subworkflows are by default based on the **Generalized Gradient Approximation** (GGA) for the Exchange-Correlation part of the total energy functional of the crystal being studied. This choice in general represents the most accurate approximation in Density Functional Theory for modeling all the complex exchange and correlation effects between the electrons in periodic crystals. 

# Flavors of Exchange-Correlation functionals

The particular flavor of GGA implemented in the Exabyte Platform is the one due to **Perdew, Burke and Ernzerhof** (PBE) [[4](#links)], which is well-entrenched in the computational material science community and has proven through the times to constitute one of the most efficient and reliable approximations to the Exchange-Correlation functional.  



# Links

1. [Wikipedia Density Functional Theory, Website](https://en.wikipedia.org/wiki/Density_functional_theory)
2. R.M. Martin: "Electronic Structure: Basic Theory and Practical Methods"; Cambridge University Press (2008)
3. [Introductory notes on Density Functional Theory, Gabriele Mogni](https://docs.wixstatic.com/ugd/02c77e_67682e5712b14fbaa8acc70d2021dd29.pdf)
4. [J.P. Perdew, K. Burke, M. Ernzerhof: "Generalized Gradient Approximation Made Simple"; Phys. Rev. Lett.,Volume 77, Number 18 (1996)](https://users.wfu.edu/natalie/s11phy752/lecturenote/PhysRevLett.77.3865.pdf)

<!-- TODO by MH -->
<!-- TODO: add input file examples and reasons for using these parameters, link to relaxation page for relaxation examples, convergence for convergence examples -->


We use density functional theory, are currently support pseudopotential approximation as implemented in quantum espresso and VASP.

# Introduction - Electronic Structure

Everything that surrounds us is a material, and every material is made of atoms and electrons.

Majority of materials are crystalline, at least at the microscale level (although there are notable exclusions). Atoms (ions or nuclei strictly speaking) are forming the crystal lattice of a material, and electrons are forming a "cloud" (in metals) or set of "localized states" (in insulators and molecules), that is taking part in defining virtually every possible property of a material at terrestrial (obtainable on Earth) conditions.

Electronic structure, or the way electrons are arranged inside a material (solid), therefore contains a great amount of information about the characteristic properties of a material. It seems very attractive to seek the data about the electronic structure in order to design and discover new materials.

## First principles

The phrase First principles is applied to work that starts directly at the level of established science and does not make assumptions such as empirical model and fitting parameters. Calculation of the electronic structure from first principles has to start from the most foundational level - the only required information is the geometric and elemental constitution of a material (or Descriptive, as we refer to it in documentation) and a model of the atomic potential (pseudopotenial or local atomic orbitals)

## Schrodinger equation
In order to obtain the information about materials from first principles, one needs to solve the Schrodinger equation, that describes how the quantum state of a physical system changes with time. In practice, time dependency is rarely studied, because of the added complexity. Solving non-time-dependent equation, can still describe the quantum state of a material and thus provide the basis for extracting characteristic properties.

## Time dependent Schrodinger equation:


where is the Hamiltonian operator of the system, E is the scalar value of energy, and is the electronic wavefunction of the many-particle system, It tells us the probability of any particular configuration of electrons (lowercase "r") and nuclei (Capital "R") occurring at any particular time (t):

In the most general form, the Hamiltonian is the sum of kinetic energies of ions and electrons, electron-electron interaction potential, electron-ion interaction potential, and ion-ion interaction potential:

## Born-Oppenheimer approximation
Compared to electrons, ions are massive and slow. This has two consequences:
whenever an ion moves, the electrons react so quickly that it may be considered instant.  The wavefunctions for the nuclei are zero except in a very small region – we may as well forget the nuclei wavefunctions and just say ‘there they are’!

Now we only have to worry about quantum mechanics for the electrons. And since they react instantly to any change in the positions of the nuclei, we only have to solve the time-independent Schrödinger equation:

Note, that now the wavefunction only includes electronic contribution.

# Density FUnctional Theory - Foundations
In the mid-1960s two papers by Hohenberg and Kohn [1], and Kohn and Sham [2] gave a solution to the problem of finding a solution for many-electron system in an external (ionic) potential. They showed that the ground state energy and charge density of interacting electrons in any external potential were exactly the same as those of non-interacting electrons in a specially modified potential.

We can therefore express the total energy in terms of the electronic density, which is a function of three spatial variables (x, y, z) only, instead of having to deal with the positions of all (1023!!!) electrons in a solid simultaneously:

The extra term on the right-hand side is a functional of the electron density ρ(r) and is called the exchange-correlation functional.

## Equations
Now we can re-formulate the problem having electronic density as the main parameter. Hamiltonian is:

And since the electrons are non-interacting in the new formalism, we have:

Thus we have reduced the problem of n interacting electrons and N ions with a complicated wavefunction that depended on each particle's position to a system of equations that are written for single electronic states and are coupled with each other through the electronic density only.

The only unknown parameter that's left is the exchange-correlation functional. This is the cornerstone parameter in Density Functional theory, that in the end defines the level of Fidelity (as discussed in Input data section) in predicting the properties of materials.

## Approximations
Several approximations were developed for the exchange-correlation functional.
### LDA
Local-density approximation or LDA is the simplest. In the special case that the electrons are evenly spread throughout space, we can actually compute Exc [ρ]. We can use this result as an approximation to the true Exc. In this approximation the contribution from any region of space only depends on the local density in that region, thus the name:

### GGA (PBE)
Generalized gradient approximations (GGA) are still local but also take into account the gradient of the density at the same coordinate:

#### PBE = Perdew-Burke-Ernzerhof
    A particular implementation of the GGA approach that is most widely used [3]. So wide that the terms GGA and PBE are often applied interchangeably.
### Other
Potentially more accurate than the GGA functionals are the meta-GGA functionals, a natural development after the GGA (generalized gradient approximation). Meta-GGA DFT functional in its original form includes the second derivative of the electron density (the Laplacian) whereas GGA includes only the density and its first derivative in the exchange-correlation potential.
Functionals of this type are, for example, TPSS and the Minnesota Functionals. These functionals include a further term in the expansion, depending on the density, the gradient of the density and the Laplacian (second derivative) of the density.
Difficulties in expressing the exchange part of the energy can be relieved by including a component of the exact exchange energy calculated from Hartree–Fock theory. Functionals of this type are known as hybrid functionals.
Lastly, there are systematic ways of correcting the errors that are produced during the calculation of exchange with LDA/PBE by using GW approximation and similar approaches that are often summarized as Random Phase Approximation techniques (or RPA).

!!! warning "DFT Limitations"
Even ‘perfect’ DFT is only exact for the ground state
Exchange-Correlation is approximated crudely
No collective electron-nuclear motion
No nuclear quantum effects (e.g. zero-point motion)

## Overview
In order to represent the solutions to Kohn-Sham equations one need to choose a suitable basis set. Or a set of functions in space that can represent any other spatial function. Some of the obvious choices for basis set functions are:
polynomials
gaussians
atomic orbitals
Although these are viable, none of them represents the periodicity of the problem (as we uncovered in the previous part).
Relation to Bloch functions
Since Bloch functions u k (r) are periodic, a natural choice is to express them as a 3D Fourier series:

where CG,k are complex Fourier coefficients, and the sum is over all wavevectors G (spatial frequencies) with the right periodicity, that satisfies Bloch theorem.
Only a discrete set of wavevectors have the right periodicity – these are the reciprocal lattice vectors. If we make the cell longer in one direction, the allowed wavevectors in that direction become shorter.
Reciprocal space
Since wavevectors are measured in units of 1/length, they describe points in reciprocal space. We can plot the allowed wavevectors in this space as it is shown below:

Each of the Fourier basis functions e iGr represents a plane-wave traveling in space, perpendicular to the vector G.
Cutoff energy
There are an infinite number of allowed G, but the coefficients CG,k become smaller and smaller as |G|2 becomes larger and larger. We define a cut-off energy:

and only include plane-waves with energies less than this cut-off, or in other words - within a sphere of radius defined by the above formula.

We always have to ensure the cut-off energy is high enough to give accurate results. We repeat the calculations with higher and higher cut-off energies until the properties we’re interested in have converged.
Below is example dependence of the results of the Density Functional Theory calculations on the cut-off energy:



# Additional resources
There are many well developed Density Functional Theory reviews on the web and below we list a few that we find the most helpful:

# Links
P. Hohenberg and W. Kohn, Phys. Rev. 136, B864 1964, http://journals.aps.org/pr/abstract/10.1103/PhysRev.136.B864
W. Kohn and L. J. Sham, Phys. Rev. 140, A1133 1965, http://journals.aps.org/pr/abstract/10.1103/PhysRev.140.A1133
J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77, 3865, http://journals.aps.org/prl/abstract/10.1103/PhysRevLett.77.3865

# Phonon Dispersions and Density of States Calculation on Grid

This tutorial page explains how to calculate the [Phonon Dispersion Curves](../../../properties-directory/non-scalar/phonon-dispersions.md) and [Phonon Density of States](../../../properties-directory/non-scalar/phonon-dos.md) of materials based on [Density Functional Theory](../../../models-directory/dft/overview.md). We will be studying crystalline Silicon in the standard cubic-diamond crystal structure, and we will use [Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md) as our simulation engine.

What sets the present tutorial apart from the [other tutorial](phonons.md) on phonon calculations is the employment of the "Grid Method" for computing the vibrational properties of materials, which is reviewed in the subsequent paragraph. This method is based on a [map type workflow](../../../workflows/components/maps.md), where multiple branches are executed as separate [Jobs](../../../jobs/overview.md). More information on this method can be found in Ref. [^1].

## The Grid Method for Phonon Calculations

The Grid Method allows for an efficient **parallelization** of the tasks for calculating the individual vibrational modes. This method optimizes the corresponding [workflow](../../../workflows/overview.md) in order to obtain the frequencies for each individual **symmetry-irreducible representation** [^2] of the phonon lattice perturbations in parallel.   

We thus implement a grid-parallel workflow for the calculation of the phonon dynamical matrices, initially explained in the first reference cited [in this page](../../../models/auxiliary-concepts/reciprocal-space/sampling.md). During the actual phonon calculation part of the workflow, the following steps happen:

- First, the irreducible representations for the vibrational modes (irreps) are generated, based on the [sampling grid in the reciprocal space](../../../models/auxiliary-concepts/reciprocal-space/sampling.md) (**q-point grid**). 

- Second, a separate  calculation  is  prepared  and submitted  for  execution in parallel for  each pair or irreducible  representation and q-point, via the implementation of a [Map](../../../workflows/components/maps.md) for performing a distributed calculation (**"map" stage**).

- Finally, after the calculations for all irreps-q points pairs are finished, the  dynamical  matrices  are  collected and aggregated together, and phonon  dispersions  and  density  of  states  are  calculated (**"reduce" stage**).

Thus, we employ a **"map-reduce"** general type of logic and scenario within the overall workflow, where the individual calculation tasks are performed independently and in parallel with one another. This allows for an improved efficiency and speedup of phonon calculations compared to the [more traditional serial approach](phonon-dispersion-dos.md), such that the limiting factor within the overall calculation is the longest run per individual irreducible representation-q point pair.

A schematic summary of the above workflow procedure is offered in the figure below. This flowchart depicts all different approaches to the calculation of the phonon dispersions and lattice vibrations. The approach used in the present tutorial is the rightmost one. Here, ”SCF” stands for the self consistent field preliminary calculation,  ”ph.x” denotes the  phonon  calculations  by  means  of  Density  Functional  Perturbation  Theory, and  "irrep"  is  an  irreducible  representation  of  a vibrational phonon mode. 

![phonons grid method](../../../images/tutorials/phonons-grid.png "phonons grid method")

## Links

[^1]: [T. Bazhirov, E. X. Abot: "Fast and accessible first-principles calculations of vibrational properties of materials"; arXiv:1808.10011v1, 29 Aug 2018](https://arxiv.org/pdf/1808.10011.pdf)

[^2]: ["Introduction to lattice modes and their symmetry", Oxford University Lecture Document](https://www2.physics.ox.ac.uk/sites/default/files/CrystalStructure_Handout8_0.pdf)

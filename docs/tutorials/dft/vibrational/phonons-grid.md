# Phonon Dispersions and Density of States Calculation on Grid

This tutorial page explains how to calculate the [Phonon Dispersion Curves](../../../properties-directory/non-scalar/phonon-dispersions.md) and [Phonon Density of States](../../../properties-directory/non-scalar/phonon-dos.md) of materials based on [Density Functional Theory](../../../models-directory/dft/overview.md). We will be studying crystalline Silicon in the standard cubic-diamond crystal structure, and we will use [Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md) as our simulation engine.

What sets the present tutorial apart from the [other tutorial](phonons.md) on phonon calculations is the employment of the "Grid Method" for computing the vibrational properties of materials, which is reviewed in the subsequent paragraph. More information on this method can be found in Ref. [^1].

## The Grid Method for Phonon Calculations

The Grid Method allows for an efficient parallelization of the tasks for calculating the individual vibrational modes. This method optimizes the modeling [workflows](../../../workflows/overview.md) in order to minimize the human time required per each calculation, and obtain the frequencies per each individual irreducible representation of the phonon perturbation in parallel.   

We implement a grid-parallel workflow for the calculation of the phonon dynamical matrices initially explained in the first reference cited [in this page](../../../models/auxiliary-concepts/reciprocal-space/sampling.md), with an additional optional preceding step for a [variable-cell relaxation](../../../workflows/addons/structural-relaxation.md).  During the phonon calculation part the following steps happen:

- First, the irreducible representations for the vibrational modes (irreps) are generated, based on the [sampling grid in the reciprocal space](../../../models/auxiliary-concepts/reciprocal-space/sampling.md) (q-point grid). Full symmetry analysis is not performed in the current implementation.

- Second, a separate  calculation  is  prepared  and submitted  for  execution  to  the  computational  infrastructure  manager  per  each  irreducible  representation (”map” stage).

- Finally, after the calculations for all irreps are finished,  the  dynamical  matrices  are  collected  and phonon  dispersions  and  density  of  states  are  calculated (”reduce” stage).

## Links

[^1]: [T. Bazhirov, E. X. Abot: "Fast and accessible first-principles calculations of vibrational properties of materials"; arXiv:1808.10011v1, 29 Aug 2018](https://arxiv.org/pdf/1808.10011.pdf)

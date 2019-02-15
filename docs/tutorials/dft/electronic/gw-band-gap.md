# Calculate Electronic Band Gap with GW Approximation

This tutorial page explains how to calculate the [electronic band gap](../../../properties-directory/non-scalar/band-gaps.md) of a semiconducting material based on [Density Functional Theory](../../../models-directory/dft/overview.md). We consider crystalline silicon in its standard equilibrium cubic-diamond crystal structure, and use [VASP](../../../software-directory/modeling/vasp/overview.md) as our main simulation engine during this tutorial.

What sets the present tutorial apart from the [other tutorial](band-gap.md) on band gap calculations is the employment of the **"GW Approximation"**, which is reviewed in the subsequent paragraph. This method is significantly slower than the conventional approach for computing electronic band gaps, however similarly to the [HSE method](hse.md) it yields more accurate electronic band structure results, thus rectifying the tendency of the [GGA to underestimate the size of the band gap](../../../models-directory/dft/notes.md#accuracy-limits-of-the-generalized-gradient-approximation). More information on this approximation, together with a demonstration of its application and results on a sample set of materials, can be found in Ref. [^1].

## The GW Approximation

A comprehensive theoretical review of the GW Approximation can be found in Refs. [^2],[^3] and [^4]. 

For the sake of this short introduction, it suffices to know that the GWapproximation is obtained using a systematic algebraic approach on the basis of Green function techniques, the most suitable approach for studying excited-state properties of extended systems. It constitutes an approximate expansion of the self-energy up to linear order in the screened Coulomb potential, which describes the interaction between the crystalline atoms. The implementation of theapproximation relies on a perturbative treatment starting from [Density Functional Theory](../../../models-directory/dft/overview.md). 

## Workflow Structure

We shall now describe the computational implementation of the GW Approximation for computing electronic band gaps on our platform, illustrating the various steps constituting the overall [Workflow](../../../workflows/overview.md). For the present explanation, we consider the example case of the [VASP](../../../software-directory/modeling/vasp/overview.md) modeling engine. Further information on how the GW method is supported by VASP can be retrieved in Refs. [^5] and [^6].

Workflows performing GW calculations follow a three-step procedure:

### 1. Preliminary Ground State SCF Calculation

The first [subworkflow step](../../../workflows/components/subworkflows.md) in the overall GW Workflow is a standard self-consistent field (scf) total ground state energy calculation, providing the ensuing steps of the workflow with the wavefunctions of the material structure under investigation (GW calculations always require a one-electron basis set). 

For the sake of the present example, we can set the [grid of special k-points](../../../models/auxiliary-concepts/reciprocal-space/sampling.md) to 6 x 6 x 6, under [Important Settings](../../../workflow-designer/subworkflow-editor/important-settings.md).

### 2. Many Bands SCF Calculation

A significant number of empty bands is required for GW calculations, such that it is typically better to perform the calculations in two steps, as two separate subworkflows: first the above-mentioned standard ground-state SCF calculation with few unoccupied orbitals only, and secondly a calculation over a large number of unoccupied orbitals (bands), by setting the `NBANDS` VASP tag to a large value. 

### 3. GW Step

The actual GW calculation is done in this final subworkflow step. Here different GW flavors are possible and are selected with the `ALGO` VASP tag. 

The "Single Shot" quasi-particle energies method, often referred to as **G0W0**, is the simplest GW calculation, and computationally the most efficient one. A single-shot calculation calculates the quasi-particle energies from a single GW iteration by neglecting all off-diagonal matrix elements of the self-energy, and employing a Taylor expansion of the self-energy around the DFT energies.

After a successful G0W0 run, VASP will write the quasi-particle energies into the main "OUTCAR" output file for every k-point in the Brillouin zone of the crystal structure under investigation.

## Creating and Executing Job

GW-based band gap calculation [workflows](../../../workflows/overview.md) can readily be [imported](../../../workflows/actions/copy-bank.md) into the account-owned [collection](../../../accounts/collections.md) from the [Workflows Bank](../../../workflows/bank.md), for example under the name "surf-D1-GW0-BG-LF".
 
Apart from this, the same procedural instructions as in the [other band gap calculation tutorial](band-gap.md) should be followed for [creating and launching](../../../jobs-designer/overview.md) the corresponding GW-based electronic band gap [Job](../../../jobs/overview.md) through our [Web Interface](../../../ui/overview.md), and for inspecting the associated results.

## Animation

In the video animation below, we outline the procedure for creating and executing an electronic band gap calculation job via the GW Approximation, considering crystalline silicon as our example material and employing [VASP](../../../software-directory/modeling/vasp/overview.md) as the main simulation engine. We conclude by inspecting the corresponding results displayed under the [Results Tab](../../../jobs/ui/results-tab.md) of [Job Viewer](../../../jobs/ui/viewer.md).

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/IWtUgsGwHzk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Links

[^1]: [P. Das, M. Mohammadi, T. Bazhirov: "Accessible computational materials design with high fidelity and high throughput"; arXiv:1807.05623, 15 Jul 2018](https://arxiv.org/abs/1807.05623)

[^2]: [Wikipedia GW Approximation, Website](https://en.wikipedia.org/wiki/GW_approximation)

[^3]: [C. Friedrich and A. Schindlmayr: "Many-Body Perturbation Theory: The GW Approximation"; John von Neumann Institute for Computing Document](https://core.ac.uk/download/pdf/34930704.pdf)

[^4]: [F. Aryasetiawan and O. Gunnarsson: "The GW method"; arXiv:cond-mat/9712013v1, 1 Dec 1997](https://arxiv.org/abs/cond-mat/9712013v1)

[^5]: [GW calculations, Official VASP Documentation](https://cms.mpi.univie.ac.at/wiki/index.php/GW_calculations)

[^6]: [Bandgap of Si in GW, Official VASP Documentation](https://cms.mpi.univie.ac.at/wiki/index.php/Bandgap_of_Si_in_GW)

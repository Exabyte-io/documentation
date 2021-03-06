# Calculate Electronic Band Gap with GW Approximation

This tutorial page explains how to calculate the [electronic band gap](../../../properties-directory/non-scalar/band-gaps.md) of a semiconducting material based on [Density Functional Theory](../../../models-directory/dft/overview.md). We consider crystalline silicon in its standard equilibrium cubic-diamond crystal structure, and use [VASP](../../../software-directory/modeling/vasp/overview.md) as our main simulation engine during this tutorial.

!!!note "VASP version considered in this tutorial"
    The present tutorial is written for VASP at versions 5.3.5 or 5.4.4.

What sets the present tutorial apart from the [other tutorial](band-gap.md) on band gap calculations is the employment of the **"GW Approximation"**, which is reviewed in [this part of the documentation](../../../models-directory/dft/notes.md#the-gw-approximation). This method is significantly slower than the conventional approach for computing electronic band gaps, however similarly to the [HSE method](hse-vasp-bg.md) it yields more accurate electronic band structure results which are closer to experimental values, thus rectifying the tendency of the [GGA to underestimate the size of the band gap](../../../models-directory/dft/notes.md#accuracy-limits-of-the-generalized-gradient-approximation). More information on this approximation, together with a demonstration of its application and results on a sample set of materials, can be found in Ref. [^1].

## Workflow Structure

We shall now describe the computational implementation of the GW Approximation for computing electronic band gaps on our platform, illustrating the various steps constituting the overall [Workflow](../../../workflows/overview.md). For the present explanation, we consider the example case of the [VASP](../../../software-directory/modeling/vasp/overview.md) modeling engine. Further information on how the GW method is supported by VASP can be retrieved in Refs. [^2] and [^3].

Workflows performing GW calculations follow a three-step procedure:

### 1. Preliminary Ground State SCF Calculation

The first [subworkflow step](../../../workflows/components/subworkflows.md) in the overall GW Workflow is a standard self-consistent field (scf) total ground state energy calculation, providing the ensuing steps of the workflow with the wavefunctions of the material structure under investigation (GW calculations always require a one-electron basis set). 

For the sake of the present example, we can set the [grid of special k-points](../../../models/auxiliary-concepts/reciprocal-space/sampling.md) to 10 x 10 x 10, under [Important Settings](../../../workflow-designer/subworkflow-editor/important-settings.md).

### 2. Many Bands SCF Calculation

A significant number of empty bands is required for GW calculations, such that it is typically better to perform the calculations in two steps, as two separate subworkflows: first the above-mentioned standard ground-state SCF calculation with only a few unoccupied orbitals, and secondly a calculation over a large number of unoccupied orbitals (bands), by setting the `NBANDS` VASP tag to a large value. 

### 3. GW Step

The actual GW calculation is done in this final subworkflow step. Here different GW flavors are possible and are selected with the `ALGO` VASP tag. 

The "Single Shot" quasi-particle energies method, often referred to as **G0W0**, is the simplest GW calculation, and computationally the most efficient one. A single-shot calculation calculates the quasi-particle energies from a single GW iteration by neglecting all off-diagonal matrix elements of the self-energy, and employing a Taylor expansion of the self-energy around the DFT energies.

After a successful G0W0 run, VASP will write the quasi-particle energies into the main "OUTCAR" output file for every k-point in the Brillouin zone of the crystal structure under investigation.

In the present example we calculate quasi-particle energies on the grid of k-points. This might not be the most accurate approach, as points on the grid might not fall exactly onto the band extrema for conduction and valence band, however, it is robust and can provide a very reasonable approximation. An intelligent interpolation technique might be used to further extract band dispersions along symmetry paths.

## Creating and Executing Job

GW-based band gap calculation [workflows](../../../workflows/overview.md) can readily be [imported](../../../workflows/actions/copy-bank.md) into the account-owned [collection](../../../accounts/collections.md) from the [Workflows Bank](../../../workflows/bank.md), for example under the name "D1-GW0-BG".

!!!info "Workflow naming convention"
    The "D1-GW0-BG" name for the GW workflow contains the following information: "D" refers to the difficulty level (see table II in Ref. [^1]), "GW0" represents the method, and "BG" is an abbreviation for the band gap. 
 
Apart from this, the same procedural instructions as in the [other band gap calculation tutorial](band-gap.md) should be followed for [creating and launching](../../../jobs-designer/overview.md) the corresponding GW-based electronic band gap [Job](../../../jobs/overview.md) through our [Web Interface](../../../ui/overview.md), and for inspecting the associated results.

## Animation

In the video animation below, we outline the procedure for creating and executing an electronic band gap calculation job via the GW Approximation, considering crystalline silicon as our example material and employing [VASP](../../../software-directory/modeling/vasp/overview.md) as the main simulation engine. We conclude by inspecting the corresponding results displayed under the [Results Tab](../../../jobs/ui/results-tab.md) of [Job Viewer](../../../jobs/ui/viewer.md).

!!!tip "Computational cost of GW calculations"
    GW calculations are in general quite computationally demanding. We therefore recommend the employment of at least 8 computing cores. For larger calculations, [OF queues](../../../infrastructure/resource/queues.md) will have faster turnaround than the OR queues considered in the video.

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/t1IDfMcTIxw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Comparison with Experimental Value

The calculated value of 1.094 eV for the indirect band gap of silicon is in better agreement with the experimental value for this material (1.17 eV [^1]) than the alternative case of standard band gap calculations performed with the [Generalized Gradient Approximation](../../../models-directory/dft/notes.md#accuracy-limits-of-the-generalized-gradient-approximation) (GGA), whose shortcomings are assessed in [another tutorial page](band-gap.md). 

This provides an example of how the GW Approximation can result in improved precision in the estimation of important material properties than more traditional approaches within [DFT](../../../models-directory/dft/overview.md).

## Links

[^1]: [P. Das, M. Mohammadi, T. Bazhirov: "Accessible computational materials design with high fidelity and high throughput"; arXiv:1807.05623, 15 Jul 2018](https://arxiv.org/pdf/1807.05623.pdf)

[^2]: [GW calculations, Official VASP Documentation](https://cms.mpi.univie.ac.at/wiki/index.php/GW_calculations)

[^3]: [Bandgap of Si in GW, Official VASP Documentation](https://cms.mpi.univie.ac.at/wiki/index.php/Bandgap_of_Si_in_GW)

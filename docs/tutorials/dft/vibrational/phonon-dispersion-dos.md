# Phonon Dispersions and Density of States Calculation

This tutorial page explains how to calculate the [Phonon Dispersion Curves](../../../properties-directory/non-scalar/phonon-dispersions.md) and [Phonon Density of States](../../../properties-directory/non-scalar/phonon-dos.md) of materials based on [Density Functional Theory](../../../models-directory/dft/overview.md). We will be studying crystalline Silicon in the standard cubic-diamond crystal structure, and we will use [Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md) as our simulation engine.

!!!note "Quantum ESPRESSO version considered in this tutorial"
    The present tutorial is written for Quantum ESPRESSO at versions 5.2.1, 5.4.0, 6.0.0 or 6.3.

## Create Job

Silicon in its cubic-diamond crystal structure is the [default material](../../../materials/default.md) that is shown on [new job creation](../../../jobs-designer/overview.md), unless this default was [changed](../../../entities-general/actions/set-default.md) by the user following [account](../../../accounts/overview.md) creation. If silicon is still the default choice, it will as such be automatically loaded at the moment of the [opening](../../../jobs/actions/create.md) of [Job Designer](../../../jobs-designer/overview.md).

## Choose Workflow

[Workflows](../../../workflows/overview.md) for calculating the [Phonon Dispersion Curves](../../../properties-directory/non-scalar/phonon-dispersions.md) and [Density of States](../../../properties-directory/non-scalar/phonon-dos.md) of [materials](../../../materials/overview.md) with [Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md) can readily be [imported](../../../workflows/actions/copy-bank.md) from the [Workflows Bank](../../../workflows/bank.md) into the account-owned [collection](../../../accounts/collections.md). This workflow can later be [selected](../../../jobs-designer/actions-header-menu/select-workflow.md) and added to the [Job being created](../../../jobs-designer/workflow-tab.md).

## Set Sampling in Reciprocal Space

It is critical to have a high [q-point density](../../../models/auxiliary-concepts/reciprocal-space/sampling.md#other-types-of-reciprocal-space-grids) in order to resolve enough details for the phonon dispersion plot.

The Phonon calculation workflow based on Quantum ESPRESSO is composed of multiple [units](../../../workflows/components/units.md). The first unit specifies the settings for the self-consistent calculation of the energy eigenvalues and wave functions. The subsequent units are narrated in detail in the theoretical explanation contained in Ref. [^1] of [this page](../../../models/auxiliary-concepts/reciprocal-space/sampling.md).

We set the size of the [grid of q-points (q-grid)](../../../models/auxiliary-concepts/reciprocal-space/sampling.md#other-types-of-reciprocal-space-grids) to 3 x 3 x 3 under the [Important Settings](../../../workflow-designer/subworkflow-editor/important-settings.md) of [Workflow Designer](../../../workflow-designer/overview.md). This provides a dense enough q-point sampling in order to resolve the fine features present within the output of the phonon dispersion computation. In order to make the q- and k-point grids commensurate and make the phonon calculation less computationally demanding, we also reduce the size of the grid of electronic k-points from its original default value to 6 x 6 x 6.

In addition, the associated "interpolated" grid or [i-grid](../../../models/auxiliary-concepts/reciprocal-space/sampling.md#other-types-of-reciprocal-space-grids) necessary for performing the transformation to and from the reciprocal and real space, and subsequent interpolation, should be set to 18 x 18 x 18.

Finally, we also apply the recommended [q-point path](../../../models/auxiliary-concepts/reciprocal-space/paths.md) to effectively sample the vibrational states throughout the Brillouin Zone of the crystal, based on the crystal symmetry.

## Submit Job

Before [submitting](../../../jobs/actions/run.md) the [job](../../../jobs/overview.md), the user should click on the ["Compute" tab](../../../jobs-designer/compute-tab.md) of [Job Designer](../../../jobs-designer/overview.md) and examine the [compute parameters](../../../infrastructure/compute/parameters.md) included therein. 

Phonon calculations are quite computationally expensive and therefore, despite Silicon being a small structure, with the aforementioned settings for the sampling grids the user should account for at least 45 minutes of calculation runtime executed on 16 compute cores for example.

## Examine Final Results

When all [unit](../../../workflows/components/units.md) computations are complete at the end of Job execution, switching to the [Results tab](../../../jobs/ui/results-tab.md) of [Job Viewer](../../../jobs/ui/viewer.md) will show the [phonon lattice vibrations](../../../properties-directory/non-scalar/phonon-dispersions.md) of silicon, plotted as a dispersion curve on the [q-point path](../../../models/auxiliary-concepts/reciprocal-space/paths.md) chosen in the preceding steps.

The plot for the [Phonon Density of States](../../../properties-directory/non-scalar/phonon-dos.md) can also be retrieved in the [Results tab](../../../jobs/ui/results-tab.md), directly above the dispersion curve. 

## Animation

We demonstrate the above-mentioned steps involved in the creation and execution of a phonon lattice vibration calculation for silicon, using the [Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md) simulation engine, in the following animation.

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/em55roTB7fc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

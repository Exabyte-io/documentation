# Electronic Band Structure Calculation

This tutorial page explains how to calculate the [electronic band structure](../../../properties-directory/non-scalar/bandstructure.md) based on [Density Functional Theory](../../../models-directory/dft/overview.md). We will be studying crystalline Silicon in the standard cubic-diamond crystal structure, and we will use [Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md) as our simulation engine.

!!!note "Quantum ESPRESSO version considered in this tutorial"
    The present tutorial is written for Quantum ESPRESSO at versions 5.2.1, 5.4.0, 6.0.0 or 6.3.

!!! Note "Accuracy of the results"
    Please note that this calculation is performed using standard [Density Functional Theory](../../../models-directory/dft/overview.md), and therefore an underestimation of the energy of unoccupied electronic states is expected. Further modifications to the input files and settings to correctly predict the band gap are possible, and will be explored later.

## Create Job

Silicon in its cubic-diamond crystal structure is the [default material](../../../materials/default.md) that is shown on [new job creation](../../../jobs-designer/overview.md), unless this default was [changed](../../../entities-general/actions/set-default.md) by the user following [account](../../../accounts/overview.md) creation. If silicon is still the default choice, it will as such be automatically loaded at the moment of the [opening](../../../jobs/actions/create.md) of [Job Designer](../../../jobs-designer/overview.md).

## Choose Workflow

[Workflows](../../../workflows/overview.md) for calculating the [band structure](../../../properties-directory/non-scalar/bandstructure.md) of [materials](../../../materials/overview.md) with [Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md) can readily be [imported](../../../workflows/actions/copy-bank.md) from the [Workflows Bank](../../../workflows/bank.md) into the account-owned [collection](../../../accounts/collections.md). This workflow can later be [selected](../../../jobs-designer/actions-header-menu/select-workflow.md) and added to the [Job being created](../../../jobs-designer/workflow-tab.md).

## Set Sampling in Reciprocal Space

It is critical to have a high [k-point density](../../../models/auxiliary-concepts/reciprocal-space/sampling.md) in order to resolve enough details for the band structure plot.

The band structure workflow is composed of two [units](../../../workflows/components/units.md). The first unit specifies the settings for the self-consistent calculation of the energy eigenvalues and wave functions.  The second unit calculation is a non self-consistent calculation using the wave functions and charge density of the previous calculation.

We set the size of the grid of k-points to 18 x 18 x 18 in the first workflow unit. This provides a dense enough k-point sampling in order to resolve the fine features present within the output of the band structure computation. The validity of this choice of k-grid size for yielding accurate results of order meV in the final energy can be verified by performing the relevant [convergence study](../../../models/auxiliary-concepts/reciprocal-space/convergence.md).

In addition, we also apply the recommended [k-point path](../../../models/auxiliary-concepts/reciprocal-space/paths.md) to effectively sample the electronic states throughout the Brillouin Zone of the crystal, based on the crystal symmetry.

## Submit Job

Before [submitting](../../../jobs/actions/run.md) the [job](../../../jobs/overview.md), the user should click on the ["Compute" tab](../../../jobs-designer/compute-tab.md) of [Job Designer](../../../jobs-designer/overview.md) and examine the [compute parameters](../../../infrastructure/compute/parameters.md) included therein.  Silicon is a small structure, so 4 CPUs and 1 minute of calculation runtime should be sufficient.

## Examine Final Results

When both [unit](../../../workflows/components/units.md) computations are complete at the end of Job execution, switching to the [Results tab](../../../jobs/ui/results-tab.md) of [Job Viewer](../../../jobs/ui/viewer.md) will show the [band structure](../../../properties-directory/non-scalar/bandstructure.md) of silicon, plotted as a dispersion curve as a function of the special [k-point paths](../../../models/auxiliary-concepts/reciprocal-space/paths.md) chosen.

## Animation

We demonstrate the above-mentioned steps involved in the creation and execution of a band structure computation on silicon using the [Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md) simulation engine in the following animation.

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/x82ntcP4Vj0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

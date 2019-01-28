# Calculate Zero Point Energy

This page explains how to run a [zero point energy](../../../properties-directory/scalar/zero-point-energy.md) calculation based on [density functional theory](../../../models-directory/dft/overview.md). For the sake of this presentation, we will calculate the zero point energy for crystalline silicon in its equilibrium cubic-diamond crystal structure, making use of [VASP](../../../software-directory/modeling/vasp/overview.md) as our simulation engine.

## Create Job

Silicon in its cubic-diamond crystal structure is the [default material](../../../materials/default.md) that is shown on [new job creation](../../../jobs-designer/overview.md), unless this default was [changed](../../../entities-general/actions/set-default.md) by the user following [account](../../../accounts/overview.md) creation. If silicon is still the default choice, it will as such be automatically loaded at the moment of the [opening](../../../jobs/actions/create.md) of [Job Designer](../../../jobs-designer/overview.md).

## Choose Workflow

[Workflows](../../../workflows/overview.md) for calculating the Zero Point Energy through [VASP](../../../software-directory/modeling/vasp/overview.md) can readily be [imported](../../../workflows/actions/copy-bank.md) from the [Workflows Bank](../../../workflows/bank.md) into the account-owned [collection](../../../accounts/collections.md). This workflow can later be [selected](../../../jobs-designer/actions-header-menu/select-workflow.md) and added to the [Job being created](../../../jobs-designer/workflow-tab.md).

## Set Sampling in Reciprocal Space

It is critical that a [well-relaxed structure](../../../workflows/addons/structural-relaxation.md) with [converged k-point density](../../../models/auxiliary-concepts/reciprocal-space/convergence.md) is used for zero point energy calculations.

We set the size of the grid of k-points to 18 x 18 x 18 in the first and only workflow [unit](../../../workflows/components/units.md). The validity of this choice of k-grid size for yielding accurate results of order meV in the final energy can be verified by performing the relevant [convergence study](../../../models/auxiliary-concepts/reciprocal-space/convergence.md).

We explain how to perform both [structural relaxations](../relaxation.md) and [k-points convergence studies](../kpt-convergence.md) in their respective tutorials.

## Submit Job

Before [submitting](../../../jobs/actions/run.md) the [Job](../../../jobs/overview.md), the user should click on the ["Compute" tab](../../../jobs-designer/compute-tab.md) of [Job Designer](../../../jobs-designer/overview.md) and inspect the [compute parameters](../../../infrastructure/compute/parameters.md) included therein.  Silicon is a small structure, so four CPUs and one minute of calculation runtime should be sufficient.

## Examine Results

Once the Job execution is finished, switching to the [Results tab](../../../jobs/ui/results-tab.md) of [Job Viewer](../../../jobs/ui/viewer.md) will show the results of the simulation, including a card titled "Zero Point Energy" that displays the value of this [property](../../../properties/overview.md) for the material in question. 

The larger its value, the more critical it becomes to include the zero point energy in ab-initio thermodynamic calculations performed at zero temperature.

## Animation

We demonstrate the above-mentioned steps involved in the creation and execution of a Zero Point Energy computation workflow on silicon, using the [VASP](../../../software-directory/modeling/vasp/overview.md) simulation engine, in the following animation.

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/VIY1mq1clLo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

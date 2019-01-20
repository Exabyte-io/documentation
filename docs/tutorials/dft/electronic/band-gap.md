# Electronic Band Gap Calculation

This tutorial page explains how to calculate an [electronic band gap](../../../properties-directory/non-scalar/band-gaps.md) based on [Density Functional Theory](../../../models-directory/dft/overview.md). We consider crystalline silicon in its standard equilibrium cubic-diamond crystal structure, and use [VASP](../../../software-directory/modeling/vasp/overview.md) as our main simulation engine during this tutorial.

!!!warning "Accuracy of the results"
    Please note that this calculation is performed using [Density Functional Theory](../../../models-directory/dft/overview.md) together with the [Generalized Gradient Approximation](../../../models-directory/dft/parameters.md#subtype), and therefore a systematic under-estimation of the band gap is to be expected. Further modifications to the input files and settings to correctly predict the band gap are possible, but lie beyond the scope of the present short introduction.

## Definitions

### Band Gap

The [electronic band gap](../../../properties-directory/non-scalar/band-gaps.md) defines the **energy difference** between the **highest occupied electronic state** and the **lowest unoccupied state** within the [electronic band-structure](../../../properties-directory/non-scalar/bandstructure.md) of the material under investigation. 

!!!info "Direct vs Indirect Gaps"
    We support the extraction of both the **direct** and **indirect** band gaps. The difference between the two types is explained [in this page](../../../properties-directory/non-scalar/band-gaps.md#direct-and-indirect-band-gaps).

## Create job

Silicon in its cubic-diamond crystal structure is the [default material](../../../materials/default.md) that is shown on [new job creation](../../../jobs-designer/overview.md), unless this default was [changed](../../../entities-general/actions/set-default.md) by the user following [account](../../../accounts/overview.md) creation. If silicon is still the default choice, it will as such be automatically loaded at the moment of the [opening](../../../jobs/actions/create.md) of [Job Designer](../../../jobs-designer/overview.md).

## Choose Workflow

[Workflows](../../../workflows/overview.md) for calculating the band gap through [VASP](../../../software-directory/modeling/vasp/overview.md) can readily be [imported](../../../workflows/actions/copy-bank.md) from the [Workflows Bank](../../../workflows/bank.md) into the account-owned [collection](../../../accounts/collections.md). This workflow can later be [selected](../../../jobs-designer/actions-header-menu/select-workflow.md) and added to the [Job being created](../../../jobs-designer/workflow-tab.md).

## Set Sampling in Reciprocal Space

It is critical to have a high [k-point density](../../../models/auxiliary-concepts/reciprocal-space/sampling.md) in order to calculate the band gap with sufficient accuracy.

For the case of [VASP](../../../software-directory/modeling/vasp/overview.md), the band gap workflow is composed of two [units](../../../workflows/components/units.md). The first unit specifies the settings for the self-consistent calculation of the energy eigenvalues and wave functions.  The second unit calculation is a non self-consistent calculation using the wave functions and charge density of the previous calculation.

We set the size of the grid of k-points to 18 x 18 x 18 in the first workflow unit. The validity of this choice of k-grid size for yielding accurate results of order meV in the final energy can be verified by performing the relevant [convergence study](../../../models/auxiliary-concepts/reciprocal-space/convergence.md).

## Submit Job

Before [submitting](../../../jobs/actions/run.md) the [job](../../../jobs/overview.md), the user should click on the ["Compute" tab](../../../jobs-designer/compute-tab.md) of [Job Designer](../../../jobs-designer/overview.md) and inspect the [compute parameters](../../../infrastructure/compute/parameters.md) included therein.  Silicon is a small structure, so 4 CPUs and 1 minute of calculation runtime should be sufficient.

## Examine results

When both [unit](../../../workflows/components/units.md) computations are complete at the end of Job execution, switching to the [Results tab](../../../jobs/ui/results-tab.md) of [Job Viewer](../../../jobs/ui/viewer.md) will show the results of the simulation, including the indirect band gap found for Si (~0.6 eV).

!!!note "Silicon as Indirect Gap Semiconductor"
    The user will notice that we identify both the direct band gap and the indirect band gap. This calculation is done during the first, self-consistent step of the calculation on the dense k-point mesh. It can be deduced that the indirect band gap is significantly smaller than the smallest direct band gap, which is the reason why silicon is classed as an **indirect gap semiconductor**. 

### Comparison with Experimental Value

The calculated value of ~0.6 eV for the indirect band gap is significantly below the tabulated experimental value for the band gap of Silicon of ~1.1 eV, however as mentioned earlier in the introduction this underestimation is expected.

## Animation

We demonstrate the above-mentioned steps involved in the creation and execution of a Band Gap computation workflow on silicon using the [VASP](../../../software-directory/modeling/vasp/overview.md) simulation engine in the following animation.

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/gn4Hi_im4So" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


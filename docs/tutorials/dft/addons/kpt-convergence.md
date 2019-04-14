# Study Convergence of the Reciprocal Space Grid

The present tutorial page explains how to run a [convergence study](../../../models/auxiliary-concepts/reciprocal-space/convergence.md) of the size of the [grid of k-points](../../../models/auxiliary-concepts/reciprocal-space/sampling.md), necessary for sampling the Brillouin Zone of the crystal structure under investigation, using [density functional theory](../../../models-directory/dft/overview.md). 

K-point convergence can be run either as a stand-alone [workflow](../../../workflows/overview.md), or prepended as a [Workflow Add-on](../../../workflows/addons/overview.md) to another [property calculation](../../../properties/overview.md).

In the present tutorial, we will study the issue of k-point convergence for the case of crystalline silicon under its equilibrium cubic-diamond crystal structure, by making use of [VASP](../../../software-directory/modeling/vasp/overview.md) as the main simulation engine. We will investigate k-point convergence in the context of a [Total Energy](../../../properties-directory/scalar/total-energy.md) calculation.

!!!note "VASP version considered in this tutorial"
    The present tutorial is written for VASP at versions 5.3.5 or 5.4.4.

## Create Job

Silicon in its cubic-diamond crystal structure is the [default material](../../../materials/default.md) that is shown on [new job creation](../../../jobs-designer/overview.md), unless this default was [changed](../../../entities-general/actions/set-default.md) by the user following [account](../../../accounts/overview.md) creation. If silicon is still the default choice, it will be automatically loaded at the moment of the [opening](../../../jobs/actions/create.md) of [Job Designer](../../../jobs-designer/overview.md).

## Choose workflow

[Workflows](../../../workflows/overview.md) for calculating the Total Energy through [VASP](../../../software-directory/modeling/vasp/overview.md) can readily be [imported](../../../workflows/actions/copy-bank.md) from the [Workflows Bank](../../../workflows/bank.md) into the account-owned [collection](../../../accounts/collections.md). This workflow can later be [selected](../../../jobs-designer/actions-header-menu/select-workflow.md) and added to the [Job being created](../../../jobs-designer/workflow-tab.md).

Thereafter, in order to add k-point convergence as an [Add-on](../../../workflows/addons/overview.md) to the total energy calculation workflow, the user should [click the appropriate button](../../../workflow-designer/subworkflow-editor/actions-menu.md#insert-add-ons) within the [Subworkflow Editor Interface](../../../workflow-designer/subworkflow-editor/overview.md) of [Workflow Designer](../../../workflow-designer/overview.md). The corresponding "Convergence" option should thus be chosen. The parameters contained in the resulting "Convergence" dialog should be set according to the instructions outlined [in this page](../../../models/auxiliary-concepts/reciprocal-space/convergence.md). For the moment, we shall just accept the default contents of such dialog, and proceed with no further modifications by clicking the bottom `Apply` button.

At the end of the insertion of the k-point convergence Add-on to the Total Energy Workflow, the user can scroll down to view the extra [units](../../../workflows/components/units.md) which have been added for convergence purposes, which are primarily of [Logical type](../../../workflows/components/units.md#unit-types). The objective of such units is to set up the parameters necessary to progressively increase [k-point density](../../../models/auxiliary-concepts/reciprocal-space/sampling.md), and consequently check the corresponding evolution of the total energy difference throughout the study to ensure a sufficiently accurate final convergence.

## Examine Input Files

Readers can open the main [Execution Unit](../../../workflows/components/units.md#execution) "vasp" by clicking it. The contents of the input files used for the convergence study within the VASP calculation can in this way be inspected, towards the bottom of the [unit editor interface](../../../workflow-designer/unit-editor.md#unit-input-templates). 

Users should be able to notice some differences in the formatting of the KPOINTS file, compared to the more conventional cases. This file should not normally be edited, or should be edited with caution, since the text is modified to contain [templating expressions](../../../workflows/templating/overview.md) (eg. `{{PARAMETER}}`) that are necessary for the workflow to function correctly.

## Submit Job

Before [submitting](../../../jobs/actions/run.md) the [Job](../../../jobs/overview.md), the user should click on the ["Compute" tab](../../../jobs-designer/compute-tab.md) of [Job Designer](../../../jobs-designer/overview.md) and inspect the [compute parameters](../../../infrastructure/compute/parameters.md) included therein. Silicon is a small structure, so four cores and a few minutes of calculation runtime should be sufficient.

## Examine Results

Once the Job execution is finished, switching to the [Results tab](../../../jobs/ui/results-tab.md) of [Job Viewer](../../../jobs/ui/viewer.md) will show the results of the computation, including the final converged value of the total energy as well as additional information about each execution unit.

## Converged k-point Density

Finally, the user can also browse the output and input files under the [Files tab](../../../jobs/ui/files-tab.md) of [Job Viewer](../../../jobs/ui/viewer.md). In order to determine the k-point density at which convergence was reached, the KPOINTS file should be [downloaded and inspected](../../../data-in-objectstorage/actions/download.md).

### Convergence plot

The convergence plot can be retrieved upon Job completion under the "Charts" tab accessible by opening the main "vasp" Execution Unit. The relevant convergence plot is the one labelled "Ionic Energy". In order for this plot to appear among the calculation results, the "convergence_ionic" option should be selected under the ["Detailed View" tab](../../../workflow-designer/subworkflow-editor/detailed-view.md) of the Total Energy [Subworkflow Editor Interface](../../../workflow-designer/subworkflow-editor/overview.md) at the moment of initial Job designing.

An example appearance of the "Ionic Energy" energy convergence chart as a function of [k-grid size](../../../models/auxiliary-concepts/reciprocal-space/sampling.md#kgrid) is given in the image below. In this case, after a sharp initial shift in energy, the desired convergence precision threshold has been reached for a k-grid size of 13 X 13 X 13. The threshold corresponds to the relative energy change between two subsequent steps in the k-grid size progression shown on the x-axis.

![Convergence Plot](../../../images/tutorials/kpoint-convergence-chart.png "Convergence Plot")

## Animation

We demonstrate the above-mentioned steps involved in the creation and execution of a k-points convergence study using silicon and [Total Energy](../../../properties-directory/scalar/total-energy.md) workflow in the video below.

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/Qdn4Rr4ZFVQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

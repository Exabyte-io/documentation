# Perform Structural Relaxation of a Crystalline Material

This tutorial page explains how to run a [structural relaxation](../../../workflows/addons/structural-relaxation.md) using [density functional theory](../../../models-directory/dft/overview.md). Relaxations consist in simultaneously relaxing the inter-atomic forces within a crystal structure, whilst optimizing the overall lattice geometry by minimizing its corresponding potential energy. 

They can be run either as a stand-alone [workflow](../../../workflows/overview.md), or prepended as a [Workflow Add-on](../../../workflows/addons/overview.md) to another [property calculation](../../../properties/overview.md).

In the present tutorial, we will study the issue of structural relaxation for the case of crystalline silicon under its equilibrium cubic-diamond crystal structure, by making use of the [VASP](../../../software-directory/modeling/vasp/overview.md) simulation engine. We will investigate how to optimize the crystal structure geometry and atomic positions in the context of a [Total Energy](../../../properties-directory/scalar/total-energy.md) computation. Relaxation prior to a property calculation is generally-speaking a critical precaution to take in order to ensure an accurate final result in the material property being sought.

## Create Job

Silicon in its cubic-diamond crystal structure is the [default material](../../../materials/default.md) that is shown on [new job creation](../../../jobs-designer/overview.md), unless this default was [changed](../../../entities-general/actions/set-default.md) by the user following [account](../../../accounts/overview.md) creation. If silicon is still the default choice, it will be automatically loaded at the moment of the [opening](../../../jobs/actions/create.md) of [Job Designer](../../../jobs-designer/overview.md).

## Choose Workflow

[Workflows](../../../workflows/overview.md) for calculating the Total Energy through [VASP](../../../software-directory/modeling/vasp/overview.md) can readily be [imported](../../../workflows/actions/copy-bank.md) from the [Workflows Bank](../../../workflows/bank.md) into the account-owned [collection](../../../accounts/collections.md). This workflow can later be [selected](../../../jobs-designer/actions-header-menu/select-workflow.md) and added to the [Job being created](../../../jobs-designer/workflow-tab.md).

Thereafter, in order to add structural relaxation as an [Add-on](../../../workflows/addons/overview.md) to the total energy calculation workflow, the user should [click the appropriate button](../../../workflow-designer/header-menu.md#inserting-add-ons) within the [Header Menu](../../../workflow-designer/header-menu.md) of [Workflow Designer](../../../workflow-designer/overview.md). The corresponding "Relaxation" option under this button should thus be chosen. 

At the end of the insertion of the relaxation Add-on to the Total Energy Workflow, the user will notice that an additional "Variable-cell Relaxation" [Subworkflow](../../../workflows/components/subworkflows.md) has been prepended to the overall [computation order flowchart](../../../workflow-designer/sidebar.md) exhibited on the left-hand side of [Workflow Designer Interface](../../../workflow-designer/overview.md).

## Examine Unit Input Files

The user can now try to open the main "vc-relax" [Execution Unit](../../../workflows/components/units.md) within the "Variable-cell Relaxation" [Subworkflow](../../../workflows/components/subworkflows.md) by clicking it. The contents of the input files used for the structural relaxation study within the VASP calculation can in this way be inspected, towards the bottom of the [unit editor interface](../../../workflow-designer/unit-editor.md#unit-input-templates). 

The type of relaxation calculation performed is always by default a variable-cell relaxation allowing for all crystalline degrees of freedom to adjust simultaneously, including therefore a relaxation of the atomic positions as well as of the unit cell shape and size.

Please note that the POSCAR file employed in the ensuing Total Energy subworkflow computation is just a placeholder, and during the course of its execution will be overwritten by a CONTCAR file obtained from the results of the preliminary relaxation.

## Submit Job

Before [submitting](../../../jobs/actions/run.md) the [Job](../../../jobs/overview.md), the user should click on the ["Compute" tab](../../../jobs-designer/compute-tab.md) of [Job Designer](../../../jobs-designer/overview.md) and inspect the [compute parameters](../../../infrastructure/compute/parameters.md) included therein.  Silicon is a small structure, so four CPUs and one minute of calculation runtime should be sufficient.

## Examine Results

Once the Job execution is finished, switching to the [Results tab](../../../jobs/ui/results-tab.md) of [Job Viewer](../../../jobs/ui/viewer.md) will show the results of the computation, including the final optimized value of the total energy as well as additional information about each execution unit.

## Optimized Crystal Structure Parameters

Finally, the user can also browse the actual output and input files that are part of the calculation under the [Files tab](../../../jobs/ui/files-tab.md) of [Job Viewer](../../../jobs/ui/viewer.md). In order to determine the crystal structure geometry for which relaxation was achieved in the end, the POSCAR file should be [downloaded and inspected](../../../data-in-objectstorage/actions/download.md). 

The crystalline structural data contained in this file can readily be visualized graphically by following the instructions outlined in a [separate tutorial].

## Animation

We demonstrate the above-mentioned steps involved in the creation and execution of a [structural relaxation](../../../workflows/addons/structural-relaxation.md) study on a silicon-based [Total Energy](../../../properties-directory/scalar/total-energy.md) workflow computation under the following animation, where we make use of the [VASP](../../../software-directory/modeling/vasp/overview.md) simulation engine.

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/Qdn4Rr4ZFVQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

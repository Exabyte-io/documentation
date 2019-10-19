# Perform Structural Relaxation 

This tutorial explains how to run a [structural relaxation](../../../workflows/addons/structural-relaxation.md) using [Density Functional Theory](../../../models-directory/dft/overview.md). Variable-cell relaxation consist in simultaneously minimizing the inter-atomic forces, whilst also optimizing the overall lattice geometry by minimizing its corresponding potential energy together with the components of its internal [stress tensor](../../../properties-directory/non-scalar/stress-tensor.md). 

## Accessing the Functionality

Relaxation can be run either as a stand-alone [workflow](../../../workflows/overview.md), or prepended as a [Workflow Add-on](../../../workflows/addons/overview.md) to another [property calculation](../../../properties/overview.md).

## Summary

In the present tutorial, we study the crystalline silicon distorted from its equilibrium cubic-diamond crystal structure and make use of the [VASP](../../../software-directory/modeling/vasp/overview.md) simulation engine. We will investigate how to optimize the crystal structure geometry and atomic positions in the context of a [Total Energy](../../../properties-directory/scalar/total-energy.md) computation. Relaxation prior to a property calculation is generally-speaking a critical precaution to take in order to ensure an accurate final result in the material property being sought.

!!!info "Generality of tutorial instructions"
    Despite making explicit references to [VASP](../../../software-directory/modeling/vasp/overview.md), the instructions presented herein are of general applicability to all [modeling engines](../../../software-directory/overview.md#modeling-applications) supported on our platform.
    
!!!note "VASP version considered in this tutorial"
    The present tutorial is written for VASP at versions 5.3.5 or 5.4.4.

## Create Job

Silicon in its cubic-diamond crystal structure is the [default material](../../../materials/default.md) shown on [new job creation](../../../jobs-designer/overview.md), unless this default was [changed](../../../entities-general/actions/set-default.md) by the user following [account](../../../accounts/overview.md) creation. If silicon is still the default choice, it will be automatically loaded at the moment of the [opening](../../../jobs/actions/create.md) of [Job Designer](../../../jobs-designer/overview.md).

## Choose Workflow

[Workflows](../../../workflows/overview.md) for calculating the Total Energy can be [imported](../../../workflows/actions/copy-bank.md) from the [Workflows Bank](../../../workflows/bank.md) into the account-owned [collection](../../../accounts/collections.md). This workflow can later be [selected](../../../jobs-designer/actions-header-menu/select-workflow.md) and added to the [Job being created](../../../jobs-designer/workflow-tab.md).

Thereafter, in order to add structural relaxation as an [Add-on](../../../workflows/addons/overview.md) to the total energy calculation workflow, the user should [click the appropriate button](../../../workflow-designer/header-menu.md#inserting-add-ons) within the [Header Menu](../../../workflow-designer/header-menu.md) of [Workflow Designer](../../../workflow-designer/overview.md). The corresponding "Relaxation" option under this button should thus be chosen. 

At the end of the insertion of the relaxation Add-on to the Total Energy Workflow, the user will notice that an additional "Variable-cell Relaxation" [Subworkflow](../../../workflows/components/subworkflows.md) has been prepended to the overall [computation order flowchart](../../../workflow-designer/sidebar.md) exhibited on the left-hand side of the [Workflow Designer Interface](../../../workflow-designer/overview.md).

## Examine Unit Input Files

The user can now try to open the main "vc-relax" [Execution Unit](../../../workflows/components/units.md) within the "Variable-cell Relaxation" [Subworkflow](../../../workflows/components/subworkflows.md) by clicking it. The contents of the input files used for the structural relaxation study can in this way be inspected, towards the bottom of the [unit editor interface](../../../workflow-designer/unit-editor.md#unit-input-templates). 

The type of relaxation calculation performed is always by default a variable-cell including the relaxation of the [atomic positions](../../../properties-directory/structural/basis.md) as well as of the [unit cell shape and size](../../../properties-directory/structural/lattice.md).

Please note that the second total energy subworkflow reads the structural information output by the preliminary relaxation, instead of the parameters in its own input.
 
!!!note "Specific example for VASP"
    The POSCAR file employed in the ensuing Total Energy subworkflow computation is just a placeholder, and during the course of its execution will be overwritten by a CONTCAR file obtained from the results of the relaxation. This behavior is triggered by the "prepare_restart" post-processor.

## Submit Job

Before [submitting](../../../jobs/actions/run.md) the [Job](../../../jobs/overview.md), the user should click the ["Compute" tab](../../../jobs-designer/compute-tab.md) of [Job Designer](../../../jobs-designer/overview.md) and inspect the [compute parameters](../../../infrastructure/compute/parameters.md) included therein. Silicon is a small structure, so four CPU cores and one minute of calculation runtime should be sufficient.

## Examine Results

Once the Job execution is finished, switching to the [Results tab](../../../jobs/ui/results-tab.md) of [Job Viewer](../../../jobs/ui/viewer.md) will show the results of the computation, including the final optimized value of the total energy as well as additional information about each execution unit.

## Optimized Structural Parameters

Finally, the user can also browse the actual output and input files that are part of the calculation under the [Files tab](../../../jobs/ui/files-tab.md) of [Job Viewer](../../../jobs/ui/viewer.md). In order to determine the structure geometry for which relaxation was achieved in the end, the POSCAR file can be [downloaded and inspected](../../../data-in-objectstorage/actions/download.md). 

The structural data contained in this file can readily be visualized graphically under the [Materials Viewer](../../../materials/ui/viewer.md) instance contained within the [Results tab](../../../jobs/ui/results-tab.md).

## Animation

We demonstrate the above-mentioned steps involved in the creation and execution of a [structural relaxation](../../../workflows/addons/structural-relaxation.md) study on a [Total Energy](../../../properties-directory/scalar/total-energy.md) workflow computation under the following animation, where we make use of the [Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md) simulation engine. The starting point is a crystal structure of silicon which has been slightly distorted from its equilibrium cubic-diamond lattice parameters and atomic positions.

As expected, the components of both the atomic forces and [stress tensor](../../../properties-directory/non-scalar/stress-tensor.md) shown at the end of the structural relaxation computation, under the interface of [Results tab](../../../jobs/ui/results-tab.md), have low values in proximity to zero, signalling successful relaxation and geometry optimization.

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/vHmId3iU_Ik" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

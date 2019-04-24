# Band Gap and Density of States with Quantum ESPRESSO (HSE)

This tutorial page explains how to calculate the [electronic band gap](../../../properties-directory/non-scalar/band-gaps.md) and [Density of States](../../../properties-directory/non-scalar/electronic-dos.md) (DoS) of semiconducting [materials](../../../materials/overview.md) based on [Density Functional Theory](../../../models-directory/dft/overview.md). We consider crystalline silicon in its standard equilibrium cubic-diamond crystal structure, and use [Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md) as our main simulation engine during this tutorial.

!!!note "Quantum ESPRESSO version considered in this tutorial"
    The present tutorial is written for Quantum ESPRESSO at versions 5.2.1, 5.4.0, 6.0.0 or 6.3.

We discuss in the present tutorial those aspects of the band gap and DoS calculation which are specific to the implementation of the **HSE (Heyd-Scuseria-Ernzerhof)** [exchange-correlation functional](../../../models-directory/dft/parameters.md#functional), a special class of [Hybrid Functionals](../../../models-directory/dft/parameters.md#hybrid-functionals). The increased [precision](../../../methods/precision.md) of Hybdrid Functionals in predicting [material properties](../../../properties/overview.md) of interest such as band gaps will hence be demonstrated. 
 
The instructions presented herein complement the general discussion introduced in a [separate tutorial](band-gap.md). The reader is referred to this latter page for an outline of the general procedure for band gap computations using DFT, whereas only HSE-specific aspects will be reviewed throughout the remainder of the present page. The reader is also invited to consult [this other tutorial](hse-qe-bs.md) for a more general review and introduction to HSE-based computations of electronic band structures using Quantum ESPRESSO. 

## Workflow for HSE Band Gap and DoS Calculation with Quantum ESPRESSO

Contrary to the case of [Quantum ESPRESSO-based HSE computations of the band structure](hse-qe-bs.md), in which the list of electronic k-points had to be extracted and then inserted manually within the main input script, in the present case where we limit ourselves to the computation of the band gap and DoS only, the [grid of special k-points](../../../models/auxiliary-concepts/reciprocal-space/sampling.md) can be defined automatically as customarily done in self-consistent field (scf) total ground-state energy computations.

Apart from this, the structure of the main Quantum ESPRESSO input script is essentially the same as for a general HSE-based band structure computation. The HSE-specific aspects and parameters of the scf calculation can be triggered by including the HSE [Refiner](../../../models-directory/dft/parameters.md#refiners), as set under the [Subworkflow Editor Interface](../../../workflow-designer/subworkflow-editor/overview-tab.md#refiners).

For band-gap computations, it is also essential to ensure that the corresponding "band_gaps" [property](../../../properties/overview.md) calculation option, available under the ["Detailed View" tab](../../../workflow-designer/subworkflow-editor/detailed-view.md) of the [Subworkflow Editor Interface](../../../workflow-designer/subworkflow-editor/overview-tab.md#refiners), gets ticked for selection before the beginning of Job execution.

### Main HSE Computation Unit

The [Workflow](../../../workflows/overview.md) for executing the HSE band gap and DoS calculation is contained within a single [Subworkflow](../../../workflows/components/subworkflows.md), itself comprising two [units](../../../workflows/components/units.md), the first one for executing the main HSE computation and the second one for extracting the DoS via the `projwfc.x` [Quantum ESPRESSO executable](../../../software-directory/modeling/quantum-espresso/components.md#executables). Except for the automatic generation of k-points, the Quantum ESPRESSO input script defined within the former unit conforms to the same general conventions of a HSE-based band structure computation such as outlined [in this other tutorial](hse-qe-bs.md).

### Size of the q-grid

It is nevertheless crucial, in order to obtain an accurate numerical estimate of the band gap size, to have a sufficiently large three-dimensional mesh for the q (k1-k2) sampling of the Fock operator, as defined through the "nqx1, nqx2, nqx3" input keywords within the Quantum ESPRESSO input script. This "q-grid" size has to be a divisor of the k-grid size, and for the sake of the present tutorial we recommend setting the k-grid dimensions to 8x8x8 and the q-grid to 4x4x4 for example, as can be set under the ["Important Settings" tab](../../../workflow-designer/subworkflow-editor/important-settings.md) of the [Subworkflow Editor interface](../../../workflow-designer/subworkflow-editor/overview.md). 

#### Restrictions on kgrid size

The user is advised that the default settings in the HSE band gap computation workflow are such that **the q-grid is set to be half the size of the kgrid** entered by the user. Hence an **even kgrid size** is always required, for example 8x8x8 yielding a q-grid of dimensions 4x4x4.
 
 Should the user enter an odd number for the kgrid dimensions by mistake, this size will automatically be increased by one in the workflow to make it even: for example, a 5x5x5 kgrid size entered by the user is increased to 6x6x6 by the workflow operations, thus resulting in a 3x3x3 q-grid. 
 
 In order to change this default behaviour, the user is invited to manually edit the Quantum ESPRESSO input script for the main HSE calculation directly through the corresponding [unit editor interface](../../../workflow-designer/unit-editor.md), within its [input script template](../../../workflow-designer/unit-editor/input-templates.md).

### Estimated Computational Cost

The user is welcome to explore how the precision of the final band gap result depends on the choice of such grid size parameters, within the limits of the computational resources at his disposal. 

The aforementioned recommended choice of grid dimensions however already constitutes a significant computational cost, requiring an estimated execution time of about 20-30 minutes on 16 CPU cores, but presents the advantage of yielding an appreciably accurate final result for the size of the silicon band gap, as explained later in the present tutorial.

## Copy HSE Workflow from Bank

[Workflows](../../../workflows/overview.md) for calculating the [electronic band gap](../../../properties-directory/non-scalar/band-gaps.md) and [Density of States](../../../properties-directory/non-scalar/electronic-dos.md) of semiconducting [materials](../../../materials/overview.md) with [Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md) via the HSE approach being presently considered can readily be [imported](../../../workflows/actions/copy-bank.md) from the [Workflows Bank](../../../workflows/bank.md) into the account-owned [collection](../../../accounts/collections.md). 

This workflow can later be [selected](../../../jobs-designer/actions-header-menu/select-workflow.md) and added to the [Job being created](../../../jobs-designer/overview.md). The same procedure as in the [general band-gap computation tutorial](band-gap.md) can otherwise be followed.

!!!warning "Computational Cost"
    The computational cost of HSE calculations is significantly higher than for more basic methods in [DFT](../../../models-directory/dft/overview.md) such as the [Generalized Gradient Approximation](../../../models-directory/dft/parameters.md#subtype). We thus recommend to allow for more [CPU cores and/or walltime](../../../infrastructure/compute/parameters.md) as appropriate for the material system under investigation.
    
## Animation

We demonstrate the steps involved in the creation and execution of a HSE Band Gap and DoS computation workflow on silicon, using the [Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md) simulation engine, in the following animation. We conclude by inspecting the final numerical result for the size of the indirect band gap of silicon under the ["Results" Tab](../../../jobs/ui/results-tab.md) of [Job Viewer](../../../jobs/ui/viewer.md). 

The final result of 1.193 eV is in excellent agreement with the value at zero temperature quoted in the literature of 1.17 eV. Thus, HSE provides a marked improvement in the accuracy of band gap estimations compared to more traditional approaches in DFT such as the [Generalized Gradient Approximation](../../../models-directory/dft/parameters.md#subtype), which is known on the other hand to significantly underestimate the size of band gaps as discussed [elsewhere](../../../models-directory/dft/notes.md#accuracy-limits-of-the-generalized-gradient-approximation).

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/ailaAlkaIRE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

# Calculate Reaction Energy Profile Using Nudged Elastic Band (NEB) method

This tutorial page explains how to calculate the [energy reaction profile](../../../properties-directory/non-scalar/reaction-energy-profile.md) and [activation barrier](../../../properties-directory/scalar/reaction-energy-barrier.md) for the multi-dimensional energy space of chemical reactions via the [**Nudged Elastic Bands (NEB) method**](../../../models/auxiliary-concepts/nudged-elastic-band.md), by making use of the [interpolated sets](../../../materials-designer/header-menu/advanced/interpolated-set.md) introduced in a [separate tutorial](../../materials/interpolated-sets.md). 

We consider the example of a one-dimensional, three-atom molecule of Hydrogen (H3) throughout the present tutorial, and shall be making use of [Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md) as the main simulation engine, via the implementation of its `PWneb` [flavor](../../../software-directory/modeling/quantum-espresso/components.md#flavors). 

!!!note "Quantum ESPRESSO version considered in this tutorial"
    The present tutorial is written for Quantum ESPRESSO at versions 5.2.1, 5.4.0, 6.0.0 or 6.3.

This example considers a simple activated reaction, consisting in the **collinear proton transfer reaction**:

```text
H2 + H  <==>  H + H2
```

In this triatomic reaction, the middle H atom breaks the bond with first atom and forms a molecule with third atom. We will thus calculate the energy activation barrier of this reaction. This same example is also offered as part of the Quantum ESPRESSO online documentation [^1]. 

## Workflow Structure

We outline here some important aspects of the [Workflow](../../../workflows/overview.md) used for executing NEB calculations on our platform via [Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md), which is composed of a single main [unit](../../../workflows/components/units.md).

### Main Executable

NEB calculations are performed through the ["neb.x" Quantum ESPRESSO Executable](../../../software-directory/modeling/quantum-espresso/components.md#executables). The input parameters for this executable are described in Ref. 4 of [this page](../../../software-directory/modeling/quantum-espresso/components.md), and can be customized by the user via the [unit input template editor](../../../workflow-designer/unit-editor.md#unit-input-templates) within the [Workflow Designer Interface](../../../workflow-designer/overview.md). 

### Broyden Algorithm

Within the neb.x input script, we note in particular the need for the [Broyden algorithm](../../../methods/auxiliary-concepts/optimization-algorithms.md) instead of the default one, for numerically solving iterative minimization and optimization problems such as the [structural relaxations](../../../workflows/addons/structural-relaxation.md) performed on the interpolated set images during the course of the NEB computation. This helps to remove the problem of ”oscillations” in the calculated activation energies. If these oscillations persist, and the user cannot afford more images, he/she should focus on smaller problems by decomposing the original one into pieces.

### Number of Images

The number of image points used to discretize the reaction path, as defined by the [interpolated set](../../../materials-designer/header-menu/advanced/interpolated-set.md) of images to be considered for the NEB calculation, is defined by the `num_of_images` input parameter, and must be larger than 3 (including the initial and final images). 

The number of intermediate NEB images should be set under the "neb" section of the ["Important Settings" Tab](../../../workflow-designer/subworkflow-editor/important-settings.md) within the [Workflow Designer Interface](../../../workflow-designer/overview.md), for their automatic generation by Quantum ESPRESSO (without consequently the need to import an interpolated set manually, as described later in this page).

### Convergence Threshold

The NEB simulation stops when the error (the norm of the force orthogonal to the path in eV/A) is less than the `path_thr` input parameter.

### Structure of Images

Atomic positions for all the images are specified within the `BEGIN_POSITIONS / END_POSITIONS` delimiters, where each instance of `ATOMIC_POSITIONS` card is prefixed either by `FIRST_IMAGE`, `INTERMEDIATE_IMAGE`, or `LAST_IMAGE` keywords, depending on its position within the overall order of the interpolated set under consideration.

## Create Job 

We start with [opening](../../../jobs/actions/create.md) an instance of the [Job Designer Interface](../../../jobs-designer/overview.md) for creating and designing new computational [Jobs](../../../jobs/overview.md) on our platform.
    
## Import Interpolated Set

The **Interpolated Set** generated in [this other tutorial](../../materials/interpolated-sets.md) under the name "NEB CONSTRAINED SET", containing the initial, final and a total of 3 intermediate images of the H3 molecule under investigation (including atomic constraints along the single dimension of the molecule), should then be [selected and imported](../../../jobs-designer/actions-header-menu/select-materials.md) into the ["Materials Viewer" Tab](../../../jobs-designer/materials-tab.md) of the NEB job being [designed](../../../jobs-designer/overview.md). This is done by [selecting](../../../entities-general/actions/select.md) all images contained in the set at the moment of import.

## Choose Workflow

[Workflows](../../../workflows/overview.md) for calculating the reaction energy profile of chemical molecules via NEB with [Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md) can readily be [imported](../../../workflows/actions/copy-bank.md) from the [Workflows Bank](../../../workflows/bank.md) into the account-owned [collection](../../../accounts/collections.md). This workflow can later be [selected](../../../jobs-designer/actions-header-menu/select-workflow.md) and added to the [Job being created](../../../jobs-designer/workflow-tab.md).

!!!warning "Size of grid of k-points"
    The user should take care to set the size of the [grid of reciprocal k-points (kgrid)](../../../models/auxiliary-concepts/reciprocal-space/sampling.md) to 1 x 1 x 1 under the ["Important Settings" Tab](../../../workflow-designer/subworkflow-editor/important-settings.md) of the [Workflow Designer Interface](../../../workflow-designer/overview.md), since we are presently dealing with single molecules as opposed to periodic crystalline structures.

## Submit Job

Before [submitting](../../../jobs/actions/run.md) the [job](../../../jobs/overview.md), the user should click on the ["Compute" tab](../../../jobs-designer/compute-tab.md) of [Job Designer](../../../jobs-designer/overview.md) and examine the [compute parameters](../../../infrastructure/compute/parameters.md) included therein. The H3 molecules being considered in the present tutorial are relatively small structures, hence 4 CPUs and a few minutes of calculation runtime should be sufficient.

## Examine Final Results

When the NEB computation is complete at the end of Job execution, switching to the [Results tab](../../../jobs/ui/results-tab.md) of [Job Viewer](../../../jobs/ui/viewer.md) will show the **Reaction Energy Profile** for the H3 molecules under investigation, plotted in the form of an energy curve as a function of the one-dimensional reaction coordinate that is varied from the initial to final configuration.

An example of such a reaction energy profile is shown in the image below, in which the intermediate activation energy barrier between reactants and products is clearly visible.

![Reaction Energy Profile](../../../images/tutorials/reaction-profile.png "Reaction Energy Profile")

## Retrieve Final Optimized Images

The final optimized image structures can be retrieved at the end of Job execution according to the instructions contained [in this page](../../../workflows/addons/structural-relaxation.md#initial/final-structures-set).

## Animation

### NEB with Manually-Generated Images

We demonstrate the above-mentioned steps involved in the creation and execution of an NEB-based reaction energy profile computation on H3 molecules using the [Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md) simulation engine in the following animation. 

Here, we have made use of the constrained interpolated set containing 3 intermediate images generated manually in a [separate tutorial](../../materials/interpolated-sets.md). It can be deduced from the final result for the energy reaction profile that the size of the activation barrier in this case is of 0.2 eV. This result is in good agreement with those published in the literature for the same collinear proton transfer chemical reaction (see for example page 26 in Ref. [^2]).

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/n5f1Eims1Y0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### NEB with Automatically Generated Images

We can repeat the same reaction profile calculation for H3 molecules as above, but this time taking advantage of the Quantum ESPRESSO feature for the automatic generation of intermediate images mentioned previously. This effectively makes it redundant to import manually an interpolated set, such as was done in the previous video. 

This feature can be enabled by selecting an appropriate number of intermediate images to be generated under the ["Important Settings" Tab](../../../workflow-designer/subworkflow-editor/important-settings.md) of the [Workflow Designer Interface](../../../workflow-designer/overview.md), as demonstrated in the animation where we select to generate a total of 5 intermediate images. In this case, only the initial and final images need to be imported manually into Job Designer.


## Links

[^1]: [Quantum ESPRESSO NEB Example, Official GitHub Repository](https://github.com/maxhutch/quantum-espresso/tree/master/NEB/examples/example01)

[^2]: [Guido Fratesi: "Low Temperature methane-to-methanol conversion on transition metal surfaces", Ph.D Thesis](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.378.7331&rep=rep1&type=pdf)

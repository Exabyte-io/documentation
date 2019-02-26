# Calculate Reaction Profile Using the Nudged Elastic Band (NEB) method

This tutorial page explains how to calculate the energy reaction profile and activation barrier for the multi-dimensional energy space of chemical reactions via the **Nudged Elastic Bands (NEB) method**, by making use of the [interpolated sets](../../../materials-designer/header-menu/advanced/interpolated-set.md) introduced in a [separate tutorial](../../materials/interpolated-sets.md). 

We consider the example of a one-dimensional, three-atom molecule of Hydrogen (H3) throughout the present tutorial, and shall be making use of [Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md) as the main simulation engine, via the implementation of its `PWneb` [flavor](../../../software-directory/modeling/quantum-espresso/components.md#flavors) [^1]. 

## Theoretical Background

A detailed theoretical review of the NEB method can be found in Ref. [^2]. A brief introductory explanation is offered in what follows.

### The Challenge: Predicting the Minimum Energy Path in Chemical Reactions
 
In the context of the present introduction, it suffices to know that NEB aims at tackling a common and important problem in theoretical chemistry and in condensed matter physics, consisting in the the identification of the **lowest energy path** for a transition/rearrangement of a group of atoms from one stable configuration to another. Such transitions may be encountered for example during the course of chemical reactions, changes in conformation of molecules, or diffusion processes in solids. 

Such a transition path is often referred to as the **"minimum energy path" (MEP)**. The potential energy maximum along the MEP is the **saddle point energy** which gives the **activation energy barrier**, a quantity of crucial importance for estimating the transition rate of the reaction.

An example of a two-dimensional energy surface landscape for a generic transition between two structures, corresponding to two local energy minima, is shown in the image below. The position of the intermediate saddle in the energy is also highlighted.

![Energy Surface](../../../images/tutorials/NEB-example.png "Energy Surface")

### The Nudged Elastic Bands Method

Many different methods, including NEB, have been proposed for finding minimum energy reaction paths and saddle points between known reactants and products. The NEB method works by optimizing a number of **intermediate images** along the reaction path. Each image finds the lowest energy possible, while maintaining equal spacing to neighboring images. This constrained optimization is done by adding spring forces along the band between images, and by projecting out the component of the force due to the potential perpendicular to the band.

### Climbing Image

The computational efficiency of the NEB method can be further improved through the adoption of the **Climbing Image** approach, which allows for a more accurate finding of saddle points using the NEB with fewer images than the original method. 

In the climbing image modification, the highest energy image is driven up to the saddle point. This image does not feel the spring forces along the band. Instead, the true force at this image along the tangent is inverted. In this way, the image tries to maximize its energy along the band, and minimize it in all other directions. When this image converges, it will be at the exact saddle point.

### Example 

The graph below shows a traditional NEB calculation (blue) and a climbing image cNEB calculation (red). The cNEB energies have been shifted by 0.05 eV so that the two curves are distinct. Notice how the climbing image calculation has shifted the position of the images (by compressing the images on the left of the plot), so that one image sits right at the saddle point.

![NEB](../../../images/tutorials/NEB.png "NEB")

## Workflow Structure

We outline here some important aspects of the [Workflow](../../../workflows/overview.md) used for executing NEB calculations on our platform via [Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md), which is composed of a single main [unit](../../../workflows/components/units.md).

### Main Executable

NEB calculations are performed through the ["neb.x" Quantum ESPRESSO Executable](../../../software-directory/modeling/quantum-espresso/components.md#executables). The input parameters for this executable are described in Ref. [^3], and can be customized by the user via the [unit input template editor](../../../workflow-designer/unit-editor.md#unit-input-templates) within the [Workflow Designer Interface](../../../workflow-designer/overview.md). 

### Broyden Algorithm

Within the neb.x input script, we note in particular the need for the **Broyden algorithm** [^4] instead of the default one. This helps to remove the problem of ”oscillations” in the calculated activation energies. If these oscillations persist, and the user cannot afford more images, he/she should focus on smaller problems by decomposing the original one into pieces.

### Number of Images

The number of image points used to discretize the reaction path, as defined by the [interpolated set](../../../materials-designer/header-menu/advanced/interpolated-set.md) of images to be considered for the NEB calculation, is defined by the `num_of_images` input parameter, and must be larger than 3 (including the initial and final images). 

The number of intermediate NEB images should be set under the "neb" section of the ["Important Settings" Tab](../../../workflow-designer/subworkflow-editor/important-settings.md) within the [Workflow Designer Interface](../../../workflow-designer/overview.md), for their automatic generation by Quantum ESPRESSO (without consequently the need to import an interpolated set manually, as described later in this page).

### Convergence Threshold

The NEB simulation stops when the error (the norm of the force orthogonal to the path in eV/A) is less than the `path_thr` input parameter.

### Structure of Images

Atomic positions for all the images are specified within the `BEGIN_POSITIONS / END_POSITIONS` delimiters, where each instance of `ATOMIC_POSITIONS` card is prefixed either by `FIRST_IMAGE`, `INTERMEDIATE_IMAGE`, or `LAST_IMAGE` keywords, depending on its position within the overall order of the interpolated set under consideration.

## Create Job and Choose Workflow

We start with [opening](../../../jobs/actions/create.md) an instance of the [Job Designer Interface](../../../jobs-designer/overview.md) for creating and designing new computational [Jobs](../../../jobs/overview.md) on our platform.

[Workflows](../../../workflows/overview.md) for calculating the reaction energy profile of chemical molecules via NEB with [Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md) can readily be [imported](../../../workflows/actions/copy-bank.md) from the [Workflows Bank](../../../workflows/bank.md) into the account-owned [collection](../../../accounts/collections.md). This workflow can later be [selected](../../../jobs-designer/actions-header-menu/select-workflow.md) and added to the [Job being created](../../../jobs-designer/workflow-tab.md).

!!!warning "Size of grid of k-points"
    The user should take care to set the size of the [grid of reciprocal k-points (kgrid)](../../../models/auxiliary-concepts/reciprocal-space/sampling.md) to 1 x 1 x 1 under the ["Important Settings" Tab](../../../workflow-designer/subworkflow-editor/important-settings.md) of the [Workflow Designer Interface](../../../workflow-designer/overview.md), since we are presently dealing with single molecules as opposed to periodic crystalline structures.
    
## Import Interpolated Set

The **Interpolated Set** generated in [this other tutorial](../../materials/interpolated-sets.md) under the name "NEB SET", containing the initial, final and a total of 10 intermediate images of the H3 molecule under investigation, should then be [selected and imported](../../../jobs-designer/actions-header-menu/select-materials.md) into the ["Materials Viewer" Tab](../../../jobs-designer/materials-tab.md) of the NEB job being [designed](../../../jobs-designer/overview.md). This is done by [selecting](../../../entities-general/actions/select.md) all images contained in the set at the moment of import.

## Submit Job

Before [submitting](../../../jobs/actions/run.md) the [job](../../../jobs/overview.md), the user should click on the ["Compute" tab](../../../jobs-designer/compute-tab.md) of [Job Designer](../../../jobs-designer/overview.md) and examine the [compute parameters](../../../infrastructure/compute/parameters.md) included therein. The H3 molecules being considered in the present tutorial are relatively small structures, hence 4 CPUs and a few minutes of calculation runtime should be sufficient.

## Examine Final Results

When the NEB computation is complete at the end of Job execution, switching to the [Results tab](../../../jobs/ui/results-tab.md) of [Job Viewer](../../../jobs/ui/viewer.md) will show the **Reaction Energy Profile** for the H3 molecules under investigation, plotted in the form of an energy curve as a function of the one-dimensional reaction coordinate that is varied from the initial to final configuration.

An example of such a reaction energy profile is shown in the image below, in which the intermediate activation energy barrier between reactants and products is clearly visible.

![Reaction Energy Profile](../../../images/tutorials/reaction-profile.png "Reaction Energy Profile")

## Animation

We demonstrate the above-mentioned steps involved in the creation and execution of an NEB-based reaction energy profile computation on H3 molecules using the [Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md) simulation engine in the following animation. 

Here, we have made use of the interpolated set containing 10 intermediate images generated in a [separate tutorial](../../materials/interpolated-sets.md). It can be deduced from the final result for the energy reaction profile that the size of the activation barrier in this case is of 0.2 eV.

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/CpFqp85v4cQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Links

[^1]: [PWneb User’s Guide, Official Documentation](https://www.quantum-espresso.org/Doc/neb_user_guide.pdf)

[^2]: [H. Jonsson, G. Mills and K.W. Jacobsen: "Nudged elastic band method for finding minimum energy paths of transitions", Document](http://theory.cm.utexas.edu/henkelman/pubs/jonsson98_385.pdf)

[^3]: [Input File Description for neb.x, Official Quantum ESPRESSO documentation](http://web.mit.edu/espresso_v6.1/i386_linux26/qe-6.1/Doc/INPUT_NEB.html)

[^4]: [Wikipedia Broyden's method, Website](https://en.wikipedia.org/wiki/Broyden%27s_method)

# Calculate Reaction Profile Using the Nudged Elastic Band (NEB) method

This tutorial page explains how to calculate the energy pathway profile and activation barrier for the multi-dimensional energy space of chemical reactions via the **Nudged Elastic Bands (NEB) method**, by making use of the [interpolated sets](../../../materials-designer/header-menu/advanced/interpolated-set.md) introduced in a [separate tutorial](interpolated-sets.md). 

We consider the example of a one-dimensional, three-atom molecule of Hydrogen (H3) throughout the present tutorial, and shall be making use of [Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md) as the main simulation engine, via the implementation of its `PWneb` flavor [^1]. 

## Theoretical Background

A detailed theoretical review of the NEB method can be found in Ref. [^2]. A brief introductory explanation is offered in what follows.

### The Challenge: Predicting the Minimum Energy Path in Chemical Reactions
 
In the context of the present introduction, it suffices to know that NEB aims at tackling a common and important problem in theoretical chemistry and in condensed matter physics, consisting in the the identification of a **lowest energy path** for a transition and rearrangement of a group of atoms from one stable configuration to another. Such transitions may be encountered for example during chemical reactions, changes in conformation of molecules, or diffusion processes in solids. 

Such a transition path is often referred to as the **"minimum energy path" (MEP)**. The potential energy maximum along the MEP is the **saddle point energy** which gives the **activation energy barrier**, a quantity of central importance for estimating the transition rate.

An example of an energy surface landscape for a generic chemical reaction between two structures, corresponding to two local energy minima, is shown in the image below. The position of the intermediate saddle in the energy is also highlighted.

![Energy Surface](../../../images/tutorials/NEB-example.png "Energy Surface")

### The Nudged Elastic Bands Method

Many different methods, such as NEB, have been presented for finding minimum energy reaction paths and saddle points between known reactants and products. The NEB method works by optimizing a number of **intermediate images** along the reaction path. Each image finds the lowest energy possible, while maintaining equal spacing to neighboring images. This constrained optimization is done by adding spring forces along the band between images and by projecting out the component of the force due to the potential perpendicular to the band.

### Climbing Image

The computational efficiency of the NEB method can be further improved through the adoption of the **Climbing Image** approach, which allows for the more accurate finding of saddle points using the NEB with fewer images than the original method. 

In the climbing image modification, the highest energy image is driven up to the saddle point. This image does not feel the spring forces along the band. Instead, the true force at this image along the tangent is inverted. In this way, the image tries to maximize its energy along the band, and minimize in all other directions. When this image converges, it will be at the exact saddle point.

### Example 

The graph below shows an NEB calculation (blue) and a climbing image cNEB calculation (red). The cNEB energies have been shifted by 0.05 eV so that the two curves are distinct. Notice how the climbing image calculation has shifted the position of the images (by compressing the images on the left), so that one image sits right at the saddle point.

![NEB](../../../images/tutorials/NEB.png "NEB")

## Workflow Structure



## Create Job and Choose Workflow

We start with [opening](../../../jobs/actions/create.md) an instance of the [Job Designer Interface](../../../jobs-designer/overview.md) for creating and designing new computational [Jobs](../../../jobs/overview.md) on our platform.

[Workflows](../../../workflows/overview.md) for calculating the reaction energy profile of chemical molecules via NEB with [Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md) can readily be [imported](../../../workflows/actions/copy-bank.md) from the [Workflows Bank](../../../workflows/bank.md) into the account-owned [collection](../../../accounts/collections.md). This workflow can later be [selected](../../../jobs-designer/actions-header-menu/select-workflow.md) and added to the [Job being created](../../../jobs-designer/workflow-tab.md).





## Links

[^1]: [PWneb User’s Guide, Official Documentation](https://www.quantum-espresso.org/Doc/neb_user_guide.pdf)

[^2]: [H. Jonsson, G. Mills and K.W. Jacobsen: "Nudged elastic band method for finding minimum energy paths of transitions", Document](http://theory.cm.utexas.edu/henkelman/pubs/jonsson98_385.pdf)

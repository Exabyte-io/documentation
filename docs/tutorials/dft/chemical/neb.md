# Calculate Reaction Profile Using the Nudged Elastic Band (NEB) method

This tutorial page explains how to calculate the energy pathway profile and activation barrier for the multi-dimensional energy space of chemical reactions via the **Nudged Elastic Bands (NEB) method**, by making use of the [interpolated sets](../../../materials-designer/header-menu/advanced/interpolated-set.md) introduced in a [separate tutorial](interpolated-sets.md). 

We consider the example of a one-dimensional, three-atom molecule of Hydrogen (H3) throughout the present tutorial, and shall be making use of [Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md) as the main simulation engine, via the implementation of its `PWneb` flavor [^1]. A theoretical review of the NEB method can be found in Ref. [^2].

## Create Job and Choose Workflow

We start with [opening](../../../jobs/actions/create.md) an instance of the [Job Designer Interface](../../../jobs-designer/overview.md) for creating and designing new computational [Jobs](../../../jobs/overview.md) on our platform.

[Workflows](../../../workflows/overview.md) for calculating the reaction energy profile of chemical molecules via NEB with [Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md) can readily be [imported](../../../workflows/actions/copy-bank.md) from the [Workflows Bank](../../../workflows/bank.md) into the account-owned [collection](../../../accounts/collections.md). This workflow can later be [selected](../../../jobs-designer/actions-header-menu/select-workflow.md) and added to the [Job being created](../../../jobs-designer/workflow-tab.md).





## Links

[^1]: [PWneb User’s Guide, Official Documentation](https://www.quantum-espresso.org/Doc/neb_user_guide.pdf)

[^2]: [H. Jonsson, G. Mills and K.W. Jacobsen: "Nudged elastic band method for finding minimum energy paths of transitions", Document](http://theory.cm.utexas.edu/henkelman/pubs/jonsson98_385.pdf)


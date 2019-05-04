# Boundary Conditions

Boundary conditions specify how the system under investigation (referred to as "Slab" for the case of interfaces) can interact or is related to its surroundings. Such customization of boundary conditions can be especially resourceful in the case of [Effective Screening Medium](../../../models/auxiliary-concepts/esm.md) calculations.

## Set Boundary Conditions Dialog

Open the "Set Boundary Conditions" dialog via the ["Advanced" menu](../advanced.md) within the Materials Designer interface. The dialog has the appearance as highlighted in the image below.

![Boundary Conditions Dialog](../../../images/materials-designer/boundary-conditions.png "Boundary Conditions Dialog")

## Boundary Conditions Types

The dialog features a drop down menu on the left, where the **type** of boundary condition can be chosen and applied perpendicularly to the central slab under consideration. We offer the possibility to choose between the following distinct types, which are also reviewed in Ref. [7] cited [in this page](../../../software-directory/modeling/quantum-espresso/components.md):

- Periodic Boundary Conditions (pbc): the system is completely surrounded by identical replicas of itself in all three dimensions [^1].
- Vacuum-Slab-Vacuum (bc1): immerse the slab between two semi-infinite vacuum regions.
- Metal-Slab-Metal (bc2): immerse the slab between two semi-infinite metallic electrodes, with optional fixed electric field applied between them.
- Vacuum-Slab-Metal (bc3): immerse the slab between one semi-infinite vacuum region (left-hand side) and one semi-infinite metallic electrode (right-hand side).

## Offset

Towards the right of the "Set Boundary Conditions" dialog, the user can set the numerical value for the **offset**, in Angstroms, defining the distance separating the system from its surroundings, which are defined via the above-mentioned boundary conditions options.

## Apply Changes

Once the desired options have been entered within the "Set Boundary Conditions" dialog, click on the `Submit` button at the bottom of the dialog to implement the corresponding changes to the material under investigation.

## Links

[^1]: [Wikipedia Periodic boundary conditions, Website](https://en.wikipedia.org/wiki/Periodic_boundary_conditions)

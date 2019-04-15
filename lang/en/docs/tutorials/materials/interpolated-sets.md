# Create Interpolated Sets

This tutorial page explains how to create an [interpolated set](../../materials-designer/header-menu/advanced/interpolated-set.md), necessary for the calculation of the energy profile and activation barrier for the multi-dimensional energy space of chemical reactions via the Nudged Elastic Bands (NEB) method, which is reviewed in a [separate tutorial](../dft/chemical/reaction-profile-qe.md). 

We consider the example of a one-dimensional, three-atom molecule of Hydrogen (H3) throughout the present tutorial.

## Upload Initial and Final Images to Materials Collection

The datafiles containing the structural information about the initial and final states of the H3 molecule under consideration should first be [uploaded](../../materials/actions/upload.md) to the account-owned collection of materials. 

For the sake of the present tutorial, we will consider the following two POSCAR files, containing the structural parameters for the initial and final molecular configurations respectively:

```text
initial
1.0
   6.350127000	   0.000000000	   0.000000000
   0.000000000	   2.645886000	   0.000000000
   0.000000000	   0.000000000	   2.645886000
H
3
direct
   0.619441600    0.000000000    0.000000000 H
   0.000000000    0.000000000    0.000000000 H
   0.129813900    0.000000000    0.000000000 H
```

```text
final
1.0
   6.350127000	   0.000000000	   0.000000000
   0.000000000	   2.645886000	   0.000000000
   0.000000000	   0.000000000	   2.645886000
H
3
direct
   0.870186100    0.000000000    0.000000000 H
   0.000000000    0.000000000    0.000000000 H
   0.380558400    0.000000000    0.000000000 H
```

## Create an Interpolated Set via Materials Designer

### Open Materials Designer and Import Initial/Final Configurations

The user should now [open](../../entities-general/actions/create.md) an instance of the [Materials Designer Interface](../../materials-designer/overview.md), through which we aim to create our Interpolated Set in between the above-mentioned initial and final configurations of the H3 molecule. 

The first step consists in importing these two configurations into the interface by following [these instructions](../../materials-designer/header-menu/input-output/import.md). It is essential then to [clone](../../materials-designer/header-menu/edit.md#clone) both initial and final images before generating the interpolated set, as well as to [delete](../../materials-designer/sidebar-items.md#delete-item) the original structures from the [left-hand items list sidebar](../../materials-designer/sidebar-items.md) of the Materials Designer Interface, for a correct final attribution of the indices within the resulting ordered set.

### Generate Interpolated Set

Before creating a new interpolated set, the user should make sure that the active structure selected on the [left-hand items list sidebar](../../materials-designer/sidebar-items.md) is the initial one, and not final. This ensures that the intermediate images will be correctly injected between the initial and final ones at the moment of creation of the new interpolated set.

The Interpolated Set itself can be generated via the [corresponding option](../../materials-designer/header-menu/advanced/interpolated-set.md) within the [Advanced Menu](../../materials-designer/header-menu/advanced.md) of the [header bar](../../materials-designer/header-menu/header-menu-intro.md).
 
In the resulting "Generate Interpolated Set" dialog, the user is able to select the total number of intermediate images that need to be generated, which we select to be 3 for the sake of the present demonstrative explanation.

### Adding Atomic Constraints

**Atomic Constraints**, specifying the constraints on the movement of atoms, can be also be defined as explained [in this page](../../properties-directory/structural/basis.md#atomic-constraints). 

These constraints need only be added to the initial image before the creation of the interpolated set, under the [basis panel](../../materials-designer/source-editor/basis.md) of the [source editor](../../materials-designer/source-editor.md) in [Materials Designer](../../materials-designer/overview.md). Later, once the interpolated set is generated, the same constraints will be applied automatically to all other intermediate images.

Adding atomic constraints in this way can help to make the ensuing NEB calculation more computationally efficient.

### Inspect Intermediate Images

The user should now be able to inspect the structures for all the resulting intermediate images, which are listed together with the previously-imported initial and final molecular configurations within the [left-hand items list sidebar](../../materials-designer/sidebar-items.md) of the Materials Designer Interface. 

These images can be visualized and cycled through with the help of the incorporated [3D structure editor](../../materials-designer/3d-editor.md).

## Save all Images in NEB SET

Finally, **all** generated images should now be [saved](../../materials-designer/header-menu/input-output/save.md) into an ordered set called "NEB SET", which can be created as explained in what follows. The creation and selection of sets in which to save images is made possible by the appropriate option of the "Save Items" dialog.

### Create an Ordered SET

[These instructions](../../entities-general/actions/create-sets.md) demonstrate how to create a [Set](../../entities-general/sets.md) within the account-owned [collection](../../accounts/collections.md) of materials, which we shall name and refer to as "NEB SET". Following its creation, the type of this set should then be [changed](../../entities-general/actions/change-set-type.md) to **ordered**.

## Animations

### General Interpolated Set Creation

We summarize the aforementioned steps involved in generating an Interpolated Set for our linear H3 molecule in the animation below. We conclude the video by inspecting the full list of images, including the initial and final molecular configurations, under the [Explorer Interface](../../entities-general/ui/explorer.md) of the newly-created "NEB SET".

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/u66sPc4Bqgs" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### Constrained Interpolated Set Creation

In this second animation, we demonstrate how to add the atomic constraints discussed previously into a new "Constrained" Interpolated Set for NEB applications, confining the movement of atoms to only the x-direction since our H3 molecules are entirely one-dimensional. This is done by adding the "1 0 0" line next to the atoms in the initial image, except for the atom located at the origin, for which a "0 0 0" constraint suffices since this this atom remains fixed at all times.

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/-2We6J5UeMs" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

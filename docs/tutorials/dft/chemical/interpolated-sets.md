# Create Interpolated Sets

This tutorial page explains how to create an [interpolated set](../../../materials-designer/header-menu/advanced/interpolated-set.md), necessary for the calculation of the energy profile and activation barrier for the multi-dimensional energy space of chemical reactions via the Nudged Elastic Bands (NEB) method, which is reviewed in a [separate tutorial](neb.md). 

We consider the example of a one-dimensional, three-atom molecule of Hydrogen (H3) throughout the present tutorial.

## Create an Ordered SET

The first step in the generation of an Interpolated Set is to [create](../../../entities-general/actions/create-sets.md) a [Set](../../../entities-general/sets.md) within the account-owned [collection](../../../accounts/collections.md) of materials, which we shall name and refer to as "NEB SET". Following its creation, the type of this set should then be [changed](../../../entities-general/actions/change-set-type.md) to **ordered**.

## Upload Initial and Final Images to Materials Collection

The datafiles containing the structural information about the initial and final states of the H3 molecule under consideration should then be [uploaded](../../../materials/actions/upload.md) to the account-owned collection of materials. 

For the sake of the present tutorial, we will consider the following two POSCAR files, containing the structural parameters for the initial and final molecular configurations respectively:

```bash
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

```bash
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

The user should now [open](../../../entities-general/actions/create.md) an instance of the [Materials Designer Interface](../../../materials-designer/overview.md), through which we aim to create our Interpolated Set in between the above-mentioned initial and final configurations of the H3 molecule. 

The first step consists in importing these two configurations into the interface by following [these instructions](../../../materials-designer/header-menu/input-output/import.md).

### Generate Interpolated Set

The Interpolated Set itself can be generated via the [corresponding option](../../../materials-designer/header-menu/advanced/interpolated-set.md) within the [Advanced Menu](../../../materials-designer/header-menu/advanced.md) of the [header bar](../../../materials-designer/header-menu/header-menu-intro.md).
 
In the resulting "Generate Interpolated Set" dialog, the user is able to select the total number of intermediate images that need to be generated, which we select to be 10 for the sake of the present demonstrative explanation.

### Inspect Intermediate Images

The user should now be able to inspect the structures for all the resulting intermediate images, which are listed together with the previously-imported initial and final molecular configurations within the [left-hand items list sidebar](../../../materials-designer/sidebar-items.md) of the Materials Designer Interface. 

These images can be visualized and cycled through with the help of the incorporated [3D structure editor](../../../materials-designer/3d-editor.md).

## Save all Images in NEB SET

Finally, **all** generated images should be [saved](../../../materials-designer/header-menu/input-output/save.md) into the previously-created "NEB SET", by [selecting](../../../materials-designer/header-menu/input-output/save.md#select-set) this set under the appropriate option of the "Save Items" dialog.

## Animation

We summarize the aforementioned steps involved in generating an Interpolated Set for our linear H3 molecule in the animation below. We conclude the video by inspecting the full list of images, including the initial and final molecular configurations, under the [Explorer Interface](../../../entities-general/ui/explorer.md) of the newly-created "NEB SET".

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/JGQqev3JhTk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

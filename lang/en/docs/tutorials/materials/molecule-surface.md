# Create Molecule on a Surface

In this tutorial, the user will learn about how the [Material Designer Interface](../../materials-designer/overview.md) of our platform can be used to create a geometry for modeling a **surface chemical reaction**, whereby a **molecule interacts with a surface**, and undergoes for example a chemical **adsorption** process [^1].

We consider the example of a **benzene molecule** adsorbed on a **gold (Au) (211) surface** throughout the present tutorial. The chemical structure of the benzene molecule is given in the expandable section below for reference purposes, in the POSCAR input data format.

## Structures

<details markdown="1">
  <summary>
    Benzene molecule, POSCAR ...
  </summary>

```text
C H
1.00000000000000
20.0000000000000000 0.0000000000000000 0.0000000000000000
0.0000000000000000 20.0000000000000000 0.0000000000000000
0.0000000000000000 0.0000000000000000 20.0000000000000000
6 6
Direct
0.5000000000000000 0.4302298156365565 0.5000000000000000
0.5603808840462569 0.4651341647080757 0.5000000000000000
0.5603808840462569 0.5348658352919243 0.5000000000000000
0.5000000000000000 0.5697701843634434 0.5000000000000000
0.4396191159537430 0.5348658352919243 0.5000000000000000
0.4396191159537430 0.4651341647080757 0.5000000000000000
0.5000000000000000 0.3757603875449354 0.5000000000000000
0.6075652945069621 0.4379113406185772 0.5000000000000000
0.6075652945069621 0.5620886593814227 0.5000000000000000
0.5000000000000000 0.6242396124550644 0.5000000000000000
0.3924347054930378 0.5620886593814227 0.5000000000000000
0.3924347054930378 0.4379113406185772 0.5000000000000000
```

</details>

Alternatively, the above benzene molecular structure can also be retrieved from the **Pubchem** public repository [^2], and then converted to the POSCAR format for uploading on our platform through any online converter, such as the **OpenBabel** Open Source Chemistry Toolbox [^3], which allows to convert between nearly all the chemical data formats. 

## Create Benzene Molecule Entry in Materials Collection

The chemical structure for Benzene can readily be [imported](../../materials/actions/copy-bank.md) from the [Materials Bank](../../materials/bank.md) into the account-owned [collection](../../accounts/collections.md), if it is not already present there. 

Alternatively, the above-mentioned POSCAR structure can be manually [uploaded](../../materials/actions/upload.md) by the user into the materials collection, after saving its data contents into a new file on the local disk.
 
## Open Materials Designer 

We start with [opening](../../entities-general/actions/create.md) an instance of the [Materials Designer Interface](../../materials-designer/overview.md) for creating and designing new [Materials structures](../../materials/overview.md) on our platform. 

## Create a Gold Surface 

In order to create a gold surface, the user should first [import](../../materials-designer/header-menu/input-output/import.md) a sample crystalline structure of pure gold into the current Materials Designer session, from the account-owned [collection](../../accounts/collections.md) of materials. 

The instructions contained [in this page](../../materials-designer/header-menu/advanced/surface-slab.md) should then be followed in order to create a surface of Gold, with normal vector oriented along the [211] axis, using our surface creator in Materials Designer, starting from the original gold crystalline sample. 

!!!warning "Order of structures is important"
    The gold surface has to be created first in order for it to appear first in the list of materials shown on the [left-had items list sidebar](../../materials-designer/sidebar-items.md) of the Materials Designer interface, so that its cell is used when later combining the two materials together.

## Import the Benzene Molecule into Materials Designer

The Benzene molecule should now be [imported](../../materials-designer/header-menu/input-output/import.md) into the current Materials Designer session, from the account-owned [collection](../../accounts/collections.md) of materials. 

Once imported into Materials Designer, the benzene molecule will appear as a new distinct entry item within the list of structures shown on the [left-had items list sidebar](../../materials-designer/sidebar-items.md) of the Designer interface, besides the previously-generated gold surface.
 
Care should be taken by the user to [remove](../../materials-designer/sidebar-items.md#delete-item) any other material structure entry listed in the sidebar, besides benzene and the gold surface being considered here, that may have been loaded by [default](../../materials/default.md) initially at the moment of the opening of Materials Designer.

## Open Multi-Materials 3D Editor

After both the benzene molecule and the gold surface have been created as two separate structural items in the current session of Materials Designer, the user should now open an instance of the [Multi-Materials 3D Editor](../../materials-designer/3d-editor/edit.md) via the ["View" Menu](../../materials-designer/header-menu/view.md#multi-material-3d-editor), located within the [header bar](../../materials-designer/header-menu/header-menu-intro.md) of the Materials Deigner Interface.

## Combine the Two Materials

The Multi-Materials 3D Editor allows the two materials under investigation, the benzene molecule and the gold surface, to be **combined** together into a new unified materials entity. 

Care should be taken by the user to place the molecule on top of the surface in as "symmetrical" a way as possible, for example by positioning the center of the benzene ring on the central portion of the surface. Relocation of the benzene molecule position can be done by following the instructions contained [in this page](../../materials-designer/3d-editor/editor-actions/move-rotate-atoms.md), after selecting the benzene atom components under the ["Scene" sidebar list](../../materials-designer/3d-editor/edit.md#3.-scene) of the 3D Editor interface.

Since in this example the plane of the 2D benzene molecule and the gold (211) surface are already parallel to each other, a simple [translation](../../materials-designer/3d-editor/editor-actions/move-rotate-atoms.md#translation) of the benzene atoms on top of the surface should suffice.

## Exit Multi-Materials 3D Editor

After the correct desired positioning of the benzene molecule on top of the gold surface, the user should now [exit](../../materials-designer/3d-editor/edit.md#exit-the-editor) the Multi-Materials 3D Editor, and return to the original Materials Designer interface.

The user will notice that a new material entry, called "New Material" by default, has now been created automatically and is listed within the [left-had items list sidebar](../../materials-designer/sidebar-items.md) of the Materials Designer interface. It contains the combined benzene-gold surface crystallographic structure, as a new single material entity.

!!!tip "Toggling of Orthographic Camera"
    The user is recommended to toggle the use of the [Orthographic camera](../../materials-designer/3d-editor/view.md#toggle-orthographic-camera) functionality, accessible via the [3D Editor interface](../../materials-designer/3d-editor.md) of Materials Designer, in order to verify the correct alignment and centrality of the benzene molecule over the surface.

This new entry should first be [renamed](../../materials-designer/sidebar-items.md#edit-name-of-item) to a more memorable form, and should finally be [saved](../../materials-designer/header-menu/input-output/save.md) via the ["Input/Output" Menu](../../materials-designer/header-menu/input-output.md) located at the top-left corner into the account-owned materials [collection](../../accounts/collections.md), as a new material structure entry which is distinct from both the original isolated benzene molecule and gold structure.

## Resulting Material

An animation of the final combined benzene molecule-gold surface structure can be viewed below.

<img data-gifffer="/images/tutorials/molecule-surface-sample.gif" />

## Run Further Analysis

The user is now free to use the newly generated benzene-gold surface system, in order to perform its further analysis, such as studying the adsorption energy.

The [Nudged Elastic Band (NEB)](../../models/auxiliary-concepts/nudged-elastic-band.md) method can be used for reaction energy profile calculations. We offer two alternative approaches for implementing the NEB method on our platform, based on the use of the [VASP](../../software-directory/modeling/vasp/overview.md) or [Quantum ESPRESSO](../../software-directory/modeling/quantum-espresso/overview.md) modeling engines, which are narrated in two separate tutorials accessible [here](../dft/chemical/reaction-profile-vasp.md) and [here](../dft/chemical/reaction-profile-qe.md) respectively.

## Animation

We demonstrate the above-mentioned steps which lead to the creation of a combined benzene molecule/gold surface crystallographic system, made possible via the functionalities of the [Materials Designer Interface](../../materials-designer/overview.md) of our platform, in the following animation. 

In this example, we consider a 3x3x3 slab supercell of the primitive unit cell of gold as a surface approximation (larger supercell dimensions should be envisaged for a more realistic surface representation). We also place the benzene molecule over the gold surface such that the molecule-surface distance is approximately 3.6 Angstroms, as measured by the difference in the z coordinates of the positions of the benzene atoms and gold surface atoms.

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/qCLJzxBlyXY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Links

[^1]: [Wikipedia Adsorption, Website](https://en.wikipedia.org/wiki/Adsorption)

[^2]: [Pubchem Benzene Datasheet, Official Website](https://pubchem.ncbi.nlm.nih.gov/compound/241)

[^3]: [OpenBabel Web Interface, ChemInfo Website](http://www.cheminfo.org/Chemistry/Cheminformatics/FormatConverter/index.html)

# Create Non-Periodic Structures

In this tutorial, the user will learn about:
(1) How the [Materials Designer Interface](../../materials-designer/overview.md) of our platform can be used to create a non-periodic structure.
(2) How the [Material Upload Interface](../../materials/actions/upload.md) of our platform can be used to upload a non-periodic structure.

## (1) Materials Designer Interface Tutorial
For this tutorial we consider the example of a methane molecule, a five-atom structure (containing one Carbon (C) atom and four Hydrogen (H) atoms).

### Structure
<details markdown="1">
  <summary>
    Methane Molecule (CH4), Cartesian Coordinates ...
  </summary>

```text
  H      0.5288      0.1610      0.9359
  C      0.0000      0.0000      0.0000
  H      0.2051      0.8240     -0.6786
  H      0.3345     -0.9314     -0.4496
  H     -1.0685     -0.0537      0.1921
```
 </details>

### Create Methane in the Materials Designer
#### Open Materials Designer
We start with [opening](../../entities-general/actions/create.md) an instance of the [Materials Designer Interface](../../materials-designer/overview.md) for creating and designing new [Materials structures](../../materials/overview.md) on our platform. 

#### Cloning a New Material
Once the [Materials Designer Interface](../../materials-designer/overview.md) is opened the user should open the [Edit Menu](../../materials-designer/header-menu/edit.md) from the [Header Menu](../../materials-designer/header-menu/header-menu-intro.md) and click the `Clone` button. This will create an exact replica of the original material opened along with the materials-designer.

#### Deleting the Original Material
After cloning the material, the user should remove the original material from the [item-list](../../materials-designer/sidebar-items.md) using the <i class="zmdi zmdi-delete zmdi-hc-border"></i> next to the original material.

#### Renaming the New Material
The user can then rename the new material in the [item-list](../../materials-designer/sidebar-items.md) by editing the name.

#### Setting the Basis
Once the material is renamed the user can then click on the `Cartesian` option within the [Crystal-Basis Editor](../../materials-designer/source-editor/basis.md). Once the units are switched to cartesian the user can the paste the coordinates found above under `Structure` into the [Crystal Basis Editor](../../materials-designer/source-editor/basis.md).

#### Toggling "isNonPeriodic"
After the basis has been set, the user can then open the [Edit Menu](../../materials-designer/header-menu/edit.md) from the [Header Menu](../../materials-designer/header-menu/header-menu-intro.md) and select the `Toggle "isNonPeriodic` option. This will cause the basis and lattice of the structure to be immediately updated. The lattice size will be based on the size of the non-periodic structure you defined in the [Crystal Basis Editor](../../materials-designer/source-editor/basis.md). The shape of the lattice will be updated to Cubic. Finally the basis will be translated so that the center of the structure is aligned with the center of the lattice.

#### Post Basis Editing
If you wish to edit the basis after clicking `Toggle "isNonPeriodic"` then the basis will NOT automatically recenter itself until after the material is saved.

#### Saving the Non-Periodic Structure
Open the Input/Output Menu from the Header Menu. Choose the save option and select `submit`

#### Animation

Click on the animation below to see `Toggle "isNonPeriodic"` in action.

### (2) Materials Upload Tutorial
For this tutorial we consider the example of a hydrogen sulfide molecule, a three-atom structure (containing one Sulfur (S) atom and two Hydrogen (H) atoms).

### Structure
<details markdown="1">
  <summary>
    Hydrogen Sulfide (H2S), POSCAR FILE
  </summary>

```text
H2S
1.0
   5.000000000	   0.000000000	   0.000000000
   0.000000000	   5.000000000	   0.000000000
   0.000000000	   0.000000000	   5.000000000
S H
1 2
direct
     0.250000    0.250000    0.250000 S
     0.250000    0.000000    0.150000 H
     0.250000    0.500000    0.150000 H
```
 </details>

### Upload the H2S POSCAR File
#### Open Materials File Upload Option
We start with [opening](../../materials/actions/upload.md) the Materials File Upload Explorer from the Materials Explorer.

#### Choose the POSCAR File to be Uploaded.
We use the`Select Items` tool <i class="zmdi zmdi-collection-plus zmdi-hc-border"></i> in the [actions toolbar](../../entities-general/ui/explorer.md#actions-toolbar), to open a file upload dialog. Through this dialog, select the H2S.poscar file from the local filesystem.

#### Tag the file as "non-periodic"
Once the file is listed on the upload page, check the select box on the lefthand side of the page. Then select the <i class="zmdi zmdi-tag zmdi-hc-border"></i> icon to open the Set Tags dialog box. On the entry line input "non-periodic" followed by a comma and then click submit.

At this point you should see the tag "non-periodic" listed in the **TAGS** column for your materials row in the Upload Files Explorer.

#### Upload the file
With the material still selected, choose the <i class="zmdi zmdi-upload zmdi-hc-border"></i> icon for the upload tool in the top right actions toolbar.

Once the material successfully uploads the **UPLOADED** column should show a <i class="zmdi zmdi-check zmdi-hc-border"></i> in the row of your material.

#### Exit the Upload Files Explorer & Verify Material is listed in the Materials Explorer
After the upload is successful you can exit out of the Upload Files Explorer using the top right X button. That should bring you back to the Materials Explorer Page.

On the Materials Explorer Page you should see your material listed with a <i class="zmdi zmdi-device-hub zmdi-hc-border"></i> icon, and a <i class="zmdi zmdi-check zmdi-hc-border"></i> icon in the **Non-Periodic** column.

#### Animation

Click on the animation below to see `Toggle "isNonPeriodic"` in action.

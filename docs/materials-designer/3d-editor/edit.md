# 3d Editor: Edit Panel

The second `Edit` button <i class="zmdi zmdi-border-color zmdi-hc-border"></i> in the interactive mode of the 3D graphical crystal viewer includes the following set of actions, which give user manoeuvrability in editing graphically, and in real time, the positions of the atoms in the material:

<!-- TODO: this image is too large, make buttons same size as in View Panel -->

![3d Editor: Edit Panel](../../images/materials-designer/edit-features-viewer.png "3d Editor: Edit Panel") 

 
Each one of these actions is reviewed separately below. Click on the visuals included at the end of each section below to view the animations for the corresponding action.     

## Rectangular Selection

Through the "Rectangular Selection" option, the user can select a certain number of atoms within a rectangular selection window. First expand the window by holding your left mouse button, and then release it once all desired atoms have been covered by the selection. The selected atoms will correspondingly undergo a slight change of color.   

!!!warning "Note: feature is not implemented yet"
    The actions that would follow from this selection tool, such as deleting or translating the selected atoms, are not implemented yet. 

## Toggle Rotate / Translate

Enabling "Rotate / Translate" feature displays a set of Cartesian coordinate axes alongside the structure viewed. Cartesian or spherical coordinate axes can be activated or hidden from the viewer interface at any time by pressing the `T` key. 

### Translation

Translational coordinate axes (cartesian) can be activated by pressing the `A` key.

#### Axial

The user can achieve an axial translation of the crystal with respect to this coordinate system by holding the corresponding axis with the left mouse button and then making the desired move. 

#### Planar

Planar translations can also be performed in much the same way, by holding the colored squares between the axes indicating the various planes of the Cartesian space.   

### Rotation

Spherical rotation axes are selected upon pressing the `R` key. This allows one to rotate the crystal basis along one of the three azimuth angles. Once the desired rotation is performed, these rotation axes can be collapsed back to the previous translation axes by pressing the "A" key again. 

<img data-gifffer="/images/materials-designer/ViewerEditTranslate.gif" />

## Inject / Delete Atoms

Instead of having to manually edit the total number of atoms in the crystal structure [basis editor](../source-editor/basis.md), it is possible to place or delete individual atoms at desired locations within the crystal structure directly in the graphical viewer. Alternatively, the functionality can be toggled by `I` key.

### Delete

Hover over an atom to see it highlighted. Righ-click on it to delete. The text of the crystal basis will adjust accordingly.

### Inject

Right click inside the unit cell will inject an atom at the cursor position. We assign the default offset from the view such that the atom is created inside the unit cell. This assumes the default view position and can, however, be affected by zoom, so this features should be used with caution.
 
<img data-gifffer="/images/materials-designer/ViewerEditInject.gif" />


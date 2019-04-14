# 3d Editor: the "Viewer"

The first `View` button <i class="zmdi zmdi-eye zmdi-hc-border"></i> under the interactive functionality of the 3D Editor offers the user the possibility to perform the following set of actions to modify the current view: 

![3d Editor: View Panel](../../images/materials-designer/view-features-viewer.png "3d Editor: View Panel")
 
Each one of these actions is reviewed separately below. Click on the visuals included at the end of each section below to view the animations for the corresponding action.    
 
## Rotate / Translate / Zoom

Toggling "Rotate / Zoom" option will allow the user to:

- `Rotate` the crystal view by moving the mouse around whilst holding the **left button**.
- `Translate` the crystal view by moving the mouse around whilst holding the **right button**.
- `Zoom` in or out of the crystal view by **scrolling** the central mouse wheel in either sense.

<img data-gifffer="/images/materials-designer/ViewerViewZoom.gif" />

## Toggle Auto Rotate

Clicking on "Auto Rotate" option will activate an automatic perpetual rotation of the crystal view around its current vertical axis.

<img data-gifffer="/images/materials-designer/ViewerViewAuto.gif" />

## Toggle Axes

Toggling the "Axes" option enables Cartesian coordinate axes, and the base XY plane (a plane perpendicular to Z axis at Z=0), for ease of orientation in 3D.

<img data-gifffer="/images/materials-designer/ViewerViewAxes.gif" />

## Toggle Orthographic Camera

**Perspective Projection** [^2] is used to see the material by default. One can switch the camera to have **Orthographic Projection** [^3] by toggling this option.

<img data-gifffer="/images/materials-designer/orthographic.gif" />

## Toggle Bonds

Clicking on this option will draw the bonds between adjacent atoms. The stick is drawn if the atoms distance is equal or less than the bond length outlined in Ref. [^1]. For atoms with no bonding data, the sum of covalent radii times the chemical connectivity factor (1.05) is used as the bond length.

<img data-gifffer="/images/materials-designer/bonds.gif" />

## Toggle Conventional Cell

This option toggles the Conventional representation of the unit cell from the Primitive cell. Users can adjust the default representation mode in [here](../../accounts/ui/preferences/settings.md). 

<img data-gifffer="/images/materials-designer/conventional.gif" />

## Reset View

There might come a point, during the course of an interactive viewing session, in which the user might wish to revert to the original default view of the material under consideration. This is precisely what the "Reset" option achieves.

<img data-gifffer="/images/materials-designer/ViewerViewReset.gif" />

## Radius

Editing this numerical text field will modify the radius of the atom spheres accordingly.

<img data-gifffer="/images/materials-designer/ViewerViewRadius.gif" />
  
## Repetitions

The user can edit this second numerical field to repeat the original unit cell a certain number of times in each spatial direction, as defined by a positive integer number. 

<img data-gifffer="/images/materials-designer/ViewerViewRepetitions.gif" />

## Links

[^1]: [Selected Bond Energies and Bond Lengths, Document](http://www.chem.tamu.edu/rgroup/connell/linkfiles/bonds.pdf)

[^2]: [Wikipedia Perspective (graphical), Website](https://en.wikipedia.org/wiki/Perspective_(graphical))

[^3]: [Wikipedia Orthographic projection, Website](https://en.wikipedia.org/wiki/Orthographic_projection)

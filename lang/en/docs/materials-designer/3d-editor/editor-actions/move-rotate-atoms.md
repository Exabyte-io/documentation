# Rotate, Translate or Scale Crystal Structure

## Toggle Option

Enabling the "Rotate / Translate / Scale" features, accessible via the corresponding buttons within the ["Footer" Menu](../edit.md#2.-footer-menu) of the main 3D editor interface, displays a set of coordinate axes alongside the structure being currently inspected. Depending on whether the `Translate`/`Scale` or `Rotate` option is selected, the resulting reference system will consist in Cartesian or Spherical coordinates respectively. In this way the component of the crystal structure, which has been selected under the ["Scene" sidebar list](../edit.md#3.-scene), can be shifted or modified in different ways, as described in what follows.

## Translation

After the translational coordinate axes (cartesian) are activated by pressing the `Translate` button, the following two possibilities are available to the user.

### Axial 

The user can achieve an axial translation of the crystal component with respect to this coordinate system by holding the corresponding axis with the left mouse button, and then making the desired move. 

### Planar 

Planar translations can also be performed in much the same way, by holding the colored squares between the axes indicating the various planes of the Cartesian space.   

### Origin 

A further colored square is present at the origin of the cartesian coordinate system, which can be held and moved in very much the same fashion as in planar translations to achieve a translation of the origin point itself.

## Rotation

Spherical rotation axes are enabled upon pressing the `Rotate` option. This allows one to rotate the selected crystal structure component along one of the three azimuth angles. 

## Scaling

Selecting the third `Scale` button option allows the user to deform the selected crystal structure component in various directions, by for example compressing or elongating it. This is done similarly to Axial translations, by holding the corresponding axis (or the origin) with the left mouse button and then making the desired move.

## Local Coordinates

There are two coordinate systems, referred to as **"local"** and **"world"**. Local position is the position of the object relative to its parent. If the user tries to move the parent object, the local position of the child objects do not change. The world position on the other hand represents the absolute position of the object in space.

The user can select to employ local coordinates by ticking the `local` checkbox located at the right-end of the ["Footer" Menu](../edit.md#2.-footer-menu).

## Animation

We demonstrate the execution of example translations, rotations and scaling of a crystal structure in the following animation.

<img data-gifffer="/images/materials-designer/move-atoms.gif" />

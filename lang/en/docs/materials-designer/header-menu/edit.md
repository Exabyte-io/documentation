# Edit Menu

The `Edit` menu in the top menu bar of the Materials Designer interface makes it possible to navigate through the various changes made to the material structure under consideration during the current session. The position of this menu within the overall interface is highlighted below:

![Edit Menu](../../images/materials-designer/edit-menu.png)


## Undo

Pressing `Undo` <i class="zmdi zmdi-undo zmdi-hc-border"></i> will revert the currently-selected material structure to the previous state (or step), or will undo any previous action. Up to 30 steps are saved during each session and can therefore be undone.

<!-- TODO: remove the below when fixed -->

!!! warning "Changing selected material" 
    Changing the currently selected material in the items list sidebar is also considered an action.

## Redo 

Conversely, the `Redo` <i class="zmdi zmdi-redo zmdi-hc-border"></i> feature will negate the effect of a previous `Undo` action and bring back the material structure (or material selection) to a more recent state.

## Reset

The user can also `Reset` <i class="zmdi zmdi-close zmdi-hc-border"></i> all changes made to the crystal structure back to the initial configuration used when the Materials Designer page is first opened. 

## Clone

The `Edit` menu also allows the user to `Clone` <i class="zmdi zmdi-collection-image zmdi-hc-border"></i> the currently selected structure into a new distinct entry in the items list sidebar. This feature is demonstrated in the short animation below, where we clone the original silicon structure into a new entry which appears below it:

<img data-gifffer="/images/materials-designer/edit-clone.gif" />

## Use Conventional Cell

The `Edit` menu also allows the user to update the material ot use a `Conventional Cell`.

## Toggle "isNonPeriodic"
The 'Edit' menu also allows the user to update the material to be categorized as `non-periodic`. By clicking the `Toggle "isNonPeriodic"` button the materials lattice and basis will be updated so that it's coordinates are centered inside a cubic lattice with dimensionality based on the size of the structure. Upon saving the basis of the stucture will be set to Cartesian Units. the difference between a `periodic` and `non-periodic` structure is denoted by a change in the icon representing the structure. `Periodic` structures are denoted by <i class="zmdi zmdi-widget zmdi-hc-border"></i> icon while `non-periodic` structures are denoted by <i class="zmdi zmdi-device-hub zmdi-hc-border"></i> icons.


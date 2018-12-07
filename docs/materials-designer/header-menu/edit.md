# Edit Menu

The `Edit` menu in the top menu bar of the Materials Designer interface makes it possible to navigate through the various changes made to the material structure under consideration during the current session. The position of this menu within the overall interface is highlighted below.

<img src="/images/edit-menu.png"/>


# Undo

Pressing `Undo` <i class="zmdi zmdi-undo zmdi-hc-border"></i> will revert the currently-selected material structure to the previous state (or step), or will undo any previous action. Up to 30 steps are saved during each session and can therefore be undone.

<!-- TODO: remove the below when fixed -->

!!! warning "Changing selected material" 
    Changing the currently selected material in the items list sidebar is also considered an action.

# Redo 

Conversely, the `Redo` <i class="zmdi zmdi-redo zmdi-hc-border"></i> feature will negate the effect of a previous `Undo` action and bring back the material structure (or material selection) to a more recent state.

# Reset

The user can also `Reset` <i class="zmdi zmdi-close zmdi-hc-border"></i> all changes made to the crystal structure back to the initial configuration used when the Materials Designer page is first opened. 

# Clone

The `Edit` menu also allows the user to `Clone` <i class="zmdi zmdi-collection-image zmdi-hc-border"></i> the currently selected structure into a new distinct entry in the items list sidebar. This feature is demonstrated in the short animation below, where we clone the original silicon structure into a new entry which appears below it.

<img data-gifffer="/images/edit-clone.gif" />

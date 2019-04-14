# View

The `View` menu allows user to modify the appearance of the Materials Designer interface. The location of this menu component within the interface is illustrated below:

![View](../../images/materials-designer/view-menu.png "View")


## Enable / Disable Component Panels

This `View` menu can be used to show or hide the panels of the Materials Designer interface, namely the items list `Sidebar`, the `Source Editor` and the `Selection Info`. This is achieved by selecting or de-selecting each component in the menu. When a check-mark is present next to a component, it is selected and therefore visible in the interface, and vice-versa.

!!! warning "Coming soon"
    The support for the Enable/Disable action is yet to be added.

## Multi-Material 3D Editor

Multi-Material 3D Editor is used to combine the materials shown inside the [Materials Designer Items List](../sidebar-items.md) and create a new material out of them. This feature can be used to put a molecule on a surface for instance.
 
When the button is clicked, the [3D Editor Modal](../3d-editor/edit.md) is opened with all materials inside the items list passed to it. The first material inside the list is used as the parent material, which means that its unit cell is used as the cell of the resulting combined material. The unit cell can be adjusted inside the editor as explained in [here](../3d-editor/edit.md).

## Full-Screen Mode

The `Full-screen` <i class="zmdi zmdi-fullscreen zmdi-hc-border"></i> view of the interface can be accessed at the bottom of the `View` menu. This full-screen mode can be subsequently exited by pressing the Esc key (or another browser-specific alternative, as appropriate). 

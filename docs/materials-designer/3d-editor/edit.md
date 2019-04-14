# 3d Editor: the "Editor" 

The second `Editor` button <i class="zmdi zmdi-border-color zmdi-hc-border"></i> in the interactive mode of the 3D graphical crystal viewer leads to the main editor interface of [Materials Designer](../overview.md), which gives user manoeuvrability in editing graphically, and in real time, the positions of the atoms in the material.

This editor interface has the appearance exhibited in the below example image:

![Editor](../../images/materials-designer/editor.png "Editor")

The main components of the editor consist in the elements labelled in the above image. The crystal structure under consideration is also visible at all times in the central 3D crystal viewer, which has exactly the same appearance as the one shown under the [main Materials Designer interface](../3d-editor.md). 

Each of these components will now be reviewed in turn. The actions that can be performed via the editor are described [separately](editor-actions/overview.md).

## 1. Header Menu

The header menu located at the top left corner of the editor interface consists of the following two sub-menus:

### The "File" Submenu

Clicking on `File` opens a menu which allows the user to export the crystal structure under investigation and/or its associated settings in various formats. The user can for example export the geometry, object or scene, and download the corresponding data as JSON files to the local disk.

The option to exit the editor is also offered at the bottom of this `File` menu.

### The "Edit" Submenu

The `Edit` submenu offers different functionalities in relation to the actions performed within the editor. Firstly, it allows the user to `redo/undo` the last action, and to `clear` the overall history of actions (viewable under the "Settings" tab of the ["Scene" sidebar](#3.-scene) described in what follows). 

In addition, the user can here also `clone` or `delete` whatever object has been selected within the main crystal viewer interface. Such actions are narrated further in a [separate part of the documentation](editor-actions/overview.md).

## 2. Footer Menu

The "Footer" Menu located at the bottom of the editor interface offers the user the possibility to perform actions such as translation/rotation of atoms, and scaling the overall size of their graphical appearance. These actions are explained more in detail [here](editor-actions/overview.md).

## 3. Scene

The main "Scene" sidebar on the right-hand side of the editor interface displays information about the camera and viewing settings employed for visualizing the crystal structure under consideration. This "Scene" sidebar conforms to the conventions of the "Three JS" editor, which is narrated and documented in detail in its respective website and dedicated information [^1] [^2].

### Crystal Structure Components

It is worth noticing that the "Scene" sidebar allows the user to select the different components comprised within the crystal structure being inspected, including the Unit Cell of its underlying Bravais Lattice as well as its constituent atoms. Selection is performed by left-clicking each item listed here. Right-clicking on the other hand opens an "actions" menu to perform the common actions on each structure component described [in this section](editor-actions/overview.md).

## Exit the Editor

The user can exit the editor either by pressing the escape key, or by selecting `Exit` from the top-left `File` menu.

!!!note "Retrieve new material in Materials Designer"
    In order to exit the editor with a new material that can then be retrieved under the main [Materials Designer Interface](../overview.md), the scene should contain a cell object and one atom at least. The order is not important, but if there are multiple cell objects inside the scene, the first cell is used as the new material unit cell. An error is shown at the moment of exit from editor if the scene objects can not be converted into a proper and well-defined material structure (for example if the cell object is missing from the material under consideration). 

## Links

[^1]: [The Three.js Javacript 3D Library](https://threejs.org)

[^2]: [The Three.js Editor](https://threejs.org)

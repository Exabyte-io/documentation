# 3D Editor

The second `3D Editor` button <i class="zmdi zmdi-border-color zmdi-hc-border"></i> in the interactive mode of the 3D graphical crystal viewer leads to the main editor interface of [Materials Designer](../overview.md), which gives user manoeuvrability in editing graphically, and in real time, the positions of the atoms in the material.

This editor interface has the appearance exhibited in the below example image:

![3D Editor](../../images/materials-designer/3D-editor.png "3D Editor")

The main components of the 3D editor consist in the elements labelled in the above image. The crystal structure under consideration is also visible at all times in the central 3D crystal viewer, which has exactly the same appearance as the one shown under the [main Materials Designer interface](../3d-editor.md). 

Each of these components will now be reviewed in turn. The actions that can be performed via the 3D editor are described [separately](3d-editor-actions/overview.md).

## 1. Header Menu

The header menu located at the top left corner of the 3D editor interface consists of the following two sub-menus:

### The "File" Submenu

Clicking on `File` opens a menu which allows the user to export the crystal structure under investigation and/or its associated settings in various formats. The user can for example export the geometry, object or scene, and download the corresponding data as JSON files to the local disk.

The option to exit the 3D editor is also offered at the bottom of this `File` menu.

### The "Edit" Submenu

The `Edit` submenu offers different functionalities in relation to the actions performed within the 3D editor. Firstly, it allows the user to `redo/undo` the last action, and to `clear` the overall history of actions. 

In addition, the user can here also `clone` or `delete` whatever object has been selected within the main crystal viewer interface. Such actions are narrated further in a [separate part of the documentation](3d-editor-actions/overview.md).

## 2. Footer Menu

The "Footer" Menu located at the bottom of the 3D editor interface offers the user the possibility to perform actions such as translation/rotation of atoms, and scaling the overall size of their graphical appearance. These actions are explained more in detail [here](3d-editor-actions/overview.md).

## 3. Scene

The main "Scene" sidebar on the right-hand side of the 3D editor interface displays information about the camera and viewing settings employed for visualizing the crystal structure under consideration. This "Scene" sidebar conforms to the conventions of the "Three JS" editor, which is narrated and documented in detail in its respective website and dedicated information [^1] [^2].

It is worth noticing that the "Scene" sidebar allows the user to select the different components comprised within the crystal structure being inspected, including the Unit Cell of its underlying Bravais Lattice as well as its constituent atoms. Selection is performed by left-clicking each item listed here. Right-clicking on the other hand opens an "actions" menu to perform the common actions on each structure component described [in this section](3d-editor-actions/overview.md).

## Links

[^1]: [The three.js Javacript 3D Library](https://threejs.org/)

[^2]: [Wikipedia Three.js, Website](https://en.wikipedia.org/wiki/Three.js)














<!-- TODO by GM -->


- How to clone/move/add/remove/rotate atom
- How to group atoms
- How to adjust cell parameters

Notes:

- In order to exit the designer with a new material, the scene should contain a cell object and one atom at least. The order is not important, but if there are multiple cell objects inside the scene, the first cell is used as the new material unit cell.

- An error is shown if there the scene objects can not be converted into a material. you can try that by removing the cells and try existing the editor.

- Use can exit the editor either by pressing escape key or select Exit from file menu.

- User can change the name of the material and atoms by clicking on the corresponding 3D object and set the name. The atom name consists of the name of the element separated from the element index by a dash, "Si-1". Si is used if the element can not be extracted from the name.

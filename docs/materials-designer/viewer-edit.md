# Interactive Crystal Viewer: the "Edit" features

The second `Edit` button <i class="zmdi zmdi-border-color zmdi-hc-border"></i> under the interactive mode of the 3D graphical crystal viewer includes the following set of actions, which give you manoeuvrability in editing graphically, and in real time, the positions of the atoms in the unit cell being viewed: 

<img src="/images/edit-features-viewer.png"/>
 
Each one of these actions will now be reviewed separately. Click on the animation included at the end of each section below to witness the corresponding action being implemented in the crystal viewer interface.    

!!!warning "Caution is advised when using these features"
    The actions included in this page are designed to modify the crystal structure itself, and not just the way it can be viewed under the crystal viewer interface. For a simple change in the viewing perspective of the crystal, without any actual structural modifications, the reader is referred to the instructions contained in [this page](viewer-view.md) instead.  

# Rectangular Selection

Through this "Rectangular Selection" option, the user can select a certain number of atoms within a rectangular selection window. First expand the window by holding your left mouse button, and then release it once all desired atoms have been covered by the selection. The selected atoms will correspondingly undergo a slight change of color from light yellow originally to light purple.   

!!!warning "Note: Features not implemented yet"
    The actions that would follow from this selection tool, such as deleting or translating the selected atoms, are not implemented yet. 

# Toggle Rotate / Translate

Enabling this "Rotate / Translate" feature displays a set of Cartesian coordinate axes alongside the crystal structure being viewed. The user can then achieve an axial translation of the crystal with respect to this coordinate system by holding the corresponding axis with the left mouse button and then making the desired move. 

Planar translations can also be performed in much the same way, by holding the colored squares between the axes indicating the various planes of the Cartesian space.   

These translation coordinate axes can be activated or hidden from the viewer interface at any time by pressing the "T" key in your keyboard. Once activated, they can additionally be morphed into a set of spherical rotation axes upon pressing the "R" key. Once the desired rotation has been performed, these rotation axes can be collapsed back to the previous translation axes by pressing the "A" key. 

<img data-gifffer="/images/ViewerEditTranslate.gif" />

# Inject / Delete

Instead of having to manually edit the total number of atoms in the crystal structure, as well as their respective atomic coordinates, through the "Crystal Basis" text editor at the centre of the Materials Designer interface, it is possible to place or delete individual atoms at desired locations within the crystal structure directly in the graphical viewer. 

This injection or deletion of atoms at the position of the mouse pointer within the crystal viewer interface is achieved by first holding the "I" key of your keyboard, and then performing a left (for deletion) or right (for injection) mouse click. 
 
<img data-gifffer="/images/ViewerEditInject.gif" />


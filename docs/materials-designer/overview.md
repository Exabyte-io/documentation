# What is Materials Designer?

 The Exabyte platform provides a graphical crystal structure viewer and builder which we refer to as the Materials Designer, and that will now be reviewed in detail. This designer essentially makes it possible to conceive and then save new crystal structures from scratch.  

Experienced computational material scientists will recognize many of the features included in this designer interface from the most commonly used crystal visualization software packages, such as VESTA [[1](#links)], VMD [[2](#links)] or XCRYSDEN [[3](#links)]. However, a comprehensive approach will be adopted in the forthcoming documentation pages to make sure that neophyte users are not excluded from embracing our platform. 

> "Note for command line users": VESTA is also supported in the remote desktop mode.

# Open the Materials Designer

In order to create a new material, one first needs to navigate to the "Materials" page using the left-hand sidebar, and then click on the "Create" button <i class="zmdi zmdi-plus-circle-o zmdi-hc-border"></i> located at the top right corner of the page. 

# Components of the Interface

The Materials Designer is structured into four main building blocks, and has the typical initial default appearance as shown in the picture below. Its four main components are demarcated in red and numbered according to the list which follows the image. 

<img src="/images/materials-designer-initial.png"/> 

## 1. Header Menu

At the top of the page users find a header menu bar which provides the general functionality, such as importing the data and undo/redo. We explain these features in details [here](header-menu/input-output.md). At the right-end of this menu bar, a status indicator is also present: a check-mark means that the computational engine of the interface is not currently busy, and that new tasks can therefore be launched.

## 2. Items List Sidebar 

On the left there is a sidebar listing all the materials structures currently available for consideration and visualization. We explain it more in details [here](sidebar-items.md).

## 3. Crystallographic Data Panel
 
In the middle of the interface, a central panel is present comprising all the necessary crystallographic data (in an editable form) for defining the crystal structure under consideration. Instructions on how to enter or modify information pertaining to the overall Bravais lattice of the structure can be found [here](lattice.md), whereas those concerning specifically the atoms in the crystal basis can be accessed [here](basis.md). 

## 4. 3D Interactive Crystal Viewer

A 3D crystal structure graphical viewer is located on the right-hand side. This viewer can be rendered interactive to modify the current view of the crystal through simple mouse moves, as explained [here](viewer-intro.md).


# Default Material

When first opened, the page is initialized with the default material (FCC Silicon initially). Readers can learn how to set and adjust default materials in [this page](../materials/other-actions.md). 

# Links

1. [VESTA homepage](http://jp-minerals.org/vesta/en/)
2. [VMD homepage](http://www.ks.uiuc.edu/Research/vmd/)
3. [XCRYSDEN homepage](http://www.xcrysden.org/)

# Materials Tab

Opening the Materials Tab within the [Jobs Designer](overview.md) confronts the user with the following interface, which can be used to inspect and review the crystal structures of the materials [added](actions-header-menu/select-materials.md) to the [Job](/jobs/overview.md) being created.

![Materials Tab](/images/materials-tab.png "Materials Tab")

# Differences from Materials Viewer

The interface under Materials Tab largely mirrors the general [Materials Viewer](/materials/ui/viewer.md), except for the differences noted in the remainder of the present documentation page. These differences are concentrated within the **top-right toolbar** highlighted in the above image.
 
Please refer to the number labeling in the zoomed version of this toolbar shown below, for understanding the correspondence with the headers of the ensuing descriptions. 

![Materials Tab Toolbar](/images/materials-tab-toolbar.png "Materials Tab Toolbar")

Another important difference of Materials Tab from the main [Viewer](/materials/ui/viewer.md) is that **no adjustments** are allowed to the name (shown on the left of the above image) or [metadata](/entities-general/actions/metadata.md) (both tags and description) of the [material](/materials/overview.md) being currently inspected. The crystal structure itself also remains immutable, just like in Viewer.

# 1. Pager for Switching Materials

The **Materials Pager** affords for the switching between the different crystal structures added to the Job being designed, for the case when multiple structures have been [selected](actions-header-menu/select-materials.md) by the user. 

Navigation between different materials is achieved by clicking the arrows <i class="zmdi zmdi-chevron-left zmdi-hc-border"></i> <i class="zmdi zmdi-chevron-right zmdi-hc-border"></i> on either side of the pager, which take the progress of the selection backwards or forward respectively. The number label of the material being currently inspected under the interface, out of the total number of structures added so far by the user, is also indicated at the centre of the Pager. 

## Animation

In the animation shown here, we demonstrate how to cycle through a series of materials by using the pager, in order to review their respective crystal structures.

<img data-gifffer="/images/materials-pager.gif">

# 2. Add / Delete Materials

Pressing the "Plus" icon <i class="zmdi zmdi-plus zmdi-hc-border"></i> allows the user to select and add new materials from the account-owned [collection](/accounts/collections.md) into the Job under creation, in an analogous fashion to how this action is described [here](actions-header-menu/select-materials.md).

Conversely, the "Minus" icon <i class="zmdi zmdi-minus zmdi-hc-border"></i> affords for the deletion of the material under current inspection. Note that at least one material has to be present at all times in Jobs Designer, which prevents the deletion of the last remaining entry. 

# 3. Open / Close Toolbar

Finally, the <i class="zmdi zmdi-close zmdi-hc-border"></i> icon can be used to close and hide the other toolbar buttons. Clicking a second time at this location then toggles and re-enables them again.

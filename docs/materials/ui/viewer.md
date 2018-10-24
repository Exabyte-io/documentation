# Materials Viewer Interface 

In order to inspect an entry listed in the Account-owned collection of materials, the user can [open it](/entities-general/actions/open-edit.md) from [Materials Explorer](explorer.md). This action opens the material under the corresponding Viewer. 

# Viewer vs. Designer

As explained in the [general introduction](/entities-general/ui/viewer.md), we generally reuse the [Designer](/materials-designer/overview.md) component as Viewer throughout the platform, with some adjustments and limitations on editing. For example, the ["Edit" functionality of the 3D crystal viewer](/materials-designer/3d-editor/edit.md) is missing from Viewer, due to the inapplicability of its structure-changing actions under the "viewing" circumstances. 

# Allowed Adjustments

Some minor adjustments, not related to the crystal structure itself, might still be performed under the Materials Viewer. These can primarily be implemented under the  header and footer of Viewer, both highlighted in red in the image below.

![Materials Viewer](/images/materials-viewer.png "Materials Viewer")

## Modify Material Name 

One such permitted action is the changing of the Material's name, as it appears under the Account-owned collection. This can be accomplished by editing the name entry displayed on the left-hand side of the header. After making the desired adjustments, they can be saved by clicking "Save" <i class="zmdi zmdi-check zmdi-hc-border"></i> at the opposite extreme of the header bar. 

## Insertion of Metadata

Descriptive [metadata](/entities-general/data.md#metadata) can also be added or modified for the material entry currently being inspected. For example, a general description can be written under the "Info" button <i class="zmdi zmdi-info-outline zmdi-hc-border"></i>  present towards the right-hand side of the header. 

Tags can moreover be inserted in the footer, following the [general instructions](/entities-general/actions/metadata.md).

## Privacy Toggle Slider

The footer also allows Accounts with the appropriate [Service Level](/pricing/service-levels.md) to choose between making the current material private to the members of the Account only, or publicly accessible to all users of the platform. The difference between these two privacy levels is explained [here](/collaboration/sharing/access-levels.md). This choice can be made via the relevant toggle slider present towards the right-side of the footer. 

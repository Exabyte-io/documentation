# Materials Viewer Interface 

In order to view a material entry listed in the Account-owned collection of materials, the user can simply [open it](/entities-general/actions/open-edit.md) from the [Materials Explorer interface](explorer.md). This action will open the material under the Materials-specific Viewer interface. 

# Viewer vs. Designer

As explained in the [general introduction](/entities-general/ui/viewer.md), we generally reuse the [Designer](/materials-designer/overview.md) component as Viewer throughout the platform with some adjustments and limitations on editing. For example, the ["Edit" functionality of the 3D crystal viewer](/materials-designer/3d-editor/edit.md) is missing from Viewer, due to the inapplicability of its crystal structure-changing actions under the "viewing" circumstances. 

# Adjustments Allowed Under Materials Viewer

Some minor adjustments not related to the crystal structure itself might still be performed under the Materials Viewer. These can primarily be implemented under the main  header and footer of the Viewer interface, which are both highlighted in red in the example image below:

![Materials Viewer](/images/materials-viewer.png "Materials Viewer")


## Modify Name of Material

One such permitted action under Viewer is the changing of the Material's name, as it appears under the Account-owned collection. This can be accomplished by editing the material's name displayed on the left-hand side of the top header bar of the Viewer interface. After making the desired adjustments to this name, they can be saved by clicking on the "Save" button <i class="zmdi zmdi-check zmdi-hc-border"></i> present at the opposite extreme of the header bar. 

## Insertion of Metadata

Descriptive [metadata](/entities-general/data.md#metadata) can also be added or modified for the material entry currently being inspected under the Viewer interface. For example, a general description of the material can be written under the "Info" button <i class="zmdi zmdi-info-outline zmdi-hc-border"></i>  present towards the right-hand side of the top header bar. 

Tags can moreover be inserted in the footer at the bottom of the interface, following the [general instructions](/entities-general/actions/metadata.md).

## Privacy Toggle Slider

This footer also allows Accounts with the appropriate [Service Level](/pricing/service-levels.md) to choose between making the material currently being viewed private to the members of the Account only, or publicly accessible to all users of the platform. The difference between these two levels of data privacy is explained [in this page](/collaboration/sharing/access-levels.md). This choice can be made via the appropriate toggle slider present towards the right-side of the footer. 



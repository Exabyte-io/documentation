# Jobs Viewer Interface

In order to inspect the content of a Job, the user can [open it](/entities-general/actions/open-edit.md) from [Jobs Explorer](explorer.md). This action opens the Job under the corresponding Viewer, except for the case of Jobs in the [pre-submitted status](../status.md) where the [Designer](/jobs-designer/overview.md) is opened instead.

The image below shows how the Viewer contains two extra highlighted tabs, in addition to the three main tabs of [Designer](/jobs-designer/overview.md). They are labelled **"Results"** and **"Files"**, and are reviewed below. The name of the Job and that of the containing [Project](../projects.md) is also indicated at the top-left corner of the page.

![Extra Jobs Viewer](/images/extra-jobs-viewer.png "Extra Jobs Viewer")

# No Adjustments

Under Jobs Viewer, it is impossible to make **any** kind of adjustments to either [Materials](/jobs-designer/materials-tab.md), [Workflow](/jobs-designer/workflow-tab.md) or [Compute](/jobs-designer/compute-tab.md) settings contained in their respective tabs. This is in contrast to [Designer](/jobs-designer/overview.md).

The only change which can be made to the Job under Viewer is the insertion of descriptive [metadata](/entities-general/actions/metadata.md), under the corresponding button <i class="zmdi zmdi-info-outline"></i> at the top-right corner of the interface.

# Results Tab

This tab displays the results of the job's computational tasks. They are presented in a user-friendly way, including graphics when applicable. 

## Panels

The results for each computational [unit](/workflow-designer/unit-editor.md) contained across the [workflow](/workflow-designer/general-overview.md) operations of the Job are displayed in separate **panels**. 

### Naming Convention

Panels are named according to the format convention "Subworkflow Name - Unit Name". The name of the [application](/applications/modeling/overview.md) implemented in the current unit is also shown directly below the name of the corresponding panel.
 
### Collapse / Expand
 
The option to collapse or expand a panel is offered at its top-right corner.

## Materials Properties

The panels contain the results for the computation of the [materials properties](/properties/overview.md) that were selected at the moment of the [creation of the subworkflow](/workflow-designer/subworkflow-editor/detailed-view.md) or subsequently adjusted during the [job design](/jobs-designer/overview.md) stage.

The manner in which these properties are displayed under the corresponding panels is explained in a [separate section](/properties/scalar/overview.md) of this documentation. 

## Example Appearance

An example of appearance of the Results tab for the case of an electronic bandstructure calculation is exhibited in the image below. The first two panels have been collapsed, whereas the one displaying the dispersion curve has been kept opened. 

![Results Tab](/images/results-tab.png "Results Tab")

# Files Tab

"Files" tab contains a list of all the files produced as part of the Job's computational tasks, both of input and output nature. This list is presented under the conventional [Explorer Interface](/entities-general/ui/explorer.md). The files specific to each computing unit in the workflow are grouped together in different [Sets](/entities-general/sets.md), under the same name as the unit.

## Files Explorer

A review of the [actions](/files/actions/overview.md) and [user interface aspects](/files/ui/explorer.md) specific to the Files Explorer is offered in a separate section of the documentation.

## Example Appearance

An example of appearance of this Files tab is portrayed below, for a bandstructure run performed using the [VASP](/applications/modeling/vasp.md) code. The user is referred to the [code-specific documentation](/applications/modeling/vasp.md) for an explanation of the contents of the files displayed in this example.

![Files Tab](/images/files-tab.png "Files Tab")

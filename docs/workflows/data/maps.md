# Maps

Maps refer to a convenient approach for performing a distributed calculation. This is achieved by splitting the input data into several distinct independent calculation branches (mapping), and then by merging the output of such calculations again at the end (reduce operation). 

An example of application of this kind of distributed computing approach is for splitting a phonon dispersion calculation to many independent calculations for the individual vibration modes.

## Map Units in Workflow Flowcharts

In practice, when a new map is added to a workflow [flowchart](../../workflow-designer/sidebar.md), via the actions introduced [in this page](../../workflow-designer/subworkflow-editor/actions-menu.md#Adding Subworkflows), an entire new workflow will be created and contained within the original parent workflow. The typical appearance of this "workflow inside another workflow" map unit is shown in the example below:

![Example Map Workflow](/images/maps-workflow.png "Example Map Workflow")

The overall content of this workflow map is in general identical to that of a normal parent workflow, except for an extra tab labelled "Data" where an array of the corresponding map data can be inserted.  

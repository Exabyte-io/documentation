# Maps

Maps refer to a convenient approach for performing a distributed calculation. This is achieved by splitting the input data into several distinct independent calculation branches (maps), and then by merging the output of such calculations again at the end (reduce operation). This entire mapping/reducing procedure is summarized in the diagram below:

![](/images/maps.jpg)

An example of application of this kind of distributed computing approach is for splitting a phonon calculation in DFT over many independent q-points calculations.  

# Map units in Workflow flowcharts

In practice, when a new map is added to a workflow flowchart sequence of subworkflows in the Workflow Designer interface, via the actions introduced [in this page](/docs/workflow-designer/subworkflow-editor/actions-menu.md#Adding Subworkflows), an entire new workflow will be created in the form of a module contained within the original parent workflow sequence. The typical appearance of this "workflow inside another workflow" map unit is shown in the example below:

![](/images/maps-workflow.png)


The overall content of this workflow map is in general identical to that of a normal parent workflow, except for an extra tab labelled "Data" where the corresponding map data can be inserted.  

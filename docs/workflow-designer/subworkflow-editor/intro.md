# Subworkflow Editor

The Subworkflow Editor displays the input parameters of a subworflow on the right-hand side of the Workflow Designer interface. Whenever a subworkflow module is clicked upon among those listed in the [left-hand sidebar](../sidebar.md) it becomes the currently active one and feeds data to the Editor component.  

## Main components

Subworkflow Editor is itself subdivided into three distinct main components: 

- **menu bar** on top implementing some general actions, 
- the main editor interface below it comprising four different selectable **tabs**, each pertaining to different aspects of the subworkflow's operations, and
 - **units flowchart** at the bottom displaying the ordered sequence of computational units included as part of the current subworkflow.

The location of each component is highlighted in the picture below for the example case of a band structure calculation workflow. Click on a panel in the image to be redirected to the corresponding documentation page for each component:

<img src="/images/workflow-designer/sw-editor-components.png" usemap="#mapname">
                                           
<map name="mapname">
<area shape="rect" coords="190,88,756,141" href="/workflow-designer/subworkflow-editor/actions-menu/">
<area shape="rect" coords="190,141,756,545" href="/workflow-designer/subworkflow-editor/tabs-general/">
<area shape="rect" coords="190,545,756,642" href="/workflow-designer/subworkflow-editor/units-flowchart/">
</map>

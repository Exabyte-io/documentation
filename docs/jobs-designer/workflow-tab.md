# Workflow Tab

Navigating to the Workflow Tab in [Jobs Designer](overview.md) displays the [Workflow](../workflows/overview.md) for the [Job](../jobs/overview.md) being created. The interface is equivalent to that of the [Workflows Designer](../workflow-designer/overview.md), except for a limited set of non-adjustable parameters outlined in what follows.

![Workflow Tab](../images/jobs-designer/workflow-tab.png "Workflow Tab")

## Non-Adjustable Settings

Some Workflow parameters can be edited under Jobs Designer, except for those pertaining to the ["Application"](../software/modeling/applications.md), ["Model"](../models/overview.md) and ["Method"](../methods/overview.md) being employed as part of the computation. 
 
These non-adjustable settings are present both under the ["Overview Tab"](../workflow-designer/subworkflow-editor/overview-tab.md) of Workflow Designer, and inside the editor of the [subworkflow units](../workflow-designer/unit-editor.md). Hovering the mouse over such settings makes it clear that the editing action is forbidden in these cases, as illustrated below.
 
 ![Forbidden Workflow Actions](../images/jobs-designer/forbidden-workflow-actions.png "Forbidden Workflow Actions")

## Workflow Settings for Multiple Materials

The same Workflow settings are attributed simultaneously to all Materials [added](actions-header-menu/select-materials.md) to Jobs Designer, regardless of which Material is currently open for inspection under the [corresponding Tab](materials-tab.md).

## Modify Units Input

### Single Material 

If only one [Material](../materials/overview.md) is present in Jobs Designer, the input parameters for each [computational unit](../workflows/components/units.md) contained in the Workflow can be edited within the [Preview Section of the unit input editor](../workflow-designer/unit-editor/input-templates.md#preview-of-the-input-file).

### Multiple Materials

If alternatively multiple [Materials](../materials/overview.md) have been added, then the use of templating logic is recommended for changing the input script parameters simultaneously for all entries. This action should be performed from the [Workflow Designer](../workflow-designer/overview.md) itself, instead of Jobs Designer. We explain the use of templating logic for rendering simulation input files [in this page](../workflows/templating/overview.md).

### See Preview for Each Material

In the animation below, we show how to cycle through the input script previews for a series of materials added to the Job Designer. Each entry can be selected in turn by clicking its corresponding radio button from the list on the right.

<img data-gifffer="/images/jobs-designer/unit-inputs-designer.gif">

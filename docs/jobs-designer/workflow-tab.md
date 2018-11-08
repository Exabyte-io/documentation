# Workflow Tab

Navigating to the Workflow Tab in [Jobs Designer](overview.md) displays the [Workflow](/workflows/overview.md) computational settings for the [Job](/jobs/overview.md) being currently created. It can be deduced from the image below that the interface is equivalent to that of [Workflows Designer](/workflow-designer/overview.md), except for a limited set of non-adjustable parameters outlined in what follows.

![Workflow Tab](/images/workflow-tab.png "Workflow Tab")

# Non-Adjustable Settings

All Workflow parameters can be edited under Jobs Designer, except for those pertaining to the ["Application"](/software/applications.md), ["Model"](/models/overview.md) and ["Method"](/methods/overview.md) being employed as part of the computation. 
 
These non-adjustable settings are present both under the ["Overview Tab"](/workflow-designer/subworkflow-editor/overview.md) of Workflow Designer, and inside the editor of the [component units](/workflow-designer/unit-editor.md). Hovering the mouse over such settings makes it clear that the editing action is forbidden in these cases, as illustrated below.
 
 ![Forbidden Workflow Actions](/images/forbidden-workflow-actions.png "Forbidden Workflow Actions")

# Workflow Settings for Multiple Materials

The same Workflow settings are attributed simultaneously to all Materials [added](actions-header-menu/select-materials.md) to Jobs Designer, regardless of which Material is currently open for inspection under the [corresponding Tab](materials-tab.md).

# Modify Units Input 

## Single Material 

If only one [Material](/materials/overview.md) is present in Jobs Designer, the input parameters for each [computational unit](/workflows/data/units.md) contained in the Workflow can be edited within the [input scripts previews](/workflow-designer/unit-editor/input-templates.md). They are displayed towards the bottom of the [unit editor interface](/workflow-designer/unit-editor.md), and can be accessed and edited directly from the Workflow Tab of Jobs Designer.

## Multiple Materials

If alternatively multiple [Materials](/materials/overview.md) have been added, then the use of templating logic is recommended for changing the input script parameters simultaneously for all entries. This action should be performed from the [Designer for the Workflow](/workflow-designer/overview.md) itself, instead of Jobs Designer. We explain the use of templating logic for rendering simulation input scripts automatically [in this page](/workflows/data/templates.md).

## See Preview for Each Material

In the animation below, we show how to cycle through the input script previews for a series of materials added to the Job being designed. Each entry can be selected in turn by clicking its corresponding radio button from the list on the right.

<img data-gifffer="/images/unit-inputs-designer.gif">

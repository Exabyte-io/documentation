# Jobs Designer

The creation of new simulation Jobs via Designer proceeds through three main steps, namely the definition of the [crystal structure](/materials/overview.md) to be investigated (1), of the type of [Workflow calculation](/workflows/overview.md) to be applied upon it (2), and finally of the [computational resources](/infrastructure/resource/overview.md) to be allocated for this calculation (3). 

# Components of the Interface

These three steps can each be formulated under the [corresponding tab](/ui/specific/tabs-navigator.md) of the main Designer interface, as highlighted in the picture below. This image also shows the location of the principal [header menu](header-menu.md) located at the top of the page. 

Please click on each component panel within the image to access the corresponding documentation section, or alternatively refer to the links listed towards the end of the present page.

<img src="/images/jobs-designer.png" usemap="#mapname">

<map name="mapname">
    <area shape="rect" coords="0,41,753,116" href="/jobs-designer/header-menu/">
    <area shape="rect" coords="0,116,233,155" href="/jobs-designer/materials-tab/">
    <area shape="rect" coords="233,116,508,155" href="/jobs-designer/workflow-tab/">
    <area shape="rect" coords="508,116,753,155" href="/jobs-designer/compute-tab">
</map>

# Open Jobs Designer

The Jobs Designer interface can be opened by [creating a new Job](/jobs/actions/create.md), starting from the [page of the Project](/jobs/ui/projects-page.md) under which the user wishes to save the new Job. Alternatively, it can be opened directly from the [left-hand sidebar menu](/ui/left-sidebar.md).

Moreover, any entry listed in [Jobs Explorer](/jobs/ui/explorer.md) which has a "Pre-submission" [status](/jobs/status.md) can also be [opened](/entities-general/actions/open-edit.md) directly into Designer, as opposed to Viewer. This is because jobs which have not been submitted for computation yet can still be fully modified by the user, with no limitations such as those imposed by the [Viewer](/jobs/ui/viewer.md#no-adjustments-allowed).

New Jobs are by default saved in the [Default Project](/jobs/projects.md) of the account being considered. Please review [this page](/entities-general/actions/set-default.md) for instructions on how this default choice can be changed, starting from the [Project Explorer](/jobs/ui/projects-explorer.md).

# Header Menu

The components of the header menu are reviewed in [this part of the documentation](header-menu.md).

# Materials Tab

The explanation for the Materials Tab is offered [in this page](materials-tab.md). 

# Workflow Tab

The Workflow tab is the object of a separate discussion, which can be found [here](workflow-tab.md).

# Compute Tab

The Compute tab is documented [in this section](compute-tab.md).

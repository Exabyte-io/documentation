# What is Workflow Designer?

 Our platform provides a convenient interface for conceiving, editing and saving workflows which implement different types of studies of materials. We refer to this interface as the Workflow Designer, and we reviewed it in detail in this section of documentation. 

## [Navigating to Workflow Designer](../entities-general/actions/create.md)

Navigating to the interface can be initiated through the "Create Workflow" action introduced [in this page](../entities-general/actions/create.md). 
 
## [Components of the Interface]()

The Workflow Designer is structured into three main building blocks, and has the typical initial default appearance as shown in the picture below when a new workflow is being created from scratch. In the image below, the three main components are outlined in red. To access their respective documentation pages, **click** on the image below.

<img src="/images/workflow-designer-initial.png" usemap="#mapname">

<map name="mapname">
    <area shape="rect" coords="0,91,190,512" href="/workflow-designer/sidebar/">
    <area shape="rect" coords="190,91,754,512" href="/workflow-designer/subworkflow-editor/intro/">
    <area shape="rect" coords="0,28,754,91" href="/workflow-designer/header-menu">
</map>

## [Convergence and Relaxation Add-ons]()

When creating a new workflow, two important preliminary controls are typically required at the beginning of the workflow, and can be implemented in the context of the Workflow Designer interface in the form of **add-on** subworkflow modules.

Firstly, to have a reasonable level of confidence that a result can be trusted, the total energy should not change significantly when the k-point density is increased.  This search for the appropriate density of k-points is called [k-point convergence](../workflows/addons/convergence-algorithms.md).

It is furthermore often desirable to start the workflow with an appropriately [relaxed structures](../workflows/addons/structural-relaxation.md) to ensure that the crystalline system under consideration is in the lowest possible total energy state configuration since the early stages of the workflow, before computing any subsequent property on it.

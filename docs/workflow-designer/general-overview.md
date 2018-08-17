# What is Workflow Designer?

 The Exabyte platform provides a convenient interface for conceiving, executing and saving workflows which implement most of the possible calculations in the computational atomistic study of materials, such as the computation of thermodynamic quantities,  phonon dispersion curves, and electronic band structures. We refer to this interface as the Workflow Designer, and we will now reviewed it in detail. 
 
 The Exabyte platform supports several widely used ab-initio quantum computational engines, all based on the plane-waves pseudopotential formulation of Density Functional Theory (DFT) [[1](#links)] for calculating approximate solutions to Schrodinger's Equations and associated physical properties in relatively complex crystalline materials. The reader who wishes to revise the fundamental theoretical framework underlying DFT is referred to the introductory literature on the subject [[2](#links)]. 

# Components of the Interface

The Workflow Designer is structured into three main building blocks, and has the typical initial default appearance as shown in the picture below when a new workflow is being created from scratch via the "Create Workflow" action introduced [in this page](../workflows/creating-workflows.md). In this image, the three main components of the interface are delimited in red. To access their respective documentation pages, please click on each component's red panel directly on the image:

<img src="/images/workflow-designer-initial.png/" usemap="#mapname">

<map name="mapname">
    <area shape="rect" coords="0,91,190,512" href="/workflow-designer/sidebar-items/">
    <area shape="rect" coords="190,91,754,512" href="/workflow-designer/source-editor-intro/">
    <area shape="rect" coords="0,28,754,91" href="/workflow-designer/header-menu-actions">
</map>

<!-- coords="x1,y1,x2,y2" -->
<!-- x1=top left X coordinate -->
<!-- y1=top left Y coordinate -->
<!-- x2=bottom right X coordinate -->
<!-- y2=bottom right Y coordinate -->



<!--  The reader who is interested in learning more about the detailed numerical implementations of such quantum mechanical calculations in both of these codes is referred to their respective [documentation websites](#links). -->

# Links

1. [Wikipedia Density Functional Theory, Website](https://en.wikipedia.org/wiki/Density_functional_theory)
2. R.M. Martin: "Electronic Structure: Basic Theory and Practical Methods"; Cambridge University Press (2008)



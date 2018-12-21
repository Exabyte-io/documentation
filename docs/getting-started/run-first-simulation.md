# Run First Simulation

This page explains how to run a simple [density functional theory calculation](../models-directory/dft/overview.md) to obtain an [electronic band structure](../properties-directory/non-scalar/bandstructure.md). Each [account](../accounts/overview.md) is pre-configured with one default [material](../materials/overview.md) and [workflow](../workflows/overview.md). For the sake of this tutorial, we will keep the *default* parameters at each step. We will thus study silicon in the standard face-centered cubic structure and use [Quantum ESPRESSO](../software-directory/modeling/quantum-espresso/overview.md) as the [simulation engine](../software-directory/overview.md).

## Prepare Material and Workflow

Users may also add new materials or workflows into their collection from the application-wise ["Bank" collection](../entities-general/bank.md) that we maintain. To do so, select the "Bank" option in the [left-hand sidebar](../ui/left-sidebar.md) of the user interface, and then "Materials" or "Workflows" as the user prefers. To import either workflows and material structures from the Bank, select the desired entry and then click "Copy" in the top-right taskbar of the page, as explained in more detail [here](../entities-general/actions/copy-bank.md).

Silicon FCC is the default material added to each account on creation. In the animation below we demonstrate how to import the "Band Structure" workflow for [Quantum ESPRESSO](../software-directory/modeling/quantum-espresso/overview.md) from the Bank.

<img data-gifffer="/images/getting-started/run-first-simulation-import-workflow.gif"/>
 
Readers can also learn how to [create](../materials-designer/overview.md) or [upload](../materials/actions/upload.md) / [import](../materials/actions/import.md) materials with the aid of the incorporated Exabyte Materials Designer tool, as well as further setting them as [default](../entities-general/actions/set-default.md) elsewhere in this documentation. 
 
## Open Job Designer

Start by clicking "Create Job" link in the [left-hand sidebar](../ui/left-sidebar.md) to open the ["Job Designer" page](../jobs-designer/overview.md), where the user can do the following actions via the relevant Tab for each.

- Choose a previously created [material](../jobs-designer/materials-tab.md)
- Choose and adjust a simulation [Workflow](../jobs-designer/workflow-tab.md)
- Setup [compute parameters](../jobs-designer/compute-tab.md)
   
## 1. Materials Tab

[Materials Tab](../jobs-designer/materials-tab.md) lets the user choose one or more previously imported [materials](../materials/overview.md) for use during the calculation. We will proceed with the default structure of Silicon.

![Materials viewer](../images/getting-started/run-first-simulation-tab-1-materials.png "Materials viewer")

## 2. Workflow Tab

Simulations usually have multiple steps that need to be executed in a certain order. This step sequence is called a ["Workflow"](../workflows/overview.md).

Open the dropdown menu of the top-level page header (see animation below), click "Select Workflow" and select "Bandstructure" workflow with "espresso" as modeling engine, after [searching](../entities-general/actions/search.md) for the corresponding keywords in the resulting "Select Workflow" dialog. We divide a workflow into ["Subworkflows"](../workflows/components/subworkflows.md), such that each individual Subworkflow can only contain one [modeling engine](../software/overview.md) and one [theoretical model](../models/overview.md) (eg. [Quantum ESPRESSO](../software-directory/modeling/quantum-espresso/overview.md), or "espresso", and [density functional theory](../models-directory/dft/overview.md) respectively).

The subworkflow ["Overview" tab](../workflow-designer/subworkflow-editor/overview-tab.md) contains the basis information about it, including the individual computational building blocks - or ["Units"](../workflows/components/units.md). Settings that we classify as most important are listed under ["Important Settings"](../workflow-designer/subworkflow-editor/important-settings.md): [k-point grid](../models/auxiliary-concepts/reciprocal-space/sampling.md) and [k-point path](../models/auxiliary-concepts/reciprocal-space/paths.md) within the [reciprocal space](../models/auxiliary-concepts/reciprocal-space.md) of the crystal are among them for the case of a "Band Structure" calculation considered here.

One can further modify the input files for each individual part of the subworkflow by clicking on the corresponding unit, and [adjusting its input content](../workflow-designer/unit-editor/input-templates.md) as the animation below demonstrates.

<img data-gifffer="/images/getting-started/run-first-simulation-tab-2-workflow.gif"/>

## 3. Compute Tab

The ["Compute" tab](../jobs-designer/compute-tab.md) lets the user set up the number of processor cores to be used for the computation, its maximum time limit and other relevant [compute parameters](../infrastructure/compute/parameters.md). We set the maximum time limit for the calculation to properly schedule the allocation of resources. The format is HH:MM:SS, so that `01:00:00` corresponds to up to 1 hour runtime.

One can also choose to be notified of the job status by clicking on his/her name in the ["Notifications" section](../infrastructure/compute/parameters.md#notifications).

For the moment, let us leave all parameters at their default values and click "Save".

![Compute Tab](../images/getting-started/run-first-simulation-tab-3-compute.png "Compute Tab")

!!! Note "Summary"
    We have just finished creating our first job. We can now proceed to submit it.

## Run Calculation

After saving the job, the user is redirected back to the default ["Project" page](../jobs/ui/project-page.md). Here, the user can [submit the job](../jobs/actions/run.md) and track its [status](../jobs/status.md).

### Submit and Track Progress

The user can run the job by clicking the three vertical dots to the right of its status label ("pre-submission"), and choosing "Run", as explained in more detail [here](../jobs/actions/run.md).

The [status](../jobs/status.md) will change from "pre-submission" to "submitted". This means that the job is finally submitted to our [computing clusters](../infrastructure/clusters/overview.md). Depending on the load, it may take some time for it to become "Active" and thus start executing.

The user can click on the job name to monitor the progress of the job in real time within the [Job Viewer Interface](../jobs/ui/viewer.md).

<img data-gifffer="/images/getting-started/run-first-simulation-submit-view-output.gif" />

### View Results and Access Files

The [Job Viewer screen](../jobs/ui/viewer.md) tracks the input parameters, output text, and convergence parameters involved in the computation (total energy in this tutorial). It also allows the user to [view the results](../jobs/ui/results-tab.md) of the calculation, and to [download output files](../jobs/ui/files-tab.md) when finished.

<img data-gifffer="/images/getting-started/run-first-simulation-view-results.gif" />

## Done

We have demonstrated in the present page how a simple electronic band structure calculation can be run using exabyte.io. For a more comprehensive tutorial, readers may refer to the dedicated ["Tutorials" section](../tutorials/dft/band-structure.md) of our documentation.

![simple electronic band structure calculation](../images/getting-started/run-first-simulation-view-bandstructure.png "simple electronic band structure calculation")

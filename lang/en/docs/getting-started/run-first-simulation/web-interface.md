# Running Jobs via Web Interface

This page explains how to run a simple [density functional theory calculation](
../../models-directory/dft/overview.md) to obtain [electronic band structure](
../../properties-directory/non-scalar/bandstructure.md) via our main
[Web Interface](../../ui/overview.md).

Below we present a short video demonstrating how to create and run jobs in
Mat3ra platform.

<div class="video-wrapper">
<iframe class="gifffer"
    width="100%"
    height="100%"
    src="https://www.youtube.com/embed/hT1VBFH7HHo"
    frameborder="0"
    allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen>
</iframe>
</div>

Creating and running a job in Mat3ra web platform involves three main steps:

1. Specify the material system by creating or importing crystal structure
2. Create or import workflow, which specifies the simulation steps
3. Create job where we set material, workflow and compute parameters

Each [account](../../accounts/overview.md) is pre-configured with a default
[material](../../materials/overview.md) and [workflow](
../../workflows/overview.md). Silicon FCC is the default material and Total
Energy calculation with Quantum ESPRESSO is the default workflow added to each
account on creation.

To add new materials or workflows from the application-wise ["Bank" collection](
../../entities-general/bank.md) that we maintain, select the "Bank" option in
the [left-hand sidebar](../../ui/left-sidebar.md) of the user interface, and
then "Materials" or "Workflows" as the user prefers. To import either workflows
and material structures from the Bank, select the desired entry and then click
"Copy" in the top-right taskbar of the page, as explained in more detail [here](
../../entities-general/actions/copy-bank.md).


## 1. Specify Material system

There are several ways, we can add new materials to the collection:

- Create a new material from scratch using [Materials Designer](
  ../../materials-designer/overview.md)
- Upload a material from your local computer such as CIF, POSCAR format
  files using [Upload](../../materials/actions/upload.md) action
- Import a material from the [Materials Bank](../../entities-general/bank.md)
- Import a material from a third-party source such as [Materials Project](
  https://materialsproject.org/) using [Import](
  ../../materials/actions/import.md) action.


Readers can find additional details on how to [create](
../../materials-designer/overview.md) or [upload](
../../materials/actions/upload.md) / [import](../../materials/actions/import.md)
materials with the aid of the incorporated Mat3ra Materials Designer tool, as
well as further setting them as [default](
../../entities-general/actions/set-default.md) as described elsewhere in this
documentation.


## 2. Specify Workflow steps

A workflow can be created from scratch or imported from the Workflow Bank. In
the animation below, we demonstrate how to import the "Band Structure" workflow
for [Quantum ESPRESSO](
../../software-directory/modeling/quantum-espresso/overview.md) from the
Workflow Bank to your account collection.

<img data-gifffer="/images/getting-started/run-first-simulation-import-workflow.gif"/>

The above task involves following steps:

  1. Navigate to the [Workflows Bank](../../workflows/bank.md) page by clicking
  on the "Bank" option in the [left-hand sidebar](../../ui/left-sidebar.md)
  2. Search with the text "curators" to filter workflows created by the
  "Curators" account
  3. Sort workflows by name, and look for the "Band Structure" workflow for
  Quantum ESPRESSO and click on the "Copy" button to add it to your account
  collection.

## 3. Open Job Designer

Start by clicking "Create Job" link in the [left-hand sidebar](
../../ui/left-sidebar.md) to open the ["Job Designer" page](
../../jobs-designer/overview.md), where the user can do the following actions
via the relevant Tab for each.

- Click "Create" new job button to open the Job Designer page
- Choose a previously created [material](../../jobs-designer/materials-tab.md)
- Select and adjust a simulation [Workflow](../../jobs-designer/workflow-tab.md)
- Navigate to the "Workflow" tab to review and adjust the workflow settings
- Navigate to the "Compute" tab to set [compute parameters](
  ../../jobs-designer/compute-tab.md)
- Click "Save and Exit" job designer

### 3.1. Materials Tab

[Materials Tab](../../jobs-designer/materials-tab.md) lets the user choose one
or more previously imported [materials](../../materials/overview.md) for use
during the calculation. We will proceed with the default structure of Silicon.

![Materials viewer](../../images/getting-started/run-first-simulation-tab-1-materials.webp "Materials viewer")

### 3.2. Workflow Tab

Simulations usually have multiple steps that need to be executed in a certain
order. This step sequence is called a ["Workflow"](../../workflows/overview.md).

Open the dropdown menu of the top-level page header (see animation below), click
"Select Workflow" and select "Bandstructure" workflow with "espresso" as
modeling engine. A workflow consists of one or multiple ["Subworkflows"](
../../workflows/components/subworkflows.md), as such each Subworkflow can only
contain one [modeling engine](../../software/overview.md) and one
[theoretical model](../../models/overview.md) (eg. [Quantum ESPRESSO](
../../software-directory/modeling/quantum-espresso/overview.md), or "espresso",
and [density functional theory](../../models-directory/dft/overview.md)
respectively).

The subworkflow ["Overview" tab](
../../workflow-designer/subworkflow-editor/overview-tab.md) contains the basic
information about it, including the individual computational building blocks -
or ["Units"](../../workflows/components/units.md). Settings that we classify as
most important are listed under ["Important Settings"](
../../workflow-designer/subworkflow-editor/important-settings.md):
[k-point grid](../../models/auxiliary-concepts/reciprocal-space/sampling.md) and
[k-point path](../../models/auxiliary-concepts/reciprocal-space/paths.md)
within the [reciprocal space](../../models/auxiliary-concepts/reciprocal-space.md)
of the crystal are among them for the case of a "Band Structure" calculation
considered here.

One can further modify the input files for each individual part of the
subworkflow by clicking on the corresponding unit, and
[adjusting its input content](
../../workflow-designer/unit-editor/input-templates.md).

![Workflow Tab](../../images/getting-started/run-first-simulation-tab-2-workflow.webp "Workflow Tab")


### 3.3. Compute Tab

The ["Compute" tab](../../jobs-designer/compute-tab.md) lets the user set the
cluster, queue, number of nodes and processor cores to be used for the
computation, maximum time limit and other relevant [compute parameters](
../../infrastructure/compute/parameters.md). We set the maximum time limit for
the calculation to properly schedule the allocation of resources. The format is
HH:MM:SS, so that `01:00:00` corresponds to up to 1 hour runtime. One can also
choose to be notified of the job status by clicking on his/her name in the
["Notifications" section](
../../infrastructure/compute/parameters.md#notifications).

![Compute Tab](../../images/getting-started/run-first-simulation-tab-3-compute.webp "Compute Tab")


## 4. Run Calculation

After saving the job, the user is redirected back to the default
["Project" page](../../jobs/ui/project-page.md). Here, the user can
[submit the job](../../jobs/actions/run.md) and track its [status](
../../jobs/status.md).

### 4.1. Submit and Track Progress

The user can run the job by clicking the three vertical dots to the right of its
status label ("pre-submission"), and choosing "Run", as explained in more detail
[here](../../jobs/actions/run.md).

The [status](../../jobs/status.md) will change from "pre-submission" to
"submitted". This means that the job is finally submitted to our
[computing clusters](../../infrastructure/clusters/overview.md). Depending on
the load, it may take some time for it to become "Active" and thus start
executing.

The user can click on the job name to monitor the progress of the job in real
time within the [Job Viewer Interface](../../jobs/ui/viewer.md).


### 4.2. View Results and Access Files

The [Job Viewer screen](../../jobs/ui/viewer.md) tracks the input parameters,
output text, and convergence parameters involved in the computation (total
energy in this tutorial). Once the job is completed, user can navigate to the
[Results Tab](../../jobs/ui/results-tab.md) to [view the results](
../../jobs/ui/results-tab.md) of the calculation, and [download output files](
../../jobs/ui/files-tab.md) from the "Files" tab.


## 5. Done

We have demonstrated in the present page how a simple electronic band structure
calculation can be run using Mat3ra web interface. For a more comprehensive
tutorial, readers may refer to the dedicated ["Tutorials" section](
../../tutorials/overview.md) of our documentation.

![simple electronic band structure calculation](
../../images/getting-started/run-first-simulation-view-bandstructure.webp "simple electronic band structure calculation")

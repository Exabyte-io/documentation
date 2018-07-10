<!-- by TB -->

This page explains how to run a simple density functional theory calculation to obtain an electronic band structure. Each account is pre-configured with one default material and workflow. For the sake of this tutorial, we will keep the *default* parameters at each step. We will thus study silicon in the standard face-centered cubic structure and use Quantum ESPRESSO as the simulation engine.

# Prepare Material and Workflow

Users may also add new materials or workflows into their collection from the application-wise "Bank" collection that we maintain. To do so, select the "Bank" option in the left-hand sidebar and then "Materials" ("Workflows"). To import both workflows and material structures from the Bank select the desired entry by ticking the checkbox at the start of the entry line and then click "Copy" in the top-right taskbar of the page.

Silicon FCC is the default material added to each account on creation. Below we demonstrate how to import the "Band Structure" workflow for Quantum ESPRESSO.

<!-- TODO by GM: add a gif of the above process -->
 
Readers can also learn how to [create](/materials/creating-structures/) or [upload/import](/materials/upload-and-import) materials with the aid of the incorporated Exabyte Materials Designer tool, as well as further setting them as [default](/materials/other-actions.md) elsewhere in this documentation. 
 

# Open Job Designer

Start by clicking "Create Job" link in the left-hand sidebar to open the "Job Designer" page where you can:

- Choose a previously created material
- Choose and adjust a simulation Workflow
- Setup compute parameters
   
# Tab #1: Materials

Materials viewer lets you choose one or more previsously imported materials for use during the calculation. We will proceed with the default structure of Silicon.

<img src="/images/run-first-simulation-tab-1-materials.png"/>

# Tab #2: Workflow

Simulations usually have multiple steps that need to be executed in a certain order. This step sequence is called a "Workflow".

Open the dropdown menu of the top-level page header (see animation below) and select "Bandstructure" workflow with "espresso" as modeling engine. We divide workflow into "Subworkflows", such that each individual Subworkflow can only contain one modeling engine and one model (eg. Quantum ESPRESSO, or "espresso", and density functional theory).

Subworkflow "Overview" contains the basis information about it including the individual building blocks - or "Units". Settings that we classify as most important naturally are listed under "Important Settings": k-point grid and k-point path are among them for "Band Structure" calculation.

One can further modify the input files for each individual part of the subworkflow by clicking on the corresponding element and adjusting its input content as the animation below demonstrates.

<img data-gifffer="/images/run-first-simulation-tab-2-workflow.gif"/>

# Tab #3: Compute

This tab lets you set up the number of processor cores and the maximum time limit for your calculation. We set the maximum time limit for the calculation to properly schedule the allocation of resources. The format is HH:MM:SS, so that `01:00:00` corresponds to up to 1 hour runtime.

One choose to be notified of the job status by clicking on our name in the "Notifications" section.

For the moment, let's leave all parameters at their default values and click "Save".

<img src="/images/run-first-simulation-tab-3-compute.png"/>

!!! Note "Summary"
    You have created and saved your first job to be run in the future. Now we can proceed to submit it.

# Run calculation

After saving the job, you are redirected back to the default "Project" page. Here you can submit the job and track its status.

## Submit and track progress

Run the job by clicking the three vertical dots to the right of its status label ("pre-submission") and choosing "Run".

You will see the status changing from "pre-submission" to "submitted". This means that the job was submitted to our compute platform.  Depending on the load it may take some time to become "Active".

You can click on the job name and monitor the progress of the job in real time.

<img data-gifffer="/images/run-first-simulation-submit-view-output.gif" />

## View results and access files

Job view screen lets you track the input parameters, output text, convergence parameters (total energy in this tutorial), and view the results of the calculation and download output files when finished.

<img data-gifffer="/images/run-first-simulation-view-results.gif" />

# Done

This is how you can run a simple electronic band structure calculation using exabyte.io. For a comprehensive tutorials readers may explore ["Tutorials" section](/tutorials/band-structure.md).

<!-- TODO by GM: add a png image of the final band structure screenshot -->

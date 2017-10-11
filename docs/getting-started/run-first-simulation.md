<!-- by MH -->

This page explains how to run a basic simulation based on density functional theory to obtain an electronic bandstructure. We will study silicon in the standard diamond-like face-centered structure and use Quantum ESPRESSO as simulation engine.

!!! Warning "Outdated visuals"
    Some visuals below may be outdated and demonstrate a similar, however not exactly accurate user experience compared to what our product currently provides.

## Open Job Designer

Start by click "Create Job" link in the left-hand sidebar.

You will be taken to the "Job Desinger" page where you can:

- Choose a material (one that you created and saved before)
- Choose and adjust a simulation Workflow
- Setup compute parameters

For the sake of this tutorial, we will keep the default parameters at each step.

## Tab #1: Materials

Materials viewer lets you choose one or more previsously imported materials for use during the calculation. We will proceed with the default structure of Silicon.

<img data-gifffer="/images/FirstJobCreate.gif" />

## Tab #2: Workflow

Simulations usually have multiple steps that need to be executed in a certain order. This step sequence is called a "Workflow".

Open the dropdown menu of the top-level page header and select "Bandstructure" workflow with "espresso" as modeling engine. We divide workflow into "Subworkflows", such that each individual Subworkflow can only contain one modeling engine and one model (eg. Quantum ESPRESSO, or "espresso", and density functional theory).

One can further modify the input files for each individual part of the subworkflow - or "Unit" as we call it - by clicking on the corresponding element. One can also customize the workflow by adding and deleting individual "Units" by adding and deleting the tabs containing input files.  We will set the k-point density to 7x7x7.

<img data-gifffer="/images/FirstJobWorkflow.gif" />

## Tab #3: Compute parameters

This tab lets you set up the number of processors and the maximum time limit for your calculation to run. Increasing the number of processors allocated to the job may accelerate the calculation if you have a larger unit cell. We set the maximum time limit for the calculation to properly schedule the allocation of compute resources to it.

One can also choose to be notified of the job status by clicking on our name in the "Notifications" section. Leave all parameters at their default values and click "Save".

<img data-gifffer="/images/FirstJobCompute.gif" />

!!! Note "Summary"
    You have created and saved your first job to be run in the future. Now we can proceed to submit it.

## Execute the job

After saving the job, you are redirected back to the default "Project" page. Here you can submit the job and track its status.

### Submit for execution

Run the job by clicking the 3 vertical dots to the right of the "Pre-Submission" box and choosing the right-pointing triangle icon labeled "Run".

You will see the status changing from "pre-submission" to "submitted". This means that the job was submitted to our compute platform.  Depending on the load it may take some time to become "Active".

<img data-gifffer="/images/FirstJobSubmit.gif" />

### View progress

You can click on the job name and monitor the progress of the job in real time.

<img data-gifffer="/images/FirstJobStatus.gif" />

### View results and access files

Job view screen lets you track the input parameters, output text, convergence parameters (total energy in this tutorial), and view the results of the calculation and download output files when finished.

<img data-gifffer="/images/FirstJobResults.gif" />

# Done

This is how you can run a band structure calculation using exabyte.io. For a more comprehensive tutorial on how to run a bandstructure calculation including editing input files click [here](/tutorials/band-structure.md).

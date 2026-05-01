# Running MatterSim and other Python-based Machine Learning Models

## Using MatterSim bank workflow

### Copy bank workflow

The easiest way to run MatterSim calculations is to use an existing bank
workflow. Before we can use a workflow to create a job, we need to copy it to
to our own account.

1. Navigate to the workflows bank from the left sidebar.
2. Search for "MatterSim" and click "Copy" in the action column on the workflow
you want to use.
![Copy bank workflow](../../images/tutorials/mattersim/mattersim-bank-workflow.webp "Copy bank workflow")
3. Now the workflow will appear in your own workflows list, and will be
available for selection in job creation process.
4. We can open the workflow for inspection and further modification if needed.
The workflow is consists of three units:
    - Input/Output unit: This unit is used to fetch materials data from the job
    context. The response is an array of materials.
    - Assignment unit: This unit is takes the first item of the above array and
    assigns a new variable named `MATERIAL` in the global scope.
    - MatterSim unit: Creates ASE material definition from `MATERIAL` and runs
    the MatterSim calculation to predict various material properties.

![MatteSim workflow units](../../images/tutorials/mattersim/mattersim-workflow.webp "MatteSim workflow units")

### Create and submit job

1. Navigate to the jobs designer page from the left sidebar.
2. Click "Create New Job".
3. Click on the "Select Job Actions" drop-down menu, and select the material and
workflow you want to use.
4. We will proceed with the default material, which is Silicon, and select
"MatterSim Python Workflow" that we just imported.
5. Save and exit the job designer.
![MatteSim Job creation](../../images/tutorials/mattersim/mattersim-job.webp "MatteSim Job creation")
6. Now the job is ready for submission. Click on the "Run" button in the
"Actions" column.
7. Once the job is completed, we can open job viewer page to see the results. We
can open the MatterSim unit under workflow tab to see the standard output. All
the input and outputs are available under the "Files" tab.

## Step-by-step Video Tutorial

In the below animation, we walk you through the whole process.

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/W8NNH_WjtI8?controls=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

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

## Creating MatterSim workflow

In this section, we will describe how to create a new workflow and use MatterSim
flavor/<wbr/>template.

1. Navigate to the workflows page, and click on the "Create" new workflow button.
2. Expand the "Details" section, select "Python Script" as application.
3. Add a "executable" unit, and click "EDIT" unit button.
![MatteSim add unit](../../images/tutorials/mattersim/mattersim-add-unit.webp "MatteSim add unit")
4. Expand the "Details" section, and select "mlff:mattersim:cell_relaxation" as
flavor.
![MatteSim edit unit](../../images/tutorials/mattersim/mattersim-edit-unit.webp "MatteSim edit unit")
5. Scroll down and edit the Python script if necessary. In this case, we want to
use ASE library to create a material definition, instead of getting material
from the job context.

```python title="SCRIPT.PY"
from ase.build import bulk
ase_atoms = bulk("GaN", "wurtzite", a=3.189, c=5.185)
```

6. Close unit modal by clicking on the "X" button in the top right.
7. Save and exit the workflow editor.
8. Now we can create a new job using this workflow, as we did in the previous
section.

### Running other Python-based Machine Learning Models

If you want to run other Python-based Machine Learning Models, you can create a
new workflow and use the same approach. In this case, select default "Python"
flavor/<wbr/>template, add python dependencies to the "requirements.txt" tab,
and write your Python script to the "script.py" tab.

![General Python template](../../images/tutorials/mattersim/general-py-template.webp "General Python template")

If your model can use multi-threading, you can specify necessary environment
variables on top of your python script.

```python title="SCRIPT.PY"
import os

# set number of CPUs to run on
ncore = "2"

# set env variables
# have to set these before importing numpy or others
os.environ["OMP_NUM_THREADS"] = ncore
os.environ["OPENBLAS_NUM_THREADS"] = ncore
os.environ["MKL_NUM_THREADS"] = ncore
os.environ["VECLIB_MAXIMUM_THREADS"] = ncore
os.environ["NUMEXPR_NUM_THREADS"] = ncore
```

## Step-by-step Video Tutorial

In the below animation, we walk you through the whole process.

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/DBW3KjdtRyc?controls=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

!!!info "Shared virtual environment"
    Python virtual environments are shared across different jobs, and users. As
    long as the content (hash/fingerprint) of the requirements.txt file is the
    same, the virtual environment will be reused. So a job might take longer
    to complete for the first time, but subsequent runs will be faster as there
    is no pip install required. If you are not getting the expected versions of
    your dependencies, you can try to update the requirements.txt file with
    exact versions of your dependencies.

## References

- [MatterSim GitHub repository](https://github.com/microsoft/mattersim)
- [MatterSim documentation](https://microsoft.github.io/mattersim/)

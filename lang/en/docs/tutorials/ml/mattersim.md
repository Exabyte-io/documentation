# Running MatterSim and other Python-based Machine Learning Models

This tutorial walks through running [MatterSim](https://github.com/microsoft/mattersim)
and other Python-based machine learning models on the Mat3ra platform. We cover
three approaches, in order of increasing customization:

1. Using an existing workflow from the Mat3ra bank.
2. Creating a new workflow and choosing one of the available MatterSim
flavors/<wbr/>templates.
3. Using the general Python template and specifying all necessary dependencies
in `requirements.txt`.

We then describe how to run jobs on GPU and how to take advantage of
multi-threading, and finish with a step-by-step video tutorial.


## 1. Using a bank workflow

### 1.1. Copy bank workflow

The easiest way to run MatterSim calculations is to import a ready-made workflow
from the Mat3ra bank into your account.

1. Navigate to the workflows bank from the left sidebar.
2. Search for "MatterSim" and click "Copy" in the action column on the workflow
you want to use (e.g. "MatterSim total energy").
![Copy bank workflow](../../images/tutorials/mattersim/mattersim-bank-workflow.webp "Copy bank workflow")
3. The workflow now appears in your own workflows list and is available for
selection in the job creation process.
4. Open the workflow to inspect or further modify it. The "MatterSim total
energy" workflow consists of three units:
    - I/O Material unit: fetches the input materials from the job context. Its
    output is an array of materials.
    - Assignment unit: takes the first item of that array and assigns it to a
    new global variable named `MATERIAL`.
    - MatterSim unit: builds an ASE material definition from `MATERIAL` and
    runs MatterSim to predict total energy, stress, and other properties.

    Beside the main `script.py`, the MatterSim unit also exposes a `utils.py`
    helper script and a `requirements.txt` file. Add any additional Python
    packages your script requires to the `requirements.txt`.

![MatterSim workflow units](../../images/tutorials/mattersim/mattersim-workflow.webp "MatterSim workflow units")

### 1.2. Create and submit a job

1. Navigate to the jobs designer page from the left sidebar and click "Create
New Job". The page is organized in three sections: material, workflow, and
compute parameters.
2. In "Select Job Actions", pick the material and the workflow:
    - Material: any structure works. The default Silicon is fine; the video
    tutorial below uses a nickel slab.
    - Workflow: the "MatterSim total energy" workflow you just imported.
3. Optionally, rename the job (e.g. "MatterSim total energy") and adjust the
compute parameters under the "Compute" section — cluster, queue, number of
processors, time limit, etc.
4. Save and exit the job designer.
![MatterSim job creation](../../images/tutorials/mattersim/mattersim-job.webp "MatterSim job creation")
5. Click "Run" in the "Actions" column to submit the job.
6. Once the job completes, open the job viewer page:
    - The "Results" tab shows a summary of the predicted output properties.
    - The "Workflow" tab → MatterSim unit exposes the standard output (raw
    log).
    - The "Files" tab lists every input and output file for preview or
    download.

![MatterSim total energy results](../../images/tutorials/mattersim/mattersim-results-total-energy.webp "MatterSim total energy results")


## 2. Creating a new workflow

When the workflow you need is not available in the bank, build one from an
existing MatterSim flavor/<wbr/>template. The example below creates a *cell
relaxation* workflow from scratch.

1. Navigate to the workflows page and click "Create" new workflow.
2. Expand the "Details" section and select "Python Script" as application.
3. Add an "Executable" unit and click the "EDIT" unit button.
![MatterSim add unit](../../images/tutorials/mattersim/mattersim-add-unit.webp "MatterSim add unit")
4. Expand the "Details" section and select `mlff:mattersim:cell_relaxation` as
the flavor.
![MatterSim edit unit](../../images/tutorials/mattersim/mattersim-edit-unit.webp "MatterSim edit unit")
5. Scroll down and edit the Python script if necessary. For example, to use
ASE to build the input material directly (instead of pulling it from the job
context), replace the material section with:

    ```python title="SCRIPT.PY"
    ...
    from ase.build import bulk
    ase_atoms = bulk("GaN", "wurtzite", a=3.189, c=5.185)
    ...
    ```

6. Close the unit modal by clicking the "X" button in the top right.
7. Save and exit the workflow editor.
8. Create and run a job using this workflow as we did in the previous section.

![MatterSim cell relaxation results](../../images/tutorials/mattersim/mattersim-results-cell-relaxation.webp "MatterSim cell relaxation results")

When the job completes, the "Results" tab shows a side-by-side comparison of
the initial and relaxed structures, and the "Files" tab contains both
structures in `.cif` and `.poscar` formats.


## 3. Using the general Python template

To run any Python-based ML model that is not covered by an existing workflow
or flavor, use the general Python template:

1. Create a new workflow as in the previous section, and select the default
"Python" flavor/<wbr/>template.
2. Add your dependencies in the "requirements.txt" tab.
3. Write your code in the "script.py" tab.

![General Python template](../../images/tutorials/mattersim/general-py-template.webp "General Python template")

As long as the model is Python-based and its dependencies can be installed via
pip, it will run on the Mat3ra platform.

!!!info "Shared virtual environment"
    Python virtual environments are shared across different jobs and users. As
    long as the content (hash/fingerprint) of `requirements.txt` is the same,
    the virtual environment will be reused. The first job may take longer to
    complete because of `pip install`, but subsequent runs start faster as no
    install is required. If you are not getting the expected versions of your
    dependencies, pin them explicitly in `requirements.txt`.

!!!tip "Multi-threading"
    If your model can use multi-threading, set the necessary environment
    variables at the top of your script, before importing NumPy or any other
    library that utilizes multi-threading.

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


## 4. Running on GPU

To run a MatterSim job on GPU, submit it to one of the platform's GPU queues.
For example, the video tutorial below uses the "MatterSim phonon dispersion"
bank workflow on Google Cloud (Cluster-001) under the "GOF" queue.

To verify that the job actually runs on GPU, add a debug print to your script
and check the standard output under the "Files" tab once the job completes:

```python title="SCRIPT.PY"
import torch

print("Using GPU:", torch.cuda.is_available())
```

When the run succeeds, the "Results" tab shows the phonon dispersion and the
phonon density-of-states plots.


![MatterSim phonon dispersion results](../../images/tutorials/mattersim/mattersim-results-phonon.webp "MatterSim phonon dispersion results")

## 5. Step-by-step Video Tutorial

The animation below walks through the entire flow on the platform end-to-end.

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/DBW3KjdtRyc?controls=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


## 6. References

- [MatterSim GitHub repository](https://github.com/microsoft/mattersim)
- [MatterSim documentation](https://microsoft.github.io/mattersim/)

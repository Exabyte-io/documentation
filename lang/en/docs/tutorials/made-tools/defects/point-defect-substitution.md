# Create Nitrogen Defects in Graphene

This tutorial demonstrates the process of creating materials with substitution defects, based on the research presented in:
<h3>Formation, stabilities, and electronic properties of nitrogen defects in graphene </h3>
Yoshitaka Fujimoto and Susumu Saito

Physical Review B, 2011. 

The paper is available [here](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.84.245446).


## Procedure overview

In this tutorial we will focus on replicating the material from FIG. 1. b) of the paper: 

<img src="/images/tutorials/made-tools/defects/point_defect_substitution/point_defect_substitution_0.webp" title="FIG. 1. a)">

- Open Materials Designer and import Graphene material from [Standata](../../../materials-designer/header-menu/input-output/standata-import.md).
- Create supercell of Graphene.
- Get coordinates of the atoms to replace via 3D editor.
- Launch [JupyterLite Session](../../../jupyterlite/overview.md) and open the `create_point_defect.ipynb` notebook.
- Configure defect settings 
- Run the notebook to create the material with defects.
- Analyze the results and save the material.

## Step 1: Import Graphene Material

Import Graphene material from Standata by following the steps in the [Import from Standata](../../../materials-designer/header-menu/input-output/standata-import.md) tutorial.

## Step 2: Create Supercell

Create a [5,5,1] supercell of Graphene by following the steps in the [Create Supercell](../../../materials-designer/header-menu/advanced/supercell.md) tutorial.

## Step 3: Get Coordinates of Atoms to Replace

Open the [3D editor](../../../materials-designer/3d-editor/edit.md) and get the coordinates of the atoms to replace.

## Step 4: Launch JupyterLite Session

Use the existing `create_point_defect.ipynb` notebook and modify the parameters by adding multiple defects dictionaries list using the approximate coordinates of the atoms to replace.

If `MULTIPLE_DEFECTS` list is not empty, the notebook will create multiple defects in the material ignoring the single defect parameters.

Adjust the "1.1. Set up defect parameters" cell in the notebook as follows:

```python
DEFECT_TYPE = "substitution"
SITE_ID = None # `from_site_id` method will be ignored
COORDINATE = None # default method will be ignored
APPROXIMATE_COORDINATE = None   
CHEMICAL_ELEMENT = "N"
SUPERCELL_MATRIX = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

MULTIPLE_DEFECTS = [
    {
        "defect_type": "substitution",
        "approximate_coordinate": [0.51, 0.5, 0.5],
        "chemical_element": CHEMICAL_ELEMENT
    },
    {
        "defect_type": "substitution",
        "approximate_coordinate": [0.5, 0.75, 0.5],
        "chemical_element": CHEMICAL_ELEMENT
    },
    {
        "defect_type": "substitution",
        "approximate_coordinate": [0.25, 0.5, 0.5],
        "chemical_element": CHEMICAL_ELEMENT
    },
    {
        "defect_type": "vacancy",
        "approximate_coordinate": [0.5, 0.5, 0.5]
    }
]
```

## 5. Run the Notebook

Run the notebook by clicking `Run` > `Run All` in the top menu to run cells and wait for the results to appear.

## 6. Analyze the Results

After running the notebook, the user will be able to visualize the structure of Graphene with substitution defects.

For the single substitution defect, the user will see the following structure:
<img src="/images/tutorials/made-tools/defects/point_defect_substitution/point_defect_substitution_1.webp" title="Graphene with substitution defects">

For the multiple substitution and vacancy defects, the user will see the following structure:
<img src="/images/tutorials/made-tools/defects/point_defect_substitution/point_defect_substitution_2.webp" title="Graphene with multiple substitution and vacancy defects">

## 7. Save the Material

The user can pass the material with substitution defects in the current Materials Designer environment and save it.

Or the user can [save or download](../../../materials-designer/header-menu/input-output.md) the material in Material JSON format or POSCAR format.

## Interactive JupyterLite Notebook

{% with notebook_name='create_point_defect.ipynb' %}
{% include 'includes/jupyterlite_embed.html' %}
{% endwith %}
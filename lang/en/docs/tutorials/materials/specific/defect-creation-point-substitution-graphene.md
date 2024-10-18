---
# YAML header
render_macros: true
---

# Substitutional Point Defects in Graphene

## Introduction

This tutorial demonstrates the process of creating materials with substitution defects, based on the work presented in the following manuscript, where nitrogen defects in graphene are studied.

[//]: # (<embed src="https://journals.aps.org/prb/abstract/10.1103/PhysRevB.84.245446" width="100%" height="300">)

!!!note "Reference"
    Yoshitaka Fujimoto and Susumu Saito, "Formation, stabilities, and electronic properties of nitrogen defects in graphene", Physical Review B, 2011. [DOI: 10.1103/PhysRevB.84.245446](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.84.245446){:target='_blank'}.

We use the [Materials Designer](../../../materials-designer/overview.md) to create a supercell of graphene, identify the crystal site positions for defects, and introduce nitrogen atoms and vacancies accordingly.

We will focus on creating graphene-nitrogen structures from FIG. 1.
Specifically, the material from FIG. 1. b) of the paper: 


![Point Defect, Substitution, 0](/images/tutorials/materials/defects/defect_creation_point_substitution_graphene/0-figure-from-manuscript.png "Point Defect, Substitution, FIG. 1. b)")


## 1. Create Graphene Supercell

First, we navigate to [Materials Designer](../../../materials-designer/overview.md) and import the graphene material from the [Standata](../../../materials-designer/header-menu/input-output/standata-import.md).

![Standata Graphene Import](/images/tutorials/materials/defects/defect_creation_point_substitution_graphene/1-standata-graphene.png "Standata Graphene Import")

We then use the [Advanced](../../../materials-designer/header-menu/advanced/supercell.md) menu to create a supercell of graphene with a size of 4x4x1.

![Supercell Creation for Graphene](/images/tutorials/materials/defects/defect_creation_point_substitution_graphene/2-advanced-supercell.png "Supercell Graphene")

## 2. Identify Defect Sites

Next, we open the [3D editor](../../../materials-designer/3d-editor.md) to identify the crystal site positions for the defects.

![3D Editor](/images/tutorials/materials/defects/defect_creation_point_substitution_graphene/4-threejs-editor-coordinates.png "3D Editor")

Hover over the atoms to get the coordinates of the atoms to replace. Then copy/paste these coordinates into a text file for later use.

## 3. Create Nitrogen Defects and Vacancies

For the defect creation, we will use the [JupyterLite](../../../jupyterlite/overview.md) environment with the corresponding notebook.

### 3.1. Launch JupyterLite Session

Select the [JupyterLite Transformation](../../../materials-designer/header-menu/advanced/jupyterlite-dialog.md) menu item to launch the JupyterLite environment.

![JupyterLite Dialog](/images/materials-designer/jupyterlite_dialog/open-jupyterlite-dialog.webp)

### 3.2. Open `create_point_defect.ipynb` notebook

Find `create_point_defect.ipynb` in the list of notebooks and click/double-click open it.

### 3.3. Open and modify the notebook

Edit `create_point_defect.ipynb` notebook to modify the parameters by adding a list of [defect configuration objects](LINK_TO_MADE_TOOLS_README) containing the approximate coordinates of the atoms to replace.

Adjust the "1.1. Set up defect parameters" cell in the notebook as follows:

```python
DEFECT_TYPE = "substitution"
SITE_ID = None # `from_site_id` method will be ignored
COORDINATE = None # default method will be ignored
APPROXIMATE_COORDINATE = None   
CHEMICAL_ELEMENT = "N"
SUPERCELL_MATRIX = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
USE_CARTESIAN_COORDINATES = True

DEFECT_CONFIGS = [
    {
        "defect_type": "substitution",
        "approximate_coordinate": [4.9, 2.85, 10],
        "chemical_element": CHEMICAL_ELEMENT,
        "use_cartesian_coordinates": USE_CARTESIAN_COORDINATES
    },
      {
        "defect_type": "substitution",
        "approximate_coordinate": [3.7, 4.9, 10],
        "chemical_element": CHEMICAL_ELEMENT,
        "use_cartesian_coordinates": USE_CARTESIAN_COORDINATES
    },
      {
        "defect_type": "substitution",
        "approximate_coordinate": [2.45, 2.85, 10],
        "chemical_element": CHEMICAL_ELEMENT,
        "use_cartesian_coordinates": USE_CARTESIAN_COORDINATES
    },
      {
        "defect_type": "vacancy",
        "approximate_coordinate": [3.7, 3.55, 10],
        "use_cartesian_coordinates": USE_CARTESIAN_COORDINATES
    },
]  
```

![Notebook setup](/images/tutorials/materials/defects/defect_creation_point_substitution_graphene/5-jl-setup.png "Notebook setup")

## 5. Run the Notebook

Run the notebook by clicking `Run` > `Run All` in the top menu to run cells and wait for the results to appear.

![Run All](/images/jupyterlite/run-all.png "Run All")

## 6. Analyze the Results

After running the notebook, the user will be able to visualize the structure of Graphene with substitution defects.

![Review the Results](/images/tutorials/materials/defects/defect_creation_point_substitution_graphene/6-jl-result-preview.png "Review the Results")

## 7. Pass the Material to Materials Designer

The user can pass the material with substitution defects in the current Materials Designer environment and save it.

![Final Material](/images/tutorials/materials/defects/defect_creation_point_substitution_graphene/7-wave-result.png "N-doped Graphene")

Or the user can [save or download](../../../materials-designer/header-menu/input-output.md) the material in Material JSON format or POSCAR format.


## Interactive JupyterLite Notebook

The following JupyterLite notebook demonstrates the process of creating materials with substitution defects in graphene.


{% with origin_url=config.extra.jupyterlite.origin_url %}
{% with notebooks_path_root=config.extra.jupyterlite.notebooks_path_root %}
{% with notebook_name='specific_examples/defect_creation_point_substitution_graphene.ipynb' %}
{% include 'jupyterlite_embed.html' %}
{% endwith %}
{% endwith %}
{% endwith %}

## Tags

`defects`, `graphene`, `substitutional`, `point-defects`, `nitrogen`
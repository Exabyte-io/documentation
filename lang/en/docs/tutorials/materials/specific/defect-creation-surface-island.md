---
# YAML header
render_macros: true
---

# TiN/TiN(001) Islands

## Introduction

This tutorial demonstrates the process of creating material with island on the surface of TiN(001) based on the work presented in the following manuscript.

[//]: # (<embed src="https://journals.aps.org/prb/abstract/10.1103/PhysRevB.97.035406" width="100%" height="300">)

!!!note "Reference"
    **D. G. Sangiovanni, A. B. Mei, D. Edström, L. Hultman, V. Chirita, I. Petrov, and J. E. Greene**, "Effects of surface vibrations on interlayer mass transport: Ab initio molecular dynamics investigation of Ti adatom descent pathways and rates from TiN/TiN(001) islands", Physical Review B, 2018. [DOI: 10.1103/PhysRevB.97.035406](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.97.035406){:target='_blank'}.

We use the [Materials Designer](../../../materials-designer/overview.md) to create a slab of TiN, identify the cartesian coordinates for an island on the surface, and build it. 

We will focus on creating graphene-nitrogen structures from FIG. 2.
Specifically, the material from FIG. 2. a) of the paper: 


![Surface Defect](/images/tutorials/materials/defects/defect_creation_surface_island/0.png "Surface Defect, Island FIG. 2. a)")


## 1. Create TiN Slab

First, we navigate to [Materials Designer](../../../materials-designer/overview.md) and import the graphene material from the [Standata](../../../materials-designer/header-menu/input-output/standata-import.md).

![Standata Graphene Import](/images/tutorials/materials/defects/defect_creation_point_substitution_graphene/1-standata-graphene.webp "Standata Graphene Import")


Then we will use the [JupyterLite](../../../jupyterlite/overview.md) environment to create a TiN slab.

### 1.1. Launch JupyterLite Session

Select the "Advanced > [JupyterLite Transformation](../../../materials-designer/header-menu/advanced/jupyterlite-dialog.md)" menu item to launch the JupyterLite environment.

![JupyterLite Dialog](/images/jupyterlite/md-advanced-jl.webp "JupyterLite Dialog")

### 1.2. Open `create_slab.ipynb` notebook

Find `create_slab.ipynb` in the list of notebooks and click/double-click open it.

### 1.3. Open and modify the notebook

Next, edit `create_slab.ipynb` notebook to modify the parameters by adding the following content to the "1.1. Set up slab parameters" cell in the notebook:

```python
# Enable interactive selection of terminations via UI prompt
IS_TERMINATIONS_SELECTION_INTERACTIVE = False 

MILLER_INDICES = (0, 0, 1)
THICKNESS = 3  # in atomic layers
VACUUM = 10.0  # in angstroms
XY_SUPERCELL_MATRIX = [[9, 0], [0, 9]]
USE_ORTHOGONAL_Z = True
USE_CONVENTIONAL_CELL = True

# Index of the termination pair to be selected
TERMINATION_INDEX = 0
```

### 1.4. Run the Notebook

Run the notebook by clicking `Run` > `Run All` in the top menu to run cells and wait for the results to appear.

![Run All](/images/jupyterlite/run-all.webp "Run All")

### 1.5. Pass the Slab to Materials Designer

After running the notebook, the user will be able to visualize the created TiN slab.

![Review the Results](/images/tutorials/materials/defects/defect_creation_surface_island/1.png "Review the Results")

The user can pass the resulting material to the current Materials Designer environment for further analysis.


## 2. Identify Island vertices coordinates

Next, we open the [3D editor](../../../materials-designer/3d-editor.md) to identify the cartesian coordinates for the island vertices.

![3D Editor](/images/tutorials/materials/defects/defect_creation_point_substitution_graphene/4-threejs-editor-coordinates.webp "3D Editor")

Click on the atoms to get the coordinates on the surface. Then copy/paste these coordinates into a text file for later use.

## 3. Create Island on the Surface

For the defect creation, we will use the [JupyterLite](../../../jupyterlite/overview.md) environment with the corresponding notebook.

### 3.1. Launch JupyterLite Session

Select the "Advanced > [JupyterLite Transformation](../../../materials-designer/header-menu/advanced/jupyterlite-dialog.md)" menu item to launch the JupyterLite environment.

![JupyterLite Dialog](/images/jupyterlite/md-advanced-jl.webp "JupyterLite Dialog")

### 3.2. Open `create_point_defect.ipynb` notebook

Find `create_island_defect.ipynb` in the list of notebooks and click/double-click open it.

### 3.3. Open and modify the notebook

Next, edit `create_island_defect.ipynb` notebook to modify the parameters by adding a list of [defect configuration objects](https://github.com/Exabyte-io/made/blob/3d938b4d91a31323dca7a02acb12b646dbb26634/src/py/mat3ra/made/tools/build/defect/configuration.py#L191) containing the cartesian coordinates of the island vertices.

Copy the below content and edit the "1.1. Set up defect parameters" cell in the notebook as follows:

```python
ISLAND_SHAPE = 'box'
AUTO_ADD_VACUUM = True
VACUUM_THICKNESS = 10.0
NUMBER_OF_ADDED_LAYERS = 0.5

BOX_PARAMS = {
    'min_coordinate': [0.25, 0.3, 0],
    'max_coordinate': [0.75, 0.8, 1],
    "use_cartesian_coordinates": False
}

```

Here's the visual of the updated content:

![Notebook setup](/images/tutorials/materials/defects/defect_creation_point_substitution_graphene/5-jl-setup.webp "Notebook setup")

## 5. Run the Notebook

Run the notebook by clicking `Run` > `Run All` in the top menu to run cells and wait for the results to appear.

![Run All](/images/jupyterlite/run-all.webp "Run All")

## 6. Analyze the Results

After running the notebook, the user will be able to visualize the created material with the island on the surface.

![Review the Results](/images/tutorials/materials/defects/defect_creation_point_substitution_graphene/6-jl-result-preview.webp "Review the Results")

## 7. Pass the Material to Materials Designer

The user can pass the resulting material to the current Materials Designer environment and save it.

![Final Material](/images/tutorials/materials/defects/defect_creation_point_substitution_graphene/7-wave-result.webp "N-doped Graphene")

Or the user can [save or download](../../../materials-designer/header-menu/input-output.md) the material in Material JSON format or POSCAR format.


## Interactive JupyterLite Notebook

The following JupyterLite notebook demonstrates the process of creating material with island. Select "Run" > "Run All Cells".

{% with origin_url=config.extra.jupyterlite.origin_url %}
{% with notebooks_path_root=config.extra.jupyterlite.notebooks_path_root %}
{% with notebook_name='specific_examples/defect_creation_island.ipynb' %}
{% include 'jupyterlite_embed.html' %}
{% endwith %}
{% endwith %}
{% endwith %}

<!--
{# TODO: Update the origin_url
    {% with origin_url="https://jupyterlite.mat3ra.com/retro/notebooks/?path=api-examples/other/materials_designer/specific_examples/defect_creation_island.ipynb" %}
    {% include 'jupyterlite_embed.html' %}
    {% endwith %}
#}
-->

## Tags

`defects`, `island`, `surface`, `surface-defects`, `TiN`, `nitrogen`, `titanium`

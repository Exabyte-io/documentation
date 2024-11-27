---
# YAML header
render_macros: true
---

# Nitrogen vacancy and Mg substitution in GaN

## Introduction

This tutorial demonstrates the process of creating material with nitrogen vacancies and magnesium substitution defects in GaN.


!!!note "Manuscript"
    **Giacomo Miceli, Alfredo Pasquarello**,
    "Self-compensation due to point defects in Mg-doped GaN", Physical Review B, 2016.
    [DOI: 10.1103/PhysRevB.93.165207](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.93.165207){:target='_blank'}.

We use the [Materials Designer](../../../materials-designer/overview.md) to create a supercell of GaN, identify the crystal site positions for defects, and introduce nitrogen atoms and vacancies accordingly.

We will focus on creating GaN-nitrogen structures from FIG. 1.
Specifically, the material from FIG. 2. c) of the manuscript: 


![Point Pair Defects: Mg Substitution and Vacancy in GaN](/images/tutorials/materials/defects/defect_point_pair_gallium_nitride/0-figure-from-manuscript.webp "Point Defect Pair: Substitution, Vacancy in GaN, FIG. 2.")


## 1. Create GaN Supercell

First, we navigate to [Materials Designer](../../../materials-designer/overview.md) and import the GaN material from the [Standata](../../../materials-designer/header-menu/input-output/standata-import.md).

![Standata GaN Import](/images/tutorials/materials/defects/defect_point_pair_gallium_nitride/1-standata-GaN.webp "Standata GaN Import")

We then use the [Advanced](../../../materials-designer/header-menu/advanced/supercell.md) menu to create a supercell of GaN with a size of 4x4x1.

![Supercell Creation for GaN](/images/tutorials/materials/defects/defect_point_pair_gallium_nitride/2-advanced-supercell.webp "Supercell GaN")

## 2. Identify Defect Sites

Next, we open the [3D editor](../../../materials-designer/3d-editor.md) to identify the crystal site positions for the defects.

![3D Editor](/images/tutorials/materials/defects/defect_point_pair_gallium_nitride/4-threejs-editor-coordinates.webp "3D Editor")

Hover over the atoms to get the coordinates of the atoms to replace. Then copy/paste these coordinates into a text file for later use.

`[1.608, 4.642, 5.240]` for the Mg substitution defect and `[1.608, 4.642, 7.210]` for the nitrogen vacancy.

## 3. Create Nitrogen Defects and Vacancies

For the defect creation, we will use the [JupyterLite](../../../jupyterlite/overview.md) environment with the corresponding notebook.

### 3.1. Launch JupyterLite Session

Select the "Advanced > [JupyterLite Transformation](../../../materials-designer/header-menu/advanced/jupyterlite-dialog.md)" menu item to launch the JupyterLite environment.

![JupyterLite Dialog](/images/jupyterlite/md-advanced-jl.webp "JupyterLite Dialog")

### 3.2. Open `create_point_defect_pair.ipynb` notebook

Find `create_point_defect_pair.ipynb` in the list of notebooks and click/double-click open it.

### 3.3. Open and modify the notebook

Next, edit `create_point_defect_pair.ipynb` notebook to modify the parameters by adding a list of [defect configuration objects](https://github.com/Exabyte-io/made/blob/3d938b4d91a31323dca7a02acb12b646dbb26634/src/py/mat3ra/made/tools/build/defect/configuration.py#L257) containing the approximate coordinates of the atoms to replace.

Copy the below content and edit the "1.1. Set up defect parameters" cell in the notebook as follows:

```python
SUPERCELL_MATRIX = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

# List of dictionaries with defect parameters
PRIMARY_DEFECT_CONFIG = {
    "defect_type": "substitution",
    "approximate_coordinate": [1.608, 4.642, 5.240],
    "chemical_element": "Mg",
    "use_cartesian_coordinates": True,
}

SECONDARY_DEFECT_CONFIG = {
    "defect_type": "vacancy",
    "approximate_coordinate": [1.608, 4.642, 7.210],
    "use_cartesian_coordinates": True,
}
```

Here's the visual of the updated content:

![Notebook setup](/images/tutorials/materials/defects/defect_point_pair_gallium_nitride/5-jl-setup.webp "Notebook setup")

## 4. Run the Notebook

Run the notebook by clicking `Run` > `Run All` in the top menu to run cells and wait for the results to appear.

![Run All](/images/jupyterlite/run-all.webp "Run All")

## 5. Analyze the Results

After running the notebook, the user will be able to visualize the structure of GaN with substitution and vacancy defects.

![Review the Results](/images/tutorials/materials/defects/defect_point_pair_gallium_nitride/6-jl-result-preview.webp "Review the Results")

## 6. Pass the Material to Materials Designer

The user can pass the resulting material in the current Materials Designer environment and save it.

![Final Material](/images/tutorials/materials/defects/defect_point_pair_gallium_nitride/7-wave-result.webp "Vacancy and Mg Substitution in GaN")

Or the user can [save or download](../../../materials-designer/header-menu/input-output.md) the material in Material JSON format or POSCAR format.


## Interactive JupyterLite Notebook

The following JupyterLite notebook demonstrates the process of creating materials with substitution defects in GaN. Select "Run" > "Run All Cells".

{% with origin_url=config.extra.jupyterlite.origin_url %}
{% with notebooks_path_root=config.extra.jupyterlite.notebooks_path_root %}
{% with notebook_name='specific_examples/defect_point_substitution_gallium_nitride.ipynb' %}
{% include 'jupyterlite_embed.html' %}
{% endwith %}
{% endwith %}
{% endwith %}

## References

1. **Giacomo Miceli, Alfredo Pasquarello**,
   "Self-compensation due to point defects in Mg-doped GaN", Physical Review B, 2016.
   [DOI: 10.1103/PhysRevB.93.165207](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.93.165207){:target='_blank'}.

## Tags

`defects`, `impurities`, `doped-semiconductors`, `substitutional`, `point-defects`, `nitrogen`, `GaN`

---
# YAML header
render_macros: true
---

# Vacancy Point Defects in Hexagonal Boron Nitride

## Introduction

This tutorial demonstrates the process of creating materials with vacancy point defects, based on the work presented in the following manuscript:

!!!note "Manuscript"
    Fabian Bertoldo, Sajid Ali, Simone Manti & Kristian S. Thygesen, "Quantum point defects in 2D materials - the QPOD database", Nature, 2022. [DOI:10.1038/s41524-022-00730-w](https://doi.org/10.1038/s41524-022-00730-w){:target='_blank'}.

We use the [Materials Designer](../../../materials-designer/overview.md) and JupyterLite environment to create a nanoribbon of hexagonal boron nitride (hBN) and introduce vacancy defects. The process combines the capabilities of nanoribbon creation and point defect introduction.

We will focus on creating a structure similar to Figure 1 from the manuscript, which demonstrates boron vacancy defects in hexagonal boron nitride:

![Vacancy in hBN](/images/tutorials/materials/defects/defect_point_vacancy_boron_nitride/0-figure-from-manuscript.webp "Vacancy in hBN")

## 1. Import Base Material

First, we need to import the hexagonal boron nitride (hBN) material from the Standata database.

### 1.1. Open Materials Designer

Navigate to [Materials Designer](../../../materials-designer/overview.md) and click on the "Input/Output" menu.

### 1.2. Import from Standata

1. Select "Import from Standata" in the Input/Output menu
2. In the search box, enter "Boron_Nitride"
3. Select the 2D category
4. Click on the hBN material to import it

![Standata hBN Import](/images/tutorials/materials/defects/defect_point_vacancy_boron_nitride/1-standata-hbn.webp "Standata hBN Import")

### 1.3. Preview the Material

After importing, user can preview the material in the 3D editor:

![3D Preview of hBN](/images/tutorials/materials/defects/defect_point_vacancy_boron_nitride/2-3d-preview.webp "3D Preview of hBN")

## 2. Create hBN Nanoribbon

Next, we'll create a nanoribbon structure using the JupyterLite environment.

### 2.1. Launch JupyterLite Session

Select the "Advanced > [JupyterLite Transformation](../../../materials-designer/header-menu/advanced/jupyterlite-dialog.md)" menu item to launch the JupyterLite environment.

![JupyterLite Dialog](/images/jupyterlite/md-advanced-jl.webp "JupyterLite Dialog")

### 2.2. Open and Configure Nanoribbon Notebook

Find and open `create_nanoribbon.ipynb` in the list of notebooks. Edit the nanoribbon parameters in section 1.1 of the notebook:

```python
WIDTH = 8  # in number of atoms
LENGTH = 14  # in number of atoms
VACUUM_WIDTH = 0 
VACUUM_LENGTH = 0
EDGE_TYPE = "zigzag"  # "zigzag" or "armchair"
```

### 2.3. Run the Notebook

Run the notebook by clicking `Run` > `Run All` in the top menu. This will create a nanoribbon structure from the imported hBN material.

### 2.4. Review Nanoribbon in Materials Designer

After the notebook completes:

1. The nanoribbon structure will be passed back to Materials Designer
2. User can view the structure in the 3D editor
3. Verify the nanoribbon dimensions and edge type

![Nanoribbon Preview](/images/tutorials/materials/defects/defect_point_vacancy_boron_nitride/3-nanoribbon-preview.webp "Nanoribbon Preview")


## 3. Create the Vacancy Defect

After creating the nanoribbon, we'll introduce the vacancy defect using the point defect notebook.

### 3.1. Open Point Defect Notebook

Open `create_point_defect.ipynb` and modify the defect configuration parameters:

```python
DEFECT_CONFIGS = [
    {
        "defect_type": "vacancy",
        "approximate_coordinate": [0.5, 0.5, 0.5],
        "use_cartesian_coordinates": False
    }
]
```

The configuration specifies:

- `defect_type`: "vacancy" for removing an atom
- `approximate_coordinate`: Position in crystal coordinates where the vacancy will be created
- `use_cartesian_coordinates`: False to use fractional coordinates

### 3.2. Run the Notebook

Click `Run` > `Run All` in the top menu for each notebook and wait for the results.

## 4. Save the Material


After running both notebooks, user can visualize the structure of hBN with the vacancy defect in the Materials Designer 3D viewer.

![Review the Results](/images/tutorials/materials/defects/defect_point_vacancy_boron_nitride/1-result-preview.webp "Review the Results")

[Save or download](../../../materials-designer/header-menu/input-output.md) in Material JSON format

## Interactive JupyterLite Notebook

The following JupyterLite notebooks demonstrate the complete process. Select "Run" > "Run All Cells".

{% with origin_url=config.extra.jupyterlite.origin_url %}
{% with notebooks_path_root=config.extra.jupyterlite.notebooks_path_root %}
{% with notebook_name='specific_examples/defect_point_vacancy_boron_nitride.ipynb' %}
{% include 'jupyterlite_embed.html' %}
{% endwith %}
{% endwith %}
{% endwith %}

## References

1. Fabian Bertoldo, Sajid Ali, Simone Manti & Kristian S. Thygesen, "Quantum point defects in 2D materials - the QPOD database", Nature, 2022. [DOI:10.1038/s41524-022-00730-w](https://doi.org/10.1038/s41524-022-00730-w){:target='_blank'}.

## Tags

`defects`, `vacancy`, `point-defects`, `hBN`, `boron-nitride`, `2D-materials`
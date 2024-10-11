# Substitutional Point Defects in Graphene

## 0. Introduction

This tutorial demonstrates the process of creating materials with substitution defects, based on the work presented in the following manuscript, where nitrogen defects in graphene are studied.

[//]: # (<embed src="https://journals.aps.org/prb/abstract/10.1103/PhysRevB.84.245446" width="100%" height="300">)

!!!note "Reference"
    Yoshitaka Fujimoto and Susumu Saito, "Formation, stabilities, and electronic properties of nitrogen defects in graphene", Physical Review B, 2011. [DOI: 10.1103/PhysRevB.84.245446](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.84.245446){:target='_blank'}.

We use the [Materials Designer](LINK) to create a supercell of graphene, identify the crystal site positions for defects, and introduce nitrogen atoms and vacancies accordingly.

We will focus on creating graphene-nitrogen structures from FIG. 1.
Specifically, the material from FIG. 1. b) of the paper: 

![FIG](../../../images/data-in-objectstorage/dropbox-page.png "FIG")

[//]: # (![Point Defect, Substitution, 0]&#40;../../../images/tutorials/made-tools/defects/point_defect_substitution/point_defect_substitution_0.webp "Point Defect, Substitution, 0"&#41;)

and the material from FIG. 1. a).:

![FIG](../../../images/data-in-objectstorage/dropbox-page.png "FIG")


## 1. Create Graphene Supercell

First, we navigate to [Materials Designer](LINK) and import the graphene material from the [Standata](LINK).

![FIG](../../../images/data-in-objectstorage/dropbox-page.png "FIG")

We then use the [Advanced](LINK) menu to create a supercell of graphene with a size of 5x5x1.

![FIG](../../../images/data-in-objectstorage/dropbox-page.png "FIG")

## 2. Identify Defect Sites

Next, we open the [3D editor](LINK) to identify the crystal site positions for the defects.

![FIG](../../../images/data-in-objectstorage/dropbox-page.png "FIG")

Hover over the atoms to get the coordinates of the atoms to replace. Then copy/paste these coordinates into a text file for later use.

## 3. Create Nitrogen Defects and Vacancies

For the defect creation, we will use the [JupyterLite](LINK) environment with the corresponding notebook.

## 3.1. Launch JupyterLite Session

Select the [JupyterLite Transformation](LINK) menu item to launch the JupyterLite environment.

![FIG](../../../images/data-in-objectstorage/dropbox-page.png "FIG")

## 3.2. Open `create_point_defect.ipynb` notebook

Find `create_point_defect.ipynb` in the list of notebooks and click/double-click open it.

## 3.3. Open and modify the notebook

Edit `create_point_defect.ipynb` notebook to modify the parameters by adding a list of [defect configuration objects](LINK_TO_MADE_TOOLS_README) containing the approximate coordinates of the atoms to replace.

[//]: # (TODO: update the notebook to only have DEFECT_CONFIG_OBJECTS)

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

![FIG](../../../images/data-in-objectstorage/dropbox-page.png "FIG")

## 6. Analyze the Results

After running the notebook, the user will be able to visualize the structure of Graphene with substitution defects.

![FIG](../../../images/data-in-objectstorage/dropbox-page.png "FIG")

## Tags

`defects`, `graphene`, `substitutional`, `point-defects`, `nitrogen`
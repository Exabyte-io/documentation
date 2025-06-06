---
tags:
  - 2d-materials
  - layers
  - bilayer
  - twisted
  - commensurate
  - molybdenum
  - disulfide

hide:
  - tags
# YAML header
render_macros: true
---

# Twisted Bilayer Molybdenum Disulfide Structure Creation.

## Introduction.

This tutorial demonstrates the process of creating a twisted bilayer molybdenum disulfide (MoS2) structure based on the work presented in the following manuscript.

!!!note "Manuscript"
    **Kaihui Liu, Liming Zhang, Ting Cao, Chenhao Jin, Diana Qiu, Qin Zhou, Alex Zettl, Peidong Yang, Steve G. Louie & Feng Wang**,
    "Evolution of interlayer coupling in twisted molybdenum disulfide bilayers" Nature Communications volume 5, Article number: 4966 (2014)
    [DOI: 10.1038/ncomms5966](https://doi.org/10.1038/ncomms5966) [@Liu2014; @Zhang2016; @Cao2018]


We use the [Materials Designer](../../../materials-designer/overview.md) to create molybdenum disulfide bilayer structure configurations with multiple twist angles.

The Figure 4 shows the twisted bilayer MoS2 configurations.

![Twisted Bilayer Molybdenum Disulfide](../../../images/tutorials/materials/interfaces/twisted-bilayer-molybdenum-disulfide/MoS2-twisted-bilayers.png   "Twisted Bilayer Molybdenum Disulfide")

## 1. Load and preview MoS2 structure.

First, we navigate to [Materials Designer](../../../materials-designer/overview.md) and import the MoS2 material from the [Standata](../../../materials-designer/header-menu/input-output/standata-import.md).


![Standata MoS2 Import](../../../images/tutorials/materials/interfaces/twisted-bilayer-molybdenum-disulfide/standata-import-mos2.png "Standata MoS2 Import")

Then we will use the [JupyterLite](../../../jupyterlite/overview.md) environment to create a twisted bilayer molybdenum disulfide structure.


## 2. Create MoS2 bilayer with a twist angle of 22 degrees.

### 2.1 Launch JupyterLite Session.

Select the "Advanced > [JupyterLite Transformation](../../../materials-designer/header-menu/advanced/jupyterlite-dialog.md)" menu item to launch the JupyterLite environment.


![JupyterLite Dialog](../../../images/jupyterlite/md-advanced-jl.webp "JupyterLite Dialog")

### 2.2. Open and modify the notebook.

Next, edit `create_twisted_interface_with_commnesurate_lattices.ipynb` notebook to modify the parameters by adding: `TARGET_TWIST_ANGLE = 22` and `INTERFACE_DISTANCE = 6.5` -- found in the publication description.

Adjust the "1.1. Set up slab parameters" cell in the notebook according to:

```python
# Material selection and basic parameters
FILM_INDEX = 0 # Index in the list of materials, to access as materials[FILM_INDEX]
SUBSTRATE_INDEX = None  # Can be None to use same material as film

# Twisted interface parameters
TARGET_TWIST_ANGLE = 22.0  # in degrees
INTERFACE_DISTANCE = 6.5  # in Angstroms
INTERFACE_VACUUM = 20.0  # in Angstroms

# Search algorithm parameters
MAX_REPETITION = 6  # Maximum supercell matrix element value
ANGLE_TOLERANCE = 0.5  # in degrees
RETURN_FIRST_MATCH = True  # If True, returns first solution within tolerance

# Visualization parameters
SHOW_INTERMEDIATE_STEPS = True
VISUALIZE_REPETITIONS = [3, 3, 1]
```

![Notebook setup](../../../images/tutorials/materials/interfaces/twisted-bilayer-molybdenum-disulfide/jl-set-nb.png "Notebook setup")


### 2.3. Run the Notebook.

After setting the parameters, run the notebook to create the twisted bilayer molybdenum disulfide structure.

![Run All](../../../images/jupyterlite/run-all.webp "Run All")

### 2.4. View Results and pass to Materials Designer.

The generation might take some time.
After that, the user can pass the material to the Materials Designer for further analysis.

The interface for 22 degrees twist is shown below.

![Result Material, 22 degrees](../../../images/tutorials/materials/interfaces/twisted-bilayer-molybdenum-disulfide/mos2-result-wavejs-22.png "MoS2 Twisted Bilayer, 22 degrees")

## 3. Create bilayers with other twist angles.

### 3.1. Repeat the steps above.
To create a twisted bilayer MoS2 structure with a different twist angle, repeat the steps above, adjusting the `TARGET_TWIST_ANGLE` and `INTERFACE_DISTANCE` parameters accordingly.

Values for angle and associated interlayer separation provided below come from the description of Figure 4 in the publication, below each example has an image of the resulting material.

```python
TARGET_TWIST_ANGLE = 0.0
INTERFACE_DISTANCE = 6.8
```

![Result Material, 0 degrees](../../../images/tutorials/materials/interfaces/twisted-bilayer-molybdenum-disulfide/mos2-result-wavejs-0.png "MoS2 Twisted Bilayer, 0 degrees")


```python
TARGET_TWIST_ANGLE =  13.0
INTERFACE_DISTANCE =  6.5
```

![Result Material, 13 degrees](../../../images/tutorials/materials/interfaces/twisted-bilayer-molybdenum-disulfide/mos2-result-wavejs-13.png "MoS2 Twisted Bilayer, 13 degrees")

```python
TARGET_TWIST_ANGLE = 38.0
INTERFACE_DISTANCE = 6.5
```

![Result Material, 38 degrees](../../../images/tutorials/materials/interfaces/twisted-bilayer-molybdenum-disulfide/mos2-result-wavejs-38.png "MoS2 Twisted Bilayer, 38 degrees")

```python
TARGET_TWIST_ANGLE = 47.0
INTERFACE_DISTANCE = 6.5
```

![Result Material, 47 degrees](../../../images/tutorials/materials/interfaces/twisted-bilayer-molybdenum-disulfide/mos2-result-wavejs-47.png "MoS2 Twisted Bilayer, 47 degrees")

```python
TARGET_TWIST_ANGLE = 60.0
INTERFACE_DISTANCE = 6.2
```

![Result Material, 60 degrees](../../../images/tutorials/materials/interfaces/twisted-bilayer-molybdenum-disulfide/mos2-result-wavejs-60.png "MoS2 Twisted Bilayer, 60 degrees")


## Interactive JupyterLite Notebook.

The interactive JupyterLite notebook for creating twisted bilayer MoS2 structures can be accessed below. To run the notebook, click on the "Run All" button.


{% with origin_url=config.extra.jupyterlite.origin_url %}
{% with notebooks_path_root=config.extra.jupyterlite.notebooks_path_root %}
{% with notebook_name='specific_examples/interface_bilayer_twisted_commensurate_lattices_molybdenum_disulfide.ipynb' %}
{% include 'jupyterlite_embed.html' %}
{% endwith %}
{% endwith %}
{% endwith %}

## References.

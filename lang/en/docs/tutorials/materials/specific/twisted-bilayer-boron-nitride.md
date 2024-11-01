---
# YAML header
render_macros: true
---

# Twisted Bilayer Boron Nitride (TBBN) Structure Creation

## Introduction

This tutorial demonstrates the process of creating a twisted bilayer boron nitride (tBBN) structure based on the work presented in the following manuscript.

!!!note "Reference"
    **Lede Xian, Dante M. Kennes, Nicolas Tancogne-Dejean, Massimo Altarelli, and Angel Rubio**, 
    "Multiflat Bands and Strong Correlations in Twisted Bilayer Boron Nitride: Doping-Induced Correlated Insulator and Superconductor" Phys. Rev. Lett. 125, 086402 – Published 20 August 2020 DOI: 10.1021/acs.nanolett.9b00986


We use the [Materials Designer](../../../materials-designer/overview.md) to  create Hexagonal boron nitride bilayer structure configurations with 2 specific twist angles.

The image shows the twisted bilayer hBN structure with a twist angle of 2.64° (a) and 62.64° (b).

![Twisted Bilayer Boron Nitride](/images/tutorials/materials/interfaces/twisted-bilayer-boron-nitride/tbbn-paper-image.png "Twisted Bilayer Boron Nitride")

## 1. Load and preview BN structure

First, we navigate to [Materials Designer](../../../materials-designer/overview.md) and import the BN material from the [Standata](../../../materials-designer/header-menu/input-output/standata-import.md).

![Standata BN Import](/images/tutorials/materials/interfaces/twisted-bilayer-boron-nitride/standata-import-bn.png "Standata BN Import")

Then we will use the [JupyterLite](../../../jupyterlite/overview.md) environment to create a twisted bilayer boron nitride structure.

### 1.1. Launch JupyterLite Session

Select the "Advanced > [JupyterLite Transformation](../../../materials-designer/header-menu/advanced/jupyterlite-dialog.md)" menu item to launch the JupyterLite environment.

![JupyterLite Dialog](/images/jupyterlite/md-advanced-jl.webp "JupyterLite Dialog")

### 1.2. Open and modify the notebook

Next, edit `create_twisted_interface_with_nanoribbons.ipynb` notebook to modify the parameters by adding: RIBBON_WIDTH=50 and RIBBON_LENGTH=50, TWIST_ANGLE=2.64.
Adjust the "1.1. Set up slab parameters" cell in the notebook according to:

```python
FILM_INDEX = 0  # Index in the list of materials, to access as materials[FILM_INDEX]
SUBSTRATE_INDEX = None  # Can be None to use same material as film

# Nanoribbon parameters
RIBBON_WIDTH = 50  # Width of the nanoribbon in unit cells
RIBBON_LENGTH = 50  # Length of the nanoribbon in unit cells
VACUUM_X = 5.0  # Vacuum along x on both sides, in Angstroms
VACUUM_Y = 5.0  # Vacuum along y on both sides, in Angstroms

# Interface parameters
TWIST_ANGLE = 2.64  # in degrees
INTERFACE_DISTANCE = 3.23  # in Angstroms
INTERFACE_VACUUM = 20.0  # in Angstroms

# Visualization parameters
SHOW_INTERMEDIATE_STEPS = True
VISUALIZE_REPETITIONS = [1, 1, 1]
```

### 1.3. Run the Notebook

After setting the parameters, run the notebook to create the twisted bilayer boron nitride structure.

![Run All](/images/jupyterlite/run-all.webp "Run All")

### 1.4. Analyze the Results

After running the notebook, the user will be able to visualize the created twisted bilayer boron nitride structure.

![Review the Results](/images/tutorials/materials/interfaces/twisted-bilayer-boron-nitride/tbbn-result-jl.png "Review the Results")

### 1.5. Pass the Material to Materials Designer

After reviewing the results, the user can pass the material to Materials Designer for further analysis.


![Result Material](/images/tutorials/materials/interfaces/twisted-bilayer-boron-nitride/tbbn-result-wavejs.png "Result Material")

## 2. Create a twisted bilayer boron nitride structure with a twist angle of 62.64°

To create a twisted bilayer boron nitride structure with a twist angle of 62.64°, we need to adjust the TWIST_ANGLE parameter in the notebook to 62.64.

### 2.1. Open and modify the notebook

Edit the `create_twisted_interface_with_nanoribbons.ipynb` notebook to modify the parameters by adding: RIBBON_WIDTH=50 and RIBBON_LENGTH=50, TWIST_ANGLE=62.64.

```python
FILM_INDEX = 0  # Index in the list of materials, to access as materials[FILM_INDEX]
SUBSTRATE_INDEX = None  # Can be None to use same material as film

# Nanoribbon parameters
RIBBON_WIDTH = 50  # Width of the nanoribbon in unit cells
RIBBON_LENGTH = 50  # Length of the nanoribbon in unit cells
VACUUM_X = 5.0  # Vacuum along x on both sides, in Angstroms
VACUUM_Y = 5.0  # Vacuum along y on both sides, in Angstroms

# Interface parameters
TWIST_ANGLE = 62.64  # in degrees
INTERFACE_DISTANCE = 3.23  # in Angstroms
INTERFACE_VACUUM = 20.0  # in Angstroms

# Visualization parameters
SHOW_INTERMEDIATE_STEPS = True
VISUALIZE_REPETITIONS = [1, 1, 1]
```

![Notebook setup](/images/tutorials/materials/interfaces/twisted-bilayer-boron-nitride/jl-set-nb.png "Notebook setup")

### 2.2. Run the Notebook

After setting the parameters, run the notebook to create the twisted bilayer boron nitride structure with a twist angle of 62.64°.

### 2.3. Analyze the Results and Pass to Materials Designer

After running the notebook, the user will be able to visualize the created twisted bilayer boron nitride structure with a twist angle of 62.64°.

After reviewing the results, the user can pass the material to Materials Designer for further analysis.

![Twisted Bilayer Boron Nitride Structure with 62.64° Twist Angle](/images/tutorials/materials/interfaces/twisted-bilayer-boron-nitride/tbbn-62_64.png "Twisted Bilayer Boron Nitride Structure with 62.64° Twist Angle")

## Interactive JupyterLite Notebook

The interactive JupyterLite notebook for creating the twisted bilayer boron nitride structure can be accessed below. Select "Run" > "Run All Cells" to create two materials.

{% with origin_url=config.extra.jupyterlite.origin_url %}
{% with notebooks_path_root=config.extra.jupyterlite.notebooks_path_root %}
{% with notebook_name='specific_examples/interface_twisted_nanoribbons.ipynb' %}
{% include 'jupyterlite_embed.html' %}
{% endwith %}
{% endwith %}
{% endwith %}

## Tags

`twisted-bilayer`,`nanoribbons`, `boron-nitride`,  `BN`, `boron`, `nitrogen`


---
tags:
  - graphene
  - silicon dioxide
  - interface
  - 2D
  - 3D
  - oxygen
  - termination

hide:
  - tags
# YAML header
render_macros: true
---


# Interfaces between 2D and 3D Materials: Graphene on SiO2 (alpha-quartz).

## Introduction.

This tutorial demonstrates the process of creating interfaces between 2D and 3D materials, specifically graphene and silicon dioxide (SiO<sub>2</sub>), based on the work presented in the following manuscript, where the electronic properties of graphene on SiO<sub>2</sub> are studied.

!!!note "Manuscript"
    **Yong-Ju Kang, Joongoo Kang, and K. J. Chang**
    "Electronic structure of graphene and doping effect on SiO2"
    Physical Review B 78, 115404 (2008)
    [DOI: 10.1103/PhysRevB.78.115404](https://doi.org/10.1103/PhysRevB.78.115404)

We use the [Materials Designer](../../../materials-designer/overview.md) to create interfaces between graphene and silicon dioxide with oxygen termination, as shown in the manuscript.

We will focus on replicating the material from FIG. 1. (b) -- with Graphene on O-terminated SiO<sub>2</sub>. The material (a) requires relaxation to correctly reproduce the structure, which is not covered in this tutorial.

![Graphene on Silicon Dioxide](/images/tutorials/materials/interfaces/interface_2d_3d_graphene_silicon_dioxide/0-figure-from-manuscript.webp "Graphene on Silicon Dioxide, FIG. 1(b)")

## 1. Load and Preview Materials.

Navigate to [Materials Designer](../../../materials-designer/overview.md) and import graphene and silicon dioxide materials from the [Standata](../../../materials-designer/header-menu/input-output/standata-import.md).

Then use the [JupyterLite](../../../jupyterlite/overview.md) environment to create the target structures.

## 2. Create Interface Between Graphene and Silicon Dioxide.

### 2.1 Launch JupyterLite Session.

Select the "Advanced > [JupyterLite Transformation](../../../materials-designer/header-menu/advanced/jupyterlite-dialog.md)" menu item to launch the JupyterLite environment.

![JupyterLite Dialog](/images/jupyterlite/md-advanced-jl.webp "JupyterLite Dialog")

### 2.2 Open and Modify the Notebook.

Select the input materials with the first being the substrate (SiO₂) and the second being the film (graphene).

Open the `create_interface_with_min_strain_zsl.ipynb` notebook and modify the parameters as follows:

- Miller indices: `(0, 0, 1)` for both materials
- Thickness: `1` layer for graphene, `7` layers for SiO₂ (resulting in 14 bilayers as specified in the manuscript)
- Interface distance: `2.58` Å (as stated in the manuscript)
- Interface vacuum: `20.0` Å (as specified in the manuscript)

Let's set `MAX_AREA=150` Å² to allow for a larger search area for the superlattice search algorithm.

`TERMINATION_PAIR_INDICES` will be set to `[1]` to get the O-terminated interface as shown in the manuscript.

Adjust the "1.1. Set up slab parameters" cell as shown:

```python
# Enable interactive selection of terminations via UI prompt
IS_TERMINATIONS_SELECTION_INTERACTIVE = False

FILM_INDEX = 1  # Index in the list of materials, to access as materials[FILM_INDEX]
FILM_MILLER_INDICES = (0, 0, 1)
FILM_THICKNESS = 1  # in atomic layers
FILM_VACUUM = 0.0  # in angstroms
FILM_XY_SUPERCELL_MATRIX = [[1, 0], [0, 1]]
FILM_USE_ORTHOGONAL_Z = True

SUBSTRATE_INDEX = 0
SUBSTRATE_MILLER_INDICES = (0, 0, 1)
SUBSTRATE_THICKNESS = 7  # in atomic layers (for 14 bilayers -- from manuscript)
SUBSTRATE_VACUUM = 0.0  # in angstroms
SUBSTRATE_XY_SUPERCELL_MATRIX = [[1, 0], [0, 1]]
SUBSTRATE_USE_ORTHOGONAL_Z = True

# Maximum area for the superlattice search algorithm
MAX_AREA = 150  # in Angstrom^2
# Set the termination pair indices
TERMINATION_PAIR_INDICES = [1]  # For O-terminated
INTERFACE_DISTANCE = 2.58  # in Angstrom -- from manuscript
INTERFACE_VACUUM = 20.0  # in Angstrom -- from manuscript
```

![Notebook Setup](/images/tutorials/materials/interfaces/interface_2d_3d_graphene_silicon_dioxide/2-jl-setup-notebook.webp "Notebook Setup")

### 2.3 Run the Notebook

Run the notebook to generate the interface structure between graphene and silicon dioxide with oxygen termination.

![Run All](/images/jupyterlite/run-all.webp "Run All")

### 2.4. View Results.

The generation might take some time.
After that, the user can pass the material to the Materials Designer for further analysis.

![Gr/SiO2 Interface](/images/tutorials/materials/interfaces/interface_2d_3d_graphene_silicon_dioxide/3-jl-result-preview.webp "Gr/SiO2 Interface")

## 3. Pass the Material to Materials Designer.

After generating the interface structure, pass the material to the Materials Designer for further analysis.

The interface between graphene and silicon dioxide with oxygen termination is shown below.

![Gr/SiO2 Interface](/images/tutorials/materials/interfaces/interface_2d_3d_graphene_silicon_dioxide/4-wave-result-material.webp "Gr/SiO2 Interface")

## Interactive JupyterLite Notebook.


The interactive JupyterLite notebook for creating interfaces between graphene and silicon dioxide is embedded below. To run the notebook, click on the "Run All" button.


{% with origin_url=config.extra.jupyterlite.origin_url %}
{% with notebooks_path_root=config.extra.jupyterlite.notebooks_path_root %}
{% with notebook_name='specific_examples/interface_3d_2d_graphene_silicon_dioxide.ipynb' %}
{% include 'jupyterlite_embed.html' %}
{% endwith %}
{% endwith %}
{% endwith %}

## References.

1. **Yong-Ju Kang, Joongoo Kang, and K. J. Chang**
    "Electronic structure of graphene and doping effect on SiO2"
    Physical Review B 78, 115404 (2008)
    [DOI: 10.1103/PhysRevB.78.115404](https://doi.org/10.1103/PhysRevB.78.115404)


2. **Arjun Dahala  and  Matthias Batzill**
    "Graphene–nickel interfaces: a review"
    Nanoscale 6, 2548-2562 (2014)
    [DOI: 10.1039/C3NR05279F](https://doi.org/10.1039/C3NR05279F)


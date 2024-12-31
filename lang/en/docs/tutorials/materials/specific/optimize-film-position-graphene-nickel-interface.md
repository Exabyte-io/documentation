---
# YAML header
render_macros: true
---

# Graphene/Ni(111) Interface Optimization

## Introduction

This tutorial demonstrates how to create and optimize a Graphene/Ni(111) interface structure following the experimental observations presented in the literature. We will focus on finding the most energetically favorable position of graphene on the Ni(111) surface.

!!!note "Manuscript"
    Arjun Dahal, Matthias Batzill
    "Graphene–nickel interfaces: a review"
    Nanoscale, 6(5), 2548. (2014)
    [DOI: 10.1039/c3nr05279f](https://doi.org/10.1039/c3nr05279f){:target='_blank'}.

We will recreate the interface structure and optimize the film position to match the experimental findings shown in the figure below:

![Gr/Ni Interface](/images/tutorials/materials/interfaces/graphene_ni_111/optimal-position.webp "Optimal position of graphene on Ni(111)")

## 1. Create Interface Structure

### 1.1. Load Base Materials

Navigate to [Materials Designer](../../../materials-designer/overview.md) and import both graphene and nickel materials from the [Standata](../../../materials-designer/header-menu/input-output/standata-import.md).

![Standata Materials Import](/images/tutorials/materials/interfaces/graphene_ni_111/standata-import.webp "Import Graphene and Nickel from Standata")

### 1.2. Launch JupyterLite Session

Select the "Advanced > [JupyterLite Transformation](../../../materials-designer/header-menu/advanced/jupyterlite-dialog.md)" menu item to launch the JupyterLite environment.

### 1.3. Open `create_interface_with_min_strain_zsl.ipynb` notebook

Find and open the `create_interface_with_min_strain_zsl.ipynb` notebook. This notebook will help us create the initial interface structure.

### 1.4. Set up interface parameters

Edit the notebook parameters to create the Gr/Ni(111) interface:

```python
# Material selection
SUBSTRATE_NAME = "Nickel"
FILM_NAME = "Graphene"

# Slab parameters
SUBSTRATE_MILLER_INDICES = (1, 1, 1)
SUBSTRATE_THICKNESS = 4  # in atomic layers
FILM_THICKNESS = 1  # in atomic layers

# Interface parameters
MAX_AREA = 50  # in Angstrom^2
INTERFACE_DISTANCE = 2.58  # in Angstrom from literature
INTERFACE_VACUUM = 20.0  # in Angstrom
```

### 1.5. Run interface creation

Run the notebook using "Run > Run All Cells". This will:
1. Create slabs from both materials
2. Find the optimal lattice matching using the ZSL algorithm
3. Generate the initial interface structure

![Interface Creation Result](/images/tutorials/materials/interfaces/graphene_ni_111/interface-created.webp "Created Gr/Ni Interface")

## 2. Optimize Film Position

### 2.1. Open `optimize_film_position.ipynb` notebook

Find and open the `optimize_film_position.ipynb` notebook which will help us find the optimal position of the graphene layer.

### 2.2. Set optimization parameters

Configure the optimization parameters:

```python
# Grid parameters
GRID_SIZE = (20, 20)  # Resolution of the x-y grid
GRID_RANGE_X = (-0.5, 0.5)  # Range in crystal coordinates
GRID_RANGE_Y = (-0.5, 0.5)  
USE_CARTESIAN = False  # Use crystal coordinates

# Visualization parameters
STRUCTURE_REPETITIONS = [3, 3, 1]
```

Key parameters explained:
- `GRID_SIZE`: Controls the resolution of position sampling
- `GRID_RANGE`: Search range in crystal coordinates
- `USE_CARTESIAN`: Set to False for hexagonal systems

### 2.3. Run optimization

Run all cells in the notebook. The optimization will:
1. Calculate energy landscape across different positions
2. Find the global minimum energy position
3. Generate visualizations of the results

![Energy Landscape](/images/tutorials/materials/interfaces/graphene_ni_111/energy-landscape.webp "Energy landscape of film positions")

## 3. Analyze Results

After running both notebooks, examine the results:

### 3.1. Interface Structure
- Verify the interface distance is ~2.58 Å
- Check that the graphene layer is parallel to the Ni(111) surface
- Confirm the supercell size is reasonable

### 3.2. Energy Landscape
The energy landscape shows:
1. Clear energy minima indicating preferred positions
2. Periodic pattern matching the hexagonal symmetry
3. Sharp peaks at unfavorable positions

### 3.3. Optimal Position
The optimized structure should show:
- Carbon atoms positioned over Ni atoms and hollow sites
- No significant distortion in the graphene layer
- Proper registry between graphene and Ni surface atoms

## 4. Save Optimized Structure

The optimized interface structure will be automatically passed back to Materials Designer where you can:
1. Save it in the workspace
2. Export it in various formats (JSON, POSCAR, etc.)
3. Use it for further calculations

## Interactive JupyterLite Notebook

The following JupyterLite notebook demonstrates the complete process. Select "Run" > "Run All Cells".

{% with origin_url=config.extra.jupyterlite.origin_url %}
{% with notebooks_path_root=config.extra.jupyterlite.notebooks_path_root %}
{% with notebook_name='specific_examples/optimize-film-position-graphene-nickel-interface.ipynb' %}
{% include 'jupyterlite_embed.html' %}
{% endwith %}
{% endwith %}
{% endwith %}

## Parameter Fine-tuning

To adjust the interface optimization:

1. Interface Creation:
   - Adjust `SUBSTRATE_THICKNESS` for more Ni layers
   - Modify `MAX_AREA` to control supercell size
   - Change `INTERFACE_DISTANCE` if needed

2. Position Optimization:
   - Increase `GRID_SIZE` for finer sampling
   - Adjust `GRID_RANGE` to search different areas
   - Enable 3D visualization with `SHOW_3D_LANDSCAPE = True`

## References

1. Dahal, A., & Batzill, M. (2014). Graphene–nickel interfaces: a review. Nanoscale, 6(5), 2548-2562. [DOI: 10.1039/c3nr05279f](https://doi.org/10.1039/c3nr05279f)

2. Gamo, Y., Nagashima, A., Wakabayashi, M., Terai, M., & Oshima, C. (1997). Atomic structure of monolayer graphite formed on Ni(111). Surface Science, 374(1-3), 61-64.

3. Bertoni, G., Calmels, L., Altibelli, A., & Serin, V. (2004). First-principles calculation of the electronic structure and EELS spectra at the graphene/Ni(111) interface. Physical Review B, 71(7).

## Tags

`graphene`, `nickel`, `interface`, `optimization`, `2D materials`, `surface science`, `Gr/Ni(111)`, `C`, `Ni`
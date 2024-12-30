---
# YAML header
render_macros: true
---

# Creating Rippled Graphene

## Introduction

This tutorial demonstrates the process of creating rippled graphene based on the work presented in the following manuscript, where the mechanical properties of graphene edges were studied.

!!!note "Manuscript"
    Thompson-Flagg, R. C., Moura, M. J. B., & Marder, M.
    "Rippling of graphene"
    EPL (Europhysics Letters), 85(4), 46002 (2009)
    [DOI: 10.1209/0295-5075/85/46002](https://doi.org/10.1209/0295-5075/85/46002)

We will focus on creating graphene with edge-induced ripples that match the patterns observed in experimental studies, as shown in FIG. 1.

![Rippled Graphene](/images/tutorials/materials/2d_materials/rippled_graphene/0-figure-from-manuscript.webp "Rippled Graphene, FIG. 1.")

## 1. Create Rippled Graphene

### 1.1. Load Graphene Material

Navigate to [Materials Designer](../../../materials-designer/overview.md) and import the graphene material from the [Standata](../../../materials-designer/header-menu/input-output/standata-import.md).

![Graphene Material](/images/tutorials/materials/2d_materials/rippled_graphene/original-material.webp "Graphene Material")

### 1.2. Launch JupyterLite Session

Select the "Advanced > [JupyterLite Transformation](../../../materials-designer/header-menu/advanced/jupyterlite-dialog.md)" menu item to launch the JupyterLite environment.

![JupyterLite Dialog](/images/jupyterlite/md-advanced-jl.webp "JupyterLite Dialog")

### 1.3. Open `create_perturbation_custom.ipynb` notebook

Find `create_perturbation_custom.ipynb` in the list of notebooks and click/double-click to open it.

### 1.4. Open and modify the notebook

Next, we need to set up the parameters for creating rippled graphene.

Edit notebook in 1.2. to set generic perturbation parameters:

```python
# Set whether to preserve geodesic distance and scale the cell accordingly to match PBC
PRESERVE_GEODESIC_DISTANCE = True

# Set whether to use Cartesian coordinates for the perturbation function
USE_CARTESIAN_COORDINATES = False
MATERIAL_NAME = "Graphene"
```

![Setup Generic Parameters](/images/tutorials/materials/2d_materials/rippled_graphene/jl-setup-generic.webp "Setup Generic Parameters")

Then modify section 1.3 to define the custom perturbation function:

```python
import sympy as sp

# Variables for the perturbation function (for SymPy)
variable_names = ["x", "y", "z"]
x, y, z = sp.symbols(variable_names)

# Set the parameters for the perturbation function
AMPLITUDE = 0.09  # Ripple amplitude
WAVELENGTH = 0.2  # Wavelength of ripples
EDGE_WIDTH = 0.25  # Width of edge effect
PHASE_X = 0.0  # Phase shift for x direction
PHASE_Y = sp.pi/2  # Phase shift for y direction

# Create edge masks for both x and y using polynomial functions
left_edge_x = sp.Max(0, (EDGE_WIDTH - x) / EDGE_WIDTH)
right_edge_x = sp.Max(0, (x - (1 - EDGE_WIDTH)) / EDGE_WIDTH)
left_edge_y = sp.Max(0, (EDGE_WIDTH - y) / EDGE_WIDTH)
right_edge_y = sp.Max(0, (y - (1 - EDGE_WIDTH)) / EDGE_WIDTH)

# Combine edge masks
edge_mask_x = left_edge_x + right_edge_x
edge_mask_y = left_edge_y + right_edge_y
edge_mask = edge_mask_x + edge_mask_y

# Wave pattern
wave_pattern = (
    sp.sin(2 * sp.pi * x / WAVELENGTH + PHASE_X) * 
    sp.sin(2 * sp.pi * y / WAVELENGTH + PHASE_Y)
)

# Combine waves with edge mask
custom_sympy_function = AMPLITUDE * wave_pattern * edge_mask
```

![Setup Perturbation Function](/images/tutorials/materials/2d_materials/rippled_graphene/jl-setup-function.webp "Setup Perturbation Function")

Key parameters explained:
- AMPLITUDE: Controls the height of the ripples (0.09 Å)
- WAVELENGTH: Controls the spacing between ripples (0.2 in crystal coordinates)
- EDGE_WIDTH: Controls how far the ripples extend from the edges (0.25 in crystal coordinates)
- PHASE_X/Y: Controls the phase shift of the ripple pattern

### 1.5. Run the notebook

After setting the parameters, run the notebook by selecting "Run > Run All Cells" from the menu.

![Run All](/images/jupyterlite/run-all.webp "Run All")

## 2. Analyze the Results

After running the notebook, the rippled graphene structure should appear in the preview.

![Rippled Graphene Result](/images/tutorials/materials/2d_materials/rippled_graphene/jl-result-preview.webp "Rippled Graphene Result")

The visualization shows:
- Top view: Displaying the overall ripple pattern across the graphene sheet
- Side view (-90x rotation): Showing the height profile of the ripples

Key features to verify:
1. Ripples should appear strongest at the edges
2. The center of the sheet should remain relatively flat
3. The ripple pattern should be symmetric
4. The wavelength and amplitude should match the experimental observations

## 3. Pass the Material to Materials Designer

The rippled graphene structure will be automatically passed back to the current Materials Designer environment where you can save it.

![Final Material](/images/tutorials/materials/2d_materials/rippled_graphene/wave-result.webp "Final Rippled Graphene")

Or you can [save or download](../../../materials-designer/header-menu/input-output.md) the material in Material JSON format or POSCAR format.

## Interactive JupyterLite Notebook

The following JupyterLite notebook demonstrates the process of creating rippled graphene. Select "Run" > "Run All Cells".

{% with origin_url=config.extra.jupyterlite.origin_url %}
{% with notebooks_path_root=config.extra.jupyterlite.notebooks_path_root %}
{% with notebook_name='specific_examples/rippled_graphene.ipynb' %}
{% include 'jupyterlite_embed.html' %}
{% endwith %}
{% endwith %}
{% endwith %}

## Parameters Fine-tuning

If you need to adjust the ripple pattern, you can modify these key parameters:

1. To change ripple height:
   - Adjust AMPLITUDE (higher value = taller ripples)

2. To change ripple spacing:
   - Adjust WAVELENGTH (higher value = more spread out ripples)

3. To change how far ripples extend from edges:
   - Adjust EDGE_WIDTH (higher value = ripples extend further from edges)

4. To change the ripple pattern:
   - Adjust PHASE_X and PHASE_Y to modify the wave interference pattern

## References

1. Thompson-Flagg, R. C., Moura, M. J. B., & Marder, M. (2009). Rippling of graphene. EPL (Europhysics Letters), 85(4), 46002. [DOI: 10.1209/0295-5075/85/46002](https://doi.org/10.1209/0295-5075/85/46002)

## Tags

`graphene`, `ripples`, `perturbation`, `2D materials`, `edge effects`
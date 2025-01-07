---
tags:
  - silicon
  - surface
  - passivation
  - hydrogen
  - Si(100)
  - surface reconstruction
  - Si
  - H

hide:
  - tags
# YAML header
render_macros: true
---

# Passivation of Silicon (100) Surface.

## Introduction.

This tutorial demonstrates how to passivate a reconstructed silicon (100) surface with hydrogen atoms, following the methodology described in the literature.

!!!note "Manuscript"
    Hansen, U., & Vogl, P.
    "Hydrogen passivation of silicon surfaces: A classical molecular-dynamics study."
    Physical Review B, 57(20), 13295–13304. (1998)
    [DOI: 10.1103/PhysRevB.57.13295](https://doi.org/10.1103/PhysRevB.57.13295){:target='_blank'}. [@Hansen1998; @Northrup1991; @Boland1990]

We will recreate the passivated surface structure shown in Fig. 8:

![Si(100) H-Passivated Surface](../../../images/tutorials/materials/passivation/passivation_surface_silicon/0-figure-from-manuscript.webp "H-Passivated Silicon (100)")

## 1. Obtain the Silicon (100) Surface Structure.

### 1.1. Load Base Material.

Navigate to [Materials Designer](../../../materials-designer/overview.md) and import the reconstructed Si(100) surface from [Standata](../../../materials-designer/header-menu/input-output/standata-import.md).

![Si(100) Structure](../../../images/tutorials/materials/passivation/passivation_surface_silicon/1-wave-original-material.webp "Si(100) Structure")

### 1.2. Launch JupyterLite Session.

Select the "Advanced > [JupyterLite Transformation](../../../materials-designer/header-menu/advanced/jupyterlite-dialog.md)" menu item to launch the JupyterLite environment.

### 1.3. Open Modified `create_supercell.ipynb` Notebook.

Open `create_supercell.ipynb`, select input material as the Si(100) structure, and set the supercell parameters in 1.1.:

```python
SUPERCELL_MATRIX = [
    [1, 0, 0], 
    [0, 1, 0], 
    [0, 0, 1]
] 

# or use the scaling factor.
SCALING_FACTOR = None # [3, 3, 1].
```

Also add to the "Get input materials" cell the following code to adjust the Si atom position:

```python
from utils.jupyterlite import get_materials
materials = get_materials(globals())
material = materials[0]

# Find coordinates of the Si atoms, list in descending order, and change the 2nd one from the top
si_atoms_coordinates = [coordinate for coordinate in slab.basis.coordinates.values]
si_atoms_sorted = sorted(si_atoms_coordinates, key=lambda x: x[2], reverse=True)
second_from_top_index = 1
second_si_atom_coordinate = si_atoms_sorted[second_from_top_index]

print(f"Coordinates of the second Si atom: {second_si_atom_coordinate}")
adjusted_coordinate = [
    coord + delta for coord, delta in zip(second_si_atom_coordinate, [0.025, 0, 0.025])
]
print(f"Adjusted coordinate: {adjusted_coordinate}")
new_coordinates = si_atoms_coordinates.copy()
index_to_adjust = slab.basis.coordinates.get_element_id_by_value(second_si_atom_coordinate)
new_coordinates[index_to_adjust] = adjusted_coordinate
slab.set_coordinates(new_coordinates)
```

![Supercell Parameters](../../../images/tutorials/materials/passivation/passivation_surface_silicon/2-jl-setup-nb-adjust.webp "Supercell Parameters Visualization")

### 1.4. Run Structure Adjustment.

Run the notebook using "Run > Run All Cells". This will:

1. Load the Si(100) structure
2. Adjust the position of the specified Si atom
3. Create a supercell if specified in the parameters
4. Visualize the adjusted structure

![Adjusted Structure](../../../images/tutorials/materials/passivation/passivation_surface_silicon/3-wave-adjusted-material.webp "Adjusted Si(100) Structure")

## 2. Passivate the Surface.

### 2.1. Open `passivate_slab.ipynb` Notebook.

Find and open the `passivate_slab.ipynb` notebook to add hydrogen atoms to the surface.

### 2.2. Set Passivation Parameters.

Configure the following parameters for hydrogen passivation:

```python
# Passivation parameters.
PASSIVANT = "H"  # Chemical symbol for hydrogen.
BOND_LENGTH = 1.46  # Si-H bond length in Angstroms.
SURFACE = "top"  # Passivate only the top surface.

# Surface detection parameters.
SHADOWING_RADIUS = 1.8  # In Angstroms.
DEPTH = 0.5  # In Angstroms.

# Visualization parameters.
CELL_REPETITIONS_FOR_VISUALIZATION = [1, 1, 1]
```

Key parameters explained:

- `BOND_LENGTH`: Si-H bond length from literature.
- `SHADOWING_RADIUS`: Controls which atoms are considered surface atoms, set to be below the distance between top Si atoms pair.
- `SURFACE`: Passivate only the top surface.
- `DEPTH`: How deep to look for surface atoms, set to include only top Si atoms.

![Passivation Parameters](../../../images/tutorials/materials/passivation/passivation_surface_silicon/4-jl-setup-nb-passivate.webp "Passivation Parameters Visualization")

### 2.3. Run Passivation.

Run all cells in the notebook. The passivation process will:

1. Detect surface Si atoms
2. Add H atoms at the specified bond length
3. Generate the passivated structure

![Passivated Structure](../../../images/tutorials/materials/passivation/passivation_surface_silicon/5-jl-result-preview.webp "H-Passivated Si(100) Structure")

## 3. Analyze Results.

After running both notebooks, examine the final structure:

Check that:

- The adjusted Si atom position is correct
- Surface reconstruction is maintained
- H atoms are properly placed above surface Si atoms

![Final Structure](../../../images/tutorials/materials/passivation/passivation_surface_silicon/6-wave-result.webp "Final H-Passivated Si(100)")

## 4. Save the Results.

The final structure will be automatically passed back to Materials Designer where you can:
1. Save it in your workspace
2. Export it in various formats
3. Use it for further calculations

## Interactive JupyterLite Notebook.

The following embedded notebook demonstrates the complete process. Select "Run" > "Run All Cells".

{% with origin_url=config.extra.jupyterlite.origin_url %}
{% with notebooks_path_root=config.extra.jupyterlite.notebooks_path_root %}
{% with notebook_name='specific_examples/passivation_surface_silicon_surface.ipynb' %}
{% include 'jupyterlite_embed.html' %}
{% endwith %}
{% endwith %}
{% endwith %}

## Parameter Fine-tuning.

To adjust the passivation:

1. Surface Detection:

   - Increase `SHADOWING_RADIUS` to be more selective about surface atoms
   - Adjust `DEPTH` to control how deep to look for surface atoms

2. Passivation:

   - Modify `BOND_LENGTH` for different Si-H distances
   - Change `SURFACE` to passivate different surfaces
   - Change `PASSIVANT` to use different passivating species

## References.

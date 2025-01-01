---
# YAML header
render_macros: true
---

# Pt Adatom Island on MoS2

## Introduction

This tutorial demonstrates how to create a platinum island on MoS2 by sequentially adding Pt adatoms, following the methodology described in the literature.

!!!note "Manuscript"
    Saidi, W. A.
    "Density Functional Theory Study of Nucleation and Growth of Pt Nanoparticles on MoS2(001) Surface"
    Crystal Growth & Design, 15(2), 642–652. (2015)
    [DOI: 10.1021/cg5013395](https://doi.org/10.1021/cg5013395){:target='_blank'}.

We will recreate the Pt island structure shown in Figure 4b:

![Pt Island on MoS2](/images/tutorials/materials/defects/defect_point_adatom_island_mos2_pt/0-figure-from-manuscript.webp "Pt island formation on MoS2")

## 1. Create MoS2 Substrate

### 1.1. Load Base Material

Navigate to [Materials Designer](../../../materials-designer/overview.md) and import the MoS2 2D material from [Standata](../../../materials-designer/header-menu/input-output/standata-import.md).

### 1.2. Launch JupyterLite Session

Select the "Advanced > [JupyterLite Transformation](../../../materials-designer/header-menu/advanced/jupyterlite-dialog.md)" menu item to launch the JupyterLite environment.

### 1.3. Open `create_adatom_defect.ipynb` Notebook

Find and open the `create_adatom_defect.ipynb` notebook. We'll use this notebook multiple times to add Pt adatoms sequentially.

## 2. Add Pt Adatoms

We'll add four Pt atoms sequentially to form the island. Each atom needs specific parameters to achieve the correct structure.

### 2.1. First Pt Atom (Base)

Set the following parameters for the first Pt atom:

```python
DEFECT_TYPE = "adatom"
PLACEMENT_METHOD = "coordinate"
CHEMICAL_ELEMENT = "Pt"
APPROXIMATE_POSITION_ON_SURFACE = [5/9, 4/9]  # Atop central Mo
DISTANCE_Z = 1.2  # Distance from surface S atoms
USE_CARTESIAN_COORDINATES = False

# Slab parameters
MILLER_INDICES = (0, 0, 1)
SLAB_THICKNESS = 1  # Single layer
VACUUM = 10.0  # in Angstrom
SUPERCELL_MATRIX = [[3, 0, 0], [0, 3, 0], [0, 0, 1]]
```

Run the notebook to add the first Pt atom.

![First Pt](/images/tutorials/materials/defects/defect_point_adatom_island_mos2_pt/pt1-added.webp "First Pt atom added")

### 2.2. Second Pt Atom

Reopen the notebook and modify the position for the second Pt atom:

```python
DEFECT_TYPE = "adatom"
PLACEMENT_METHOD = "coordinate"
CHEMICAL_ELEMENT = "Pt"
APPROXIMATE_POSITION_ON_SURFACE = [5/9, 4/9]  # Atop central Mo
DISTANCE_Z = 1.2  # Distance from surface S atoms
USE_CARTESIAN_COORDINATES = False

# Slab parameters
MILLER_INDICES = (0, 0, 1)
SLAB_THICKNESS = 1  # Single layer
VACUUM = 0.0  # in Angstrom
SUPERCELL_MATRIX = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
```

This time the supercell is set to a 1x1x1 and vacuum to 0.0 to not change the substrate.

### 2.3. Third Pt Atom

Add the third Pt atom:

```python
APPROXIMATE_POSITION_ON_SURFACE = [5/9, 7/9]  # Next clockwise atop Mo
DISTANCE_Z = 1.2
```

### 2.4. Fourth Pt Atom (Top)

Finally, add the topmost Pt atom:

```python
APPROXIMATE_POSITION_ON_SURFACE = [4/9, 5/9]  # Atop S
DISTANCE_Z = 1.6  #  # Distance between Pt atom layers, in Angstrom
```

![Complete Island](/images/tutorials/materials/defects/defect_point_adatom_island_mos2_pt/4-wave-result-top.webp "Complete Pt island structure")

![Complete Island, side view](/images/tutorials/materials/defects/defect_point_adatom_island_mos2_pt/5-wave-result-side.webp "Complete Pt island structure, side view")

## 3. Analyze the Structure

After adding all Pt atoms, verify the following:

### 3.1. Base Layer Geometry

- Three Pt atoms should form a triangular base
- Each base Pt should be positioned atop Mo atoms
- Distance from surface S atoms should be ~1.2 Å

### 3.2. Top Atom Position

- Fourth Pt should be centered above the triangle
- Position should be approximately above a surface S atom
- Height should be ~2.8 Å from surface (1.6 Å from base Pt atoms)

## 4. Save the Structure

The final structure will be automatically passed back to Materials Designer where user can:

1. Save it in userr workspace
2. Export it in various formats
3. Use it for further calculations

## Interactive JupyterLite Notebook

The following embedded notebook demonstrates the complete process. Select "Run" > "Run All Cells".

{% with origin_url=config.extra.jupyterlite.origin_url %}
{% with notebooks_path_root=config.extra.jupyterlite.notebooks_path_root %}
{% with notebook_name='specific_examples/defect_point_adatom_island_mos2_pt.ipynb' %}
{% include 'jupyterlite_embed.html' %}
{% endwith %}
{% endwith %}
{% endwith %}

## Parameter Fine-tuning

To adjust the island structure:

1. Base Layer:
   - Adjust `APPROXIMATE_POSITION_ON_SURFACE` to shift Pt positions
   - Modify `DISTANCE_Z` to change height from surface

2. Top Atom:
   - Adjust position to change island shape
   - Modify height to change Pt-Pt spacing

## References

1. Saidi, W. A. (2015). Density Functional Theory Study of Nucleation and Growth of Pt Nanoparticles on MoS2(001) Surface. Crystal Growth & Design, 15(2), 642–652.

2. Le, D., et al. (2014). Growth of Pt on MoS2 monolayer catalysts: From atomic-scale structure to catalytic activity. Journal of Physical Chemistry C, 118(11), 5346-5351.

3. Wang, H., et al. (2013). Interaction between single gold atom and the graphene edge: A study via high-level ab initio calculations. Nanoscale, 5(21), 10534-10540.

## Tags

`MoS2`, `platinum`, `adatoms`, `surface science`, `2D materials`, `nanoparticles`, `Mo`, `S`, `Pt`
---
# YAML header
render_macros: true
---

# Pt Nanoparticles on MoS2(001) Surface via Adatoms

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

### 1.3. Open `create_point_defect.ipynb` Notebook

Find and open the `create_point_defect.ipynb` notebook. We'll configure all Pt adatoms at once using the new multiple defect configuration.

## 2. Configure and Create Structure

### 2.1. Set Parameters

Set up the slab and defect parameters in the notebook:

```python
# Slab parameters
MILLER_INDICES = (0, 0, 1)  # MoS2 basal plane
SLAB_THICKNESS = 1  # Single layer
VACUUM = 10.0  # in Angstrom
SUPERCELL_MATRIX = [[3, 0, 0], [0, 3, 0], [0, 0, 1]]  # 3x3 supercell

# Defect configurations for all Pt atoms
DEFECT_CONFIGS = [
    {
        "defect_type": "adatom",
        "placement_method": "coordinate",
        "chemical_element": "Pt",
        "position_on_surface": [5/9, 4/9],  # First Pt: atop central Mo
        "distance_z": 1.2, # Distance from surface S atoms
        "use_cartesian_coordinates": False
    },
    {
        "defect_type": "adatom",
        "placement_method": "coordinate",
        "chemical_element": "Pt",
        "position_on_surface": [2/9, 4/9],  # Second Pt: next clockwise atop Mo
        "distance_z": 1.2, # Distance from surface S atoms
        "use_cartesian_coordinates": False
    },
    {
        "defect_type": "adatom",
        "placement_method": "coordinate",
        "chemical_element": "Pt",
        "position_on_surface": [5/9, 7/9],  # Third Pt: next clockwise atop Mo
        "distance_z": 1.2, # Distance from surface S atoms
        "use_cartesian_coordinates": False
    },
    {
        "defect_type": "adatom",
        "placement_method": "coordinate",
        "chemical_element": "Pt",
        "position_on_surface": [4/9, 5/9],  # Fourth Pt: centered atop S
        "distance_z": 1.6,  # Distance between Pt atom layers, in Angstrom
        "use_cartesian_coordinates": False
    }
]
```

Key parameters explained:

- Base layer Pt atoms (first three configs):
  * Positioned atop Mo atoms in a triangular arrangement
  * Height 1.2 Å from surface S atoms to achieve separation from Mo atoms of 2.8 A -- from publication
- Top Pt atom (fourth config):
  * Centered above the triangle, atop S atom
  * Height 1.6 Å from surface (1.6 Å from base Pt atoms)

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

1. Saidi, W. A. (2015). Density Functional Theory Study of Nucleation and Growth of Pt Nanoparticles on MoS2(001) Surface. Crystal Growth & Design, 15(2), 642–652. [DOI: 10.1021/cg5013395](https://doi.org/10.1021/cg5013395){:target='_blank'}.

2. Jiao, M., Song, W., Qian, H.-J., Wang, Y., Wu, Z., Irle, S., & Morokuma, K. (2016). QM/MD studies on graphene growth from small islands on the Ni(111) surface. Nanoscale, 8(5), 3067–3074. doi:10.1039/c5nr07680c  [DOI: 10.1039/c5nr07680c](https://doi.org/10.1039/c5nr07680c){:target='_blank'}.

3. Kristen A. Fichthorn and Matthias Scheffler, "Island Nucleation in Thin-Film Epitaxy: A First-Principles Investigation", Phys. Rev. Lett. 84, 5371 (2000). [DOI: 10.1103/PhysRevLett.84.5371](https://doi.org/10.1103/PhysRevLett.84.5371){:target='_blank'}.

4. Jörg Neugebauer and Matthias Scheffler, "Mechanisms of island formation of alkali-metal adsorbates on Al(111)", Phys. Rev. Lett. 71, 577 (1993). [DOI: 10.1103/PhysRevLett.71.577](https://doi.org/10.1103/PhysRevLett.71.577){:target='_blank'}.

5. Mahbube Hortamani, Peter Kratzer, and Matthias Scheffler, "Density-functional study of Mn monosilicide on the Si(111) surface:
Film formation versus island nucleation", Phys. Rev. B 76, 235426 (2007). [DOI: 10.1103/PhysRevB.76.235426](https://doi.org/10.1103/PhysRevB.76.235426){:target='_blank'}.

## Tags

`MoS2`, `platinum`, `adatoms`, `surface science`, `2D materials`, `nanoparticles`, `Mo`, `S`, `Pt`
---
# YAML header
render_macros: true
---

# 2D Grain Boundaries in Hexagonal Boron Nitride

## Introduction

This tutorial demonstrates the process of creating 2D grain boundary structures in hexagonal boron nitride (h-BN), based on the work presented in the following manuscript:

!!!note "Manuscript"
    Qiucheng Li, Xiaolong Zou, Mengxi Liu, Jingyu Sun, Yabo Gao, Yue Qi, Xiebo Zhou, Boris I. Yakobson, Yanfeng Zhang, and Zhongfan Liu, "Grain Boundary Structures and Electronic Properties of Hexagonal Boron Nitride on Cu(111)", ACS Nano 2015 9 (6), 6308-6315. [DOI: 10.1021/acs.nanolett.5b01852](https://doi.org/10.1021/acs.nanolett.5b01852){:target='_blank'}.

We will focus on creating h-BN grain boundary structures similar to Figure 2c from the manuscript:

![h-BN Grain Boundary](/images/tutorials/materials/interfaces/grain_boundary_hbn/0-figure-from-manuscript.webp "h-BN Grain Boundary, FIG. 2c.")

## 1. Create Initial h-BN Structure

### 1.1. Load h-BN Material

Navigate to [Materials Designer](../../../materials-designer/overview.md) and import the h-BN material from the [Standata](../../../materials-designer/header-menu/input-output/standata-import.md).

1. Click on "Input/Output" menu
2. Select "Import from Standata"
3. Search for "Boron_Nitride" and select the 2D h-BN material

![h-BN Material Import](/images/tutorials/materials/interfaces/grain_boundary_hbn/1-standata-hbn.webp "h-BN Material Import")

### 1.2. Launch JupyterLite Session

Select "Advanced > [JupyterLite Transformation](../../../materials-designer/header-menu/advanced/jupyterlite-dialog.md)" to open JupyterLite.

### 1.3. Open and Configure Notebook

Find and open `create_grain_boundary_film.ipynb`. Edit the grain boundary parameters in section 1.1:

`TARGET_TWIST_ANGLE = 9.0` -- As described in the manuscript.
`ANGLE_TOLERANCE = 0.5` -- Tolerance for twist angle matching, in degrees. 
`BOUNDARY_GAP = 0.0` -- Gap between orientations in X direction, should be set to 0.0 for seamless boundaries.
`DISTANCE_TOLERANCE = 1.43` -- Distance tolerance for atom merging, in Angstroms. Set to be smaller than the B-N length to avoid symmetrical atoms.
`EDGE_INCLUSION_TOLERANCE = 0.0` -- Edge inclusion parameter, in Angstroms. Controls the overlap of the second phase onto the first phase.

```python
# Grain boundary parameters
TARGET_TWIST_ANGLE = 9.0  # in degrees
BOUNDARY_GAP = 0.0  # Gap between orientations in X direction
XY_SUPERCELL_MATRIX = [[1, 0], [0, 2]]

# Search algorithm parameters
MAX_REPETITION = None
ANGLE_TOLERANCE = 0.5  # in degrees
RETURN_FIRST_MATCH = True

# Distance tolerance for atom merging
DISTANCE_TOLERANCE = 1.43  # in Angstroms

# Edge inclusion parameter
EDGE_INCLUSION_TOLERANCE = 0.0  # in Angstroms
```

!!!note "Important Parameter"
    The `DISTANCE_TOLERANCE` parameter (1.43 Å) is larger than B-N distances at the one specific spot in the boundary. This will cause certain nitrogen atoms to be removed during structure generation, which we'll need to restore later.

## 2. Generate Grain Boundary

### 2.1. Run Initial Configuration

Run the first part of the notebook to:
1. Load the h-BN structure
2. Set up the grain boundary configuration
3. Initialize the builder with the specified parameters

### 2.2. Create and Analyze Grain Boundaries

The notebook will:
1. Generate possible grain boundary structures
2. Display the number of structures found
3. Show the actual twist angle and number of atoms for each structure
4. Plot angle vs. number of atoms for all solutions

![Solutions Analysis](/images/tutorials/materials/interfaces/grain_boundary_hbn/2-solutions.webp "Solutions Analysis")

### 2.3. Review Selected Structure

Select and visualize the grain boundary structure (by default, the first solution is used):

```python
selected_structure = grain_boundaries[0]
visualize_materials(selected_structure, repetitions=[1, 1, 1])
```

## 3. Restore Missing Nitrogen Atom

Due to the `DISTANCE_TOLERANCE` setting, some nitrogen atoms at the boundary are removed. We need to restore them:

### 3.1. Add Missing Nitrogen

Use the adatom builder to add the missing nitrogen atom:

```python
from mat3ra.made.tools.build.defect import AdatomSlabDefectBuilder, AdatomSlabPointDefectConfiguration

config = AdatomSlabPointDefectConfiguration(
    crystal=selected_structure,
    chemical_element="N",
    position_on_surface=[0.5, 0.45],
    distance_z=0.01,
)

builder = AdatomSlabDefectBuilder()
adjusted_structure = builder.get_material(config)
```

### 3.2. Verify Final Structure

Review the completed structure:
1. Check the atomic positions at the boundary
2. Verify the restored nitrogen atom
3. Confirm overall structure integrity

![Final Structure](/images/tutorials/materials/interfaces/grain_boundary_hbn/3-final-structure.webp "Final Structure")

## 4. Save the Structure

The final structure can be:
1. Passed back to Materials Designer
2. [Saved or downloaded](../../../materials-designer/header-menu/input-output.md) in Material JSON format
3. Exported as a POSCAR file

## Interactive JupyterLite Notebook

The following JupyterLite notebook demonstrates the complete process. Select "Run" > "Run All Cells".

{% with origin_url=config.extra.jupyterlite.origin_url %}
{% with notebooks_path_root=config.extra.jupyterlite.notebooks_path_root %}
{% with notebook_name='specific_examples/grain_boundary_2d_hbn.ipynb' %}
{% include 'jupyterlite_embed.html' %}
{% endwith %}
{% endwith %}
{% endwith %}

## References

1. Qiucheng Li, et al., "Grain Boundary Structures and Electronic Properties of Hexagonal Boron Nitride on Cu(111)", ACS Nano 2015 9 (6), 6308-6315. [DOI: 10.1021/acs.nanolett.5b01852](https://doi.org/10.1021/acs.nanolett.5b01852)

## Tags

`grain-boundary`, `h-BN`, `2D-materials`, `interface`, `twist-angle`, `atom-restoration`

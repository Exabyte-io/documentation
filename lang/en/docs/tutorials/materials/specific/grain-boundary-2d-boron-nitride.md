---
tags:
  - grain-boundary
  - h-BN
  - 2D-materials
  - interface
  - twist-angle
  - atom-restoration

hide:
  - tags
# YAML header
render_macros: true
---

# 2D Grain Boundaries in Hexagonal Boron Nitride.

## Introduction.

This tutorial demonstrates the process of creating 2D grain boundary structures in hexagonal boron nitride (h-BN), based on the work presented in the following manuscript:

!!!note "Manuscript"
    Qiucheng Li, Xiaolong Zou, Mengxi Liu, Jingyu Sun, Yabo Gao, Yue Qi, Xiebo Zhou, Boris I. Yakobson, Yanfeng Zhang, and Zhongfan Liu, "Grain Boundary Structures and Electronic Properties of Hexagonal Boron Nitride on Cu(111)", ACS Nano 2015 9 (6), 6308-6315. [DOI: 10.1021/acs.nanolett.5b01852](https://doi.org/10.1021/acs.nanolett.5b01852){:target='_blank'}. [@Li2015]

We will focus on creating h-BN grain boundary structures similar to Figure 2c from the manuscript:

![h-BN Grain Boundary](/images/tutorials/materials/defects/grain_boundary_2d_boron_nitride/0-figure-from-manuscript.webp "h-BN Grain Boundary, FIG. 2c.")

## 1. Create Initial h-BN Structure.

### 1.1. Load h-BN Material.

Navigate to [Materials Designer](../../../materials-designer/overview.md) and import the h-BN material from the [Standata](../../../materials-designer/header-menu/input-output/standata-import.md).

1. Click on "Input/Output" menu
2. Select "Import from Standata"
3. Search for "Boron_Nitride" and select the 2D h-BN material

![Standata h-BN Import](/images/tutorials/materials/interfaces/twisted-bilayer-boron-nitride/standata-import-bn.png "Standata h-BN Import")


### 1.2. Launch JupyterLite Session.

Select "Advanced > [JupyterLite Transformation](../../../materials-designer/header-menu/advanced/jupyterlite-dialog.md)" to open JupyterLite.

### 1.3. Open and Configure Notebook.

Find and open `create_grain_boundary_film.ipynb`. Edit the grain boundary parameters in section 1.1:

`TARGET_TWIST_ANGLE = 9.0` -- As described in the manuscript.
`ANGLE_TOLERANCE = 0.5` -- Tolerance for twist angle matching, in degrees.
`BOUNDARY_GAP = 0.0` -- Gap between two phases in X direction, should be set to 0.0 for seamless boundary.
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

![Notebook Setup](/images/tutorials/materials/defects/grain_boundary_2d_boron_nitride/2-jl-setup-nb-gb.webp "Notebook Setup")

!!!note "Important Parameter"
    The `DISTANCE_TOLERANCE` parameter (1.43 Å) is larger than B-N distances at the one specific spot in the boundary. This will cause certain nitrogen atoms to be removed during structure generation, which we'll need to restore later.

## 2. Run the Notebook.

Run the notebook by selecting "Run" > "Run All Cells".

The notebook will generate the h-BN grain boundary structure based on the parameters provided.

![Initial h-BN Structure](/images/tutorials/materials/defects/grain_boundary_2d_boron_nitride/4-wave-result-gb.webp "Initial h-BN Structure")

## 3. Restore Missing Nitrogen Atom.

Due to the `DISTANCE_TOLERANCE` setting, one nitrogen atom at the boundary is removed. We need to restore it:

### 3.1. Add Missing Nitrogen.

Open JupyterLite Session and find `create_point_defect.ipynb` notebook.

Select the h-BN grain boundary structure as input material and configure the adatom defect parameters in the "1.1. Set Notebook Parameters" section:

```python
DEFECT_TYPE = "interstitial"  # (e.g. "vacancy", "substitution", "interstitial")
SITE_ID = None  # Site index of the defect
COORDINATE = [0.5, 0.45, 0.5]  # Position of the defect in crystal coordinates
APPROXIMATE_COORDINATE = None  # Approximate coordinates of the defect in crystal coordinates
CHEMICAL_ELEMENT = "N"  # Element to be placed at the site (ignored for vacancy)

SUPERCELL_MATRIX = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

# List of dictionaries with defect parameters
DEFECT_CONFIGS = [
    {
        "defect_type": DEFECT_TYPE,
        "coordinate": COORDINATE,
        "chemical_element": CHEMICAL_ELEMENT,
    }
]
```

![Notebook Setup](/images/tutorials/materials/defects/grain_boundary_2d_boron_nitride/5-jl-setup-nb-final-gb.webp "Notebook Setup")

### 3.2. Run the Notebook.

Run the notebook to add the missing nitrogen atom to the h-BN grain boundary structure.

![Final Structure Preview](/images/tutorials/materials/defects/grain_boundary_2d_boron_nitride/6-jl-result-preview-final-gb.webp "Final Structure Preview")

## 4. Pass Final Material to Materials Designer.

The user can pass the material with substitution defects in the current Materials Designer environment and save it.

![Final Material](/images/tutorials/materials/defects/grain_boundary_2d_boron_nitride/7-wave-result-final-gb.webp "Final Material")

Or the user can [save or download](../../../materials-designer/header-menu/input-output.md) the material in Material JSON format or POSCAR format.

## 5. Manual Adjustment.

To fill the gaps between two phases edge atoms can be adjusted manually in Materials Designer 3D editor.
The resulting structure should be similar to the one shown in the manuscript.

![Adjusted Structure](/images/tutorials/materials/defects/grain_boundary_2d_boron_nitride/8-wave-result-final-gb-relaxed.webp "Adjusted Structure")

## Interactive JupyterLite Notebook.

The following JupyterLite notebook demonstrates the complete process. Select "Run" > "Run All Cells".

{% with origin_url=config.extra.jupyterlite.origin_url %}
{% with notebooks_path_root=config.extra.jupyterlite.notebooks_path_root %}
{% with notebook_name='specific_examples/grain_boundary_2d_boron_nitride.ipynb' %}
{% include 'jupyterlite_embed.html' %}
{% endwith %}
{% endwith %}
{% endwith %}

## References.

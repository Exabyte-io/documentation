---
# YAML header
render_macros: true
---

# Terrace Steps on Platinum (111) Surface

## Introduction

This tutorial demonstrates two different approaches to creating terrace steps on platinum surfaces, based on the work presented in the following manuscript:

!!!note "Manuscript"
    Šljivančanin, Ž., & Hammer, B., "Oxygen dissociation at close-packed Pt terraces, Pt steps, and Ag-covered Pt steps studied with density functional theory." Surface Science, 515(1), 235–244. [DOI: 10.1016/s0039-6028(02)01908-8](https://doi.org/10.1016/s0039-6028(02)01908-8){:target='_blank'}.

We will demonstrate two methods:

1. Creating a Pt(211) surface which inherently contains steps
2. Creating a terrace step on a Pt(111) surface using the TerraceSlabDefectBuilder

## Method 1: Creating Pt(211) Step Surface

### 1.1. Import Base Material

First, we need to import the platinum material from Standata:

1. Navigate to [Materials Designer](../../../materials-designer/overview.md)
2. Click on "Input/Output" menu
3. Select "Import from Standata"
4. Search for "Pt" and select the bulk platinum material

### 1.2. Launch JupyterLite Environment

Select "Advanced > [JupyterLite Transformation](../../../materials-designer/header-menu/advanced/jupyterlite-dialog.md)" to open JupyterLite.

### 1.3. Configure Slab Parameters

Open a new notebook and set up the slab parameters:

```python
MATERIAL_NAME = "Pt"
MILLER_INDICES = (2, 1, 1)
THICKNESS = 6  # in atomic layers
VACUUM = 10.0  # in angstroms
XY_SUPERCELL_MATRIX = [[1, 0], [0, 1]]
USE_ORTHOGONAL_Z = True
USE_CONVENTIONAL_CELL = True
```

These parameters will create a Pt(211) surface with:

- 6 atomic layers thickness
- 10 Å vacuum region
- Orthogonal z-axis
- Using the conventional unit cell

### 1.4. Create the Slab

Use the following code to create the Pt(211) slab:

```python
from mat3ra.made.tools.build.slab import SlabConfiguration, create_slab, get_terminations

slab_configuration = SlabConfiguration(
    bulk=material,
    miller_indices=MILLER_INDICES,
    thickness=THICKNESS,
    vacuum=VACUUM,
    xy_supercell_matrix=XY_SUPERCELL_MATRIX,
    use_orthogonal_z=USE_ORTHOGONAL_Z,
    use_conventional_cell=USE_CONVENTIONAL_CELL,
)

slab_terminations = get_terminations(slab_configuration)
slab_211 = create_slab(slab_configuration, slab_terminations[0])
```

## Method 2: Creating Terrace Step on Pt(111)

### 2.1. Create Pt(111) Surface

First, create a Pt(111) surface with the following parameters:

```python
DEFAULT_SLAB_PARAMETERS = {
    "miller_indices": (1, 1, 1),
    "thickness": 6,
    "vacuum": 10.0,
    "use_orthogonal_z": True,
    "xy_supercell_matrix": [[2, 0], [0, 2]]
}
```

### 2.2. Configure Terrace Parameters

Set up the terrace defect configuration:

```python
CUT_DIRECTION = [0, 1, 1]  # Normal vector for cutting plane
PIVOT_COORDINATE = [0.5, 0.5, 0.5]  # Point the cutting plane passes through
NUMBER_OF_ADDED_LAYERS = 1  # Height of terrace
USE_CARTESIAN_COORDINATES = False
ROTATE_TO_MATCH_PBC = True  # Rotate to match periodic boundary conditions
```

### 2.3. Create the Terrace

Use TerraceSlabDefectBuilder to create the step:

```python
from mat3ra.made.tools.build.defect.builders import TerraceSlabDefectConfiguration, TerraceSlabDefectBuilder

config = TerraceSlabDefectConfiguration(
    crystal=slab_111,
    cut_direction=CUT_DIRECTION,
    pivot_coordinate=PIVOT_COORDINATE,
    number_of_added_layers=NUMBER_OF_ADDED_LAYERS,
    use_cartesian_coordinates=USE_CARTESIAN_COORDINATES,
    rotate_to_match_pbc=ROTATE_TO_MATCH_PBC
)

builder = TerraceSlabDefectBuilder()
terrace_slab = builder.get_material(config)
```

## Comparing the Methods

### Pt(211) Method

- Creates a surface with inherent steps
- Smaller unit cell
- Fixed step geometry
- Good for studying specific crystal faces

### Terrace Builder Method

- More flexible control over step placement
- Larger surface area available
- Customizable terrace height
- Better for complex step arrangements

## Interactive JupyterLite Notebook

The following JupyterLite notebook demonstrates both approaches. Select "Run" > "Run All Cells" to execute the notebook.

{% with origin_url=config.extra.jupyterlite.origin_url %}
{% with notebooks_path_root=config.extra.jupyterlite.notebooks_path_root %}
{% with notebook_name='specific_examples/defect_surface_step_platinum.ipynb' %}
{% include 'jupyterlite_embed.html' %}
{% endwith %}
{% endwith %}
{% endwith %}

## References

1. Šljivančanin, Ž., & Hammer, B., "Oxygen dissociation at close-packed Pt terraces, Pt steps, and Ag-covered Pt steps studied with density functional theory." Surface Science, 515(1), 235–244.

## Tags

`surface`, `platinum`, `terrace`, `step`, `slab`, `Pt(211)`, `Pt(111)`
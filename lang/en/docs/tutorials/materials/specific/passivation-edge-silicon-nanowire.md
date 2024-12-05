---
# YAML header
render_macros: true
---

# Passivation of Silicon Nanowire

## Introduction

This tutorial demonstrates the process of creating passivated silicon nanowires based on the work presented in the following manuscript, where the chemical gap tuning in silicon nanowires is studied.


!!!note "Manuscript"
    B. Aradi, L. E. Ramos, P. Deák, Th. Köhler, F. Bechstedt, R. Q. Zhang, and Th. Frauenheim,
    Theoretical study of the chemical gap tuning in silicon nanowires
    Phys. Rev. B 76, 035305 (2007)
    DOI: [10.1103/PhysRevB.76.035305](https://doi.org/10.1103/PhysRevB.76.035305)


We will focus on creating silicon nanowires with hydrogen passivation from FIG. 1.

Specifically, the material from FIG. 1. of the publication:

![Passivated Silicon nanowire](/images/tutorials/materials/passivation/passivation_edge_silicon_nanowire/0-figure-from-manuscript.webp "Passivated Silicon nanowire, FIG. 1.")


## 1. Create Silicon Nanowire

### 3.1. Load Silicon Material
First, we navigate to [Materials Designer](../../../materials-designer/overview.md) and import the silicon material from the [Standata](../../../materials-designer/header-menu/input-output/standata-import.md).

![Standata Silicon Import](/images/tutorials/materials/passivation/passivation_edge_silicon_nanowire/1-standata-silicon.webp "Standata Silicon Import")

### 3.2. Launch JupyterLite Session

Select the "Advanced > [JupyterLite Transformation](../../../materials-designer/header-menu/advanced/jupyterlite-dialog.md)" menu item to launch the JupyterLite environment.

![JupyterLite Dialog](/images/jupyterlite/md-advanced-jl.webp "JupyterLite Dialog")

### 3.3. Open `create_nanowire_custom_shapeipynb` notebook

Find `create_nanowire_custom_shape.ipynb` in the list of notebooks and click/double-click open it.

### 3.4. Open and modify the notebook

Next, we need to create a nanowire wit ha custom shape.

We'll specify the orientation of the nanowire with Miller indices of `(1,1,0)` as described in the manuscript.

Then we'll define a supercell matrix to add enough of material to cut the nanowire from: `[[3, 0, 0], [0, 2, 0], [0, 0, 2]]`.

Finally, we'll define a custom coordinate condition to create a rhombus-shaped nanowire with coordinates of the vertices corresponding to the corners of the rhombus.

The vertices of the rhombus are defined as follows:

Bottom:`[0.5, 0.2, 0]`, 
Left:`[0, 0.5, 0]`,
Top:`[0.5, 1, 0]`,
Right:`[1, 0.5, 0]`


For that, edit `create_nanowire_custom_shape.ipynb` notebook to modify the parameters by adding the following content to the "1.1. Set up nanowire parameters" cell:

```python
from typing import List
import numpy as np
from mat3ra.made.tools.utils.coordinate import CoordinateCondition

USE_CARTESIAN_COORDINATES = False # Flag to use Cartesian coordinates for the center and radii

# Wire parameters 
MILLER_INDICES= (1,1,0)  # Miller indices of the nanowire direction
SUPERCELL_MATRIX = [[3, 0, 0], [0, 2, 0], [0, 0, 2]] # Supercell matrix to cut the cylinder from
VACUUM = 10.0 # Vacuum thickness on the sides in Angstroms
ALIGN_ALONG_X = False

# Custom Coordinate Condition for
class CustomCoordinateCondition(CoordinateCondition):
    vertices: List[List[float]]

    def condition(self, coordinate: List[float]) -> bool:
        coord = np.array(coordinate)

        v0, v1, v2, v3 = np.array(self.vertices)

        vec0 = v1 - v0
        vec1 = v2 - v1
        vec2 = v3 - v2
        vec3 = v0 - v3

        # Calculate cross products
        cross0 = np.cross(vec0, coord[:2] - v0[:2])
        cross1 = np.cross(vec1, coord[:2] - v1[:2])
        cross2 = np.cross(vec2, coord[:2] - v2[:2])
        cross3 = np.cross(vec3, coord[:2] - v3[:2])

        # Check if point is inside the rhombus
        return (np.all(cross0 >= 0) and np.all(cross1 >= 0) and np.all(cross2 >= 0) and np.all(cross3 >= 0)) or \
               (np.all(cross0 <= 0) and np.all(cross1 <= 0) and np.all(cross2 <= 0) and np.all(cross3 <= 0))


# Define the vertices of the rhombus
vertices = [
    [0.5, 0.2, 0],
    [0, 0.5, 0],
    [0.5, 1, 0],
    [1, 0.5, 0]
]

condition = CustomCoordinateCondition(vertices=vertices).condition
```

Here's the visual of the updated content:

![Notebook setup](/images/tutorials/materials/passivation/passivation_edge_silicon_nanowire/2-jl-setup.webp "Notebook setup")

## 3.5. Run the Notebook and use the Material

Run the notebook by clicking `Run` > `Run All` in the top menu to run cells and wait for the results to appear.

![Run All](/images/jupyterlite/run-all.webp "Run All")

After running the notebook and submitting the material, the user will be able to visualize the structure of Silicon Nanowire.

![Silicon Nanowire](/images/tutorials/materials/passivation/passivation_edge_silicon_nanowire/3-silicon-nanowire.webp "Silicon Nanowire")

## 4. Create Hydrogen Passivation

### 4.1. Open `passivate_nanoribbon.ipynb` notebook

Next, we need to passivate the silicon nanowire with hydrogen atoms.

Open the `passivate_nanoribbon.ipynb` notebook and set:

`BOND_LENGTH = 1.46` -- Si-H bond length in Angstroms,

`COORDINATION_THRESHOLD = 3` -- Silicon that has less than 4 neighbors is undercoordinated in the silicon lattice, so all with 3 or less neighbors will be passivated,

`COORDINATION_SEARCH_RADIUS = 2.5` -- Search radius for neighbors for every atom, in Angstroms,

`MAX_BONDS_TO_PASSIVATE = 2`  -- Maximum number of bonds to saturate for undercoordinated atoms.


Copy the below content and edit the "1.1. Set up defect parameters" cell in the notebook as follows:

```python
# Enable interactive selection of coordination threshold
IS_COORDINATION_SELECTION_INTERACTIVE = False

MATERIAL_INDEX = 0

BOND_LENGTH = 1.46 # in Angstroms
PASSIVANT = "H" # Chemical symbol of the passivant
COORDINATION_SEARCH_RADIUS = 2.5 # in Angstroms (sphere in which to search for neighbors)
COORDINATION_THRESHOLD = 3 # Coordination number below which to passivate
MAX_BONDS_TO_SATURATE = 2 # Maximum number of bonds to saturate

SYMMETRY_TOLERANCE = 0.1 

SHOW_INTERMEDIATE_STEPS = True
CELL_REPETITIONS_FOR_VISUALIZATION = [1, 1, 1] 
```

Here's the visual of the updated content:

![Notebook setup](/images/tutorials/materials/passivation/passivation_edge_silicon_nanowire/5-jl-setup.webp "Notebook setup")

### 4.2. Run the Notebook

Run the notebook by clicking `Run` > `Run All` in the top menu to run cells and wait for the results to appear.

![Run All](/images/jupyterlite/run-all.webp "Run All")

### 4.3. Analyze the Results

After running the notebook, the user will be able to visualize the structure of Silicon Nanowire with substitution defects.

![Review the Results](/images/tutorials/materials/passivation/passivation_edge_silicon_nanowire/6-jl-result-preview.webp "Review the Results")

## 5. Pass the Material to Materials Designer

The user can pass the material with substitution defects in the current Materials Designer environment and save it.

![Final Material](/images/tutorials/materials/passivation/passivation_edge_silicon_nanowire/7-wave-result.webp "H-Passivated Silicon Nanowire")

Or the user can [save or download](../../../materials-designer/header-menu/input-output.md) the material in Material JSON format or POSCAR format.


## Interactive JupyterLite Notebook

The following JupyterLite notebook demonstrates the process of creating materials with substitution defects in silicon. Select "Run" > "Run All Cells".

{% with origin_url=config.extra.jupyterlite.origin_url %}
{% with notebooks_path_root=config.extra.jupyterlite.notebooks_path_root %}
{% with notebook_name='specific_examples/defect_point_substitution_silicon.ipynb' %}
{% include 'jupyterlite_embed.html' %}
{% endwith %}
{% endwith %}
{% endwith %}

## References

1. B. Aradi, L. E. Ramos, P. Deák, Th. Köhler, F. Bechstedt, R. Q. Zhang, and Th. Frauenheim,
   Theoretical study of the chemical gap tuning in silicon nanowires
   Phys. Rev. B 76, 035305 (2007)
   DOI: [10.1103/PhysRevB.76.035305](https://doi.org/10.1103/PhysRevB.76.035305)

## Tags

`defects`, `silicon`, `substitutional`, `point defects`, `hydrogen`, `passivation`

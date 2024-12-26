# Creating High-k Metal Gate Stack: Si/SiO2/HfO2/TiN

## Introduction

This tutorial demonstrates how to create a high-k metal gate stack heterostructure consisting of four materials: Si (substrate), SiO2 (gate oxide), HfO2 (high-k dielectric), and TiN (metal gate). We'll use a sequential approach combining Zero Strain Layer (ZSL) and simple interface builders.

The process involves first creating a critical Si/SiO2 interface using strain matching, then adding subsequent layers using simple interface builder to maintain the established structure.

!!!note "Process Overview"
    1. Create Si/SiO2 interface using ZSL matching (most critical interface)
    2. Add HfO2 layer using simple interface builder
    3. Add TiN layer using simple interface builder

## 1. Set Up Materials

First, navigate to Materials Designer and import the following materials from Standata:
- Silicon (Si)
- Silicon dioxide (SiO2)
- Hafnium dioxide (HfO2)
- Titanium nitride (TiN)

![Materials Import](/images/tutorials/materials/interfaces/highk_metal_gate/materials-import.webp "Materials Import")

## 2. Create Si/SiO2 Interface

### 2.1. Launch First JupyterLite Session

Select "Advanced > JupyterLite Transformation" and open the `create_interface_with_min_strain_zsl.ipynb` notebook.

### 2.2. Configure ZSL Interface Parameters

Modify the notebook parameters for the Si/SiO2 interface:

```python
# Global parameters
MAX_AREA = 200  # Maximum area for strain matching
MAX_AREA_RATIO_TOL = 0.25  # Maximum area ratio tolerance
MAX_ANGLE_TOLERANCE = 0.15  # Maximum angle tolerance
MAX_LENGTH_TOLERANCE = 0.15  # Maximum length tolerance

# Structure parameters
FILM_INDEX = 1  # SiO2
FILM_MILLER_INDICES = (1, 0, 0)
FILM_THICKNESS = 3
FILM_VACUUM = 0.0
FILM_USE_ORTHOGONAL_Z = True

SUBSTRATE_INDEX = 0  # Si
SUBSTRATE_MILLER_INDICES = (1, 0, 0)
SUBSTRATE_THICKNESS = 4
SUBSTRATE_VACUUM = 5.0
SUBSTRATE_USE_ORTHOGONAL_Z = True

INTERFACE_DISTANCE = 2.5  # Angstroms
INTERFACE_VACUUM = 5.0  # Angstroms
```

### 2.3. Run ZSL Interface Creation

Run the notebook to create the Si/SiO2 interface. The process will:
1. Generate possible interfaces with different strains
2. Plot strain vs. number of atoms
3. Select the optimal interface configuration

![Strain Plot](/images/tutorials/materials/interfaces/highk_metal_gate/strain-plot.webp "Strain vs Atoms Plot")

## 3. Add HfO2 Layer

### 3.1. Launch Second JupyterLite Session

Open the `create_interface_with_no_strain.ipynb` notebook for adding the HfO2 layer.

### 3.2. Configure Simple Interface Parameters

Set the parameters for adding HfO2:

```python
# Enable scaling of film to match substrate
ENABLE_FILM_SCALING = True
CREATE_SLABS = False

FILM_INDEX = 0  # HfO2
FILM_MILLER_INDICES = (0, 0, 1)
FILM_THICKNESS = 4
FILM_VACUUM = 0.5
FILM_XY_SUPERCELL_MATRIX = [[1, 0], [0, 2]]

SUBSTRATE_INDEX = 1  # Previous Si/SiO2 structure
SUBSTRATE_MILLER_INDICES = (0, 0, 1)
SUBSTRATE_THICKNESS = 1  # Use full previous structure
SUBSTRATE_VACUUM = 0.5

INTERFACE_DISTANCE = 2.5  # Angstroms
INTERFACE_VACUUM = 0.5  # Angstroms
```

### 3.3. Add HfO2 Layer

Run the notebook to add the HfO2 layer. The simple interface builder will:
1. Scale the HfO2 layer to match the substrate
2. Position it at the specified distance
3. Create the three-layer structure

## 4. Add TiN Layer

### 4.1. Configure TiN Layer Parameters

In the same notebook or a new instance, set parameters for adding TiN:

```python
FILM_INDEX = 1  # TiN
FILM_MILLER_INDICES = (0, 0, 1)
FILM_THICKNESS = 3
FILM_VACUUM = 10.0  # Final vacuum layer
FILM_USE_ORTHOGONAL_Z = True

SUBSTRATE_INDEX = 0  # Previous Si/SiO2/HfO2 structure
SUBSTRATE_MILLER_INDICES = (0, 0, 1)
SUBSTRATE_THICKNESS = 1
SUBSTRATE_VACUUM = 0.0

INTERFACE_DISTANCE = 2.5  # Angstroms
INTERFACE_VACUUM = 10.0  # Final vacuum spacing
```

### 4.2. Complete the Stack

Run the notebook one final time to add the TiN layer and complete the stack.

## 5. Final Structure

The final high-k metal gate stack should show:
1. Crystalline Si substrate
2. Well-matched Si/SiO2 interface
3. HfO2 high-k dielectric layer
4. TiN metal gate layer
5. Appropriate vacuum spacing

![Final Stack](/images/tutorials/materials/interfaces/highk_metal_gate/final-stack.webp "Complete High-k Metal Gate Stack")

## Important Notes

1. The Si/SiO2 interface is created using strain matching because it's the most critical interface for device performance
2. Subsequent layers use simple interface builder to maintain the established structure
3. Vacuum spacing is important between layers and at the top of the structure
4. Miller indices and thicknesses can be adjusted based on specific requirements
5. The final structure can be saved or exported for further analysis

## References

1. **D. A. Muller et al.**
    "The electronic structure at the atomic scale of ultrathin gate oxides"
    Nature 399, 758–761 (1999)
    [DOI: 10.1038/21602](https://doi.org/10.1038/21602)

2. **J. Robertson**
    "High dielectric constant gate oxides for metal oxide Si transistors"
    Reports on Progress in Physics 69, 327 (2006)
    [DOI: 10.1088/0034-4885/69/2/R02](https://doi.org/10.1088/0034-4885/69/2/R02)

## Tags

`interfaces`, `high-k`, `metal-gate`, `semiconductor`, `heterostructure`, `strain-matching`
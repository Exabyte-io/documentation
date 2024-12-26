# Creating High-k Metal Gate Stack: Si/SiO2/HfO2/TiN

## Introduction

This tutorial demonstrates how to create a high-k metal gate stack heterostructure consisting of four materials: Si (substrate), SiO2 (gate oxide), HfO2 (high-k dielectric), and TiN (metal gate). The process involves:
1. Creating individual slabs for HfO2 and TiN
2. Building the Si/SiO2 interface using strain matching
3. Adding the pre-created slabs sequentially using simple interface builder

## 1. Set Up Materials

First, navigate to Materials Designer and import from Standata:
- Silicon (Si)
- Silicon dioxide (SiO2)
- Hafnium dioxide (HfO2)
- Titanium nitride (TiN)

## 2. Create HfO2 and TiN Slabs

Before building the stack, we need to create properly terminated slabs for HfO2 and TiN.

### 2.1. Create HfO2 Slab

Open `create_slab_with_termination.ipynb` and set parameters:

```python
# HfO2 slab parameters
MILLER_INDICES = (0, 0, 1)
THICKNESS = 4  # atomic layers
VACUUM = 0.5  # Angstroms
XY_SUPERCELL_MATRIX = [[1, 0], [0, 2]]
USE_ORTHOGONAL_Z = True
USE_CONVENTIONAL_CELL = True

# Select termination (usually first one is fine)
TERMINATION_INDEX = 0
```

Run the notebook to create and save the HfO2 slab.

### 2.2. Create TiN Slab

Open another instance of `create_slab_with_termination.ipynb` for TiN:

```python
# TiN slab parameters
MILLER_INDICES = (0, 0, 1)
THICKNESS = 3  # atomic layers
VACUUM = 10.0  # Angstroms - more vacuum for final layer
XY_SUPERCELL_MATRIX = [[1, 0], [0, 1]]
USE_ORTHOGONAL_Z = True
USE_CONVENTIONAL_CELL = True

TERMINATION_INDEX = 0
```

Run the notebook to create and save the TiN slab.

## 3. Create Si/SiO2 Interface

### 3.1. Launch ZSL Interface Builder

Open `create_interface_with_min_strain_zsl.ipynb` and configure:

```python
# Global parameters
MAX_AREA = 200  # Maximum area for strain matching
MAX_AREA_RATIO_TOL = 0.25
MAX_ANGLE_TOLERANCE = 0.15
MAX_LENGTH_TOLERANCE = 0.15

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

### 3.2. Create Initial Interface

Run the notebook to create the Si/SiO2 interface. This is the most critical interface, so we use strain matching to optimize it.

## 4. Add HfO2 Layer

### 4.1. Configure Simple Interface Builder

Open `create_interface_with_no_strain.ipynb` and set:

```python
# Important: Disable slab creation since we're using pre-created slab
ENABLE_FILM_SCALING = True
CREATE_SLABS = False  # We already have our HfO2 slab

FILM_INDEX = 0  # Pre-created HfO2 slab
SUBSTRATE_INDEX = 1  # Si/SiO2 structure

# Interface parameters
INTERFACE_DISTANCE = 2.5  # Angstroms
INTERFACE_VACUUM = 0.5  # Angstroms
```

### 4.2. Add HfO2

Run the notebook to add the pre-created HfO2 slab to the Si/SiO2 structure.

## 5. Add TiN Layer

### 5.1. Configure Final Layer Addition

Use `create_interface_with_no_strain.ipynb` again:

```python
# Keep slabs disabled
ENABLE_FILM_SCALING = True
CREATE_SLABS = False  # Using pre-created TiN slab

FILM_INDEX = 1  # Pre-created TiN slab
SUBSTRATE_INDEX = 0  # Si/SiO2/HfO2 structure

# Final interface parameters
INTERFACE_DISTANCE = 2.5  # Angstroms
INTERFACE_VACUUM = 10.0  # Final vacuum spacing
```

### 5.2. Complete the Stack

Run the notebook to add the TiN layer and complete the stack.

## 6. Analysis and Verification

The final structure should show:
1. Well-matched Si/SiO2 interface (from ZSL matching)
2. Proper HfO2 slab orientation and termination
3. Correct TiN slab placement and vacuum spacing

Key characteristics to verify:
- Interface distances between layers
- Layer thicknesses
- Surface terminations
- Vacuum spacing

## Important Notes

1. Creating slabs separately ensures proper terminations and orientations
2. Setting `CREATE_SLABS = False` tells the interface builder to use pre-created slabs
3. The Si/SiO2 interface uses strain matching for optimal contact
4. Subsequent layers use simple interface builder to maintain structure
5. Vacuum spacing is critical, especially for the final TiN layer

## References

1. **D. A. Muller et al.**
    "The electronic structure at the atomic scale of ultrathin gate oxides"
    Nature 399, 758–761 (1999)

2. **J. Robertson**
    "High dielectric constant gate oxides for metal oxide Si transistors"
    Reports on Progress in Physics 69, 327 (2006)

## Tags

`slab-creation`, `interfaces`, `high-k`, `metal-gate`, `semiconductor`, `heterostructure`, `strain-matching`
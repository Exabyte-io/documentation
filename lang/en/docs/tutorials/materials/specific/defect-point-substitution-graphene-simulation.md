---
tags:
  - defects
  - graphene
  - substitutional
  - point-defects
  - nitrogen
  - band-structure
  - D-0D-SUB

hide:
  - tags
# YAML header
render_macros: true
---

# Substitutional Point Defects in Graphene (Band Structure)

## Introduction

This tutorial demonstrates the calculation of the band structure for graphene with vacancy and N substitutions, reproducing results from the following manuscript:

!!!note "Manuscript"
    Yoshitaka Fujimoto and Susumu Saito, "Formation, stabilities, and electronic properties of nitrogen defects in graphene", Physical Review B, 2011. [DOI: 10.1103/PhysRevB.84.245446](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.84.245446){:target='_blank'}. [@Yoshitaka2011]

This tutorial builds upon the [Substitutional Point Defects in Graphene](defect-point-substitution-graphene.md) tutorial, where we created the N-doped graphene structure. Here, we calculate its electronic band structure using Quantum ESPRESSO and compare with the published results.

The calculation uses density functional theory (DFT) with the local density approximation (LDA) and norm-conserving pseudopotentials, following the methodology described in the manuscript.

## Prerequisites

Before starting this tutorial, you should:

1. Complete the [Substitutional Point Defects in Graphene](defect-point-substitution-graphene.md) tutorial to create the N-doped graphene structure, OR
2. Have the N-doped graphene material file saved in the `uploads` folder

## Workflow Overview

The band structure calculation workflow consists of the following steps:

1. **Set up the environment and parameters**: Configure material, workflow, and computational settings
2. **Authenticate and initialize API client**: Connect to the platform
3. **Load material**: Import the N-doped graphene structure from file or Standata
4. **Create workflow**: Set up the band structure calculation workflow with optional relaxation
5. **Configure compute resources**: Select cluster, queue, and processor settings
6. **Create and submit job**: Assemble and run the calculation
7. **Monitor job status**: Wait for completion
8. **Retrieve and visualize results**: Display the calculated band structure

## Calculation Parameters

### Run Profiles

The notebook supports two run profiles:

- **Debug mode**: Quick validation run with minimal k-point sampling and no relaxation. Completes in a few minutes.
- **Production mode**: Paper-quality settings with structural relaxation and dense k-point sampling, following Fujimoto & Saito (2011).

### DFT Parameters

The calculation uses the following DFT parameters (consistent with the manuscript):

- **Functional**: LDA (Perdew-Zunger parametrization)
- **Pseudopotentials**: Norm-conserving (ONCV)
- **Energy cutoff**: 50 Ry for wavefunctions, 200 Ry for density
- **K-point grid** (production): 6×6×1 for SCF and relaxation
- **K-path**: K → Γ → M → K (high-symmetry path in hexagonal Brillouin zone)

### Relaxation Settings

In production mode, the structure is relaxed before the band structure calculation to optimize atomic positions while maintaining the cell parameters.

## Step-by-Step Instructions

### 1. Open the Notebook

Navigate to the API examples repository and open the band structure calculation notebook:

```
other/materials_designer/specific_examples/defect_point_substitution_graphene_simulation.ipynb
```

### 2. Configure Parameters

In cell 1.2, set the run profile and material parameters:

```python
# Switch between "debug" and "production" modes
RUN_PROFILE = "debug"  # Change to "production" for paper-quality results

# Material parameters
FOLDER = "./uploads"
MATERIAL_NAME = "N-doped Graphene"

# Workflow parameters
APPLICATION_NAME = "espresso"
MODEL_SUBTYPE = "lda"
```

For first-time use, start with `"debug"` mode to validate the workflow. Once confirmed working, switch to `"production"` for final results.

### 3. Set DFT Parameters

The specific DFT parameters are configured in cell 1.3:

```python
# Pseudopotential settings
PSEUDOPOTENTIAL_TYPE = "nc"
FUNCTIONAL = "pz"

# Energy cutoffs
ECUTWFC = 50
ECUTRHO = 4 * ECUTWFC

# K-point sampling and path (automatically set based on RUN_PROFILE)
```

### 4. Run the Notebook

Execute all cells by selecting `Run` > `Run All` from the menu.

The notebook will:

1. Authenticate with the platform
2. Load the N-doped graphene material
3. Create and configure the band structure workflow
4. Submit the calculation job
5. Monitor the job status
6. Display the results when complete

### 5. Monitor Progress

The notebook includes automatic job monitoring with status updates. In debug mode, the calculation typically completes in 5-10 minutes. Production mode may take several hours depending on the cluster load.

### 6. Analyze Results

Once the job completes, the band structure will be displayed automatically. The plot shows:

- Energy bands along the K → Γ → M → K path
- Fermi level position
- Band gap (if present)
- Comparison with pristine graphene (if available)

## Expected Results

The calculated band structure should show:

- **Modified electronic structure** near the Fermi level due to nitrogen substitution
- **Breaking of symmetry** compared to pristine graphene
- **Localized states** introduced by the nitrogen defects
- **Band gap opening** (depending on defect configuration)

These results can be compared with Figure 3 in the Fujimoto & Saito manuscript, which shows the electronic band structure for various nitrogen defect configurations in graphene.

## Customization Options

### Modifying K-path

To change the k-point path for band structure calculation, edit the `KPATH` parameter in cell 1.3:

```python
KPATH = [
    {"point": "K", "steps": 20},
    {"point": "Г", "steps": 20},
    {"point": "M", "steps": 20},
    {"point": "K", "steps": 1},
]
```

### Adjusting Computational Resources

Modify the compute parameters in cell 1.2:

```python
CLUSTER_NAME = "101"  # Your cluster name
QUEUE_NAME = QueueName.D  # Queue selection
PPN = 1  # Processors per node
```

### Adding or Removing Relaxation

Toggle structural relaxation by changing the `ADD_RELAXATION` flag (automatically set by `RUN_PROFILE`):

```python
ADD_RELAXATION = True  # Enable relaxation
RELAXATION_KGRID = [6, 6, 1]  # K-point grid for relaxation
```

## Troubleshooting

### Material Not Found

If the material is not found in the uploads folder:

1. Run the [defect creation notebook](defect-point-substitution-graphene.md) first
2. Ensure the material is saved with the exact name "N-doped Graphene"
3. Check that the material file is in the correct `uploads` folder

### Job Fails or Takes Too Long

If the job fails or runs longer than expected:

1. Start with debug mode to validate the setup
2. Check the job logs for error messages
3. Verify that energy cutoffs are appropriate for the pseudopotentials
4. Reduce k-point sampling if needed for testing

### Convergence Issues

If the calculation doesn't converge:

1. Increase the number of SCF iterations
2. Adjust mixing parameters
3. Check that the structure is reasonable (no overlapping atoms)
4. Verify pseudopotential compatibility

## Interactive JupyterLite Notebook

The following JupyterLite notebook demonstrates the complete workflow for calculating the band structure of N-doped graphene. Select "Run" > "Run All Cells".

{% with origin_url=config.extra.jupyterlite.origin_url_lab %}
{% with notebooks_path_root=config.extra.jupyterlite.notebooks_path_root %}
{% with notebook_name='specific_examples/defect_point_substitution_graphene_simulation.ipynb' %}
{% include 'jupyterlite_embed.html' %}
{% endwith %}
{% endwith %}
{% endwith %}

## References

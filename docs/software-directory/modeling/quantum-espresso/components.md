# Components

We present in this page the different [components](../../../software/components.md) (executables and flavors) comprised within the [Quantum ESPRESSO](overview.md) distribution package. 

Only those components implemented on our platform to date are mentioned here, as can be inspected from the lists of available executables and flavors under the [Unit Editor Interface](../../../workflow-designer/unit-editor.md#application).

!!!warning "Implementation on our platform"
    The user who wishes for additional functionality to be added to our platform in future should express so via a [support request](../../../ui/support.md).

## Executables

The core plane wave DFT functions of QE are provided by the PWscf (Plane-Wave Self-Consistent Field) component, further referred to under the name of its [executable](../../../software/components.md#executables) `pw.x`. Further components are included in the distribution package, such as the `ph.x` executable for performing phonon calculations via the density functional perturbation theory and linear response theoretical formalisms [^8].

Complete documentation about the software package can be found in its corresponding website [^1](overview.md#links). The input file description for `pw.x` can be found in Ref. [^2]. The package-specific documentation [^3] contains links to input descriptions for other [executables](../../../software/components.md#executables) as well.

The following executables have been implemented on our platform so far.

- `pw.x`:
- `projwfc.x`:
- `q2r.x`:
- `dynmat.x`:
- `matdyn.x`:
- `pp.x`:
- `ph.x`:
- `dos.x`:
- `bands.x`:

## Flavors

The `pw.x` executable for the Quantum ESPRESSO modeling application, for example, allows for the execution of the following different types of calculation [flavors](../../../software/components.md#flavors) [^4], to be specified in the corresponding input file.

- `scf`: "self-consistent field" [total ground-state energy](../../../properties-directory/scalar/total-energy.md) calculation    
- `nscf`: for further processing of the results of non-scf calculations (for instance, in DOS calculations)
- `bands`: [electronic band structure](../../../properties-directory/non-scalar/bandstructure.md) calculation
- `relax`: optimization of the atomic positions to relax the inter-atomic forces 
- `vc-relax`: "variable-cell" [structural relaxation and optimization](../../../workflows/addons/structural-relaxation.md)

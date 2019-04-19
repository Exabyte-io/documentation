# Components
 
We present in this page the different [components](../../../software/components.md) (executables and flavors) comprised within the [VASP](overview.md) distribution package. 
 
Only those components implemented on our platform to date are mentioned here, as can be inspected from the lists of available executables and flavors under the [Unit Editor Interface](../../../workflow-designer/unit-editor.md#application).
 
!!!warning "Implementation on our platform"
     The user who wishes for additional functionality to be added to our platform in future should express so via a [support request](../../../ui/support.md).
     
## Executables

the VASP package is composed of one main `vasp` [executable](../../../software/components.md#executables) only, through which all calculation [flavors](../../../software/components.md#flavors) explained in what follows can be performed.

## Flavors

The following computation [flavors](../../../software/components.md#flavors) are available within VASP.

- `vasp`: "self-consistent field" [total ground-state energy](../../../properties-directory/scalar/total-energy.md) calculation.
- `vasp_vc_relax_conv`: 
- `vasp_nscf`: for further processing of the results of non-scf calculations (for instance, in DOS calculations).
- `vasp_zpe`: for [Zero Point Energy](../../../properties-directory/scalar/zero-point-energy.md) calculations.
- `vasp_kpt_conv`: for performing a [k-points convergence study](../../../models/auxiliary-concepts/reciprocal-space/convergence.md).
- `vasp_relax`: optimization of the atomic positions to relax the inter-atomic forces. 
- `vasp_vc_relax`: "variable-cell" [structural relaxation and optimization](../../../workflows/addons/structural-relaxation.md).
- `vasp_bands`: [electronic band structure](../../../properties-directory/non-scalar/bandstructure.md) calculation.
- `vasp_hse`: for performing calculations using the HSE hybrid exchange-correlation functional.
- `vasp_bands_hse`: [electronic band structure](../../../properties-directory/non-scalar/bandstructure.md) calculations using HSE.
- `vasp_nscf_hse`: for further processing of the results of non-scf HSE calculations.

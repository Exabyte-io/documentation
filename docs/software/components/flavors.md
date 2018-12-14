# Flavors

The [executables](executables.md) for running [modeling applications](../applications.md) may in turn be composed of numerous distinct **Flavors**, implementing different forms and types of materials computations such as total ground-state energy calculations, structural relaxations or electronic bandstructure calculations.

## Example 

The "pw.x" executable for the [Quantum ESPRESSO](../../software-directory/modeling/quantum-espresso.md) modeling application, for example, allows for the execution of the following different types of calculation flavors [^1], to be specified in the executable's corresponding input script.

- 'scf': "self-consistent field" [total ground-state energy](../../properties-directory/scalar/total-energy.md) calculation    
- 'nscf': for further processing of the results of non-scf calculations (for instance, in DOS calculations)
- 'bands': [electronic band structure](../../properties-directory/non-scalar/bandstructure.md) calculation
- 'relax': optimization of the atomic positions to relax the inter-atomic forces 
- 'md': ab-initio molecular dynamics simulation
- 'vc-relax': "variable-cell" [structural relaxation and optimization](../../workflows/addons/structural-relaxation.md)
- 'vc-md': "variable-cell" ab-initio molecular dynamics simulation

!!!warning "Implementation on our platform"
    Only a subset of the above flavors have been implemented on our platform to date, as can be inspected from the list of available flavors under the [Unit Editor Interface](../../workflow-designer/unit-editor.md#application). The user who wishes for additional functionality to be added to our platform in future should express so via a [support request](../../ui/support.md).
           
## Links

[^1]: [PWscf User’s Guide, Official Documentation](https://www.quantum-espresso.org/Doc/pw_user_guide.pdf)

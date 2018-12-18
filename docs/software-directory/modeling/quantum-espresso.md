# Quantum ESPRESSO

Quantum ESPRESSO (QE, also referred to as **"espresso"** in our platform) is a software suite for ab-initio quantum methods performing general electronic-structure calculations and materials modeling. It is distributed for free under the GNU General Public License. Quantum ESPRESSO is based on [Density Functional Theory](../../models-directory/dft/overview.md), [plane wave basis sets and pseudopotentials](../../methods-directory/pseudopotential/overview.md) (both norm-conserving and ultrasoft). 

## Executables

The core plane wave DFT functions of QE are provided by the PWscf (Plane-Wave Self-Consistent Field) component, further referred to under the name of its [executable](../../software/parameters.md#executables) `pw.x`. Further components are included in the distribution package, such as the `ph.x` executable for performing phonon calculations via the density functional perturbation theory and linear response theoretical formalisms [^8].

Complete documentation about the software package can be found in its corresponding website [^1]. The input file description for `pw.x` can be found in Ref. [^2]. The package-specific documentation [^3] contains links to input descriptions for other [executables](../../software/parameters.md#executables) as well.

## Flavors

The `pw.x` executable for the Quantum ESPRESSO modeling application, for example, allows for the execution of the following different types of calculation [flavors](../../software/parameters.md#flavors) [^4], to be specified in the corresponding input file.

- 'scf': "self-consistent field" [total ground-state energy](../../properties-directory/scalar/total-energy.md) calculation    
- 'nscf': for further processing of the results of non-scf calculations (for instance, in DOS calculations)
- 'bands': [electronic band structure](../../properties-directory/non-scalar/bandstructure.md) calculation
- 'relax': optimization of the atomic positions to relax the inter-atomic forces 
- 'md': ab-initio molecular dynamics simulation
- 'vc-relax': "variable-cell" [structural relaxation and optimization](../../workflows/addons/structural-relaxation.md)
- 'vc-md': "variable-cell" ab-initio molecular dynamics simulation

!!!warning "Implementation on our platform"
    Only a subset of the above flavors have been implemented on our platform to date, as can be inspected from the list of available flavors under the [Unit Editor Interface](../../workflow-designer/unit-editor.md#application). The user who wishes for additional functionality to be added to our platform in future should express so via a [support request](../../ui/support.md).
    
## Supported Versions

We support 5.2.1, 5.4.0, 6.0.0, and 6.3.0 versions of Quantum ESPRESSO.

## Links

[^1]: [Official Quantum ESPRESSO website](https://www.quantum-espresso.org/)
[^2]: [Input file description of the pw.x code](https://www.quantum-espresso.org/Doc/INPUT_PW.html)
[^3]: [Quantum ESPRESSO package-specific documentation](https://www.quantum-espresso.org/resources/users-manual/specific-documentation)
[^4]: [PWscf User’s Guide, Official Documentation](https://www.quantum-espresso.org/Doc/pw_user_guide.pdf)
[^7]: [Official Quantum ESPRESSO GitHub repository](https://github.com/QEF/q-e/tags)
[^8]: [Calculation of Phonon Dispersions on the Grid Using Quantum ESPRESSO](http://users.ictp.it/~pub_off/lectures/lns024/10-giannozzi/10-giannozzi.pdf)

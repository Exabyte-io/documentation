# Vienna Ab initio Simulation Package

The Vienna Ab initio Simulation Package, better known as VASP, is a package for performing ab-initio electronic structure calculations and molecular dynamics, using either Vanderbilt ultra-soft pseudopotentials or the projector-augmented wave (PAW) method, together with a plane wave basis set. 

The underlying theoretical model is Density Functional Theory (DFT), but the code also allows for the use of post-DFT corrections, such as hybrid functionals mixing DFT and Hartree–Fock exchange, many-body perturbation theory (the GW method), and dynamical electronic correlations within the Random Phase Approximation (RPA).

Complete information and documentation about the VASP code can be found in its corresponding website [^1], [^2], [^3].

!!!warning "License Requirements"
    VASP is a proprietary software, and as such it requires a license in order to be operated. All users who would like to use this code are advised to send us a [support request](../../../ui/support.md) so that we can check their existing licenses. Contact us about an on-demand license option for interested parties.

## Supported Versions

We provide support and implementations for both the 5.3.5 and 5.4.4 versions of VASP.

!!! note "Default Pseudopotentials"
    As mentioned in the [dedicated section](../../../methods-directory/pseudopotential/default.md), the list of default pseudopotentials follows the versions of the VASP software itself (versions 5.2 and 5.4).
    
## [Components](components.md)

We introduce the different [components](../../../software/components.md) which are part of the VASP software distribution [in this page](components.md).

## [Compute Parameters](compute-parameters.md)

We explain the specific aspects of [compute parameters](../../../infrastructure/compute/parameters.md) [here](compute-parameters.md).

## [Data](data.md)

The [structured representation](../../../data-structured/overview.md) for VASP is explained [in this page](data.md).

## Links

[^1]: [Official VASP website](https://www.vasp.at/)
[^2]: [Official VASP Documentation Manual, pdf copy](http://cms.mpi.univie.ac.at/vasp/vasp.pdf)
[^3]: [Official VASP Documentation Manual, online version](http://cms.mpi.univie.ac.at/vasp/vasp/vasp.html)

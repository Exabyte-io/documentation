# Modeling Engines

Material Modeling engines are used in computational materials science to implement the [computational methods](../../methods/overview.md) available for calculating [material properties](../../properties/overview.md) of interest [^1] [^2]. 

These engines may be based on such [theoretical models](../../models/overview.md) as Hartree-Fock Theory, Density Functional Theory (DFT), classical Molecular Dynamics, Quantum Monte Carlo or semi-empirical Quantum Chemistry methods. They can be of either open-source or proprietary nature, and are typically comprised of numerous [executables](../components/executables.md), for implementing the different computation [flavors](../components/flavors.md) that they were designed to support.

## Structured Representations

We present in what follows the [JSON-based structured representations](../../data-structured/overview.md) for those modeling engines which are [supported on our platform](../../software-directory/overview.md).

### Quantum ESPRESSO

This is the structured representation for the [Quantum ESPRESSO](../../software-directory/modeling/quantum-espresso.md) modeling software.

```json tab="Schema" 
{!schema/software/modeling/espresso.json!}
```

```json tab="Example" 
{!example/software/modeling/espresso.json!}
```

### VASP

The data structure for the [VASP](../../software-directory/modeling/vasp.md) modeling code can be found below.

```json tab="Schema" 
{!schema/software/modeling/vasp.json!}
```

```json tab="Example" 
{!example/software/modeling/vasp.json!}
```

## Links

[^1]: [Wikipedia List of quantum chemistry and solid-state physics software, Website](https://en.wikipedia.org/wiki/List_of_quantum_chemistry_and_solid-state_physics_software)

[^2]: [Wikipedia Comparison of software for molecular mechanics modeling, Website](https://en.wikipedia.org/wiki/Comparison_of_software_for_molecular_mechanics_modeling)

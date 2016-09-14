<!-- TODO by MH
For all of the characteristic properties:
        explain how we assert fidelity
-->
Currently we support the characteristic property simulations [**here**](../materials/characteristic-properties)

# Core Properties

**VASP**: requires the standard INCAR, KPOINTS, POTCAR, & POSCAR files

**Quantum Espresso**: requires the standard *.in and *.upf files only

## [Electronic wave functions](../materials/characteristic-properties#electronic-wave-functions)
Please see the [first simulation tutorial](../tutorials/first-simulation.md) for more details.

## [Electronic energies](../materials/characteristic-properties#electronic-energies)
Please see the [first simulation tutorial](../tutorials/first-simulation.md) for more details.

Both electronic energies and wave functions are calculated concurrently in the example below:

# [Principal Properties](../materials/characteristic-properties#principal-properties)
Please see the [first simulation tutorial](../tutorials/first-simulation.md) for more details.
Total Energy, Entropy, Fermi energy, Atomic forces, Stress tensor, Average pressure, and Charge density are all usually calculated concurrently as shown in the example below:

# [Derived Properties](../materials/characteristic-properties#derived-properties)
**VASP**: requires the standard INCAR, KPOINTS, POTCAR, & POSCAR files unless otherwise noted

**Quantum Espresso**: requires the standard *.in and *.upf files only unless otherwise noted

## [Electronic Properties](../materials/characteristic-properties#electronic-properties)

### [Band Structure](../materials/characteristic-properties#band-structure)
Please see the [band structure tutorial](../tutorials/band-structure.md) for more details.

**VASP**: requires INCAR, KPOINTS, POTCAR, & POSCAR files as well a second version of the KPOINTS file and the CHGCAR file for the second step of the simulation

**Quantum Espresso**: requires the standard *.in and *.upf files for pw.x execution and alternate *.in and input wavefunctions and charge density for executions of bands.x


### [Band Gap](../materials/characteristic-properties#band-gap)
Please see the [band gap tutorial](../tutorials/band-gap.md) for more details.

### [Density of States and Partial DOS](../materials/characteristic-properties#sensity-of-states-and-partial-dos)
Please see the [density of states tutorial](../tutorials/density-of-states.md) for more details.

### [Fermi surface](../materials/characteristic-properties#fermi-surface)
Please see the [Fermi surface tutorial](../tutorials/fermi-surface.md) for more details.

## [Chemistry Properties](../materials/characteristic-properties#chemical-properties)

### [Formation energy at 0K](../materials/characteristic-properties#formation-energy-at-0K)
Please see the [formation energy tutorial](../tutorials/formation-energy.md) for more details.

## [Vibrational Properties](../materials/characteristic-properties#vibrational-properties)

### [Zero Point Energy](../materials/characteristic-properties#zero-point-energy)
Please see the [zero point enegry tutorial](../tutorials/zero-point-energy.md) for more details.

**Quantum Espresso**: requires the standard *.in and *.upf files as well as a ph.in input file as well as the wavefunctions from the first step in the methodology

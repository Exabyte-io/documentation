<!-- TODO: recycle or remove on cleanup -->

Extraction of some characteristic properties require multiple calculations.  We automate these multi-step workflows. Currently we have two of such workflows for formation energy and band gap described below.  We provide a convenient way to add both k-point convergence and relaxation as initial steps in any subsequent property calculation.

<hr>


# Formation Energy

We pre-calculated the total energy and zero point energy of all elemental pseduopotentials supported and saved these values for use during formation energy calculation. Please note that the reference state for the elements is at 0 K and 0 pressure. The formation energy of a material as well as the reference state total and zero point energy for each element in the material are displayed in the "Results" tab.

Please see the [formation energy tutorial](../tutorials/formation-energy.md) for more details. Below is the formula used to calculate formation energy:

```tex
    E_fmt = E_tot (compound) - \sum {all elements} \sum {all atoms for element} (E_zpe + E_tot)
```

above, `E_fmt` and `E_tot`, `E_zpe` are the formation energy, total energy and zero point energy for the compound and lowest energy elemental structures.

!!! warning "Formation energy automation"
    We support calculation of formation energy for the pseudopotentials that we currently provide ([1](#links) and [2](#links)).  If you chose to import your own pseudopotentials, you will need to manually calculate your reference total and zero point energies at converged k-point densities at the moment. In the future we will automate this entire flow for user-imported pseudopotentials as well.

<hr>

# Band Gap

The band gap is defined as the energy difference between the highest occupied energy state of a material and the lowest unoccupied energy state of the material.  However, a band gap can either be a direct or indirect band gap.  Direct band gap means the minimum change in energy between occupied and unoccupied states at the same k-point.  The indirect band gap means the minimum change in energy between occupied and unoccupied states at different k-points.  The indirect band gap could potentially be smaller than the direct band gap.  We have automated the search for both types of band gaps.

Please see the [band gap tutorial](../tutorials/dft/band-gap.md) for more details.

<hr>

# Links

1. [PAW pseudopotentials for VASP](http://cms.mpi.univie.ac.at/vasp/vasp/PAW_potentials.html)
2. [GBRV pseudopotentials for Quantum ESPRESSO](https://www.physics.rutgers.edu/gbrv/)


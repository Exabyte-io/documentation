<!-- TODO by MH -->

# Model
A model is an entity that contains scientifically valuable information about the approximations used for a simulation.

# Method
A model may have multiple numerical methods of of implementation of the model.  Since method is a numerical property, it has a certain [precision](#precision).  A method is implemented inside a [simulation engine](#simulation-engine) (or application/app), and a single simulation engine can contain also use one or more methods (QuantumWise, NWChem, and VASP).

If we use Newtonian mechanics as the model, then the method would be the algorithmic implementation of calculating the multiple between m and a in the F = ma equation.

# Simulation Engine
A simulation engine is an implementation of a simulation algorithm in software.
## Currently Exabyte.io supports:
### Quantum ESPRESSO
### VASP
## Upcoming simulation engines supported:
### BerkelyGW
### NWChem
## Future simulation engines planned:
### LAMMPS
### OMEN/NEMO
### NEGF/DFT

# Precision
Precision characterizes the degree of numerical approximation.  For the planewave pseudopotential method the input parameters that affect precision are:
## k-point sampling
## Number of points in irreducible Brillouin zone (N kIBZ)
## Additional parameters - may affect precision significantly
### Electronic occupations (smearing, tetrahedra, fixed)
### Smearing (gaussian, Methfessel-Paxton, Marzari-Vanderbilt, Fermi-Dirac)
### Electronic wavefunction cutoff energy (or kinetic energy cutoff) - (e_cut_wfc)
### Electronic density cutoff energy (e_cut_den)

# Accuracy
Accuracy measures  the degree of proximity between the result of a simulation to the results of an experimental measurement. When one model is more accurate than another one, the end results of a simulation based on the first model is closer to an experimental value.

For Density Functional Theory Model. the input parameters that affect accuracy include:
## Electronic exchange and correlation functional used in the pseudopotentials (pseudo_xc_type)
## Type of the model applied (DFT LDA, DFT GGA, DFT LDA + U, DFT GGA + U, DFT HSE, DFT LDA + GW, DFT GGA + GW - as explained on wikipedia

!!! warning "Accuracy and Precision are unique"
    Although Accuracy and Precision are often used interchangeably, they have different meanings.

Accuracy is a direct property of the Model and can be thought about as a limit for when all computational parameters are at their optimum values.
Precision is a characteristic of a particular computational implementation of the Model (property of Method) and is directly dependent on the input parameters.

If we use Newtonian's laws as the model, then the Accuracy would be limited by the relativistic effects - for example, for a spaceship it is important to introduce corrections beyond the Newtonian laws because the accuracy of it does not match experimentally found flight trajectories.
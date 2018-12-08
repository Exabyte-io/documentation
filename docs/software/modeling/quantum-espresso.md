# Quantum ESPRESSO

Quantum ESPRESSO (QE, also referred to as "espresso" in our platform) is a software suite for ab-initio quantum methods performing general electronic-structure calculations and materials modeling. It is distributed for free under the GNU General Public License. Quantum ESPRESSO is based on Density Functional Theory, plane wave basis sets, and pseudopotentials (both norm-conserving and ultrasoft). 

The core plane wave DFT functions of QE are provided by the PWscf (Plane-Wave Self-Consistent Field) component further reffered to as "pw.x". Further components are included in the distribution package, such as the Ph module for performing phonon calculations via the density functional perturbation theory and linear response theoretical formalisms.

Complete documentation about the software package can be found in its corresponding website [[1](#links)]. The input file description for pw.x can be found in Ref. [[2]](#links). The package-specific documentation [[3]](#links) contains links to input descriptions for other executables as well.

## Default settings

### Default Pseudopotentials

The list of pseudopotentials currently available on the Quantum Espresso website can be found in Ref [[4]](#links) below. Our platform provides the GBRV [[5]](#links) set at version 1.5 by default.

## Links

1. [Official Quantum ESPRESSO website](https://www.quantum-espresso.org/)
2. [Input file description of the pw.x code](https://www.quantum-espresso.org/Doc/INPUT_PW.html)
3. [Quantum ESPRESSO package-specific documentation](https://www.quantum-espresso.org/resources/users-manual/specific-documentation)
4. [Pseudopotentials list for Quantum ESPRESSO](http://www.quantum-espresso.org/pseudopotentials/)
5. [GBRV pseudopotentials, Rutgers](https://www.physics.rutgers.edu/gbrv/)

6. [Official Quantum ESPRESSO GitHub repository](https://github.com/QEF/q-e/tags)
7. [Calculation of Phonon Dispersions on the Grid Using Quantum ESPRESSO](http://users.ictp.it/~pub_off/lectures/lns024/10-giannozzi/10-giannozzi.pdf)


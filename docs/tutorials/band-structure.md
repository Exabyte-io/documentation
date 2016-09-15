<!-- TODO by MH -->
We will calculate the band structure of Silicon.  Please note that this calculation will be performed using standard DFT-LDA and therefore underprediction of the band gap is to be expected.  Further modifications to the input files and settings to correctly predict the band structure and the distance between the highest occupied band and lowest unoccupied band are possible and will be explored and implemented in the future.

Si is the default material, so if you choose "Create a Job" from the sidebar on the home page Si will automatically be loaded.  Under workflow chose the "Bandstructure" for either VASP or Quantum Espresso.

In Quantum Espresso, this will result in 3 workflow units being automatically populated.  The first unit specifies the settings for the self-consistent calculation of the eigenvalues and wave functions.  The second unit calculation is a non self-consitent calculation using the wave functions and charge density of the previous calculation.  The 3rd unit calculates the bands energy at each of the kpoints in the non self-consistent calculation.

If we examine the input files for each step in the workflow we will see that the k-point path for Si has been defined along special high symmetry k-points.  Currently we only support the automatic generation of high symmetry k-points for FCC structures.  Support for high symmetry k-point path sampling for band structure calculations of all 14 lattice types will be supported in a future release.

As each workflow is executing, you can monitor it's progress live by monitoring both the output of the executable as well as a graphical representation of the total energy convergence on the Status tab under each execution's sub-tab.

When all 3 units are complete, switching to the Results tab and the sub-tab for the final execution unit will show the band structure of silicon as a function of the special k-point paths chosen
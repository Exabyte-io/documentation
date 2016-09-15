<!-- TODO by MH -->

We will calculate the electon density mesh of Silicon.  The electron density mesh is a pre-requisite for any band structure calculation so this tutorial is closely related to the [band structure tutorial](band-structure.md)

Si is the default material, so if you choose "Create a Job" from the sidebar on the home page Si will automatically be loaded.  Under workflow chose the "Bandstructure" for either VASP or Quantum Espresso.

<img data-gifffer="/images/BandStep1.gif" />

In addition, for electronic properties with a non-self consistent step it is critical to have a high k-point density to give enough detail to calculate an accurate band structure.  For this reason we add both k-point convergence and relaxation as pre-processors to the band structure calculation.  You can see more details of these workflows at [kpt-convergence](kpt-convergence) and [relaxation tutorials](relaxation)

<img data-gifffer="/images/BandStep2.gif" />

In VASP, this will result in 2 workflow units being automatically populated.  The first unit specifies the settings for the self-consistent calculation of the eigenvalues and wave functions.  The second unit calculation is a non self-consitent calculation using the wave functions and charge density of the previous calculation.

If we examine the input files for each step in the workflow we will see that the k-point path for Si has been defined along special high symmetry k-points.  Currently we only support the automatic generation of high symmetry k-points for FCC structures.  Support for high symmetry k-point path sampling for band structure calculations of all 14 lattice types will be supported in a future release.

<img data-gifffer="/images/BandStep3.gif" />

Before submitting the calculation, click on the "Go to Compute" button and examine the compute parameters.  The example below shows how to increase the total run time to 15 minutes, the number of cores to 2 cores, and how to turn on email notifications of when the job starts and ends.  Click "No" when it asks if you want to save a duplicate material.

<img data-gifffer="/images/BandStep4.gif" />

As each workflow is executing, you can monitor it's progress live by monitoring both the output of the executable as well as a graphical representation of the total energy convergence on the Status tab under each execution's sub-tab.

<img data-gifffer="/images/BandStep5.gif" />

When all 5 units are complete we are ready to go to the terminal window to visualize the electron density mesh.  The next step is to open a Remote Desktop Connection to the terminal so that you can run graphical interface programs for visualization.  In the right sidebar obtained when clicking on your username or avatar in the upper right hand corner is a "Remote Desktop" option.  Select this and a different overlay will appear in your web browser of a graphical user session.

<img data-gifffer="/images/OpenRemoteDesktop.gif" />

Find and open XCrysden from ???.  Within XCrysden, go to file->Open and navigate to the directory where you the electron density file ??? is and open to a visualization of the electron density

<img data-gifffer="/images/VisualizeElectronDensity.gif" />
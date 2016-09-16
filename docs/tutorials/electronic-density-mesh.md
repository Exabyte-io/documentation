<!-- TODO by MH -->

This page explains how to calculate the electon density mesh of Silicon. The electron density mesh is a pre-requisite for any band structure calculation so this tutorial is closely related to the [band structure tutorial](band-structure.md)

# Create new job
Si is the default material, so if you choose "Create a Job" from the sidebar on the home page Si will automatically be loaded.

<img data-gifffer="/images/BandStep1.gif" />

# Create Workflow

Under workflow chose the "Bandstructure" for either VASP or Quantum Espresso.
In addition, for electronic properties with a non-self consistent step it is critical to have a high k-point density to give enough detail to calculate an accurate band structure.  For this reason we add both k-point convergence and relaxation as pre-processors to the band structure calculation.  You can see more details of these workflows at [kpt-convergence](kpt-convergence) and [relaxation tutorials](relaxation)

<img data-gifffer="/images/BandStep2.gif" />

## Adjust KPoints

In addition, for electronic properties with a non-self consistent step it is critical to have a high k-point density to give enough detail to calculate an accurate band structure.

In VASP, the band structure workflow has 2 units.  The first unit specifies the settings for the self-consistent calculation of the eigenvalues and wave functions.  The second unit calculation is a non self-consitent calculation using the wave functions and charge density of the previous calculation.

We set the kpoint density to 11x11x11 in the first workflow unit to provide sufficient density for the second non-consistent calculation step of the band structure.  In addition we also apply the recommended k-point path to effectively sample the electronic states based on the symmetry of the crystal.

<img data-gifffer="/images/BandStep3.gif" />
# Submit job

Before submitting the calculation, click on the "Go to Compute" button and examine the compute parameters.  This is a small structure so 1 core and 5 minutes are sufficient.  Click "No" when it asks if you want to save a duplicate material.

<img data-gifffer="/images/BandStep4.gif" />

# Monitoring status

As each workflow is executing, you can monitor it's progress live by monitoring both the output of the executable as well as a graphical representation of the total energy convergence on the Status tab under each execution's sub-tab.

<img data-gifffer="/images/BandStep5.gif" />

# Preparing for Visualization

When all 5 units are complete we are ready to go to the terminal window to visualize the electron density mesh.  The next step is to open a Remote Desktop Connection to the terminal so that you can run graphical interface programs for visualization.  Underneath the "Terminal" option in the right sidebar you used earlier in the tutorial is a "Remote Desktop" option.

![Remote Desktop](../images/ChooseRemoteDesktop.png "Remote Desktop")

# Remote Desktop

Select this and a different overlay will appear in your web browser of a graphical user session.

![Start Remote Desktop](../images/StartRemoteDesktop.png "Start Remote Desktop")

# Open Crysden

Find and open XCrysden under the "Other" dropdown menu item.

![Other->XCrysden](../images/RemoteDesktopApps.png "Other->XCrysden")

Within XCrysden, go to file->Open and navigate to the directory where you the electron density file is and open to a visualization of the electron density.

<img data-gifffer="/images/VisualizeElectronDensity.gif" />
<!-- TODO by MH -->

This page explains how to calculate the electon density mesh of Silicon. The electron density mesh is a pre-requisite for any band structure calculation so this tutorial is closely related to the [band structure tutorial](band-structure.md)

# Create new job
Si is the default material, so if you choose "Create a Job" from the sidebar on the home page Si will automatically be loaded.

<img data-gifffer="/images/BandStep1.gif" />

# Create Workflow

Under workflow chose the "Electronic Density Mesh" for Quantum Espresso.  In addition, for electronic properties with a non-self consistent step it is critical to have a high k-point density to give enough detail to calculate an accurate band structure.

<img data-gifffer="/images/Charge1.gif" />

## Adjust K-points

For charge density it is critical to have a high k-point density to properly sample the isosurfaces.  In VASP, the band structure workflow has 2 units.  The first unit specifies the settings for the self-consistent calculation of the eigenvalues and wave functions.  The second unit is a post-processing unit to generate the file for visualization. We set the kpoint density to 11x11x11 in the first workflow unit.

<img data-gifffer="/images/Charge2.gif" />

# Submit job

Before submitting the calculation, click on the "Go to Compute" button and examine the compute parameters.  This is a small structure so 1 core and 5 minutes are sufficient.  Click "No" when it asks if you want to save a duplicate material.

<img data-gifffer="/images/Charge3.gif" />

# Monitoring status

As each workflow is executing, you can monitor it's progress live by monitoring both the output of the executable as well as a graphical representation of the total energy convergence on the Status tab under each execution's sub-tab.

<img data-gifffer="/images/Charge4.gif" />

# Checking Results

Once the calculation is complete, under the Results tab at the bottom of the page there will be a listing of the files and directories on the system that is clickable to download and transit directories.  The screen shots below show the location of the charge density file

<img data-gifffer="/images/Charge5.gif" />


# Preparing for Visualization

When all 5 units are complete we are ready to go to the terminal window to visualize the electron density mesh.  The next step is to open a Remote Desktop Connection to the terminal so that you can run graphical interface programs for visualization.  Underneath the "Terminal" option in the right sidebar you used earlier in the tutorial is a "Remote Desktop" option.

![Remote Desktop](../images/ChooseRemoteDesktop.png "Remote Desktop")

# Remote Desktop

Select this and a different overlay will appear in your web browser of a graphical user session.

![Start Remote Desktop](../images/StartRemoteDesktop.png "Start Remote Desktop")

# Open Crysden

Find and open XCrysden under the "Other" dropdown menu item.

![Other->XCrysden](../images/RemoteDesktopApps.png "Other->XCrysden")

# Visualize Charge Density

Within XCrysden, go to file->Open and navigate to the directory where you the electron density file is and open to a visualization of the electron density.

<img data-gifffer="/images/Charge6.gif" />

Adjust the value of charge density to be displayed and toggle the isosurface buttons to display the data.

<img data-gifffer="/images/Charge7.gif" />

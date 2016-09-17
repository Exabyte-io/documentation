<!-- TODO by TB -->

This page explains how to calculate the Fermi surface for metallic FCC copper.

# Create job

Clicking on "Create Job" from the sidebar on the home page Si will automatically be loaded as it is the default material.  Si is a semiconductor and a Fermi surface is most meaningful for a metallic material such as copper.  We will need to import a Cu structure from Materials Project.

# Import material

To import Cu go to the sidebar, and select "Materials".  Then click the cloud button on the upper right of the Materials Designer page for import.  In the search box, put Cu and after a few seconds, the entries for Cu from the database and Material Project will appear.  Choose the version of Cu with space group "Fm-3m" and click on it.  Then click on the right side of the entry to bring up the option to "import" the material

<img data-gifffer="/images/ImportCu.gif" />

# Create project

To create a new project, click on the "Project" link located in the sidebar/menu on the left. After that, click <i class="zmdi zmdi-plus-circle zmdi-hc-border"></i> button in the top right corner, as shown in the animation below. Every user has a default project and we will use during this tutorial.

<img data-gifffer="/images/CreateCuJob.gif" />

# Select material

The FCC Si structure is provided by default for every user.  The exact list of materials in your personal database will differ, so you may need to search for the Cu structure you just imported and select it as shown below:

<img data-gifffer="/images/SetUpCuETotWithConvergence.gif" />

# Choose workflow

Next, click on the "Workflow" tab choose VASP as the simulation engine to be used and choose the "Total Energy" workflow.

## Adjust kpoints

For charge density it is critical to have a high k-point density to properly visualize charge isosurfaces.  The second unit is a post-processing unit to generate the file for visualization. We set the kpoint density to 11x11x11 in the first workflow unit.

<img data-gifffer="/images/Charge2.gif" />

# Compute parameters

Before submitting the calculation, click on the "Compute" tab and examine the compute parameters.  The example below shows how to increase the total run time to 15 minutes, the number of cores to 2 cores, and how to turn on email notifications of when the job starts and ends.

<img data-gifffer="/images/ComputCuFermiSurface.gif" />

# Monitor status

Finally while the calculation is running you will see a tab for each of the VASP execution units in the workflow.  You will notice the kpt-convergence tab will update in real time as the simulations progress.  The graphical interface will show the delta energy between successive self-consistent steps.  The text based output of VASP also updates in real time with the output of the VASP simulation.

<img data-gifffer="/images/RunningCuFermiSurface.gif" />

# Examine results

When both calculation units are complete, the yellow buttons will have turned green and the "Results" tab will become clickable.  You can click on the "Results" tab to see the final total energy, Fermi energy, and more information about each execution unit.

<img data-gifffer="/images/ConvergeStep6.gif" />

# Browse output files

Finally you can also browse the actual output and input files that are part of the calculation at the bottom of the results page.

# Start terminal

Once the simulation is complete, you will need to connect to a terminal to create a file to visualize the Fermi surface.  We provide a interface to a terminal command line window directly through the web to enable this.  This is also the preferred method of execution for a software tool that we have not yet implemented in our automated framework.

To use the terminal interface, click on the right sidebar which is obtained by clicking on your username in the upper-right corner of the home page.

![Right Sidebar](../images/RightSidebar.png "Right Sidebar")

One of the options in this side bar is "Terminal".

![Right Sidebar->Terminal](../images/StartTerminal.png "Right Sidebar->Terminal")

After clicking on "Terminal" an overlay will appear filling up your browser window with a text based terminal emulator called Guacamole.

![Terminal Overlay](../images/LogInToTerminal.png "Terminal Overlay")

# Prepare fermi surface file

As below, navigate into the directory containing all your simulation results.  "cd ~/data/demo; ls -ort" to see the directories present where all your simulation files are held.

![Jobs Directory List](../images/JobDirectoryList.png "Job Directory List")

Once in the correct simulation directory run the following command to generate the post-processing bxsf file:

<img data-gifffer="/images/GenerateBXSFFile.gif" />

# Exit terminal

Now type "exit" in the terminal to log out of the terminal.

![Log Out](../images/LogoutOfTerminal.png "Log Out")

# Start remote desktop

The next step is to open a Remote Desktop Connection to the terminal so that you can run graphical interface programs for visualization.  Underneath the "Terminal" option in the right sidebar you used earlier in the tutorial is a "Remote Desktop" option.

![Remote Desktop](../images/ChooseRemoteDesktop.png "Remote Desktop")

Select this and a different overlay will appear in your web browser of a graphical user session.

![Start Remote Desktop](../images/StartRemoteDesktop.png "Start Remote Desktop")

# Open XCrysden

Find and open XCrysden under the "Other" dropdown menu item.

![Other->XCrysden](../images/RemoteDesktopApps.png "Other->XCrysden")

Within XCrysden, go to file->Open and navigate to the directory where you created the bxsf file to open a visualization of the Fermi Surface.

<img data-gifffer="/images/VisualizeFermiSurface.gif" />


<!-- TODO by TB -->

This page explains how to calculate the Fermi surface [[1](#links)] for metallic FCC Cu using pseudopotential density functional theory [[2](#links)]. We will use Quantum ESPRESSO [[3](#links)] as our simulation engine for this tutorial.

# Create job

Clicking on "Create Job" from the sidebar on the home page Si will automatically be loaded as it is the default material.  Si is a semiconductor and a Fermi surface is most meaningful for a metallic material such as copper.  We will need to import a Cu structure from Materials Project.

# Import material

To import Cu go to the sidebar, and select "Materials".  Then click the cloud button on the upper right of the Materials Designer page for import.  In the search box, put Cu and after a few seconds, the entries for Cu from the database and Material Project will appear.  Choose the version of Cu with space group "Fm-3m" and click on it.  Then click on the right side of the entry to bring up the option to "import" the material

<img data-gifffer="/images/ImportCu.gif" />

# Create project

To create a new project, click on the "Project" link located in the sidebar/menu on the left. After that, click <i class="zmdi zmdi-plus-circle zmdi-hc-border"></i> button in the top right corner, as shown in the animation below. Every user has a default project and we will use during this tutorial.

# Select material

The FCC Si structure is provided by default for every user.  The exact list of materials in your personal database will differ, so you may need to search for the Cu structure you just imported and select it as shown below:

<img data-gifffer="/images/CreateCuJob.gif" />

# Choose workflow

Next, click on the "Workflow" tab choose Quantum ESPRESSO as the simulation engine to be used and choose the "Band Structure + DOS" workflow.

## Adjust kpoints

For fermi surface it is critical to have a high k-point density to properly visualize charges.  We set the kpoint density to 11x11x11 in the first workflow unit.

<img data-gifffer="/images/ChargeCu2.gif" />

# Compute parameters

Before submitting the calculation, click on the "Compute" tab and examine the compute parameters.


# Monitor status

Finally while the calculation is running you will see a tab for each of the Quantum ESPRESSO execution units in the workflow.  The graphical interface will show the delta energy between successive self-consistent steps.  The text based output of Quantum ESPRESSO also updates in real time with the output of the Quantum ESPRESSO simulation.

# Examine results

When all calculation units are complete, the yellow buttons will have turned green and the "Results" tab will become clickable.  You can click on the "Results" tab to see the final total energy, Fermi energy, and more information about each execution unit.

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

As below, navigate into the directory containing all your simulation results.  Once in the correct simulation directory run the commands in the window below to generate the post-processing bxsf file:

![Generate BXSF File](../images/GenerateBXSFFile.png "Generate BXSF File")

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

Within XCrysden, go to file->Open and navigate to the directory where you created the *.bxsf file to open a visualization of the Fermi Surface.

![Visualize Fermi Surface 1](../images/FermiSurface1.png "Visualize Fermi Surface 1")
![Visualize Fermi Surface 2](../images/FermiSurface2.png "Visualize Fermi Surface 2")
![Visualize Fermi Surface 3](../images/FermiSurface3.png "Visualize Fermi Surface 3")

# Links

1. [Fermi Surface, Wikipedia](https://en.wikipedia.org/wiki/Fermi_surface)
2. [Density Functional Theory, Wikipedia](https://en.wikipedia.org/wiki/Density_functional_theory)
3. [Quantum ESPRESSO, Website](http://www.quantum-espresso.org/)

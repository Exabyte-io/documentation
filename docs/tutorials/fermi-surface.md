<!-- TODO by TB -->

We will calculate the Fermi surface for an fcc metal Copper.

On the "Create a Job" from the sidebar on the home page Si will automatically be loaded as it is the default material.  Si is a semiconductor and a Fermi surface is usually only meaningful for a metallic material such as copper.  We will need to import a Cu structure from Materials Project.  To import Cu go to the sidebar, and select the "Materials" page.  On that page click the cloud button on the upper right of that page for import.  In the search box, put Cu and after a few seconds, the entries for Cu from the database and Material Project will appear.  Choose the version of Cu with the point group  and click on it.  Then click on the right side of the entry to bring up the option to "import" the material

<img data-gifffer="/images/ImportCu.gif" />

To create a new project, click on the "Project" link located in the sidebar/menu on the left. After that, click <i class="zmdi zmdi-plus-circle zmdi-hc-border"></i> button in the top right corner, as shown in the animation below. Every user has a default project and we will use during this tutorial.

<img data-gifffer="/images/CreateCuJob.gif" />

Import the copper structure from Materials Project Chose the FCC Si structure provided by default for every user.  The exact list of materials in your personal database will differ, so you may need to search for the Si structure and select it as shown below:

<img data-gifffer="/images/SetUpCuETotWithConvergence.gif" />

Next, click on the "Workflow" tab choose VASP as the simulation engine to be used and choose the "Total Energy" workflow.  Also rename the structure at this point to be "Copper Fermi Surface Test"

Then, to add k-point convergence as a pre-processor to total energy calculation, expand the <i class="zmdi zmdi-plus-circle zmdi-hc-border"></i> Advanced section to show unhighlighted buttons for Relaxation and k-point convergence.  Click on the k-point convergence.  If you scroll down the screen to look at the computation units and then toggle the k-point convergence button on and off in the "Advanced" section you will see the units various units that are added for convergence to set up the parameters to increase k-point density and track the total energy throughout the study.

<img data-gifffer="/images/ConvergeCuFermiSurface.gif" />

If you would like to see more details of this k-point convergence workflow visit [kpt-convergence](kpt-convergence)

Before submitting the calculation, click on the "Go to Compute" button and examine the compute parameters.  The example below shows how to increase the total run time to 15 minutes, the number of cores to 2 cores, and how to turn on email notifications of when the job starts and ends.

<img data-gifffer="/images/ComputCuFermiSurface.gif" />

Finally while the calculation is running you will see a tab for each of the VASP execution units in the workflow.  You will notice the kpt-convergence tab will update in real time as the simulations progress.  The graphical interface will show the delta energy between successive self-consistent steps in the DFT calculation for all SCF steps in all simulations as k-point density is increased.  The text based output of VASP also updates in real time with the output of each VASP simulation concatenated to the previous output.

<img data-gifffer="/images/RunningCuFermiSurface.gif" />

!!! Note "Future developments"
    In the future we will split each simulation of a k-point convergence study into different data series to make the progress of each step more clear.  In addition we will also seperate the text output of each individual simulation into it's own tracking box.

When both calculation units are complete, the yellow buttons will have turned green and the "Results" tab will become clickable.  You can click on the "Results" tab to see the final total energy, Fermi energy, and more information about each execution unit.

<img data-gifffer="/images/ConvergeStep6.gif" />

Finally you can also browse the actual output and input files that are part of the calculation at the bottom of the results page.  Once the simulation is complete, you will need to connect to a terminal to create a file to visualize the Fermi surface.  We provide a interface to a terminal command line window directly throught the web to enable this.  This is also the preferred method of execution for a software tool that we have not yet implemented in our automated framework.

To use the terminal interface, click on the right sidebar which is obtained by clicking on your username in the upper-right corner of the home page.  One of the options in this side bar is "Terminal".  After clicking on "Terminal" an overlay will appear filling up your browser window with a text based terminal emulator called Guacamole.

Run "ls -ort ~" to see the directories present and then "cd ~/data" to enter the directory.  Once in that directory run "grep 'Copper Fermi Surface Test' */*" to find the directory that contains the results of your most recent Fermi Surface calculation.  "cd" into the appropriate directory.  Then run the following command to generate the post-processing bxsf file.

Now type "exit" in the terminal to log out of the terminal.  The next step is to open a Remote Desktop Connection to the terminal so that you can run graphical interface programs for visualization.  Underneath the "Terminal" option in the right sidebar you used earlier in the tutorial is a "Remote Desktop" option.  Select this and a different overlay will appear in your web browser of a graphical user session.

Find and open XCrysden from ???.  Within XCrysden, go to file->Open and navigate to the directory where you created the bxsf file to open a visualization of the Fermi Surface


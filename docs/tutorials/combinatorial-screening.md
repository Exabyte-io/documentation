<!-- TODO by MH -->

This tutorial demonstrates how to create a set of of III-V compound semiconductor materials with permutations of n and p-type dopants in a 16-atom Si supercell, and subsequently track the impact on electronic band gap. We use Quantum ESPRESSO as our simulation engine for this tutorial.

# Import materials

To import III-V compound semiconductors go to the Materials webpage using the sidebar on the homepage.  Once on the homepage you can click on the cloud icon in the upper right with an embedded down arrow.  In the resulting overlay search enter AlP for Aluminum Phosphide.  After a few seconds the search results from Materials Project will appear.  The F-43m space group option is the lowest energy AlP.  Click on the right side on this line and choose "import".  This will load the material into your database.

<img data-gifffer="/images/tutorials/tutorials/ImportAlP.gif" />

# Create material combinations

To create a job go to the "Create Job" webpage using left sidebar.  Once on the "Create Job" webpage and "Material" tab scroll down to the visualization of the atomic structure.  Just above and to the right of the visualization will be a button to "Activate Combinatorial".  Click this button and the box surrounding the atomic positions will be highlighted in orange.  To create the combinatorial set, change the elements labels for each atom to `Al/Al/Al/In/In/In/Ga/Ga/Ga` and `P/As/Sb/P/As/Sb/P/As/Sb`.

<img data-gifffer="/images/tutorials/tutorials/CreateAlP.gif" />
<img data-gifffer="/images/tutorials/tutorials/CreateAlP2.gif" />

# Choose workflow

Click on the "Workflow" tab.  Since we are substituting different elements in AlP crystal structure it's important to relax the cell parameters to the new lattice parameters.  Click the "+" next to the "Advanced" accordion then click on the "Relaxation" button.  For an accurate band gap calculation it's also important to have a high k-point density so click on the "+" button next to "k-points grid" and increase the density to 9 x 9 x 9 as shown below.  If you click on the first relaxation unit in the workflow at the bottom of the page you will see that the input file includes all the pseudopotentials for all elements.  When the jobs are created, 9 unique input files will be created automatically that can be run directly in Quantum ESPRESSO.

<img data-gifffer="/images/tutorials/tutorials/WorkflowAlP.gif" />


# Compute settings

Since some materials will be relaxing into new unit cell parameters, increase the maximum run time to 15 minutes.  Then click "Save" to create the combination set of jobs.

<img data-gifffer="/images/tutorials/tutorials/ComputeAlP.gif" />

# Submit jobs

After saving on the "Compute" tab you will be taken to the "Jobs" webpage where you will see all 9 jobs.  To submit each job right click on the 3 vertical dots next to each job and click "run".  You will see the status of the job switch to "Submitted" and "Active" once they start running.

<img data-gifffer="/images/tutorials/tutorials/SubmitAlP.gif" />

# Create permutation job

Next we will set up the jobs for the permutation set for doped Silicon.  We will examine the effect of n and p-type dopants on silicon.  On the "Create Job" page, select the Silicon material, then click the "Activate Combinatorial" button above the unit cell visualization.  To set up the permutations, change the element label of one of the elements to Si, As, P, O, B, C, N, S, Se, Ge, Al. Similar to above with the AlP combination series, add relaxation to the workflow, increase the k-point density, increase the maximum run time to 15 minutes, save the job, then "run" each job that is created on the jobs page.

<img data-gifffer="/images/tutorials/tutorials/CreateSiDopant.gif" />
<img data-gifffer="/images/tutorials/tutorials/CreateSiDopant2.gif" />

!!! Warning "Not all III-V's will exit successfully."
    Combinatorial runs can be challenging especially when all atoms in a base material are replaced.  In the case of III-V's, depending on your relaxation settings, likely some of your materials will fail to relax to the correct structure, or end up in a local minimum during relaxation and a 0 eV band gap.  Other simulations will relax into the correct new material unit cells and generate results for the band gap. Some materials currently require more hands-on management of the relaxation settings with follow-up calculations.  The power of the combinatorics module is that it has automated as much of this process as possible and identified the materials that require your more detailed attention and manual follow-up.

# Analytics

After all the jobs complete, the best way to aggregate the results are through the "Analytics" tab.  From the home page bring up the left-hand sidebar on the "Analytics" entry to bring up the analysis window.

<img data-gifffer="/images/tutorials/tutorials/Analytics.gif" />

# Compare materials

Within the analytics page, you will see a list of all materials, search for and select the Al, Ga, & In compounds.  Next find the graph icon on the top of the page it will be named "Compare" and click.  By default pressure will be the default property for comparison.  You can click the "X" next to the pressure property and then if you click in the same box, you will be given an option to select the property of interest for all the materials and it will be displayed in one chart showing the band gap of all materials.

<img data-gifffer="/images/tutorials/tutorials/CombinatorialBandGap.gif" />

!!! Warning "Dopant band gaps report as 0 eV due to Fermi energy shift"
    We have not graphed the combinatorial set of dopants in Silicon in this tutorial as doping results in the Fermi energy moves into the valence band edge or conduction band edge. In effect, this turns the material into a conductor with a 0 band gap. In the future we expect to develop an automated way to predict the change in the band gap of the original base material (pure silicon in this case).

# Links

1. [Combinatorial Screening, Wikipedia](1. [Density Functional Theory, Wikipedia](https://en.wikipedia.org/wiki/Density_functional_theory)
2. [Quantum ESPRESSO, Website](http://www.quantum-espresso.org/)

<!-- TODO by MH -->

This tutorial will demonstrate combinatorial capabilities on a set of III-V compound semiconductor combinations and a range of permutations of n and p-type dopants in a 16-atom Si supercell to investigate the impact on electronic band gap.

# Import materials

To import III-V compound semiconductors go to the Materials webpage using the sidebar on the homepage.  Once on the homepage you can click on the cloud icon in the upper right that is labeled "Import" when you mouse over the icon.  This will bring up an overlay with a search box where you can AlP.  After a few seconds the search results from Materials Project will come up.  The F-dm3 space group option is the lowest energy AlP.  Click on the right side on the icon with three vertical dots to "import".  This will load the material into your database.

<img data-gifffer="/images/ImportAlP.gif" />

# Create combination job

To create a job go to the "Create Job" webpage using the sidebar on the homepage.  Once on the "Create Job" webpage scroll down to the visualization of the atomic structure.  Just above and to the right of the visualization will be a button to "Activate Combinatorial".  Click on this button and the basis listing the atom positions will be highlighted in orange.  To create the combinatorial set, change atom label for each atom to Al/Al/Al/In/In/In/Ga/Ga/Ga and P/As/Sb/P/As/Sb/P/As/Sb.

<img data-gifffer="/images/CreateAlP.gif" />
<img data-gifffer="/images/CreateAlP2.gif" />

# Choose workflow

Click on the "Workflow" tab.  Since we are substituting different elements into an AlP crystal structure it's important to relax the cell parameters to the new lattice parameters.  Click the "+" next to the "Advanced" text then click on the "Relaxation" button.  For an accurate band gap calculation it is also important to have a high k-point density so increase click on the "+" button next to the "k-point grid" text and increase the density to 9x9x9 as shown below.  If you click on the first relaxation unit in the workflow at the bottom of the page you will see that the input file includes all the pseudopotentials for all elements.  When the jobs are created, 9 unique input files will be created automatically that can be run directly in Quantum ESPRESSO.

<img data-gifffer="/images/WorkflowAlP.gif" />


# Compute settings

Since some of the materials will be relaxing into new unit cell parameters, increase the maximum run time to 15 minutes.  Then click "Save" to create the combination set of jobs.

<img data-gifffer="/images/ComputeAlP.gif" />

# Submit jobs

After saving on the "Compute" tab you will be taken to the "Jobs" webpage where you will see all 9 jobs.  To submit each job right click on the 3 vertical dots next to each job and click "run".  You will see the status of the job switch to "Submitted" and "Active" once they start running.

<img data-gifffer="/images/SubmitAlP.gif" />

# Create permutation job

Next we will set up the jobs for the permutation set.  We will examine the effect of a range of n and p-type dopants on the silicon band gap.  On the "Create Job" page, select the Silicon material, then click the "Activate Combinatorial" button above the unit cell visualization.  To set up the permutations, change the element label of one of the elements to Si, As, P, O, B, C, N, S, Se, Ge, Al. Similar to above with the AlP combination series, add relaxation to the workflow, increase the k-point density, increase the maximum run time to 15 minutes, save the job, then "run" each job that is created on the jobs page.

<img data-gifffer="/images/CreateSiDopant.gif" />
<img data-gifffer="/images/CreateSiDopant2.gif" />

# Navigate to analytics

After all the jobs are complete, the best way to aggregate the results are through the "Analytics" tab.  From the home page bring up the left-hand sidebar on the "Analytics" entry to bring up the analysis window.

<img data-gifffer="/images/Analytics.gif" />

- Combinatorial-screening:
       - when finished navigate to analytics
       - find materials by Formula and compare bandgaps for both cases

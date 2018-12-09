<!-- by MH -->

This tutorial explains how to use the combinatorial screening capabilities to calculate the electronic band gap [[1](#links)] based on density functional theory for a range of III-V semiconductors using VASP [[2](#links)] as our simulation engine.  After the first series of calculations using Density Functional Theory [[3](#links)]and Generalized Gradient Approximation using PAW pseudopotentials [[4](#links)], [[5](#links)] with Perdew-Burke-Ernzerhof functionals. [[6](#links)] We follow-up with a second set of calculations using Hybrid Screened Exchange for more accurate prediction of the band gaps [[7](#links)].

# Import material

We will use InAs as our base structure for materials screening because its lattice parameter is in the middle of the range of lattice parameters of the III-V's we will study.  To import AlP go to the Materials web page using the sidebar on the homepage.  Once on the homepage you can click on the cloud icon in the upper right with an embedded down arrow.  In the resulting overlay search enter AlP for Aluminum Phosphide.  After a few seconds the search results will appear.  The F-43m space group option is the lowest energy AlP structure.  Click on the right side on this line and choose "import".  This will load the material into your database.

<img data-gifffer="/images/IIIVImport.gif"/>

# Create material combinations

To create a job go to the "Create Job" webpage using left sidebar.  Once on the "Create Job" webpage and "Material" tab scroll down to the visualization of the atomic structure.  Just above and to the right of the visualization will be a button to "Activate Combinatorial".  Click this button and the box surrounding the atomic positions will be highlighted in orange.  To create the combinatorial set, change the elements labels for each atom to `In/In/In/Ga/Ga/Ga/Al/Al/Al` and `As/Sb/P/As/Sb/P/As/Sb/P`.

<img data-gifffer="/images/IIIVCreate.gif"/>

# Choose band gap workflow

Choose VASP simulation engine. You will see the Total Energy workflow as the default.  Click on the box saying "Total Energy" and select the "Density of States" workflow to provide the band gap value estimate.

# Add relaxation

Because we are doing a combinatorial study with different materials, it is important to add a relaxation step to the workflow to allow the lattice parameters to adjust to the equilibrium value for each material.  Click on "Advanced" and press the "Relaxation" button.  You will see this had added an additional unit to the workflow below.  Open that unit and adjust the k-point density to 7 x 7 x7.  Next open the second unit that actually does the band gap calculation and change that k-point density to 15 x 15 x 15  to ensure a dense enough k-mesh for a band gap prediction.

<img data-gifffer="/images/IIIVWorkflow.gif"/>

# Compute parameters

Next we set up compute parameters for the number of processors and the maximum time limit (wall-time).  Increasing the number of processors allocated to the job may accelerate the calculation, especially if you have a larger unit cell.  Since we added a relaxation unit to this workflow and are using a dense mesh for the band gap calculation, we increased the wall time to 55 minutes and the number of cores to 2.

# Submit job

Click "Submit Job" as shown below. You will be asked if you want to keep a duplicate copy of the material since it has already been saved before. Answer "No" to proceed forward.

<img data-gifffer="/images/IIIVSubmit.gif"/>

# Monitor status

Once the jobs are submitted you will be taken to the Jobs Status page.  You will see that 9 jobs have been created and submitted.  Depending on the number of cores available at that time, some jobs may stay in the "Submitted" status until other jobs go "Active" and "Finish" to make cores available to run subsequent simulations.

<img data-gifffer="/images/IIIVResults.gif"/>

# Analytics

After all the jobs complete, the best way to aggregate the results are through the "Analytics" tab.  To bring up the Analytics use the left-hand sidebar on to bring up the analysis window.

<img data-gifffer="/images/IIIVAnalytics.gif"/>

# Compare materials

Within the analytics page, you will see a list of all materials, search for and select the Al, Ga, & In compounds.  Next find the graph icon on the top of the page it will be named "Compare" and click.  By default pressure will be the default property for comparison.  Clicking next to the "Pressure" will bring up a new selection box where you can add "Direct Band Gap" and "Indirect Band Gap".  All 3 properties will be displayed for all 3 materials in the charts .

<img data-gifffer="/images/IIIVBandGaps.gif"/>

# Increasing accuracy with HSE

Hybrid Screened Exchange is a more computationally expensive model to be used within DFT that more accurately predicts the energy of excited state electrons.  The screen shots below show how to edit a similar workflow as described above to set us the HSE calculation.  The INCAR file below for the band gap prediction stage of the calculation is contains the last 4 lines necessary to set up the HSE settings for this calculation:

```
LWAVE  = .FALSE.
ISMEAR =    0
SIGMA  = 0.05
LORBIT = 11
LHFCALC = .TRUE.
HFSCREEN = 0.2
ALGO = D
TIME = 0.4
```

As this is more computationally intensive we increase the maximum runtime to and cores for each simulation.

<img data-gifffer="/images/IIIVHSECreate.gif"/>

# HSE band gaps

After the subsequent HSE calculations have finished, you can once again go to the Analytics page to analyze the results.  Search for and select the Al, Ga, & In compounds as before.  If you click on each material you will expand the results to see 2 band gap calculations.  You can see that the band gaps from the HSE calculations are larger than the previous calculation.  The table below summarizes the results as well as compares with experimental data.

<img data-gifffer="/images/IIIVHSEAnalytics.gif"/>

| Material | Band Gap (eV) with traditional DFT | Band Gap (eV) with HSE DFT | Experimental Band Gap (eV) [[8](#links)]|
|:---------------|:------------|:------------|:------------|
| InSb | 0    | 0     | 0.17  |
| InAs | 0    | 0.072 | 0.36  |
| GaSb | 0    | 0.39  | 0.75  |
| InP  | 0.39 | 1.11  | 1.34  |
| GaAs | 0.16 | 0.93  | 1.42  |
| BAs  |      | 1.86  | 1.5   |
| AlSb | 1.22 | 1.88  | 1.62  |
| BSb  |      | 1.29  | -     |
| BP   |      | 2.31  | 2.1   |
| AlAs | 1.51 | 2.18  | 2.153 |
| GaP  | 1.51 | 2.38  | 2.272 |
| AlP  | 1.63 | 2.36  | 2.45  |

# Links

1. [Electronic Band gap, Wikipedia](https://en.wikipedia.org/wiki/Band_gap)
2. [Vienna ab-inito simulation package, Website](https://www.vasp.at/)
3. [PAW Potentials - Blochl](http://journals.aps.org/prb/abstract/10.1103/PhysRevB.50.17953)
4. [PAW Potentials - Kresse](http://journals.aps.org/prb/abstract/10.1103/PhysRevB.59.1758)
5. [PBE Functionals, PDF](http://journals.aps.org/prl/abstract/10.1103/PhysRevLett.77.3865)
6. [Density Functional Theory, Wikipedia](https://en.wikipedia.org/wiki/Density_functional_theory)
7. [Hybrid Screened Exchange, PDF](https://www.vasp.at/index.php/news/36-highlights/68-hse-hybrid-functional)
8. [III-V Semiconductors, Website](http://www.semiconductors.co.uk/propiiiv5653.htm)

# What is a structural relaxation calculation?

It is often desirable, before commencing any other calculation on a particular material structure of interest, to perform a "Variable-cell Relaxation" calculation as the starting initial step of a new workflow. This helps to ensure that the initial crystalline structure is fully relaxed and optimized (within some approximate tolerance criteria being monitored), and that accurate and realistic property calculations can therefore be subsequently executed on it throughout the rest of the workflow. 

The variable-cell relaxation calculation bears its name from the fact that the material's unit cell is systematically allowed to undergo a series of sequential small structural changes in terms of its lattice parameters and atomic positions. This affords for an effective sampling of the free energy landscape of the material under consideration, across which the crystal structure configuration can move (except for overcoming significant energy barriers), and can thus be fully optimized by the time the calculation is terminated according to the various threshold criteria outlined below.  


# Equilibrium threshold conditions for relaxations

## Equilibrium condition on the internal stress tensor

By an optimized (or relaxed) crystal structure, it is generally meant firstly that the internal stress tensor components of the material should match the externally applied pressure as closely as possible, which for a material under equilibrium conditions corresponds to the ambient atmospheric pressure (the default choice for a new workflow creation). This ambient pressure is in fact typically approximated as exactly zero in DFT ab-initio calculations, since it is normally considered to be negligible compared to the usual pressures of at least order kbar encountered in such calculations, necessary to perceptibly distort any solid-state crystal structure. 

## Equilibrium condition on the inter-atomic forces

Secondly, a relaxation calculation ensures that the inter-atomic forces within the crystal structure under consideration also become negligibly small. This aspect, together with the above-mentioned pressure criterion, contributes to stabilizing the overall structure as much as possible and to therefore minimize its potential energy.    

# Why relaxations are recommended

Performing such an initial relaxation at the beginning of any type of workflow is in general a recommended practice, since having a fully-optimized crystal structure as the starting point will ensure more reliable results throughout the course of the execution of the rest of the workflow tasks. The user is advised that not even the pre-defined crystal structures which can be imported directly from centralized databases, such as the [Materials Bank](../../materials/actions/bank.md) or the [Material Project](../../materials/actions/import.md) repositories reachable on the Exabyte platform, are always guaranteed to be fully pre-relaxed and pre-optimized. 

# Execution of the Variable-cell Relaxation calculation

The user can add such a variable-cell relaxation calculation as the first subworkflow step in a newly-created workflow by clicking on the `Relaxation` option under the drop-down menu button labelled with three vertical dots located at the right-hand side of the header menu of the Workflow Designer interface. 

Once the Relaxation calculation has been selected and added to the beginning of the current workflow, a tick <i class="zmdi zmdi-check zmdi-hc-border"></i> will appear next to the previously-clicked `Relaxation` option to remind the user about this inclusion. The "Variable-cell Relaxation" calculation will furthermore be inserted as a subworkflow module at the start of the flowchart portraying the overall workflow on the left-hand sidebar of the Designer interface, as elaborated in its respective [documentation page](../../workflow-designer/sidebar.md). 

# Animation

The above steps for adding the relaxation subworkflow at the beginning of an existing band structure calculation workflow are demonstrated in the animation below:

<img data-gifffer="/images/add-relaxation.gif" />


# Relaxation types

Relaxations are usually classified by the number of degrees of freedom allowed to relax during the calculation, which may include:

1. Atoms - position of the atoms
2. Cell shape - angles between lattice vectors
3. Cell size - length of lattice vectors and/or parameters

Default settings include the relaxation of all three above aspects of the crystal structure. Experienced users can open the input files to edit the exact behavior, as explained [in this page](../../workflow-designer/subworkflow-editor/intro.md). 

# Constrained relaxation
    
For large structures where a full relaxation of cell size is not computationally feasible, priority should be given to relaxing atomic positions. 
    
In many cases, simulation software allows one to specify constraints in certain directions or specific atoms. In some cases one can significantly reduce the computation time for relaxations by only relaxing a certain number of atoms within the structure when appropriate. For example, when simulating a 256 atom Si silicon supercell with 1 Si atom replaced by a P atom, fixing positions of all atoms other than the 2nd nearest neighbors of P will improve the speed of the calculation significantly.

!!! Note "Tutorial"
    Please visit the [relaxation tutorial](../../tutorials/relaxation.md) for a more expansive and detailed look at adding a relaxation calculation as part of a workflow.

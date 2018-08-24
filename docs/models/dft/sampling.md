# k-points sampling of the Brillouin Zone

In the unit-specific "kgrid" settings sections in the "Important Settings" tab of the Subworkflow Editor interface lie the choice for the size and density of the grid of reciprocal k-points employed for sampling the Brillouin Zone of the electronic structure of the crystal under investigation. 

Together with a sufficiently high plane-wave cutoff for the electronic wavefunction explained in [this page](../../methods/pseudopotential/cutoffs.md), a sufficiently large size for this k-points grid is of paramount importance in establishing the overall accuracy of the corresponding DFT calculation, and preliminary convergence testing for this parameter is therefore mandatory. For instructions on how to add a preliminary convergence subworkflow add-on to the current workflow, please see [this page](../../workflow-designer/subworkflow-editor/actions-menu.md). 

The size of the grid of k-points is typically defined in terms of its dimensions in the three-dimensional reciprocal space (for example 10x10x10), in conjunction with the distance by which the grid is shifted in  reciprocal space in order to cover a wider volume of the Brillouin Zone. Both of these grid settings can be entered in their respective entries, "dimensions" and "shifts", under the "kgrid" section.

# The KPPRA option
 
 Alternatively, the option "KPPRA" can be selected through the right-hand side "preferKPPRA" checkbox to define the density of the grid of k-points in terms of k-points per reciprocal atom. The default minimum value for this KPPRA setting is indicated immediately below the "kgrid" header label.

# Other types of reciprocal space grids 

 Similar considerations as the above-mentioned elements apply to other types of unit-specific settings, such as the "qgrid" settings for defining reciprocal grids of q-points for performing phonon calculations, and the associated "igrid" settings. The reader is referred to Ref. 1 [[1](#links)] for a theoretical explanation of each of these grid concepts for sampling the reciprocal space of crystal structures, in the context of phonon calculations performed with Quantum Espresso. 
 
# Links

1. [Calculation of Phonon Dispersions on the Grid Using Quantum ESPRESSO](http://users.ictp.it/~pub_off/lectures/lns024/10-giannozzi/10-giannozzi.pdf)

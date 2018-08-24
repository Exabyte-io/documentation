# The Important Settings tab

When a new subworkflow is being created from scratch, the "Important Settings" tab is initially devoid of content. Once new computational Units are added to this new subworkflow (following the procedure outlined in [this page](units-flowchart.md)), the user will begin to see the settings global to all units contained in the subworkflow, as well as unit-specific settings, appearing in this tab. 

# Example for total energy calculation with DFT

An example of appearance of this "Important Settings" tab, for the case of a basic ground-state total energy subworkflow calculation performed with Quantum Espresso (comprising a single Unit of type "pw-scf"), is illustrated in the image below. In this image, the two most common types of input settings encountered in general DFT calculations, namely the wavefunction and the density "cutoffs", and the size of the grid of reciprocal k-points (the so-called "kgrid"), are both shown to be contained as part of this total energy subworkflow:

<img src="/images/important-settings-tab.png"/>

# Advanced examples of DFT calculations

More complex subworkflows for performing advanced DFT calculations, such as electronic band structure energy or phonon frequency calculations, will contain further settings in this tab, offering the possibility of defining such parameters as the path in reciprocal space for computing the corresponding dispersion curves. An example of such advanced unit-specific settings, for specifying the reciprocal path of k-points for a band structure dispersion calculation (the so-called "kpath"), is shown in the picture below:

<img src="/images/path-settings.png"/>

These widely-used types of global and unit-specific settings will now be reviewed in turn in the rest of this documentation page, from the point of view of their appearance within the Subworkflow Editor interface.

# Cutoff settings

The initial section of the "Important Settings" tab titled "cutoffs" contains settings which are always global to all units in the current subworkflow. In particular, under the label "wavefunction", the user can enter the plane-wave cutoff parameter for expanding the electronic wavefunction of the crystal.   

In the text field directly to the right, under the label "density", the user can then also set the cutoff for the electronic charge density and potential.

The user is referred to this [specialized documentation page](../../methods/pseudopotential/cutoffs.md) for a more detailed review of the above-mentioned cutoff concepts. 

# k-points grid settings

The settings in the "kgrid" section are normally unit-specific. The name of the subworkflow unit to which each kgrid settings section applies is indicated on top of each section. 

Under these kgrid settings lies the choice for the size and density of the grid of reciprocal electronic k-points, as described in the [corresponding page](../../models/dft/sampling.md).

# Reciprocal path settings

Sections containing unit-specific settings labelled either "kpath", "qpath", or "ipath", are necessary for defining the path in reciprocal space as part of a subworkflow for calculating band structure or phonon dispersion curves. The name of the unit to which each one of these settings sections applies is indicated on top of each section. Please refer to [this page](../../models/dft/paths.md) for more detailed explanations.


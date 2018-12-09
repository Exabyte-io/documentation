# Paths in reciprocal space for dispersion calculations

Sections in the "Important Settings" tab of the Subworkflow Designer interface containing unit-specific settings labelled either "kpath", "qpath", or "ipath", are necessary for defining the path in reciprocal space as part of a subworkflow for calculating electronic band structure energy or phonon frequency dispersion curves. 

In this type of settings section, the user is first presented with a graphic outline of the Brillouin zone of the crystal structure under consideration, drawn with respect to the indicated reciprocal coordinate system. In this image, the special symmetry k or q points in reciprocal space are labelled with the conventional Greek letters, and the path connecting them which is to be computed is traced in red. 

An example for specifying the reciprocal path of k-points for a band structure dispersion calculation (the so-called "kpath"), is portrayed in the picture below:

<img src="/images/path-settings.png"/>

The notions of "qpath" and "ipath" instead pertain specifically to phonon dispersion calculations, as explained in Ref. [[1](#links)]. 

Further information on the appearance and overall symmetry of such Brillouin Zones in reciprocal space is explained in Refs. [[2-3](#links)].  

## Order of reciprocal symmetry points

Below the image of the Brillouin Zone, the user can set the order of the special symmetry points of the Brillouin Zone defining the path in reciprocal space for computing the desired band structure energy or phonon frequency dispersion curves. By clicking on each Greek letter label listed here, the selection for the corresponding symmetry point can be changed as needed to alter their overall order in the path list. Alternatively, on the right-hand side of each entry in the list, two arrows can be found for swapping the order of the corresponding points accordingly. The "X" button can moreover be pressed to delete the point entry altogether. To insert new symmetry point entries and add them to the overall path, the "plus" sign icon at the bottom of the list can be clicked upon. 

## Path branches

Finally, the number of steps at which band structure energies or phonon frequencies have to be calculated, along each branch of the reciprocal path, can also be entered next to the Greek letter label of the symmetry point defining one of the branch ends (the other end-point is set by the subsequent entry in the list). 

## Links

1. [Calculation of Phonon Dispersions on the Grid Using Quantum ESPRESSO](http://users.ictp.it/~pub_off/lectures/lns024/10-giannozzi/10-giannozzi.pdf)
2. [Wikipedia Brillouin zone, Website](https://en.wikipedia.org/wiki/Brillouin_zone)
3. [Setyawan, Wahyu; Curtarolo, Stefano (2010). "High-throughput electronic band structure calculations: Challenges and tools". Computational Materials Science. 49 (2): 299–312](https://arxiv.org/pdf/1004.2974.pdf)


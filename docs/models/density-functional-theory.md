<!-- TODO by MH -->
<!-- TODO: add input file examples and reasons for using these parameters, link to relaxation page for relaxation examples, convergence for convergence examples -->


We use density functional theory, are currently support pseudopotential approximation as implemented in quantum espresso and VASP.

In most cases to have a reasonable level of confidence that a result can be trusted the total energy should not increase significantly when the k-point density is increassed.  This search for the appropriate density of k-points is called [k-point convergence](convergence-algorithms.md).

It is often desirable to obtain [relaxed structures](structural-relaxation.md) to ensure that your system is in the lowest total energy state configuration possible before computing your property.

# Additional resources
There are many well developed Density Functional Theory reviews on the web and below we list a few that we find the most helpful:

# Links
P. Hohenberg and W. Kohn, Phys. Rev. 136, B864 1964, http://journals.aps.org/pr/abstract/10.1103/PhysRev.136.B864
W. Kohn and L. J. Sham, Phys. Rev. 140, A1133 1965, http://journals.aps.org/pr/abstract/10.1103/PhysRev.140.A1133
J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77, 3865, http://journals.aps.org/prl/abstract/10.1103/PhysRevLett.77.3865

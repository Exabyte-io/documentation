# Density Functional Theory
 
Our platform currently supports multiple widely used first-principles quantum computational engines (see [applications](/software/overview.md)). These are based on the Density Functional Theory (DFT) [[1](#links)] theoretical model, for calculating approximate solutions to Schrodinger's Equations and associated physical properties. The reader who wishes to revise the fundamental theoretical framework underlying DFT is referred to the introductory literature on the subject [[2](#links)].

# Subtype

New subworkflows are by default based on the **Generalized Gradient Approximation** (GGA). **Local Density Approximation** is another commonly used subtype. 

# Functional

The particular default exchange-correlation functional is **Perdew, Burke and Ernzerhof** (PBE) [[3](#links)], which is widely used.

> NOTE: for planewave pseudopotential DFT the functional part matches that used in the corresponding [pseudopotential](/methods/pseudopotential/overview.md)

# Refiners

Hybrid Screened Exchange (HSE) [[4]](#links) or [[5]](#links) GW approximation (G0W0, for example) can be used as example refiners for a Density Functional Theory model.  

# Modifiers

DFT calculations might of might not treat the spin-orbit coupling interaction or magnetic interactions, which are both considered modifiers:

- Spin-Orbit Coupling (soc), a relativistic quantum physical interaction of a particle's spin with its motion inside a potential [[5](#Links)]. 

- Magnetism (magn), resulting from the spontaneous polarization (parallel lining up) of the spins of conduction electrons in ferromagnetic metals, such as iron, nickel and cobalt, giving rise to a magnetic moment in these materials even in the absence of an externally applied magnetic field [[6](#Links)].

# Links

Additional resourceful general references on DFT and associated concepts, beyond those outlined below, are contained in this [page](references.md), to be referred to at the reader's discretion.

1. [Wikipedia, Density Functional Theory](https://en.wikipedia.org/wiki/Density_functional_theory)
2. R.M. Martin: "Electronic Structure: Basic Theory and Practical Methods"; Cambridge University Press (2008)
3. [J.P. Perdew, K. Burke, M. Ernzerhof: "Generalized Gradient Approximation Made Simple"; Phys. Rev. Lett. 77, 3865 (1996)](https://users.wfu.edu/natalie/s11phy752/lecturenote/PhysRevLett.77.3865.pdf)
4. [Wikipedia, Hybrid Screened Exchange](https://en.wikipedia.org/wiki/Hybrid_functional#HSE)
5. [Wikipedia, GW Approximation](https://en.wikipedia.org/wiki/GW_approximation)
6. [Wikipedia, Spin–orbit interaction](https://en.wikipedia.org/wiki/Spin%E2%80%93orbit_interaction)
7. [Wikipedia, Ferromagnetism](https://en.wikipedia.org/wiki/Ferromagnetism)

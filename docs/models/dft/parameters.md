# Density Functional Theory Parameters
 
Our platform currently supports multiple widely used first-principles quantum computational engines (see [applications](../../software-directory/overview.md)). These are based on the Density Functional Theory (DFT) [^1] theoretical model, for calculating approximate solutions to Schrodinger's Equations and associated physical properties.
 
The reader who wishes to revise the fundamental theoretical framework underlying DFT is referred to the [introductory literature on the subject](references.md).

We present in what follows the [parameters](../parameters.md) which apply specifically to the DFT **model type**.

## Subtype

We support the following **Subtypes** [^1].

- **Generalized Gradient Approximation (GGA)**, on which new subworkflows are based by default
- **Local Density Approximation (LDA)**, another commonly used model subtype

## Functional

We support the following list of exchange-correlation functional flavours.

- **Perdew, Burke and Ernzerhof (PBE)** [^3], the flavor implemented by default which is widely used.

> NOTE: for planewave pseudopotential DFT the functional part matches that used in the corresponding [pseudopotential](../../methods/pseudopotential/overview.md)

## Refiners

The following can be used as example refiners for the DFT model.

- Hybrid Screened Exchange (HSE) [^4] 
- GW approximation [^5] (G0W0, for example)   

## Modifiers

DFT calculations might of might not treat the spin-orbit coupling interaction or magnetic interactions, which are both considered modifiers:

- Spin-Orbit Coupling (soc), a relativistic quantum physical interaction of a particle's spin with its motion inside a potential [^6]. 
- Magnetism (magn), resulting from the spontaneous polarization (parallel lining up) of the spins of conduction electrons in ferromagnetic metals, such as iron, nickel and cobalt, giving rise to a magnetic moment in these materials even in the absence of an externally applied magnetic field [^7].

## Links

Additional resourceful general references on DFT and associated concepts, beyond those outlined below, are contained in this [page](references.md), to be referred to at the reader's discretion.

[^1]: [Wikipedia Approximations (exchange–correlation functionals), Website](https://en.wikipedia.org/wiki/Density_functional_theory#Approximations_(exchange%E2%80%93correlation_functionals))
[^1]: [J.P. Perdew, K. Burke, M. Ernzerhof: "Generalized Gradient Approximation Made Simple"; Phys. Rev. Lett. 77, 3865 (1996)](https://users.wfu.edu/natalie/s11phy752/lecturenote/PhysRevLett.77.3865.pdf)
[^2]: [Wikipedia Hybrid Screened Exchange, Website](https://en.wikipedia.org/wiki/Hybrid_functional#HSE)
[^3]: [Wikipedia GW Approximation, Website](https://en.wikipedia.org/wiki/GW_approximation)
[^4]: [Wikipedia Spin–orbit interaction, Website](https://en.wikipedia.org/wiki/Spin%E2%80%93orbit_interaction)
[^5]: [Wikipedia Ferromagnetism, Website](https://en.wikipedia.org/wiki/Ferromagnetism)

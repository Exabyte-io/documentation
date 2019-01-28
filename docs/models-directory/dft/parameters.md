# Density Functional Theory Parameters
 
Our platform currently supports multiple first-principles simulation engines (see [applications](../../software/components.md)). These are based on the [Density Functional Theory (DFT)](overview.md) model.
 
The reader who wishes to revise the fundamental theoretical framework underlying DFT is referred to the [introductory literature on the subject](references.md).

We present in what follows the [parameters](../../models/parameters.md) which apply specifically to the DFT **model type**.

## Subtype

We support the following **Subtypes**:

- Local Density Approximation (`lda`) [^1]
- Generalized Gradient Approximation (`gga`) [^1] (default)

## Functional

We support the following list of exchange-correlation functionals.

- Perdew, Burke and Ernzerhof (`pbe`) [^2] (default).
- Perdew-Zunger (`pz`) [^3]

> NOTE: for planewave pseudopotential DFT the functional part matches that used in the corresponding [pseudopotential](../../methods-directory/pseudopotential/overview.md)

## Refiners

The following can be used as example refiners for the DFT model.

- Heyd-Scuseria-Ernzerhof (`hse`) [^4], a special class of [Hybrid Functionals](notes.md#hybrid-functionals).
- GW approximation [^5] (`g0w0`, for example)   

## Modifiers

DFT calculations might of might not treat the spin-orbit coupling interaction or magnetic interactions, which are both considered modifiers:

- Spin-Orbit Coupling (soc), a relativistic quantum physical interaction of a particle's spin with its motion inside a potential [^6]. 
- Magnetism (magn), resulting from the spontaneous polarization (parallel lining up) of the spins of conduction electrons in ferromagnetic metals, such as iron, nickel and cobalt, giving rise to a magnetic moment in these materials even in the absence of an externally applied magnetic field [^7].

## Links

Additional resourceful general references on DFT and associated concepts, beyond those outlined below, are contained in this [page](references.md), to be referred to at the reader's discretion.

[^1]: [Wikipedia Approximations (exchange–correlation functionals), Website](https://en.wikipedia.org/wiki/Density_functional_theory#Approximations_(exchange%E2%80%93correlation_functionals))
[^2]: [J.P. Perdew, K. Burke, M. Ernzerhof: "Generalized Gradient Approximation Made Simple"; Phys. Rev. Lett. 77, 3865 (1996)](https://users.wfu.edu/natalie/s11phy752/lecturenote/PhysRevLett.77.3865.pdf)
[^3]: [J.P. Perdew and A. Zunger: "Self-interaction correction to density-functional approximations for many-electron systems"; Phys. Rev. B 23, 5048 (1981)](https://journals.aps.org/prb/pdf/10.1103/PhysRevB.23.5048)
[^4]: [Wikipedia Hybrid Screened Exchange, Website](https://en.wikipedia.org/wiki/Hybrid_functional#HSE)
[^5]: [Wikipedia GW Approximation, Website](https://en.wikipedia.org/wiki/GW_approximation)
[^6]: [Wikipedia Spin–orbit interaction, Website](https://en.wikipedia.org/wiki/Spin%E2%80%93orbit_interaction)
[^7]: [Wikipedia Ferromagnetism, Website](https://en.wikipedia.org/wiki/Ferromagnetism)

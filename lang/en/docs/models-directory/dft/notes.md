# Special Notes 

We list in the present page some special notices concerning the [parameters](parameters.md) underlying the [Density Functional Theory model](overview.md).

## Accuracy Limits of the Generalized Gradient Approximation

### Electronic Band Gap

When computations of the [Electronic Band Gap](../../properties-directory/non-scalar/band-gaps.md) are executed through [Density Functional Theory](../../models-directory/dft/overview.md), operated in conjunction with the [Generalized Gradient Approximation](parameters.md#subtype) (GGA), a systematic **under-estimation of the band gap** is to be expected. This is a well-known shortcoming of the GGA technique, and should be taken into account when following the [procedure](../../tutorials/dft/electronic/band-gap.md) for calculating the band-gap of semiconducting materials. 

Further modifications to the input files and settings to correctly predict the band gap are possible, but lie beyond the scope of the present discussion.

## Hybrid Functionals

Hybrid functionals [^1] are a class of approximations to the exchange–correlation energy functional in DFT that incorporate a portion of exact exchange energy from Hartree–Fock theory [^2], with the rest of the exchange-correlation energy from other sources (ab-initio or empirical). 

This approach typically results in improved [precision](../../methods/precision.md) in the estimation of the values of numerous [material properties](../../properties/overview.md) of interest, as demonstrated in the scientific literature [^3].

A demonstration of the effectiveness of the HSE Hybrid Functional in predicting the [electronic band gap](../../properties-directory/non-scalar/band-gaps.md) of semiconducting materials is offered in the [relevant tutorial page](../../tutorials/dft/electronic/hse.md).

<!-- TODO: add corresponding theoretical background information about the GW method as well in respective task
-->

## Links

[^1]: [Wikipedia Hybrid functional, Website](https://en.wikipedia.org/wiki/Hybrid_functional)
[^2]: [The Hartree-Fock method, Document](https://web.stanford.edu/~kimth/www-mit/thk_hartreefock.pdf)
[^3]: [Sayan Kanungo, DFT Simulation Datasheet for Quantum Espresso, Indian Institute of Engineering Science and Technology, Shibpur, Jun 2017, Online Document](https://drive.google.com/file/d/185fPU--Zggp7yLt8lIMjzOaSKb4rH7a4/view?usp=sharing)

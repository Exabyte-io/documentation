# Calculate Electronic Band Structure with GW Approximation and Plasmon-pole Approach

This tutorial page explains how to calculate the [electronic band structure](../../../properties-directory/non-scalar/bandstructure.md) of a semiconducting material based on [Density Functional Theory](../../../models-directory/dft/overview.md). We consider a **Boron Nitride (BN) film monolayer** (in its hexagonal form) [^1] as our sample material, and use [Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md) as our main simulation engine during this tutorial.

!!!note "Quantum ESPRESSO version considered in this tutorial"
    The present tutorial is written for Quantum ESPRESSO at versions 5.2.1, 5.4.0, 6.0.0 or 6.3.

Here, we shall make use of the **"GW Approximation"**, which is reviewed in [this part of the documentation](../../../models-directory/dft/notes.md#the-gw-approximation). What sets the present tutorial apart from the [other tutorial](gw-qe-bs-fullfreq.md) on band structure calculations via the GW Approximation, as implemented under Quantum ESPRESSO, is the employment of the **Plasmon pole** approach [^2], as opposed to the Full-frequency method described in the latter separate tutorial. Whereas in the Full-frequency method a full-frequency axis sampling is performed, for the case of plasmon pole **we only sample at zero frequency**.

The aim of the present tutorial is to calculate the quasi-particle corrections for a BN film at the Gamma point. In this example, we use a **Godby-Needs plasmon-pole model** along the imaginary axis. The plasmon-pole method is enabled within Quantum ESPRESSO via the **SternheimerGW** additional code, which is introduced in the [other tutorial page on GW calculations](gw-qe-bs-fullfreq.md). The user is invited to consult this latter separate tutorial first for complete instructions on how to operate and execute Quantum ESPRESSO-based GW Workflows on our platform, since only plasmon pole-specific aspects of GW computations shall be reviewed and explained here.

## Workflow Structure

We shall now review the plasmon pole-specific components of the input file for the second main SternheimerGW compute [unit](../../../workflows/components/units.md), within the overall plasmon pole GW [Workflow](../../../workflows/overview.md) based upon the [Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md) modeling engine.

#### Truncation

If we do not specify a particular truncation (for both correlation and exchange) used to overcome the divergence of the Coulomb potential for small G vectors, a spherical truncation is employed. This relies on the system being somewhat isotropic. For films or other systems with strong anisotropy, the use of a spherical truncation is no longer appropriate. 

For films, such as the example being presently considered, using a "2d" truncation is recommended. Even more general is the Wigner-Seitz (ws) truncation, limiting the Coulomb interaction to the actual simulation box. Note that the initial setup of the ws truncation is not parallelized, so it might be quite computationally expensive for larger systems.

#### Configuration of the Coulomb and Green solver

Using the values `thres_coul` and `thres_green`, the user can tweak the accuracy of the linear solver to optimize it for the system under investigation. `max_iter_coul` and `max_iter_green` allow the user to specify a maximum number of iterations, that the linear solver should try to converge upon. If this maximum is exceeded, the code will try a different linear solver.

#### Configuration of W in the convolution

For comparison with other GW codes, SternheimerGW offers the possibility to evaluate the GW correction in the plasmon-pole (PP) model. When using the Godby-Needs PP model, the user must specify exactly the following two frequencies:

$$
\omega_1 = 0 \qquad \omega_2 = \text{i} \omega_\text{p}
​​$$

These two frequencies are then used to construct an approximation for the screened Coulomb interaction. Note that we do not make use of the analytic expression of this approximation, so the convolution to obtain the self-energy is not significantly faster.

## Create and Submit Job

The user should, at this point, follow the instructions included in the [alternative GW tutorial](gw-qe-bs-fullfreq.md#create-job) for explanations on how to create and execute a GW Workflow computational [Job](../../../jobs/overview.md), and on how to retrieve and inspect its corresponding results.

## Animation

We demonstrate the steps involved in the creation and execution of a GW band structure computation on a BN film (in its hexagonal form), using the [Quantum ESPRESSO](../../../software-directory/modeling/quantum-espresso/overview.md) simulation engine together with the SternheimerGW code for enacting the Plasmon pole sampling at zero frequency, in the following animation. 

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/kx60KAoNn9o" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

Here, we set the size along the z dimension of the k-grids and q-grid to 1, since we are considering a 2D material. In summary, we use a plane-wave cutoff of 80 Ry, k-grids size of 8 x 8 x 1 and q-grid size of 4 x 4 x 1.

The final result for the indirect band gap of the BN monolayer of 6.460 eV, between the Gamma and M Brillouin Zone special points, is in good agreement with other first-principles calculations [^3].

## Links

[^1]: [Wikipedia Boron nitride nanosheet, Website](https://en.wikipedia.org/wiki/Boron_nitride_nanosheet)

[^2]: [J. Lischner, S. Sharifzadeh, J. Deslippe, J.B. Neaton, and S.G. Louie: "Effects of self-consistency and plasmon-pole models on GW calculations for closed-shell molecules"; Phys. Rev. B 90, 115130 (2014)](https://arxiv.org/pdf/1409.2901.pdf)

[^3]: [D. Wickramaratne, L. Weston, and C.G. Van de Walle: "Monolayer to Bulk Properties of Hexagonal Boron Nitride"; J. Phys. Chem. C, 2018, 122 (44), pp 25524–25529](https://pubs.acs.org/doi/abs/10.1021/acs.jpcc.8b09087?journalCode=jpccck&)

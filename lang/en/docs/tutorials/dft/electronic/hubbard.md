# DFT+U and Hubbard parameter calculation in Quantum Espresso

In this tutorial we demonstrate how to perform DFT+U calculation, followed by
calculation of Hubbard parameter using Quantum Espresso simulation engine on our
web platform.

!!!warning
    Here we will follow the latest DFT+U syntax and method introduced in Quantum
    Espresso version `7.1`. The new template (syntax) **pw_scf_dft_u** is only
    available to Quantum Espresso version `7.1` or above. If the user would like
    to use old syntax, please select Quantum Espresso version `7.0` or below,
    and use **pw_scf_dft_u_legacy**.

1. Navigate to workflow page from the sidebar, and create new workflow. Expand
details section and select Quantum Espresso version `7.2` from the drop-down.

2. Click **Edit** button on the default **pw_scf** workflow unit. Expand details
pane in the unit modal, and select **pw_scf_dft_u** flavor/ template. Close the
unit modal.

3. Navigate to **Important Settings** tab, and scroll down to **hubbard**
section. Here we are able to specify the Hubbard U values specific to atomic
species and orbital (Hubbard manifold). You can add new or delete a row in the
Hubbard card.

4. We can use this workflow to run DFT+U PWscf calculation.

## Calculation of Hubbard parameters

Hubbard parameters can be obtained from the *first principles*. We will use
Quantum Espresso `hp.x` implementation of Linear Response theorem[^1]. For this,
we need to add new execution unit to our workflow. Click the edit unit button,
and select `hp.x` executable. The `q`-grid for `hp.x` can be modified in the
important settings.

In the below animation, we go through an example calculation.

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/Uh9OWJHKlQY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## References

[^1]: [HP – A code for the calculation of Hubbard parameters using density-functional perturbation theory, I. Timrov, N. Marzari, M. Cococcioni, Computer Physics Communications, **279**, 108455 (2022)](https://doi.org/10.1016/j.cpc.2022.108455).

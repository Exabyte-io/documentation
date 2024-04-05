# DFT+U and Hubbard parameter calculation in Quantum Espresso

In this tutorial, we demonstrate how to perform DFT+U calculation, followed by
calculation of Hubbard parameters using Quantum Espresso on our web platform.

## Create DFT+U workflow

First, we need to create PWscf workflow with DFT+U enabled.

### Add pw.x unit

A PWscf calculation
(using `pw.x`) is a prerequisite for the Hubbard parameter (using `hp.x`) calculation.

- Navigate to the workflows page from the sidebar and create a new workflow. Expand
details section and select Quantum Espresso version `7.2` from the drop-down.

![Navigation sidebar](/images/tutorials/hubbard/hubbard-01-navigation-sidebar.webp "Navigation sidebar")

![Select application version and build](/images/tutorials/hubbard/hubbard-02-select-ver-build.webp "Select application version and build")

- Click **Edit** button on the default **pw_scf** workflow unit. Expand the details
pane in the unit modal, and select **pw_scf_dft_u** flavor/ template. Close the
unit modal.

![Select executable and flavor](/images/tutorials/hubbard/hubbard-03-select-executable-flavor.webp "Select executable and flavor")

!!!warning
    Here we follow the latest DFT+U syntax and method introduced in Quantum
    Espresso version `7.1`. The new template (syntax) **pw_scf_dft_u** is only
    available to Quantum Espresso version `7.1` or above. If the user would like
    to use old syntax, please select Quantum Espresso version `7.0` or below
    and use **pw_scf_dft_u_legacy**.


### Add hp.x unit to the workflow

Hubbard parameters can be obtained from the *first principles*. We will use
Quantum Espresso `hp.x` implementation of Linear Response theorem[^1].

We can add the `hp.x` workflow to the previous PWscf (DFT+U) workflow by adding a new
execution unit. Click the edit unit button on the second unit, and select `hp.x`
executable. The `q`-grid for `hp.x` can be modified in the important settings
tab.

![Add new unit](/images/tutorials/hubbard/hubbard-04-add-new-unit.webp "Add new unit")

!!!tip
    We have a bank workflow **Hubbard U - HP** incorporating above two steps.
    Navigate to Bank Workflows page via left sidebar and search for
    *Hubbard U - HP* workflow, and copy/clone it to your account. Then you may
    further modify (as necessary) and use it.


## Create and submit job

After the above:

- Navigate to the jobs page via the sidebar menu and create a new job.
- Select material. Here, we have selected FeO. You can import new material from
banks or upload structure files.
- Select workflow, here, we select the Hubbard workflow that we just created.

![Select material and workflow](/images/tutorials/hubbard/hubbard-05-select-mat-workflow.webp "Select material and workflow")

- Navigate to **Important Settings** tab, and scroll down to **hubbard**
section. Here we are able to specify the Hubbard U values specific to atomic
species and orbital (Hubbard manifold). You can add new or delete a row in the
Hubbard card.

![Important settings](/images/tutorials/hubbard/hubbard-06-imp-settings.webp "Important settings")

![Edit Hubbard card](/images/tutorials/hubbard/hubbard-07-card-values.webp "Edit Hubbard card")

- Go to **Compute** tab, and select the number of processors and other compute
parameters.

![Set compute parameters](/images/tutorials/hubbard/hubbard-08-compute-parameters.webp "Set compute parameters")

!!!warning
    As of 20/Dec/2023, there is a bug in our platform that prevents running MPI
    jobs in a single processor when the Intel (default) build of Quantum
    ESPRESSO is used. Please select at least two processors/ cores when using
    Intel build as a workaround. Alternatively, you may use the GNU build of
    Quantum ESPRESSO.

    **Update (18-Feb-2024):** The above MPI bug is resolved in platform version
    `2024.2.15`. Now user may run MPI jobs on a single processor when using
    Intel build of Quantum ESPRESSO.

- Now, we are ready to submit the job for running the calculation.

![Results](/images/tutorials/hubbard/hubbard-09-result.webp "Results")

Once the job is finished, the Hubbard U values are shown in the **Results** tab.

## Step-by-step screenshare video

In the below animation, we go through an example calculation.

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/33PykNO8QlQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


## References

[^1]: [HP – A code for the calculation of Hubbard parameters using density-functional perturbation theory, I. Timrov, N. Marzari, M. Cococcioni, Computer Physics Communications, **279**, 108455 (2022)](https://doi.org/10.1016/j.cpc.2022.108455).

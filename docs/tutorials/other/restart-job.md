# Restart From Previous Run

This page explains how to **restart** a [Job](../../jobs/overview.md) from the **results of a previous calculation**.  We will restart from a previous "Electronic Density Mesh" simulation, which is reviewed in a [separate tutorial](../dft/electronic/electronic-density-mesh.md).

## Select Parent Job

In [Job Designer](../../jobs-designer/overview.md), Job restarting is accomplished via the [Select Parent Option](../../jobs-designer/actions-header-menu/select-parent.md) under the main [header menu](../../jobs-designer/header-menu.md) of the interface. 

The user should first create a new [Job](../../jobs/overview.md) with "Electronic Density Mesh" as the main [workflow](../../workflows/overview.md) by following the same instructions as in the [original tutorial](../dft/electronic/electronic-density-mesh.md#create-job). 

The next steps consist in finding the previously-run Electronic Density Mesh job via the aforementioned ["Select Parent" option](../../jobs-designer/actions-header-menu#select-parent-job), and in selecting that job in order to prepend its results as a precursor to the new restart job being created.  

## Submit Job

The same instructions for submitting and executing the restart Job as in the main electronic density mesh [tutorial](../dft/electronic/electronic-density-mesh.md#submit-job) can be followed.

## Animation

We demonstrate the above-mentioned steps involved in restarting an electronic charge density mesh computation workflow performed on silicon, using the [Quantum ESPRESSO](../../software-directory/modeling/quantum-espresso/overview.md) simulation engine, in the following animation. 

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/088lBmRzZ98" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

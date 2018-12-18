# Subworkflow

We define a **Subworkflow** as a set of distinct **units** (elementary calculations) combined together in a flowchart (algorithm), in order to extract one or more [properties](../../properties/overview.md). A subworkflow must be specific to a particular simulation engine [application](../../software/parameters.md), [model](../../models/overview.md) and [method](../../methods/overview.md).

## Model

A **Model** is an entity that contains **scientifically valuable information** about the approximations used for a **simulation**. Models are the object of a [separate discussion](../../models/overview.md).

## Method

A model may have multiple numerical **Methods**, or computational implementations, which are described in detail [here](../../methods/overview.md). A method is implemented inside a [simulation engine](#simulation-engine) (or application), and a single simulation engine can also use one or more methods.

## Simulation Engine

A **Simulation Engine** is an implementation of a simulation algorithm in software. The engines available on our platform are reviewed [in this section](../../software/parameters.md) of the documentation.

## Subworkflow Add-ons

There are certain types of (sub)workflows that are commonly used in practice. We have support for their quick **addition**, as explained for the following two cases.

### Convergence

This option converges a certain property with respect to the input parameters (Example: [k-point convergence of total energy](../addons/convergence-algorithms.md)). 

### Optimization

This second option optimizes the material's structure, typically with respect to the total energy, in order to find the most stable equilibrium configuration of the crystal structure (Example: [geometry optimization/structural relaxation](../addons/structural-relaxation.md)).

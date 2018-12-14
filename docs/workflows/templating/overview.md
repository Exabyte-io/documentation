# Templating for Input Scripts

We implement **templating** for generalizing and automating the generation of **input scripts**, which are necessary for executing relevant simulations through the required [simulation engine](../../software/modeling/applications.md). This ensures, for example, that the same template can conveniently be applied to many different [materials](../../materials/overview.md) under the same [simulation job](../../jobs/overview.md).

## [Important Templating Concepts](concept.md)

We review and explain the general concept of templating in computer science in [this page](concept.md). 

## [Template Engine](engine.md)

[Under this page](engine.md) we also introduce the basic syntax of the templating language that we adopt.

## [Exabyte Templating Conventions](exabyte-conventions.md)

The specific aspects of how templating is implemented on our platform are the object of [this discussion](exabyte-conventions.md).

## [Example](examples.md)

We provide an example of input script templating for a materials science computation [here](examples.md).

## [User Interface Components](ui.md)

The [User Interface components](ui.md) which are pertinent to setting templating options, for the generation of input scripts during the [Design stage of a new Workflow](../../workflow-designer/overview.md), are reviewed [in this page](../../workflow-designer/unit-editor/input-templates.md).

## [Tutorials](../../tutorials/templating/overview.md)

Additional examples on how templating can be adapted to different simulation circumstances, such as the need to vary certain input parameters based on material composition, or the need to set the initial magnetic moments in ferromagnetic material structures, are discussed in the relevant Tutorial section of our documentation, introduced [here](../../tutorials/templating/overview.md).

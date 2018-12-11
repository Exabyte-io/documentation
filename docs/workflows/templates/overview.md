# Templating for Input Scripts

We implement **templating** for the **generalized and automatic** generation of **input scripts** necessary for executing relevant simulations through the required simulation engine. This ensures, for example, that the same template can conveniently be applied to many different [materials](../../materials/overview.md) under the same [simulation job](../../jobs/overview.md).

## Important Concepts for Templating

We review and explain the general concept of templating in computer science in [this page](concept.md). 

## Jinja Template Engine

[Here](jinja-syntax.md), we also introduce the basic syntax of the templating language that we adopt.

## Exabyte Conventions

The specific aspects of how templating is implemented on our platform are the object of [this discussion](exabyte-conventions.md).

## Templating Example

We provide an example of input script templating for a materials science computation [here](examples.md).

## User Interface Components

The User Interface components which are pertinent to setting templating options, for generalizing and automating the generation of input scripts during the [Design stage of a new Workflow](../../workflow-designer/overview.md), are reviewed [in this page](../../workflow-designer/unit-editor/input-templates.md).

## Tutorials

Additional examples on how templating can be adapted to different simulation circumstances, such as the need to vary certain input parameters based on material composition, or the need to set the initial magnetic moments in ferromagnetic material structures, are discussed in the relevant Tutorial section of our documentation, introduced [here](../../tutorials/templating/overview.md).

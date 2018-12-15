# Templating Concept

**Templating** is a general concept [^1] for automating and generalizing the production of textual data based on a common source, referred to as the core **"Template"**. Template usually looks much like the final output, with placeholders instead of the actual data. The data, henceforth referred to as **Context**, is a set of **input parameters** which are passed to the template through the **Template Engine** in order to generate distinct outputs, each representing a custom variant of the original template.

## Origins in Web Development

Templating is commonly encountered in web publishing, where it lets web designers and developers work with web templates to automatically generate custom web pages. In this case, web templates support static content, providing the basic structure and appearance of the web page, on top of which more complex dynamic elements can then be added.

The basic process for a web templating system is illustrated in the picture below. Here, the content parameters of the web-page (originating from a database), and a web template, are combined together through the Template Engine to mass-produce web documents.

![Templating](../../images/workflows/templating.png "Templating")

## Use within the platform

In this respect, templates are applied to many different [materials](../../materials/overview.md) during the creation of [Jobs](../../jobs/overview.md), in conjunction with different input parameters (or template variables/context), specific for each material. 

We allow for using templates specifically inside the input of [units](../components/units.md) comprised in a [subworkflow](../components/subworkflows.md). In this way, we can decouple material-specific information from workflow-specific. The latter lets us apply a workflow for multiple materials at the same time, without having to adjust it extensively.


### Template Rendering

The templates (input files) are rendered in two places, on [web interface](../../ui/overview.md) when workflows (or jobs) are designed and in [computing clusters](../../infrastructure/clusters/overview.md) when the job is executed, henceforth referred to as **design-time rendering** and **runtime rendering** respectively. The is necessary as some templates require data which is only available at runtime (e.g. `outdir` in Quantum Espresso PWScf input file) 

## Links

[^1]: [Wikipedia Web template system, Website](https://en.wikipedia.org/wiki/Web_template_system)

# Templating Important Concepts

**Templating** is a general concept in computer science [^1] for automating and generalizing the mass-production of scripts based on a common fundamental framework, referred to as the core **"Template"** for those scripts. Different sets of **input parameters (or variables)** can then be passed to this template in order to generate distinct scripts, each representing a custom variant of the original template.

## Origins in Web Development 

Templating is commonly encountered in web publishing, where it lets web designers and developers work with web templates to automatically generate custom web pages. In this case, web templates support static content, providing the basic structure and appearance of the web page, on top of which more complex dynamic elements can then be added.

The basic process for a web templating system is illustrated in the picture below. Here, the content parameters of the web-page (originating from a database), and a web template, are combined together through the **Template Engine** to mass-produce web documents.

![Templating](../../images/workflows/templating.png "Templating")

## Jinja Template Engine

In the context of our platform, we make use of **Jinja** [^2] [^3], a text-based template engine originally intended for web development, but which we use for automating the generation of input scripts for materials science computations. In this respect, templates are particularly resourceful when they are applied to many different [material entities](../../materials/overview.md) in turn under the same [Job](../../jobs/overview.md), potentially in conjunction with different input computational parameters for each material. 

The syntax underlying the Jinja templating language is further described [in this page](jinja-syntax.md).

## Links

[^1]: [Wikipedia Web template system, Website](https://en.wikipedia.org/wiki/Web_template_system)

[^2]: [Jinja Templating Engine, Official Website](http://jinja.pocoo.org/)

[^3]: [Wikipedia Jinja (template engine), Website](https://en.wikipedia.org/wiki/Jinja_(template_engine))

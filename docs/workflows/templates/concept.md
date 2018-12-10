# Templating Important Concepts

**Templating** is a general concept in computer science [^1] for automating and generalizing the mass-production of scripts based on a common fundamental framework, referred to as the core **"Template"** for those scripts. Different sets of **input parameters (or variables)** can then be passed to this template in order to generate distinct scripts, each representing a custom variant of the original template.
 
Templating is commonly encountered in web publishing, where it lets web designers and developers work with web templates to automatically generate custom web pages. In this case, web templates support static content, providing the basic structure and appearance of the web page, on top of which more complex dynamic elements can then be added.

The basic process for a web templating system is illustrated in the picture below. Here, the content parameters of the web-page (originating from a database), and a web template, are combined together through the **Template Engine** to mass-produce web documents.

![Templating](../../images/workflows/templating.png "Templating")

In the context of our platform, we make use of **Jinja** [^2] [^3], a text-based template engine originally intended for web development, but which we use for automating the generation of input scripts for materials science computations. In this respect, templates are particularly resourceful when they are applied to many different [material entities](../../materials/overview.md) in turn under the same [Job](../../jobs/overview.md), potentially in conjunction with different input computational parameters for each material. 

## Basic Syntax

In the Jinja templating language, there exist a few kinds of delimiters. The default delimiters are configured following the general conventions of the **Jinja syntax** [^4], as explained in the list below.

- `{% ... %}`: for **Statements**
- `{{ ... }}`: for **Expressions** to print to the template output
- `{# ... #}`: for **Comments** not included in the template output
- `#  ... ##`: for **Line Statements**

The following simple example illustrates the basic syntax behind the functioning of Jinja templating expressions for inserting variables, based on the use of pairs of curly braces mentioned above.

```
{{name}} has the chemical formula {{formula}}.
```

If name=`Silica` and formula=`SiO2`, then the templating engine will generate, or **Render**, the following **final output** after acting upon the above template **input**.

```
Silica has the chemical formula SiO2.
```

The database of input variable definitions and associated values is called the **Context** of the template, which is typically stored in the form of a **Dictionary** of keyword-value pairs. 

## Loops and Conditional Statements

Control structures such as Loops and Conditional Statements can control the flow of the template. Here, we cover conditionals and for-loops by way of examples.

### Conditionals

A basic conditional "if/else" type of statement in Jinja would consist in the following block of statements.

```
{% if truth %}
 This is true
{% else %}
 This is false
{% endif %}
```

### For-Loops

We now create a template containing a "for-loop" as follows. 

```
{% for color in colors %}
    {{ color }}
{% endfor %}
```

We then pass the following list to the above template: `colors = ['red', 'green', 'blue']`. As a result, the following output will be rendered.

```
    red

    green

    blue
```


## Passing Standard Output

It is often convenient to pass the output of one unit to another. This can currently be accomplished for standard output at the subworkflow level through referencing units by name.

For example, let's assume that a workflow contains a subworkflow with a single shell script unit named "grep-nbands", which has the following input (it is assumed that it returns a number as part of its standard output).

```bash
grep "NBANDS" ./OUTCAR | awk '{print $3}'
```

Then the units inside any of the ensuing subworkflows can reference the result of the above unit at **runtime**, by using a special template variable inside their input template as follows.

```jinja
NBANDS = {% raw %} {{grep-nbands.stdout}} {% endraw %} 
```

Note the usage of "raw" filter in order to make sure that the *Design-time* rendering will still preserve the content as `NBANDS = {{grep-nbands.stdout}}`.



## Links

[^1]: [Wikipedia Web template system, Website](https://en.wikipedia.org/wiki/Web_template_system)

[^2]: [Jinja Templating Engine, Official Website](http://jinja.pocoo.org/)

[^3]: [Wikipedia Jinja (template engine), Website](https://en.wikipedia.org/wiki/Jinja_(template_engine))

[^4]: [Jinja Template Designer Documentation, Website](http://jinja.pocoo.org/docs/2.10/templates/)

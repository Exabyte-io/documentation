# Template Engine

In the context of our platform, we make use of **Jinja** [^1] [^2], a text-based [template engine](concept.md) originally intended for web development, but which we use for automating the generation of input scripts for materials science computations. In this respect, templates are particularly resourceful when they are applied to many different [material entities](../../materials/overview.md) in turn under the same [Job](../../jobs/overview.md), potentially in conjunction with different input computational parameters for each material. 

We allow for using Jinja templates specifically inside the input to individual [units](../components/units.md) comprised in a [subworkflow](../components/subworkflows.md) computation. In this way, we can decouple material-specific information from workflow-specific. The latter lets us apply a workflow for multiple materials at the same time, without having to adjust it extensively.

We introduce in this page the basics of the syntax employed in the Jinja template engine. An introductory Jinja tutorial can be found under Ref. [^3], complementing the contents of the present documentation page. The reader is also referred to the official documentation [^4].

## Basic Syntax

In the Jinja templating language, there exist a few kinds of delimiters. The default delimiters are configured following the general conventions of the **Jinja syntax** [^4], as explained in the list below.

- `{% ... %}`: for **Statements**
- `{{ ... }}`: for **Expressions** to print to the template output
- `{# ... #}`: for **Comments** not included in the template output
- `#  ... ##`: for **Line Statements**

### Inserting and Defining Variables

The following simple example illustrates the basic syntax behind the functioning of Jinja templating expressions for inserting variables, based on the use of pairs of curly braces mentioned above.

```jinja2
{{name}} has the chemical formula {{formula}}.
```

If name=`Silica` and formula=`SiO2`, then the templating engine will generate, or **Render**, the following **final output** after acting upon the above **template input**.

```jinja2
Silica has the chemical formula SiO2.
```

The database of input variable definitions and associated values is called the **Context** of the template, which is typically stored in the form of a **Dictionary** of keyword-value pairs. 

### Variables Assignment

Inside code blocks, the user can also **assign** values to variables using the **"set" statement**, such as in the following example, where `element_name` is the variable name and `"Al"` represents its assigned value.

```jinja2
{% set element_name = "Al" %}
```

### Nested Context Dictionaries

Jinja additionally employs a **dotted notation** for importing variables from across different levels across nested context dictionaries. For example, in the case of the nested context shown below, the KPPRA variable would be imported from its parent keyword "kgrid" as shown in the ensuing line.

```jinja2
{
    "kgrid": {
        "KPPRA": 32000,
    }
}
```

```jinja2
KPPRA =  {{kgrid.KPPRA}} 
```

## Loops and Conditional Statements

Control structures such as Loops and Conditional Statements can control the flow of the template. Here, we cover conditionals and for-loops by way of examples.

### Conditionals

A basic conditional "if/else" type of statement in Jinja would consist in the following block of statements.

```jinja2
{% if truth_value %}
This is true
{% else %}
This is false
{% endif %}
```

If `truth_value=True`, then the output once the above template is rendered will be `This is true`, since the first truth condition of the above statements block is met.

### For-Loops

We now create a template containing a "for-loop", as in the following example.

```jinja2
{% for element in elements %}
{{ element }}
{% endfor %}
```

If `elements = ['Bi', 'O', 'Cu']`, then the following output is rendered.

```
    Bi

    O

    Cu
```

## Filters

Variables in Jinja can be modified by **filters**. Filters are separated from the variable by a **pipe symbol (|)**, and may have optional arguments passed to them in parentheses. Multiple filters can also be **chained**, meaning that the output of one filter is applied to the next.

Jinja supports a set of **built-in filters**, which are reviewed in its documentation web-page [^5]. 

## Links

[^1]: [Jinja Templating Engine, Official Website](http://jinja.pocoo.org/)

[^2]: [Wikipedia Jinja (template engine), Website](https://en.wikipedia.org/wiki/Jinja_(template_engine))

[^3]: [Jinja2 Templating Engine Tutorial, Website](https://medium.com/@jasonrigden/jinja2-templating-engine-tutorial-4bd31fb4aea3)

[^4]: [Jinja Template Designer Documentation, Official Website](http://jinja.pocoo.org/docs/2.10/templates/)

[^5]: [Jinja Built-in Filters, Official Documentation](http://jinja.pocoo.org/docs/2.10/templates/#builtin-filters)


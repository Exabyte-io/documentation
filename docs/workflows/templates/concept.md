# Templating Important Concepts

#Template is a general concept in computing....

**Jinja** [^1] [^2] is a text-based **template engine**. It was first developed for web dev, but we use it for writing materials input scripts

A particularly useful application of templating, in the context of our platform, consists in using the same template for generating the main input scripts of the simulation engine under consideration, and applying it to many different materials in turn, potentially in conjunction with different input computational parameters for each material. 

## Syntax

The following simple template example illustrates the basic syntax behind the functioning of the Jinja templating engine, which is based on the use of pairs of curly braces.

```
{{name}} has the chemical formula {{formula}}.
```

If name=`Silica` and formula=`SiO2`, then the templating engine will generate, or **render**, the following output starting from the above template input.

```
Silica has the chemical formula SiO2.
```

The list of input variable definitions and associated data is called the **Context** of the template, which is typically stored as a **Python Dictionary** of keyword-value pairs. 

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

[^1]: [Jinja Templating Engine, Official Website](http://jinja.pocoo.org/)

[^2]: [Wikipedia Jinja (template engine), Website](https://en.wikipedia.org/wiki/Jinja_(template_engine))

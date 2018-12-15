# Template Engines

We make use of **Jinja2** [^1], a [template](concept.md)  engine written in pure Python and **Swig** [^2], a JavaScript template engine with similar methodologies as Jinja2 to render the templates (input file) at [**runtime** and **design time**](concept.md#template-rendering) respectively. 

The templating syntax for the above engines are very similar, however, there are differences. Most importantly, Swig provides access to native JavaScript constructs, while Jinja2 enables access to Python (like `list.append()` in Python, but `array.push()` in Javascript). However, if accessing the native language features are avoided and solely relied on pure templating features, it should be easy to make templates compatible.

We introduce in this page the basics of the syntax used by both engines. The reader is referred to the official documentations for further information [^1][^2].

## Basic Syntax

The general convention of the syntax [^3]:

- `{% ... %}`: for **Statements**
- `{{ ... }}`: for **Expressions** to print to the template output
- `{# ... #}`: for **Commentaries** not included in the template output

### Variables Assignment

Inside code blocks, the user can also **assign** values to variables using the **"set" statement**, such as in the following example, where `element_name` is the variable name and `"Al"` represents its assigned value.

```jinja2
{% set element_name = "Al" %}
```

### Inserting Variables

The following simple example illustrates the basic syntax for inserting variables, based on the use of pairs of curly braces mentioned above.

```jinja2
{{name}} has the chemical formula {{formula}}.
```

If `name="Silica"` and `formula="SiO2"`, then the templating engine will generate, or render, the following final output after acting upon the above template input.

```jinja2
Silica has the chemical formula SiO2.
```

### Accessing Context Nested Keys

The **bracket notation** is employed for accessing keys from different levels across a nested context. For example, in the case of the nested context shown below, the KPPRA variable would be imported from its parent keyword "kgrid" as shown in the ensuing line.

```jinja2
{
    "kgrid": {
        "KPPRA": 32000,
    }
}
```

```jinja2
KPPRA =  {{ kgrid["KPPRA"] }} 
```

!!! tip "Dot Notation"
    For the template variables rendered at design time one can use Javascript "dot notation" to access a nested key.

    ```jinja2
    KPPRA =  {{ kgrid.KPPRA }} 
    ```

The input variable definitions and associated values are provided in the **Context** of the template. 

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

If boolean `truth_value` resolves to `true`, then the output of the above template will be `This is true` and vice versa.

### Loops

We now create a template containing a "for" loop, as in the following example.

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

Template variables can be modified by **filters**. Filters are separated from the variable by a **pipe symbol (|)**, and may have optional arguments passed to them in parentheses. Multiple filters can also be **chained**, meaning that the output of one filter is applied to the next.

Supported Jinja2 **built-in filters** are reviewed in its documentation web-page [^4]. 
The reader is also referred to Swig official documentation for a list of supported filters [^5]. 

## Javascript Native Prototypes Support in "Swig"

All Javascript-related prototypes such as *Array* [^6] and *Object* [^7] are supported by Swig, as long as the function does not require a callback (function) as one of its arguments. For example `Array.prototype.find()` is not supported by Swig as it needs a callback, however it can be implemented by pure templating features as below.

```jinja2
{% set elements = [{"id": 0, "value": "Si"}, {"id": 1, "value": "Ge"}] %}
{% set element = "" %}
{% set element_found = false %}
{% for element_ in elements %}
  {% if not element_found and element_["id"] == 1 %}
    {% set element = element_ %}
    {% set element_found = true %}
  {% endif %}
{% endfor %}
element = {{ element["value"] }}
```  

## Links

[^1]: [Jinja Templating Engine, Official Website](http://jinja.pocoo.org/)

[^2]: [Swig template engine, Official Documentation](http://node-swig.github.io/swig-templates/)

[^3]: [Jinja Template Designer Documentation, Official Website](http://jinja.pocoo.org/docs/2.10/templates/)

[^4]: [Jinja Built-in Filters, Official Documentation](http://jinja.pocoo.org/docs/2.10/templates/#builtin-filters)

[^5]: [Swig Built-in Filters, Official Documentation](http://node-swig.github.io/swig-templates/docs/filters/)


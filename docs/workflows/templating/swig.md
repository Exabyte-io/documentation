# Swig

As mentioned in [Template Engines](./engines.md) we make use of **Swig** to render the templates on the [Web Interface](../../ui/overview.md). 
We introduce in this page Swig-specific templating statements and its support for native Javascript prototypes.

## Javascript Native Prototypes

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

## Specific Statements

### Spaceless

`{% spaceless %}` statement ensures that the text is rendered with no extra white spaces or empty lines added to it, and has to be terminated by `{% endspaceless %}`.

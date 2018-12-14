# Swig

We make use of the **"Swig" template engine** [^1], which adds support for [Jinja syntax](engine.md) within a Javascript/ES6 environment. All Javascript-related prototypes such as *Array* and *Object* [^2] are supported, as long as the function does not require a callback (function) as one of its arguments (e.g. `Array.prototype.find()` would not work).

## Specific statements

### Spaceless

`{% spaceless %}` statement ensures that the text is rendered with no extra white spaces or empty lines added to it, and has to be terminated by `{% endspaceless %}`.

## Links

[^1]: [Swig template engine, Official Documentation](http://node-swig.github.io/swig-templates/)
[^2]: [Javascript Global Objects, MDN Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/)

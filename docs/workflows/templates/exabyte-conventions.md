# Exabyte Templating Conventions

Following the [general introduction](concept.md) to the templating concepts and language using the Jinja engine, we now review the specific aspects concerning its implementation in the context of our platform.

## "Swig" Javascript Implementation of Jinja  

In our implementation of templating, we make use of the **"Swig" template engine** [^1], which adds support for Javascript/ES6 to the Jinja templating language.

## Context in our platform

Two different contexts on our platform - WebApp and Execution
Schemas for VASP, QE, Other applications # maybe move to application
Different variables are available in each - In particular Execution only has WORKDIR variable, WebApp has all the rest
"Raw" syntax necessary when entering Execution variables under WebApp
Raw is necessary for preventing WebApp from rendering Execution variables, because they are not available there

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

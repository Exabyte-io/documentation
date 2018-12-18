# Exabyte Templating Conventions

Following the [general introduction](concept.md) to the templating concepts and language, we now review the specific aspects concerning its implementation in the context of our platform.

## "Swig" Implementation of Jinja syntax

As explained in this [dedicated page](swig.md).

## Contexts in our Platform

As introduced [in this section](engine.md#inserting-and-defining-variables), we define the **Context** of a template as a database of input variable definitions and associated values. There are two different contexts on our platform, the first related to the **[Web Interface](../../ui/overview.md)** and the second associated with the **Execution Stage** of the [simulation Job](../../jobs/overview.md) on the corresponding [computing clusters](../../infrastructure/clusters/overview.md). We shall henceforth refer to these two contexts as the **"Web Context"** and **"Execution Context"** respectively.

### Availability of Variables in Contexts

Different variables are available in each of the two contexts mentioned above. In particular, the Execution Context only has access to the `JOB_WORK_DIR` variable defining the main [Working Directory](../../jobs-cli/batch-scripts/directories.md) for the [Job](../../jobs/overview.md) under consideration. This is a system-level [Environment Variable](../../jobs-cli/batch-scripts/directives.md#environment-variables) that will be resolved only during the final runtime. 

The Web Context on the other hand has access to all other available variables, such as those presented in the [templating examples](examples.md).

### "Raw" Syntax for Execution Variables in Web Context

The "Raw" filter syntax is required when referring to the Execution variables under the "Web Context". This is necessary for preventing the Web Interface from rendering these variables during the **Design-time rendering**, given that such variables are only available during the ensuing **Execution-time rendering** (Design rendering first occurs during the [job design](../../jobs-designer/overview.md) stage, where multiple materials can be selected within a single job design session).

Hence, for example, the above-mentioned `JOB_WORK_DIR` variable would need to be entered as follows in a [Quantum ESPRESSO](../../software-directory/modeling/quantum-espresso/overview.md) input script template, containing the line which defines the pseudopotential directory inside the [Working Directory](../../jobs-cli/batch-scripts/directories.md).

```jinja2
pseudo_dir = {% raw %}'{{ JOB_WORK_DIR }}/pseudo'{% endraw %}
```

In this way, the job working directory will only be assigned at the time of job execution, based on the [account](../../accounts/overview.md) and job/workflow information provided automatically.

## Passing Standard Output

It is often convenient to pass the output of one [unit](../components/units.md) to another. This can currently be accomplished for the case of standard output at the [subworkflow](../components/subworkflows.md) level, through referencing units by name.

For example, let's assume that a [workflow](../overview.md) contains a subworkflow with a single shell script unit named "grep-nbands", which has the following input (it is assumed that it returns a number as part of its standard output).

```bash
grep "NBANDS" ./OUTCAR | awk '{print $3}'
```

Then the units inside any of the ensuing subworkflows can reference the result of the above unit at execution stage, by using a special `stdout` variable inside their input templates as follows.

```jinja2
NBANDS = {% raw %} {{grep-nbands.stdout}} {% endraw %} 
```

Note the usage of the aforementioned "Raw" filter, in order to make sure that no Design-time rendering is performed in this case.

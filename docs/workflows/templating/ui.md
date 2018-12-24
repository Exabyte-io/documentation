# Templating Implementation on User Interface

The implementation of the [Jinja-powered](jinja.md) [Templating and Rendering](concept.md) of simulation input files can be found and customized by the user under the relevant section of the [Workflow Designer Interface](../../workflow-designer/unit-editor/input-templates.md) of our platform.

## Editing Unit Input

There are two ways to access the Workflow Designer Interface and edit the templating input of an individual [unit](../components/units.md).

### From Workflow Explorer

The user can edit and save the template directly inside the [workflow](../../workflows/overview.md) itself, by [opening](../../entities-general/actions/open-edit.md) its entry as listed under the [Workflows Explorer Interface](../../workflows/ui/explorer.md) for browsing the corresponding account-owned [collection](../../accounts/collections.md). In this case, **all** [jobs](../../jobs/overview.md) that will subsequently be created with this workflow will inherit the changes. 

### From Job Designer

Alternatively, the user can edit the template during [job creation](../../jobs-designer/overview.md), under the corresponding [Workflow Tab](../../jobs-designer/workflow-tab.md). In this other case, only the job being currently designed will have its input changed, but not the original entry of the workflow itself.

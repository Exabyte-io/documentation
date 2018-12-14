# Applications

The concept of **"Software Application"** is related to the main **modeling engine** and associated software tools employed by the user for the design, execution and postprocessing of a [simulation Job](../jobs/overview.md), through the implementation of any of the available [computational methods](../methods/overview.md). 

## Structured Representation of Applications

We provide below an example of JSON-based structured representation for an application, based upon the [Exabyte Data Convention](../data-structured/overview.md) implemented on our platform. This representation contains information about the application's name, summary description, and version number/build.

```json tab="Schema" 
{!schema/software/application.json!}
```

```json tab="Example" 
{!example/software/application.json!}
```

## Executables and Flavors

Each application may be comprised of one or multiple [Executables](components/executables.md), implementing in turn different possible computation [Flavors](components/flavors.md).

# Structured Representations

We provide below examples of JSON-based structured representation for an application, and for each of its possible [components](overview.md#applications) (executables and flavors) and [classification categories](classification/overview.md). This structured representation is based upon the [Exabyte Data Convention](../data-structured/overview.md) implemented throughout our platform. 

!!!note "Unavailability of structured data for some Applications"
    Not all applications have been integrated on our platform to the point of having their own structured representation. For example the software codes, among those listed [here](../software-directory/overview.md), which are only available via [Command Line Interface](../cli/overview.md) rely entirely on [unstructured data files stored on disk](../data-on-disk/overview.md).

## Application

This representation contains information about the application's name, summary description, and version number/build.

```json tab="Schema" 
{!schema/software/application.json!}
```

```json tab="Example" 
{!example/software/application.json!}
```

## [Executable](components.md#executables)

```json tab="Schema" 
{!schema/software/executable.json!}
```

```json tab="Example" 
{!example/software/executable.json!}
```

## [Flavor](components.md#flavors)

```json tab="Schema" 
{!schema/software/flavor.json!}
```

```json tab="Example" 
{!example/software/flavor.json!}
```

## Application Classification Categories

### Exabyte Machine Learning Engine

We have reproduced below the [structured representation](../data-structured/overview.md) for our own Exabyte [Machine Learning Engine](classification/machine-learning.md). 

```json tab="Schema" 
{!schema/software/ml/exabyteml.json!}
```

```json tab="Example" 
{!example/software/ml/exabyteml.json!}
```

### Modeling

We present the [structured representations](../data-structured/overview.md) for those [modeling engines](classification/modeling.md) which are supported on our platform in their respective [documentation sections](../software-directory/overview.md).

### Scripting

We present in what follows the [structured representations](../data-structured/overview.md) for those [scripting languages](classification/scripting.md) that are [supported on our platform](../software-directory/overview.md).

#### Shell Scripting

```json tab="Schema" 
{!schema/software/scripting/shell.json!}
```

```json tab="Example" 
{!example/software/scripting/shell.json!}
```

#### Python

```json tab="Schema" 
{!schema/software/scripting/python.json!}
```

```json tab="Example" 
{!example/software/scripting/python.json!}
```

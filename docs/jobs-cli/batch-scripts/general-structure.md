# Batch Script General Structure

The [Batch Scripts](overview.md) used for [job submission via CLI](../overview.md) have a general structure subdivided into several main sections, corresponding to each highlighted panel in the image below. The reader is referred to their number labels for finding their ensuing explanations.

![Batch Script General Structure](/images/jobscript_structure.png "Batch Script General Structure")

A common convention is to append the suffix ".pbs" or ".job" or ".sh" to the filename of batch scripts.

## 1. Shebang

The **shebang** [^1] is a short character sequence at the beginning of the Batch Script. It uses the "#!" syntax to indicate an interpreter for execution of the script under UNIX / Linux operating systems. Typically, the shebang of our Batch Scripts consists in either of the following options for selecting the corresponding [environment](../../cli/environment.md#shell-type) of the shell interpreter.

- `#!/bin/sh` – Execute the file using the **Bourne shell**, or a compatible shell, with path `/bin/sh`.
- `#!/bin/bash` – Execute the file using the **Bash shell**.

## 2. Comments (if needed)

Comments (annotations) can conveniently be written anywhere within the batch script at the user's discretion, by inserting the "hash" character `#` at the start of the corresponding line.
 
Comments may consist in any text string containing any type of character, except for placing an exclamation mark `!` or `PBS` character sequences immediately after the hash, since these character combinations are reserved respectively for the above-mentioned shebang, and for the scheduler directives explained below.

## 3. Directives

As introduced [here](overview.md#implementation), we make use of the **Portable Batch System (PBS)** protocol for organizing job scheduling on our platform. A comprehensive set of **PBS directives** is available for setting the relevant job parameters, such as allocating the necessary [computational resources](../../infrastructure/compute/parameters.md). 

These directives are the object of a [dedicated review](directives.md).

## 4. Commands

**Unix commands** can be inserted towards the bottom of the batch script, following the conventions of Shell scripting. The most frequently needed commands for parallel batch job execution are described [in this page](commands.md).

## Links

[^1]: [Wikipedia Shebang (Unix), Website](https://en.wikipedia.org/wiki/Shebang_(Unix))

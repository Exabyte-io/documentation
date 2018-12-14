# Executables

[Applications](applications.md) are typically run via the launching of their respective **executable binary files** [^1] (more simply referred to as **executables**), of which there may be just one or multiple.

## Structured Representation of Executables

We provide an example of [structured representation](../../data-structured/overview.md) for an application-specific executable in what follows.

```json tab="Schema" 
{!schema/software/executable.json!}
```

```json tab="Example" 
{!example/software/executable.json!}
```

## Example from Quantum ESPRESSO

The [Quantum ESPRESSO](../../software-directory/modeling/quantum-espresso.md) modeling application for example is comprised of the following main input executables [^2], included as part of its distribution package.

- PWscf (pw.x)
- PHonon: ph.x, dynmat.x
- PWneb (neb.x)
- PWCOND (pwcond.x)
- CP (cp.x)
- TurboTDDFT: turbo_lanczos.x, turbo_spectrum.x, turbo_davidson.x .
- XSpectra (xspectra.x)
- atomic (ld1.x)

!!!warning "Implementation on our platform"
    Only a subset of the above executables have been implemented on our platform so far, as can be deduced from the list of available executables under the [Unit Editor Interface](../../workflow-designer/unit-editor.md#application).

Other applications such as [VASP](../../software-directory/modeling/vasp.md) on the other hand contain just a single main executable, through which all of its supported computation features can be performed.

## Links

[^1]: [Wikipedia Executable, Website](https://en.wikipedia.org/wiki/Executable)

[^2]: [Quantum ESPRESSO Input Data Description, Official Website](https://www.quantum-espresso.org/resources/users-manual/input-data-description)

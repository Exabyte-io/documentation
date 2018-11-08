# Structure-based approach

Our current work is focused on **structure-based** atomistic approach, where the information about the atomistic arrangement is known *a priori* (see [data conventions](/data/convention/overview.md)).

!!! note "Non-structure-based scenario"
    Our data convention has support for materials data where no structural information is available, however this topic is beyond the content of the current documentation.

## Features, Fingerprints, Targets

On many occasions, terms "Features", "Fingerprints", "Targets" are used for materials informatics purposes. For example, when constructing a machine learning model, a dataset containing information about multiple materials is used in order to find regular patterns and inter-dependencies. Such dataset is usually split into properties that represent the known data, or *features*, and the properties to be predicted, or *targets*.

 First we clarify this terminology as follows.

- **Feature**: any property of a material, eg. density or electronic band gap.
- **Fingerprint**: property of a material used as an input for a (statistical modeling) Workflow, equivalent of **Descriptive** property by definition

    > By default, we only store the minimal amount of information required to identify a material enough to reveal a set of its **Fingerprints**. Such minimal set of properties is called **Identity Fingerprints**, and the rest - **Derived Fingerprints**.

 - **Target**: property of a material used as an input for a (statistical modeling) Workflow, equivalent of a **Characteristic** property by definition.

 Thus a *property-descriptive-characteristic* triad is equivalent to *feature-fingerprint-target*.

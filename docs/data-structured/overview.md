# Data Classification

We now consider the general practices for managing data related to materials modeling and computation, and identify the categories and relationships between them. 

# By domain

Firstly, we identify the domain of the data.

- **materials**: information uniquely associated with a certain [material](/materials/overview.md).
- **workflows**: information about a computational [Workflow](/workflows/overview.md) routine used to extract the data.
- **other**: any other information.

> NOTE: it is generally possible to disentangle the data about materials from that concerning the Workflow program that extracts the properties of such materials. The "Other" category exists for the limiting cases where such a distinction is problematic.

# By source

We further classify data into the following three main subtypes, distinguished by their source.

- **experimental**: obtained with experimental equipment.
- **model**: obtained using modeling (computational or analytical).
- **other**: data that cannot be classified according to any of the above.

# By publication status

When the data is first obtained it can be raw, or unprocessed. The opposite occurs when the data is assembled for a peer-reviewed publication, and was able to pass multiple filter channels.
 
- **raw**: directly obtained from the source.
- **published**: published in a peer-reviewed journal or analogs.

# Advanced Materials Search

The steps for performing [advanced searche](/entities-general/actions/advanced-search.md) for Materials are illustrated in the animation below. 

We use the advanced search query builder to construct a query that filters the large dataset of materials (over 4000 entries) according to the formula ("Al"), unit cell volume (less than "80" in cubic Angstroms) and tags containing a certain keyword ("high pressure").

<img data-gifffer="/images/advanced_search.gif" />

# Searchable Properties 

The following materials keywords are available.

## Generic Keywords

Generic keywords present for all materials are described below. These can also be referred to as [descriptive properties](/data/convention/structured.md#by-relation-to-workflow).

| Keyword    |   Description      |  
| :-------- |:----------- |
| name | Name of the Material | 
| formula | Chemical formula, for example "CaTiO3" | 
| latticeType | The [Bravais lattice type](/materials-designer/source-editor/lattice.md) of the crystal structure under consideration |
| model  | The [theoretical model](/models/overview.md) employed to calculate the materials properties  | 
| method | The [computational method](/methods/overview.md) implementing the above model |  
| spaceGroupSymbol | The space group symbol describing the symmetry elements present in the crystal structure, e.g. "Fd-3m" | 
| volume  | The volume of the unit cell of the structure, in units of angstrom^3 | 
| density | The density of the crystal structure, in units of g/cm^3 | 
| owner | The Account name which [owns](/entities-general/ownership.md) the material under consideration  |
| tags | Descriptive [metadata](/entities-general/data.md#Metadata) tags added to the material entry by the user  |

## Properties

[Characteristic properties](/data/convention/structured.md#by-relation-to-workflow) present for materials after the corresponding calculation(s) are done are described below and in the [corresponding page](/properties/properties.md).

| Property    |   Description      |  
| :-------- |:----------- |
| pressure | External pressure in kbar | 
| total_energy | Total internal energy of the system in eV | 
| band_gaps:direct | The direct band gap in eV   | 
| band_gaps:indirect | The indirect band gap in eV  |
| band_structure | The availability of electronic bandstructure data (boolean) |
| density_of_states | The availability of electronic density of states data (boolean) |

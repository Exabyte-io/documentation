# Advanced Materials Search

The steps for performing [advanced searches](/entities-general/actions/advanced-search.md), in the specific case of Materials, are illustrated in the animation below. 

Here, we use the advanced search query builder to construct a query that filters the large dataset of materials (over 4000 entries). This filtering is done according to the formula ("Al"), unit cell volume (less than "80" in cubic Angstroms) and tags containing a certain keyword ("high pressure").

<img data-gifffer="/images/advanced_search.gif" />

# Searchable Properties 

The following materials properties are available to be searched under the advanced method.

| Property    |   Description      |  
| :-------- |:----------- |
| name | Name of the Material, as listed under the Account-owned collection | 
| formula | The Material's chemical formula, for example "CaTiO3" | 
| latticeType | The [Bravais lattice type](/materials-designer/source-editor/lattice.md) of the crystal structure under consideration |
| model  | The [theoretical model](/models/overview.md) employed to calculate the materials properties  | 
| method | The [computational method](/methods/overview.md) implementing the above model |  
| spaceGroupSymbol | The space group symbol describing the symmetry elements present in the crystal structure, e.g. "Fd-3m" for a cubic-diamond structure | 
| volume  | The volume of the unit cell of the structure, in units of angstrom^3 | 
| density | The density of the crystal structure, in units of g/cm^3 | 
| pressure | The external pressure applied at the moment of the properties calculation, in units of kbar | 
| total_energy | The total internal energy of the system, in units of eV | 
| band_gaps:direct |  The direct band gap for the case of semiconductors, in units of eV   | 
| band_gaps:indirect | The indirect band gap of semiconductors, in units of eV  |
| band_structure | The availability of electronic bandstructure calculation results  |
| density_of_states | The availability of electronic density of states calculation results  |
| owner | The Account name which [owns](/entities-general/ownership.md) the material under consideration  |
| tags | Descriptive [metadata](/entities-general/data.md#Metadata) tags added to the material entry by the user  |

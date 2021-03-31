# Structured Representation of Materials

We present an example of our approach towards defining and storing structured data for materials. The aspects presented herein complement the [general introduction](../entities-general/data.md).

## Example Representation

In the expandable section below, the user can find an example JSON representation of a face-centered cubic Silicon: 

<details markdown="1">
  <summary>
     Expand to view
  </summary> 

```json tab="Schema" 
{!esse/schema/material.json!}
```

```json tab="Example" 
{!esse/example/material.json!}
```

</details>
  


## Explanation of Keywords

| Keyword    |  Short Description      | Details        | 
| :-------- |:----------- |:------------- |
| basis   | Crystal [basis](../properties-directory/structural/basis.md) with explicit identification per atom  | The information about the atomic type and coordinates |
| lattice | Crystal [lattice](../properties-directory/structural/lattice.md) in both Bravais and vector notations  | Crystal lattice parameters - lattice constants and angles. Components of the corresponding lattice vectors are also included. |
| derivedProperties | [descriptive properties](../data-structured/overview.md#by-relation-to-workflow) derived from lattice/basis (only one example shown above) | Additional properties of the crystal structure under investigation as explained in the section ensuing the present table. |
| hash | Hash string calculated by the [Bank Mapping Function](bank.md)  |   Structure-based hash string for the primitive standard representation of this material, calculated when checking this material against existing entries within the Materials Bank |
| scaledHash | As above, but for the lattice axis scaled to 1.0 (i.e. to identify same structures under different uniform pressure) | This hash string is calculated by scaling all the dimensions of the primitive unit cell representation of the material by the $a$ lattice constant |

## Derived Properties

As seen above, we use the crystal **lattice** and **basis** JSON objects as the main [identifying properties](../data-structured/overview.md#by-relation-to-uniqueness). Based upon them, we calculate the **derivedProperties**, that may include such information as:
 
 - the unit cell volume, 
 - density, 
 - chemical formula, 
 - and a large number of other possibilities. 
 
 For every material imported/uploaded to our platform, we pre-calculate a set of such descriptors, and store them inside this "derivedProperties" section. This information can be further used during data analysis or the construction of statistical predictive models.

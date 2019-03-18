# Reaction Energy Profile

<span class="btn badge b-success border-50">Non-Scalar</span> <span class="btn badge b-info border-50">Chemical</span>

Any chemical reaction or process can be characterized by its **Reaction Energy Profile** [^1]. This profile is a theoretical representation of the reaction's energetic pathway, followed by the reactants as they are transformed into products during the course of the reaction. It is typically plotted along the main **reaction coordinate**, a parametric curve that follows the pathway of a reaction, and that indicates its overall progress.
 
The purpose of energy profiles is to provide a qualitative representation of how potential energy varies with molecular motion for a given chemical reaction.

## Example

Reaction Energy Profile calculations can be performed with an appropriate [Workflow](../../workflows/overview.md), based on the **Nudged Elastic Bands** method [^2] such as [implemented](../../tutorials/dft/chemical/neb.md) by the [Quantum ESPRESSO modeling application](../../software-directory/modeling/quantum-espresso/overview.md). 

The final results are portrayed in the [Results Tab](../../jobs/ui/results-tab.md) of [Job Viewer](../../jobs/ui/viewer.md) in the form of a **profile curve**, as illustrated in the graphic below. The visual contains the reaction energy profile for a chemical reaction with [activation energy barrier](../scalar/activation-barrier.md) of approximately 0.2 eV.

![Reaction Profile](../../images/properties-directory/reaction-profile.png "Reaction Profile")

### Export as Image

The possibility to export the graph is offered as mentioned [here](../../properties/ui/viewer.md#export-as-images).

## Schema

The JSON schema and an example representation for this property can be found [here](../../properties/data/list.md#reaction-energy-profile).

## Links

[^1]: [Wikipedia Energy profile (chemistry), Website](https://en.wikipedia.org/wiki/Energy_profile_(chemistry))

[^2]: [H. Jonsson, G. Mills and K.W. Jacobsen: "Nudged elastic band method for finding minimum energy paths of transitions", Document](http://theory.cm.utexas.edu/henkelman/pubs/jonsson98_385.pdf)

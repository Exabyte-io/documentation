# Activation Energy Barrier

<span class="btn badge b-success border-50">Scalar</span> <span class="btn badge b-info border-50">Chemical</span>

The Activation Energy Barrier marks the highest energy state encountered during the course of the progress of a chemical reaction [^1], as visualized through its [Reaction Energy Profile](../non-scalar/reaction-energy-profile.md). It is a **[Scalar and Auxiliary](../../properties/classification/general.md) property** of the chemical reaction under consideration.

## Example

Its value can be estimated with any [Nudged Elastic Band](../../tutorials/dft/chemical/neb.md) [Workflow](../../workflows/overview.md), and it is returned under the [Results Tab](../../jobs/ui/results-tab.md) interface with the following appearance (in eV).

<div class="clearfix">
    <center>
        <div class="chart"><i class="zmdi zmdi-battery-flash zmdi-hc-3x"></i></div>
        <div class="count">
        	<small>Reaction energy barrier (eV)</small>
            <h2>0.201</h2>
        </div>
     </center>
</div>

## Transition States

The highest potential energy state across a reaction energy profile is often referred to as the **transition state** [^2] for the chemical reaction under investigation.  

## Schema 

The JSON schema and an example representation for this property can be found [here](../../properties/data/list.md#activation-energy-barrier).

## Links

[^1]: [Wikipedia Activation energy, Website](https://en.wikipedia.org/wiki/Activation_energy)

[^2]: [Wikipedia Transition state, Website](https://en.wikipedia.org/wiki/Transition_state)

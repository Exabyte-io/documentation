# Resource Categories

Different **speed categories** are available at different prices, depending on the urgency of the [simulation job](../../jobs/overview.md) that needs to be submitted. 

Below we outline the available category options, in order of ascending **Charge factor** associated with each of them. The relevant pricing information can be found under the [service levels page](../../pricing/service-levels.md). 

## Ordinary

The "Ordinary" category is meant as the common "workhorse" option, and is useful for most intent and purposes.

## Debug

The "Debug" option is fast to execute, but contains limited resources. It is as such only good for preliminary testing and debugging of simulations.

## Saving

This option is available at a significantly lower charge factor, through utilizing idle compute resources. Its main downside is that job execution may be terminated at any time depending on the load in the data center, which can make the compute resources unavailable since assigned to other jobs with higher priority.

## Fast

This category provides fast access to computational resources. This is particularly resourceful for urgent jobs, but at the same time more expensive to use. The option to use Graphical Processing Units (GPUs) is also offered here for better performance.

## Premium

Our infrastructure includes [multiple compute clusters](../clusters/overview.md) at a time, with some providing premium performance. Premium hardware has an extra charge factor incurred as part of its usage, due to its superior performance.

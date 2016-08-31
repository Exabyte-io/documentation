<!-- TODO: to be revised by MM, add hardware specification, information about cloud providers, add note about support for on-premises deployment -->

# Compute platform

## Compute levels

We have multiple levels of compute:

- Debug
- Regular
- Saving

`Regular` level is meant for most production tasks. It provides extensive compute resources at the base rate defined by [subscription level](/billing/accounts-and-billing#pricing).

`Debug` level provides a relatively small amount of compute resources immediately with no wait time at an increased cos.

`Saving` compute level is charged at a significantly lower price than Regular, because it is using compute resources that are currently idle. Users need to be aware, however, that cost-saving compute resources may be terminated depenging on the load in the datacenter. More information on this subject is [here](../cli/jobs.md#job-termination)

## Resources

As of Mar, 2016 major compute and storage systems have:

* 100,000 compute cores,
* 100 terabytes of memory,
* 8 exabytes of disk storage,
* low latency interconnect

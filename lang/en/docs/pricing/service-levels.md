# Pricing

> Updated pricing scheme as of July 2019. For the information about the legacy pricing scheme please contact our support team.

The pricing is dependent on the [Service Level](../accounts/service-levels.md). We aim to have a flexible scheme where customers always pay on-demand for the value they extract.

## Cost structure

The cost of using our platform is comprised of the following components, added together.

### Subscription Fee 

The cost of accessing the platform. Charged on a monthly or yearly basis. [Free](../accounts/service-levels.md#free-service-level) tier is available.

### Computing Cost

The cost of running computations. Accounts can refill their Balance on demand at any time.

### Cost of Other Resources

The cost of other resources, such as disk storage or account members.

## Comparison Table

Below is a quick comparison of our pricing for different [Service Levels](../accounts/service-levels.md).
Readers are referred to [Service Levels](../accounts/service-levels.md) page for detailed information about available features.

| Fees                                      | Free         | Pro            | Team           | Enterprise     |
| :-------------                            | :----------- | :------------- | :------------- | :------------- |
| Monthly Subscription Fee                  | -            | $10            | $30            | -              |
| Yearly Subscription Fee                   | -            | $100           | $300           | $1,000         |
| Minimum Compute Allocation[^1]            | -            | -              | $700           | $1,000         |
| Total Minimum Commitment                  | -            | -              | $1000          | Contact Us     |
| Additional Account Members - Member/Month | -            | -              | $20            | $20            |
| Additional Account Members - Member/Year  | -            | -              | $200           | $200           |
| Additional Disk Space - GB/Month          | -            | $0.2           | $0.2           | $0.2           |
| Additional Dropbox Space - GB/Month       | -            | $0.2           | $0.2           | $0.2           |
| Ordinary Compute Price - Core-Hour        | -            | $0.12          | $0.12          | $0.12          |

[^1] Only for organizational accounts that opt for [wire-based electronic payments](../accounts/payments-charges.md#wire-based-payments).

!!! note "Contact us for detailed pricing"
    For detailed pricing or a quotation please contact us at <a href="mailto:sales@exabyte.io" target="_blank">sales@exabyte.io</a>.

## Category-based pricing

The compute price above refers to the **Ordinary** [cost category](../infrastructure/resource/category.md#cost-categories) for each service level. One can further control the price by varying the category type. When using submission queues with "Saving" cost category, for example, the relative unit price can be as low as 1/5th of the Ordinary.

|Cost Category| Charge factor
|:---------   |:------------
|Debug        | 2.0
|Ordinary     | 1.0
|Saving       | 0.2

## Queue- and Cluster-dependent pricing

As the type of hardware and scheduling policies vary for different submission queues, the pricing is also different. For, example, GPU-enabled nodes are available within a certain subset of queues and are generally priced higher.

Detailed description of submission queues is available [here](../infrastructure/resource/queues.md). Clusters and associated hardware and pricing are explained in [this section](../infrastructure/clusters/overview.md)

!!! tip "Least expensive pricing options"
    The options explained above can be combined in order to achieve the least expensive pricing. For example, when "Enterprise" service level is used in combination with submission queues that belong to the "Saving" cost category, the resulting price per core hour can be as low as $0.024. When we take into account the performance per core [benchmarks](../benchmarks/2018-11-12-comparison.md#performance-per-core) this presents a unique performance per price option.

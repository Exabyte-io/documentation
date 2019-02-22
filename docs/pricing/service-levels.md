# Pricing

The pricing on our platform is dependent on the [Service Level](../accounts/service-levels.md). We aim to have a flexible scheme where customers always pay on-demand for the value they extract. We give preferential pricing to scenarios with larger upfront commitment, as  helps us optimize and lower our maintenance costs.

!!! note "Contact us for detailed pricing"
    For detailed pricing or a quotation please contact us at <a href="mailto:support@exabyte.io" target="_blank">support@exabyte.io</a>

## Comparison Table

Below is a quick comparison of our pricing for different [Service Level](../accounts/service-levels.md).

<!-- | price per core-hour       |  $0.20      | $0.20              | $0.18              | $0.17              | $0.10                     | -->

| Feature per Plan         |  Promo      | Advanced           | Pro                | Enterprise         |  Enterprise-Extra         |
| :-------------           |:----------- |:-------------      |:-------------      |:-------------      |:-------------             |
| pre-payment              |  -          | $50                | $500               | $5,000             | $50,000                   |
| relative unit price [^1] |  2.0        | 2.0                | 1.8                | 1.7                | 1.0                       |
| validity period          |  -          | 1 month            | 3 months           | 6 months           | 12 months                 |
| monthly data usage       |  10Gb       | 50Gb               | 100Gb              | 500Gb              | 5Tb                       |
| private data             |  -          | -                  | +                  | +                  | +                         |
| organizations/teams      |  -          | -                  | -                  | +                  | +                         |
| maximum team size        |  -          | -                  | -                  | 5                  | 15                        |
| support                  |  email      | email              | email              | email / phone      | email / phone / videoconference |
| command line access      |  -          | -                  | +                  | +                  | +                         |

[^1]: *relative unit price* refers to the relative price per compute unit (core-hour) for the Ordinary [compute category](../infrastructure/resource/category.md). Absolute price depends on multiple additional factors, and is specified in the individual agreements. [Contact our support team](../ui/support.md) for more information.

///FOOTNOTES GO HERE///

## Category-based pricing

The price above refers to the **Ordinary** [cost category](../infrastructure/resource/category.md#cost-categories) for each service level. One can further control the price by varying the category type. When using submission queues with "Saving" cost category, for example, the relative unit price can be as low as 1/5th of the Ordinary.

|Cost Category| Charge factor
|:---------   |:------------
|Debug        | 2.0
|Ordinary     | 1.0
|Saving       | 0.2

## Queue- and Cluster-dependent pricing

As the type of hardware and scheduling policies vary for different submission queues, the pricing is also different. For, example, GPU-enabled nodes are available within a certain subset of queues and are generally priced higher.

Detailed description of submission queues is available [here](../infrastructure/resource/queues.md). Clusters and associated hardware and pricing are explained in [this section](../infrastructure/clusters/overview.md)

!!! tip "Least expensive pricing options"
    The options explained above can be combined in order to achieve the least expensive pricing. For example, when "Enterprise-Extra" service level is used in combination with submission queues that belong to the "Saving" cost category, the resulting price per core hour can be as low as $0.02. When we take into account the performance per core [benchmarks](../benchmarks/2018-11-12-comparison.md#performance-per-core) this presents a unique performance per price option.
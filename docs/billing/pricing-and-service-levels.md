# Overview

Service levels define the price per the amount of compute you consume while using our product. We measure the amount in compute-units, or [core-hours](https://en.wikipedia.org/wiki/CPU_time). You always pay on-demand, however depending on Service Level price per compute unit may vary.

# Comparison Table

Below is a quick comparison of our service levels:

| Feature per Plan         |  Promo      | Advanced           | Pro                | Enterprise         |  Enterprise-Extra         |
| :-------------           |:----------- |:-------------      |:-------------      |:-------------      |:-------------             |
| pre-payment               |  -          | $50                | $500               | $5,000             | $50,000                   |
| price per core-hour       |  $0.20      | $0.20              | $0.18              | $0.17              | $0.10                     |
| validity period          |  -          | 1 month            | 3 months           | 6 months           | 12 months                 |
| reserved compute nodes   |  -          | -                  | -                  | +                  | +                         |
| monthly data usage       |  10Gb       | 50Gb               | 100Gb              | 500Gb              | 5Tb                       |
| private data             |  -          | -                  | +                  | +                  | +                         |
| organizations/teams      |  -          | -                  | -                  | +                  | +                         |
| maximum team size        |  -          | -                  | -                  | 5                  | 15                        |
| support level            |  email      | email              | email/web          | email/web          | email/web/videoconference |
| command-line access      |  -          | -                  | +                  | +                  | +                         |

> "Base rate": the price above refers to the Base Rate for each service level. You can further control how quickly your calculations are finished by varying submission queues.

# How Service Levels are set

Your service level is defined by the payment that you make.

> Service level is defined by the maximum amount of the most recent payment(s).

Here's how it works:

1. Upon signing up the service level is initially set to `Promo`.
2. When user provides a payment method, purchases allocation and pays the minimum amount ($50) the service level is set to `Advanced`
3. When/if user pays in excess of $500 instead, service level is set to `Pro`
4. Users with a valid payment method can create [**organizations**](/organizations/overview.md):

    - the first organization per user is given $10 credit to try the functionality
    - by paying $5,000 a user can secure 'Enterprise' service level for his/her organization
    - entities created under the organization account will be charged according to `Enterprise` rates
    - by paying $50,000 a user can secure `Enterprise-extra` service level for his/her organization
    - other special rates are available upon request

# Validity period

Our users only pay for what they use, however we require that they use the allocation within a designated validity period.

!!! tip "Unused credits"
    Unused credits roll-over into the next validity period.

# Queue-based pricing

Detailed description of submission queues and compute levels is available [elsewhere](../compute/levels-queues.md). Brief summary of charge factors for each queue types wrt the base price are shown below

|Queue type| Charge factor
|:---------|:------------
|Debug     | 2.0
|On-demand | 1.0
|Saving    | 0.2
|Premium   | 2.0

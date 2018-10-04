# Overview

Service levels define the price per the amount of compute you consume while using our product. We measure the amount in compute-units, or [core-hours](https://en.wikipedia.org/wiki/CPU_time). You always pay on-demand, however depending on Service Level price per compute unit may vary.

# Comparison Table

Below is a quick comparison of our service levels:

| Feature per Plan         |  Promo      | Advanced           | Pro                | Enterprise         |  Enterprise-Extra         |
| :-------------           |:----------- |:-------------      |:-------------      |:-------------      |:-------------             |
| pre-payment               |  -          | $50                | $500               | $5,000             | $50,000                   |
| price per core-hour       |  $0.20      | $0.20              | $0.18              | $0.17              | $0.10                     |
| validity period          |  -          | 1 month            | 3 months           | 6 months           | 12 months                 |
| monthly data usage       |  10Gb       | 50Gb               | 100Gb              | 500Gb              | 5Tb                       |
| private data             |  -          | -                  | +                  | +                  | +                         |
| organizations/teams      |  -          | -                  | -                  | +                  | +                         |
| maximum team size        |  -          | -                  | -                  | 5                  | 15                        |
| support level            |  email      | email              | email/web          | email/web          | email/web/videoconference |
| command-line access      |  -          | -                  | +                  | +                  | +                         |

> NOTE: the price above refers to the Ordinary Rate for each service level. One can further control the price by varying submission queues (see below). When using "Saving" queue, for example, the final price can be as low as $0.02.

# How Service Levels are set

The service level is defined by the pre-payment that an account holder makes. When multiple payments are applied, we prioritize the maximum amount within its validity period.

Here's how it works:

- Upon signup the service level is initially set to `Promo`.
- When user provides a payment method, purchases allocation and pays the minimum amount ($50) the service level is set to `Advanced`
- When/if user pays in excess of $500 instead, service level is set to `Pro`

> NOTE: validity periods for the same service level add up, so in case a user pays $500 and then adds $500 within 3 months, the total allocation of $1000 can be used within 6 months

# Service levels for Enterprise

Enterprise service level plans are designed for groups of users that represent an enterprise team and collaborate with each other on a regular basis. However, any user with a valid payment method can create [**organizations**](/organizations/overview.md).

Notes:

- the first organization per user is given $10 promo credit
- by paying $5,000 a user can secure 'Enterprise' service level for his/her organization
- entities created under the organization account will be charged according to `Enterprise` rates
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
|Ordinary  | 1.0
|Saving    | 0.2

# Premium hardware

Our infrastructure includes multiple compute clusters at a time, with some providing premium performance. The state of the system is summarized for logged-in users [here](https://platform.exabyte.io/clusters). Premium hardware has an extra charge factor as shown below:

|Compute type | Charge factor
|:---------|:------------
|Premium   | 2.0

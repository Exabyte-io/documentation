<!-- DB -->

## Service Levels

Service levels define the price per the amount of compute you consume while using our product. We measure the amount in compute-units, or [CPU-hours](https://en.wikipedia.org/wiki/CPU_time). You always pay on-demand, however dependent on your service level your price per compute unit may vary and you may have additional services and features included.

## Service levels comparison

Below is a quick comparison of our service levels:

| Feature/Plan             |  Promo      | Advanced           | Pro                | Enterprise         |  Enterprise-extra         |
| -------------            |:----------- |:-------------      |:-------------      |:-------------      |:-------------             |
| minimum payment          |  -          | $50                | $500               | $5,000             | $50,000                   |
| price per CPU-hour       |  $0.20      | $0.20              | $0.18              | $0.15              | $0.10                     |
| validity period          |  -          | 1 month            | 3 months           | 6 months           | 12 months                 |
| reserved compute nodes   |  -          | -                  | -                  | +                  | +                         |
| monthly data usage       |  10Gb       | 50Gb               | 100Gb              | 500Gb              | 5Tb                       |
| private data             |  -          | -                  | +                  | +                  | +                         |
| organizations/teams      |  -          | -                  | -                  | +                  | +                         |
| maximum team size        |  -          | -                  | -                  | 5                  | 15                        |
| support level            |  web/email  | web/email          | web/email/phone    | web/email/phone    | web/mail/email/personal   |
| command line access      |  -          | -                  | +                  | +                  | +                         |

!!! note "Base rate"
    The price above refers to the base rate for each service level. You can further control how quickly your calculations are finished by varying submission queues.

## How service levels are set

Your service level is defined by the payment that you make. **Organizations** let users set up a collaboration, sharing and work in teams, and are well suited for enterprise users and those working in groups.

> Service level is defined by the maximum amount of the recent payment(s) that you make.

Here's how it works:

1. Upon signup your service level is set to `Promo`.

2. When you provide a payment method, purchase allocation and pay the minimum amount ($50) - your service level is set to `Advanced`

3. If you decide to pay in excess of $500 instead, your service level is set to `Pro`

4. Users with valid payment method can create **organizations**:

    - the first organization per user is given $10 credit to try the functionality

    - by paying $5,000 a user can secure 'Enterprise' service level (and rates) for his/her organization

    - all entities created under the organization account will be charged according to `Enterprise` service level rates

    - by paying $50,000 a user can secure `Enterprise-extra` service level for his/her organization

    - other special rates are available upon request

## Validity period

You get to access our services free of charge, and only pay for what you use, however we require that you use the allocations within the validity period (as shown in the table above).

Every 1st day of the week we run a check on each user and organization account and the account balance is set to 0 in if any of the following is true:

- account value X is `< $50` and last payment happened >1 month ago
- account value X is `$50 <= X < $500` and last payment happened >3 month ago
- account value X is `$500 <= X < $5000` and last payment happened >6 month ago
- account value X is `> $5000` and last payment happened >12 month ago

We recommend setting automatic payment option (auto-renew) when upgrading or adding credit, so that your service level is automatically renewed after validity period is over.

!!! tip "Unused credits"
    All unused credits automatically roll over into the next validity period.

## Queue-based pricing

Detailed description of submission queues is available [elsewhere](../compute/queues.md). In brief, there are three types: debug (for short calculations with very quick turnaround), on-demand (for most production runs) and saving (for lower priority tasks). Charge factors for each queue types wrt the base price are shown below

|Queue type| Charge factor
|:---------|:------------
|Debug     | 2.0
|On-demand | 1.0
|Saving    | 0.2

## Increasing Quota

You can purchase extra storage to increase the limits beyond the default value for your service level at $0.2 per GB per month. Thus, 100GB of extra storage would cost $20 per calendar month. More information available [here](increase-quota.md).

## Changing Service Level

You can secure better compute costs and other benefits by optimising the service level to suit your needs, Click [here](upgrade-service-level.md) to learn how to upgrade your service level.


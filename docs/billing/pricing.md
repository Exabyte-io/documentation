# Pricing

## We charge for ...

the amount of compute you consume while using our product. We measure the amount in compute-units, or [CPU-hours](https://en.wikipedia.org/wiki/CPU_time).

You always pay on-demand, however dependent on your subscription level your price per compute unit may vary and you may have additional services and features included.


## Subscription levels

Below is a quick overview of our subscription levels:

```py
+------------------------------------------------------------------------------------------------------------------------+
| Feature/Plan            |  Newbie      Advanced            Pro                 Enterprise          Enterprise-extra    |
|------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                        |
| minimum payment            -           $50                 $500                $5,000              $50,000             |
| price per CPU-hour         $0.20       $0.20               $0.15               $0.12               $0.10               |
| validity period            -           1 month             3 months            6 months            12 months           |
| reserved compute nodes     -           -                   -                   +                   +                   |
| monthly data usage         10Gb        50Gb                100Gb               500Gb               5Tb                 |
| private data               -           -                   +                   +                   +                   |
| organizations/teams        -           -                   -                   +                   +                   |
| maximum team size          -           -                   -                   5                   50                  |
| support level              web/email   web/email           web/email/phone     web/email/phone     <- + in person      |
| command line access        -           -                   +                   +                   +                   |
|                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------+
```

## How subscription levels are set

Your subscription level is defined by the payment that you make. **Organizations** let users set up a collaboration, sharing and work in teams, and are well suited for enterprise users and those working in groups.

Here's how it works:

- Upon signup you are given $10 credit to try the platform and your subscription level is set to `Newbie`.
- When you provide a payment method, purchase allocation and pay $50 - your subscription level is set to `Advanced`
- If you decide to pay $500 instead, your subscription level is set to `Pro`
- Users with valid payment method can create **organizations**:
    - the first organization per user is given $10 credit to try the functionality
    - by paying $5,000 a user can secure 'Enterprise' subscription level (and rates) for his/her organization
    - all entities created under the organization account will be charged according to `Enterprise` subscription level rates
    - by paying $50,000 a user can secure `Enterprise-extra` subscription level for his/her organization
    - other special rates are available upon request


## Validity period

You get to access our services for free. We only charge for what you use, however we require that you use the allocations within a certain validity period (as shown in the table above).

Every 1st day of the week we run a check on each user and organization account and the account balance is set to 0 in if any of the following is true:

- account value X is `<$50` and last payment happened >1 month ago
- account value X is `$50<=X<$500` and last payment happened >3 month ago
- account value X is `$500<=X <$5000` and last payment happened >6 month ago
- account value X is `>$5000` and last payment happened >12 month ago

We recommend setting up an automatic payment option, so that your subscription level is automatically renewed after validity period is over.

## Base rate

The price above refers to the base rate for each subscription level. You can further control how quickly your calculations are finished by using submission queues.

## Queue-based pricing

Detailed description on submission queues is available [elsewhere](../compute/queues.md). In brief, there are three types: debug (for short calculations with very quick turnaround), on-demand (for most production runs) and saving (for lower priority tasks).

Debug queue is charged at `2x` the [base rate](../billing/pricing.md), on-demand queues are charged at `1x` the base rate and saving queues are charged at `0.2x` the base.

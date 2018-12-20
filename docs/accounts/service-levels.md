# Service Levels

Service levels define the types, qualities and quantities of services provided to the accounts within our platform. The features associated with using our platform which are affected by the opted Service Level consist of the following list.

## Features

| Feature  | Description  	|
| :------------- | :------------- |
| Ordinary Rate<sup class="c-red">1</sup> | The cost of computational consumption while using our product. We quantity the amount of computational consumption in compute-units, otherwise known as [core-hours](https://en.wikipedia.org/wiki/CPU_time). |
| Minimum Payment |  Minimum one-time initial payment necessary for account to be activated. This payment will still contribute to the account's balance for performing computational tasks |
| Validity Period |  The duration of time over which the account will remain active and accessible by the users |
| Reserved Compute Nodes |	The number of supercomputing clusters which are made available to the users of the account | 
| Month Data Usage | The total quota of storage space which is allocated to the account on a monthly basis |
| Private Data  | The possibility to hold private entities inside an account. Otherwise all entities are public for all other platform users to see |
| Organizations/Teams  | The possibility to create organization accounts, and multiple teams inside each of these organizations |
| Maximum Team Size  | The maximum number of users that can be hosted inside teams in general |
| Support Level	| The different forms and depths of support that users will receive by our support staff in case of technical difficulties being encountered |
| Command Line Access  |  The possibility to access the platform interface via command line |

<sup class="c-red">1</sup> Ordinary = general case without the usage of any saving, premium or specialized type hardware. 

## Types

For the [personal accounts](overview.md#personal-accounts) we offer "Promo", "Advanced", and "Pro" service levels. For the [organizational accounts](overview.md#personal-accounts) we offer "Promo", "Enterprise" and "Enterprise-Extra" levels. The "Promo" service level is designed as a temporary promotional way for the users to understand the operations of our platform. For the detailed comparison of the pricing and features associated with the different Service Levels offered as part of our platform, the user is referred to the [pricing documentation page](../pricing/service-levels.md). 

## View/Change Service Level

All the relevant information concerning Service Levels, under the context of the currently selected Account, can be inspected through the corresponding [component of the User Interface](ui/service-level.md). It is important to bear in mind that, when dealing with collaborative accounts, only the Owner or an Administrator of the account is given the rights to undergo such operations on behalf of the whole Organization. 

## How Service Levels are set

The service level is defined by the pre-payment that an account holder makes. When multiple payments are applied, we prioritize the maximum amount within its validity period.

Here's how it works:

- Upon signup the service level is initially set to `Promo`.
- When user provides a payment method, purchases allocation and pays the minimum amount the service level is set to `Advanced`
- When/if user next pays in excess of the minimum amount for `Pro` instead, service level is set to `Pro`

> NOTE: validity periods for the same service level add up. In case a user pays the minimum amount and then adds another equivalent payment within the validity period, the total allocation can then be used within the combined period equal to twice the validity period time

## Service levels for Enterprise

Enterprise service level plans are designed for groups of users that represent an enterprise team and collaborate with each other on a regular basis. However, any user with a valid payment method can create [**organizations**](../collaboration/organizations/overview.md). 

Notes:

- the first organization per user is given $10 promo credit
- by paying $5,000 a user can secure 'Enterprise' service level for his/her organization
- entities created under the organization account will be charged according to `Enterprise` rates
- other special rates are available upon request

## Validity period

Our users only pay for what they use, however we provide access to the product within a designated period of time - validity period. Any **Unused credits** at the end of the current validity period will be available (roll-over) into the next validity period, following another payment.

## Links

[^1]: [CPU time, Wikipedia](https://en.wikipedia.org/wiki/CPU_time)

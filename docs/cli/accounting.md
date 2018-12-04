# Accounting

As explained in detail in the corresponding [part of the documentation](../accounts/overview.md), we implement as system of **Accounts** for managing the user consumption of our computational resources. 

These accounts each have a [storage quota](../accounts/quota.md) and a [balance](../accounts/balance.md) for making the necessary [payments](../accounts/payments-charges.md) to our system. These account-related features depend on the choice of the [Service Level](../pricing/service-levels.md).

Information pertaining to accounts can also be retrieved under the [Command Line Interface](overview.md) (CLI) of our platform, as introduced in what follows.

## Accounting CLI Actions

We introduce the relevant actions and commands for inspecting the account balance and quota via CLI [in this dedicated page](actions/balance-quota.md).

## Implementation

The full documentation manual for the software used to implement the allocation manager under the CLI can be found under Ref. [^1] below. 

## Links

[^1]: [Gold Allocation Manager User’s Guide, Document](http://docs.adaptivecomputing.com/gold/pdf/GoldUserGuide.pdf)

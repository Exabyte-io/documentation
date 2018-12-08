# Accounting

As explained in detail in the corresponding [part of the documentation](../accounts/overview.md), we implement as system of **Accounts** for managing the user consumption of our computational resources. 

These accounts can be of either [personal](../collaboration/organizations/roles.md#organizations-vs.-personal-accounts) or [Organizational](../collaboration/organizations/overview.md) (collaborative) nature, and to each one of them is associated a [storage quota](../accounts/quota.md) and an [account balance](../accounts/balance.md) for making the necessary consumption-based [payments](../accounts/payments-charges.md) to our system. These account-related features depend on the choice of an appropriate [Service Level](../pricing/service-levels.md) for the account under consideration.

Information pertaining to accounts can also be retrieved under the [Command Line Interface](overview.md) (CLI) of our platform, as introduced in what follows.

## Accounting CLI Actions

We introduce the relevant actions and commands for inspecting the account balance and quota via CLI [in this dedicated page](actions/balance-quota.md).

## Gold Account Manager

The full documentation manual for the accounting system software that we implement under the CLI, called **"Gold"**, can be found under Ref. [^1]. 

### Command-line parameters

The account manager system is comprehensive and accepts multiple parameters. The full list of flags for each of the commands can be obtained by passing `--help` and is reproduced below for reference purposes using `statement`.

```bash
# > statement --help

Usage:
    gstatement [[-a] *account_id*] [-p *project_name*] [-u *user_name*] [-m
    *machine_name*] [-s *start_time*] [-e *end_time*] [--summarize] [-h,
    --hours] [--debug] [-?, --help] [--man] [-V, --version]
```

## Links

[^1]: [Gold User’s Guide, Document](http://docs.adaptivecomputing.com/gold/pdf/GoldUserGuide.pdf)

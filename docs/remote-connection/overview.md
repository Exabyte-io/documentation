# Remote Connection Methods

We offer alternative **connection methods** other than the [Web Interface](../ui/overview.md) to submit [simulation jobs](../jobs/overview.md) to the [computing clusters](../infrastructure/clusters/overview.md) of our platform, and access the associated data via the [login node](../infrastructure/login/overview.md).

The login node can be accessed via any of the following options.

## SSH Terminal 

The user can use an **external SSH client** [^1] under any Operating System to connect to our [Command Line Interface](../cli/overview.md). We explain how to do so in [this page](ssh.md).

## Web Terminal

Alternatively, we offer an incorporated Terminal within our Web Interface which also takes the user to the same [Command Line Interface](../cli/overview.md). We refer to this as the [Web Terminal](web-terminal.md).

## Remote Desktop

If the user wants to experience a fully graphical desktop environment, he can do so via the [Remote Desktop Application](remote-desktop.md).

!!!info "Guacamole Server implementation"
    Both the Web Terminal and Remote Desktop mentioned above are implemented via the **Apache Guacamole Server** [^2]. Instructions on how to open the Guacamole Sidebar within our interface can be found [here](actions/guacamole.md).

## Actions common to Web Terminal and Remote Desktop

We introduce the actions common to both the Web Terminal and Remote Desktop interfaces in [this section](actions/overview.md) of the documentation.

## Actions specific to Remote Desktop

Some actions are only available for Remote Desktop, and they are documented [here](actions-rd/overview.md).

## Links

[^1]: [Wikipedia Secure Shell, Website](https://en.wikipedia.org/wiki/Secure_Shell)

[^2]: [Apache Guacamole, Website](https://guacamole.apache.org/)

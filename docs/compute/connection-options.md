There are 3 ways you can connect to our compute platform, CLI via ssh terminal, CLI via web portal and remote desktop via web portal.

## CLI via ssh terminal
In order to use CLI via ssh terminal you need to generate ssh keys and upload your public key to our compute platform. For more information please visit [login via command line](../cli/login/#login-via-command-line). When you have ssh keys in place you can use a ssh terminal or Putty for windows to connect to the compute platform.

```
% ssh steve@bohr.exabyte.io

------------------------------------------------------------------
                          _           _
        ___ __   __ __ _ | |__ __  __| |_ ___     _   ___ 18
       / _ \\ \ / // _` ||  _ \\ \/ _  __/ _ \   | | / _ \
      |  __/ ) X (( (_| || |_) ))  / | ||  __/ _ | |( (_) )
       \___//_/ \_\\__,_||____//__/  |_| \___/(_)|_| \___/


------------------------------------------------------------------

  Exabyte.io secure shell login node
  Homepage: http://exabyte.io/
  Documentation: http://docs.exabyte.io/cli
  Support: support@exabyte.io

  This node contains:

    - resource management system
    - accounting system
    - sofware modules

  To view system status:

    - `exaclusters` : list clusters and their state
    - `exanodes` : list compute nodes and their state

  Job submission cheat sheet:

    - `qstat` : show status of batch jobs
    - `qsub` : submit batch jobs (e.g. `qsub ./job.sh`)
    - `qdel` : delete batch jobs (e.g. `qdel 7`)

  Accounting cheat sheet:

    - `balance` : show my detailed balance
    - `statement` : show detailed usage statistics

------------------------------------------------------------------
 *  By using the system you indicate your awareness and consent  *
 *  to the terms and conditions you were presented at the time   *
 *  of obtaining access credentials. ® 2016 Exabyte Inc.         *
------------------------------------------------------------------

[steve@bohr.exabyte.io:~]$
``` 

## CLI via web portal

 Web terminal is an alternative for users who want to use a web-based SSH terminal or are behind a firewall that blocks SSH connections. We use [Apache Guacamole](https://guacamole.incubator.apache.org/), a clientless remote desktop gateway that supports standard protocols like VNC, RDP, and SSH. Guacamole SSH terminal is accessible from the [right sidebar](../getting-started/ui-overview/#account-navigation-right-sidebar) of the web application.

![Guacamole SSH Terminal Sidebar](../images/GuacamoleSSHTerminalSidebar.png "Guacamole SSH Terminal Sidebar")

Guacamole SSH terminal covers the whole page. You need to click on the close bottom at the top right corner to go back to the main content area.

![Guacamole SSH Terminal](../images/GuacamoleSSHTerminal.png "Guacamole SSH Terminal")

### Guacamole menu
The Guacamole menu is a sidebar which is hidden until explicitly shown. On a desktop or other device which has a hardware keyboard, you can show this menu by pressing Ctrl+Alt+Shift. If you are using a mobile or touchscreen device that lacks a keyboard, you can also show the menu by swiping right from the left edge of the screen. To hide the menu, you press Ctrl+Alt+Shift again or swipe left across the screen. 

The Guacamole menu provides options for:

* Navigating back to the home screen
* Reading from (and writing to) the clipboard of the remote desktop
* Uploading and downloading files
* Selecting alternative methods of typing or controlling the mouse, particularly for use on mobile or touchscreen devices
* Zooming in and out of the remote display
* Disconnecting from the current connection entirely

For more information please visit [Guacamole Manual](https://guacamole.incubator.apache.org/doc/gug/using-guacamole.html).

![Guacamole SSH Terminal Menu](../images/GuacamoleSSHTerminalMenu.png "Guacamole SSH Terminal Menu")

## Remote desktop via web portal:
Remote desktop on the [right sidebar](../getting-started/ui-overview/#account-navigation-right-sidebar) provides you with a way to connect to our platform visually from the web application. This type of connection is recommended to users who are not familiar with SSH terminal or want to run GUI-based applications.

![Guacamole Remote Desktop](../images/GuacamoleRemoteDesktop.png "Guacamole Remote Desktop")

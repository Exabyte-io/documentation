<!-- TODO by MH - ask TB if not clear -->

This tutorial describes the steps to connect to a remote desktop session through your web browser. In some cases advanced visualization requires access to a wide array of tools.  Therefore we provide cloud-based remote desktop software for visualization functionality.

# Pre-installed visualization software

We have pre-installed the following list of application for graphical visualization on the remote desktop.

1. [XCrysden](#links)
2. [VESTA](#links)

# Accessing remote desktop

One must open a Remote Desktop Connection to the terminal so that you can run graphical interface programs for visualization.  Underneath the "Terminal" option in the right sidebar is a "Remote Desktop" option.

![Remote Desktop](../../images/ChooseRemoteDesktop.png "Remote Desktop")

Select this and an overlay will appear in your web browser with a graphical user interface connected to remote Linux desktop.

![Start Remote Desktop](../../images/StartRemoteDesktop.png "Start Remote Desktop")

# Finding visualization software

Find and open XCrysden or Vesta under the "Applications" > Other" dropdown menu item.

![Other->XCrysden](../../images/RemoteDesktopApps.png "Other->XCrysden")

You may read more about the visualization options for each of the above applications at the links below.

> If you used the default project for this calculation, then you can find files associated with the job inside: `/home/<your username>/data/<your username>/<job name>/`; otherwise the path would contain the project name in place of the second username: `/home/<your username>/data/<project name>/<job name>/`

!!! warning "Avoid compute intensive visualization tasks"
    We ask users to avoid running excessively compute intensive visualization tasks, as it may interfere with other users' operations during the execution.

# Links

1. [XCrysden, Website](http://www.xcrysden.org/)
1. [VESTA, Website](http://jp-minerals.org/vesta/en/)

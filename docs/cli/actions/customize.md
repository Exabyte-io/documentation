# Customize Shell Environment

The action of customizing the [shell environment](../environment.md#shell-type) from the default "bash" setting can in general be performed by running the `change_shell` command, together with the path to the shell executable present under the `/bin` system folder. 

## Example: Change to ZSH

Here, we offer a specific example of the command necessary to change the shell from the default "bash" to the "zsh" option.

```
change_shell /bin/zsh
```

## Dot Files

There exist several hidden system configuration files, or "dot-files", within the [Login Home](../../infrastructure/login/directories.md), such as the `.bashrc` and `.bash_profile` files. Caution is advised when modifying such files, since they can significantly affect the functionality of the shell environment. In case of uncertainty, we recommend the reader to consult relevant documentation manuals on the general Linux environment before implementing any change to these files.

!!!warning "**NEVER** remove content of the ".ssh" folder"
    We urge the user not to remove the default content of the ".ssh" hidden folder present under the home directory, since doing this might break the operations of the [SSH keys](../../remote-connection/ssh.md) necessary for [remote login](../../remote-connection/overview.md) to our platform. 




<!-- TODO
There exist several "standard" dot-files within the [Login Home](../../infrastructure/login/directories.md), including one for each shell type that we support, that represent symbolic links to read-only files controlled by the platform administrator. Thus, the user should **NEVER** attempt to modify these files. Examples include the .bash_profile, .bashrc, .cshrc, .kshrc, .login, .profile, or .zshrc files. 

Instead, the user should put his/her customizations to the shell environment into the corresponding files that have an ".ext" suffix, such as .bashrc.ext, .cshrc.ext, .kshrc.ext, .login.ext, .profile.ext, and .zshrc.ext (depending on the choice of shell).

!!!warning "Feature not implemented yet"
    The above-mentioned customizations via dot files with ".ext" suffix are not supported on our platform yet.
-->

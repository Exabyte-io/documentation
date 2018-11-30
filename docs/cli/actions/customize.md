# Customize Shell Environment

The action of customizing the [shell environment](../environment.md#shell-type) from the default "bash" setting can in general be performed by running the `change_shell` command, with the path to the shell executable present under the `/bin` system folder inserted as flag. 

## Example: Change to ZSH

Here, we offer a specific example of the command necessary to change the shell from the default "bash" to the "zsh" option.

```
change_shell /bin/zsh
```

## Dot Files

There exist several "standard" dot-files within the [Login Home](../../infrastructure/login/directories.md), including one for each shell type that we support, that represent symbolic links to read-only files controlled by the platform administrator. Thus, the user should **NEVER** attempt to modify these files. Examples include the .bash_profile, .bashrc, .cshrc, .kshrc, .login, .profile, or .zshrc files. 

Instead, the user should put his/her customizations to the shell environment into the corresponding files that have an ".ext" suffix, such as .bashrc.ext, .cshrc.ext, .kshrc.ext, .login.ext, .profile.ext, and .zshrc.ext (depending on the choice of shell).

!!!warning "Feature not implemented yet"
    The above-mentioned customizations via dot files with ".ext" suffix are not supported on our platform yet.

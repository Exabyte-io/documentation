running the `change_shell` command, for example to change your shell to zsh run 

```
change_shell /bin/zsh
```

There are several "standard" dot-files that are symbolic links to read-only files that Exabyte.io controls. Thus, you should NEVER modify or try to modify such files as .bash_profile, .bashrc, .cshrc, .kshrc, .login, .profile, or .zshrc. Instead, you should put your customizations into files that have a ".ext" suffix, such as .bashrc.ext, .cshrc.ext, .kshrc.ext, .login.ext, .profile.ext, and .zshrc.ext. Which of those you modify depends on your choice of shell, although note that we recommend bash.

The table below contains examples of basic customizations directives one can put inside dot files. Note that when making changes such as these it's always a good idea to have two terminal sessions active so that you can back out changes if needed!

| Bash                  | Csh                   |
|:-------------------   |:-------------------   |
| `export ENVAR=var`    | `setenv ENVAR var`    |
| `alias ll='ls -lrt’`  | `alias ll “ls –lrt”`  |

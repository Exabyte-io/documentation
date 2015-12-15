# Compute Environment

When you log in to exabyte.io via command-line, you are in your global $HOME directory. You initially land in the same place all the time. This means that if you have files or binary executables that are located in your home directory, they will be available on all cluster nodes through a network-shared filesystem.

## Customizing Environment

The way you interact with compute resources can be controlled via certain startup scripts that run when you log in and at other times.  You can customize some of these scripts, which are called "dot files," by setting environment variables and aliases in them.

<!-- TODO: figure out how to deal with dotfiles There are several "standard" dot-files that are symbolic links to read-only files that Exabyte.io controls. Thus, you should NEVER modify or try to modify such files as .bash_profile, .bashrc, .cshrc, .kshrc, .login, .profile, .tcshrc, or .zprofile. Instead, you should put your customizations into files that have a ".ext" suffix, such as .bashrc.ext, .cshrc.ext, .kshrc.ext, .login.ext, .profile.ext, .tcshrc.ext, .zprofile.ext, and .zshrc.ext. Which of those you modify depends on your choice of shell, although note that we recommend bash. -->

The table below contains examples of basic customizations directives one can put inside dot files. Note that when making changes such as these it's always a good idea to have two terminal sessions active so that you can back out changes if needed!

| Bash                | Csh                 |
| ------------------- | ------------------- |
| `export ENVAR=var` &nbsp;&nbsp; | `setenv ENVAR var`    |
| `alias ll='ls -lrt’`  | `alias ll “ls –lrt”`  |


## Modules

Easy access to software is controlled by the *modules* utility. With modules, you can easily manipulate your computing environment to use applications and programming libraries. In many cases, you can ignore modules because NERSC has already loaded a rich set of modules for you when you first log in. If you want to change that environment you "load," "unload," and "swap" modules. A small set of module commands can do most of what you'll want to do.

### module list

The first command of interest is "module list", which will show you your currently loaded modules. When you first log in, you have NO modules loaded for you. Here is an example:

`# > module list`

```
Currently Loaded Modulefiles:
 1) modules/3.2.6.6 3) gni-headers/2.1-1.0400.4156.6.1.gem 5) xt-shmem/5.4.4
 2) xtpe-network-gemini 4) xpmem/0.1-2.0400.30792.5.6.gem  6) xt-mpich2/5.4.4
```

### module avail

Let's say you want to use a compiler. The "module avail" command will list all the available modules. It could be a very long list. But you can use the module's name stem to do a useful search. For example

`# > module avail applications`

```
--------------------- /export/compute/modulefiles ---------------------
applications/espresso/521-i-174-impi-044
applications/vasp/535-i-174-impi-044

```

### module swap

To swap already loaded modules with the new ones

`# > module swap PrgEnv-gnu/4.0.46 PrgEnv-intel/3.1.61`

That's all you have to do. You don't have to change your makefiles, or anything else in your build script unless they contain GNU or Intel-specific options or features. Note that modules doesn't give you any feedback about whether the swap command did what you wanted it to do, so always double-check your environment using the `module list` command.

### module load

If you want to use [Quantum ESPRESSO](http://quantum-espresso.org) application, just load that module.

`# > module load applications/espresso/521-i-174-impi-044`

Now you can invoke Quantum ESPRESSO with the `pw.x` command (that's the name of the binary executable).

<!-- by MM -->

# Login via Command Line

This page explains the process of connecting to exabyte.io through command-line interface: how to generate, upload ssh keys and use them to connect.

## Overview

We use [SSH keys](https://wiki.archlinux.org/index.php/SSH_keys) as a way to identify users and trusted computers during command-line sessions. Keys provide improved security, however they need to be set properly before use. The steps below will walk you through generating SSH key pair and adding the public key to your account.

## Create SSH keys

### Directives for Windows

If you are using [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html) as an SSH client, you will need to set it up with [puttygen.exe](http://the.earth.li/~sgtatham/putty/latest/x86/putty.exe) to generate SSH keys. [This page](http://www.rackspace.com/knowledge_center/article/generating-rsa-keys-with-ssh-puttygen) illustrates how to do that. Otherwise, please use directives below.

#### Step One: check for existing keys

Open command-line prompt, and run:

```
cd %userprofile%/.ssh
```

If you see "No such file or directory", then there aren't any existing keys: go to [Step Three](#step-three-generate-a-new-key). Otherwise, check to see if you have a key already:

```
dir id_*
```

If there are existing keys, you may want to use those: go to [Upload key](#upload-ssh-key) section.

#### Step Two - back up old keys

If you have existing SSH keys, but you don't want to use them when connecting to exabyte.io, you should back them up. In a command prompt on your local computer, run:

```
mkdir key_backup
copy id_rsa* key_backup
```

#### Step Three - generate a new key

If you don't have an existing SSH key that you wish to use, generate one as follows:

- log in to your local computer as an administrator
- In a command prompt, run:

    ```
    ssh-keygen -t rsa -C "your_email@example.com"
    ```

    Associating the key with your email address helps you to identify the key later on. Note that the ssh-keygen command is only available if you have already installed [Git](https://git-scm.com/download/win) (with Git Bash).

- press "Enter" to accept the default location and file name. If .ssh directory does not exist, the system creates one for you.
- enter, and re-enter, a passphrase when prompted.
- done, go to go to [Upload key](#upload-ssh-key) section.

### Directives for Linux and Mac OSX

#### Step One: check for existing keys

Open command-line prompt, and run:

```
cd ~/.ssh
```

If you see "No such file or directory", then there aren't any existing keys: go to [Step Three](#step-three-generate-a-new-key_1). Otherwise, check to see if you have a key already:

```
ls id_*
```

If there are existing keys, you may want to use those: go to [Upload key](#upload-ssh-key) section.

#### Step Two - back up old keys

If you have existing SSH keys, but you don't want to use them when connecting to exabyte.io, you should back them up. In a command prompt on your local computer, run:

```
mkdir key_backup
cp id_rsa* key_backup
```

#### Step Three - generate a new key

If you don't have an existing SSH key that you wish to use, generate one as follows:

- log in to your local computer as an administrator
- In a command prompt, run:

    ```
    ssh-keygen -t rsa -C "your_email@example.com"
    ```

    Associating the key with your email address helps you to identify the key later on.

- press "Enter" to accept the default location and file name. If .ssh directory does not exist, the system creates one for you.
- enter, and re-enter, a passphrase when prompted.
- done, go to go to [Upload key](#upload-ssh-key) section.

## Upload ssh key

Now you should have two files that start with *id_rsa* in your ".ssh" directory. One of them contains private key (.ssh/id_rsa by default) and one of them contains public key (.ssh/id_rsa.pub). We will upload public key to Exabyte.io.

!!! warning "**Never** share your private key with anyone"
    Your private key is only for you and is used to identify you with exabyte.io. A user logged in with your private key will automatically have access to your data and allocation.

To upload a public key:

- go to your Profile's "Settings" page. You will see "SSH Keys" section that contains a list of SSH keys associated with your account.

- add a key using the (+) button. When the input form appears, print a name for your key in the "Title" field and upload (or copy/paste) your public key (.ssh/id_rsa.pub) to the "Key" textarea. Then click "Save".

Your public will be saved with exabyte.io. This could take a few seconds. If everything is OK, the key label  (small circle in the left side of the saved key) becomes green. This means that your key is active and you are all set and ready to connect to exabyte.io via command-line.

<img data-gifffer="/images/SSHKeyUpload.gif">

## Connect to exabyte.io

### SSH Client Software

There is a variety of SSH clients that you can use to connect to a our platform. We will cover the following two:

- command-line terminal with OpenSSH (Linux and Mac OS X): a collection of software that ships with most Unix-like operating systems

- PuTTY (Windows): a free SSH client that can run on Windows, and is available for download on the [PuTTY Download Page](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html). The client executable is named [*putty.exe*](http://the.earth.li/~sgtatham/putty/latest/x86/putty.exe). **puttygen.exe** is also necessary to handle SSH keys.

### SSH Login via terminal

Replace the text inside braces below with the corresponding names/paths:

1. Change the permissions on the private key to be accessible to you only:

    ```
    chmod 400 {path/to/your/private_key}
    ```

2. At the command prompt, enter the following command:

    ```
    ssh -i {path/to/your/private_key} {exabyte.io_username}@bohr.exabyte.io
    ```


### SSH Login via PuTTY

When using PuTTY, one would need to load the SSH keys through its interface before connecting. [This page](http://www.rackspace.com/knowledge_center/article/logging-in-with-an-ssh-private-key-on-windows) has a great tutorial with visuals.

### Welcome screen

Once the ssh connection is established, you will see the following screen:

```
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

    - `exalist_nodes` : list compute nodes and their state
    - `showjobs` : view expected start time for your jobs

  Job submission cheat sheet:

    - `qstat` : show status of batch jobs
    - `qstat -a` : show status of batch jobs, use human time
    - `qsub` : submit batch jobs (e.g. `qsub ./job.sh`)
    - `qdel` : delete batch jobs (e.g. `qdel 7`)

  Accounting cheat sheet:

    - `balance` : show my detailed balance
    - `statement` : show detailed usage statistics

------------------------------------------------------------------
 *  By using the system you indicate your awareness and consent  *
 *  to the terms and conditions you were presented at the time   *
 *  of obtaining access credentials. ® 2015 Exabyte Inc.         *
------------------------------------------------------------------
```

## Data transfer

Depenging on your client, you may use one of the options below

### Transfer data via secure copy

Replace the text inside braces below with the corresponding names/paths:

1. To transfer files to exabyte.io:

```bash
scp -i <path to private_key> <path to file> <username>@bohr.exabyte.io:<path inside home dir>
```

2. To transfer files from exabyte.io::

```
scp -i <path to private_key> <username>@bohr.exabyte.io:<path inside home dir> <path to file>
```

### Transfer data via WinSCP

When using [WinSCP](https://winscp.net), one would need to load the private key through its interface before connecting. [This page](https://winscp.net/eng/docs/ui_login_authentication#private_key) explains how to do so.

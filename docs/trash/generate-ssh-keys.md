### Directives for Windows Using Putty

If you are using [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html) as an SSH client, you will need to set it up with [puttygen.exe](http://the.earth.li/~sgtatham/putty/latest/x86/putty.exe) to generate SSH keys. [This page](http://www.rackspace.com/knowledge_center/article/generating-rsa-keys-with-ssh-puttygen) illustrates how to do that. Otherwise, please use directives below.

#### Step One: check for existing keys

Open command-line prompt, and run.

```
cd %userprofile%/.ssh
```

If you see "No such file or directory", then there aren't any existing keys: go to [Step Three](#step-three-generate-a-new-key). Otherwise, check to see if you have a key already.

```
dir id_*
```

If there are existing keys, you may want to use those: go to [Upload key](#upload-ssh-key) section.

#### Step Two - back up old keys

If you have existing SSH keys, but you don't want to use them when connecting to exabyte.io, you should back them up. In a command prompt on your local computer, run.

```
mkdir key_backup
copy id_rsa* key_backup
```

#### Step Three - generate a new key

If you don't have an existing SSH key that you wish to use, generate one as follows.

- log in to your local computer as an administrator
- In a command prompt, run.

    ```
    ssh-keygen -t rsa -C "your_email@example.com"
    ```

    Associating the key with your email address helps you to identify the key later on. Note that the ssh-keygen command is only available if you have already installed [Git](https://git-scm.com/download/win) (with Git Bash).

- press "Enter" to accept the default location and file name. If .ssh directory does not exist, the system creates one for you.
- enter, and re-enter, a passphrase when prompted.
- done, go to go to [Upload key](#upload-ssh-key) section.

### Directives for Linux and Mac OSX

#### Step One: check for existing keys

Open command-line prompt, and run.

```
cd ~/.ssh
```

If you see "No such file or directory", then there aren't any existing keys: go to [Step Three](#step-three-generate-a-new-key_1). Otherwise, check to see if you have a key already.

```
ls id_*
```

If there are existing keys, you may want to use those: go to [Upload key](#upload-ssh-key) section.

#### Step Two - back up old keys

If you have existing SSH keys, but you don't want to use them when connecting to exabyte.io, you should back them up. In a command prompt on your local computer, run.

```
mkdir key_backup
cp id_rsa* key_backup
```

#### Step Three - generate a new key

If you don't have an existing SSH key that you wish to use, generate one as follows.

- log in to your local computer as an administrator
- In a command prompt, run.

    ```
    ssh-keygen -t rsa -C "your_email@example.com"
    ```

    Associating the key with your email address helps you to identify the key later on.

- press "Enter" to accept the default location and file name. If .ssh directory does not exist, the system creates one for you.
- enter, and re-enter, a passphrase when prompted.
- done, go to go to [Upload key](#upload-ssh-key) section.

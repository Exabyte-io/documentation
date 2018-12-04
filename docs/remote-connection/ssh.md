# Command Line Interface via SSH

The user can connect to the [Command Line Interface](../cli/overview.md) (CLI) of our platform using an **external SSH terminal client** under any Operating System (OS), as an alternative to the [Web Terminal](web-terminal.md).

We use **SSH keys** [^1] as a way to identify users and trusted computers during command-line sessions. Keys provide improved security, however they need to be set properly before use. The steps included in the present page will guide the user through generating SSH keys and adding them to the account being employed. 

Experienced users who are already familiar with how SSH clients operate under their preferred Operating System can navigate directly to the [Upload SSH key](#upload-ssh-key) section of the present page.

## OS-specific SSH Clients

We particularly recommend the following SSH clients for each OS.

- **Putty** [^2], a widespread SSH client for Windows.
- **OpenSSH** [^3], the standard protocol in Unix-based OSs (both Linux and Mac OS distributions) for connecting through SSH via the terminal.

## Generate SSH Keys

As introduced previously, SSH keys are necessary to connect to the CLI using the credentials for the account under consideration. 

External tutorials are available on how to generate such keys for each of the Putty [^4] and OpenSSH [^5] clients.

## Upload SSH Key

After generating the keys, they need to be uploaded to our platform and associated with the user's account. This effectively establishes a **secure link** between the external SSH client and the corresponding Exabyte account.

We explain how to upload the SSH keys to our platform in a [separate section](../accounts/ui/preferences/ssh.md) of the documentation.
            
!!!warning "Privacy of SSH keys"
    SSH keys are **private** and are meant to be used to identify exclusively the user with our platform. Any other user logged in with such private keys would automatically have access to the account's data and allocation, and because of this they should not be shared with anyone else.

## Connect to Server

Once the secure SSH link is established via the SSH keys, the remote Exabyte server can be accessed as follows (the user should replace the text inside braces below with the corresponding names/paths).

!!!info "Name of remote server"
    Our Exabyte server for accepting remote connections is referred to under the alias of **"bohr"**, and is accessible via the corresponding address `bohr.exabyte.io`.

### OpenSSH for Unix

1. The user should first change the permissions on the private key to be accessible to him/her only.

    ```
    chmod 400 {path/to/your/private_key}
    ```

2. At the command prompt, the user should then enter the following command.

    ```
    ssh -i {path/to/your/private_key} {exabyte.io_username}@bohr.exabyte.io
    ```

### Putty for Windows
  
Instructions on how to operate Putty to connect to our remote server can be found in Ref. [^6]. The name of the server to be used in this case is the same as before, namely `bohr.exabyte.io`.
  
### Enter the CLI

Following successful SSH connection, the user is presented with the [CLI of our platform](../cli/overview.md).

Some useful instructions are already contained in the CLI **splash welcome screen** greeting the user at the moment of login. A copy of this welcome screen is reproduced below.

![CLI Welcome Screen](/images/CLI-Welcome-Screen.png  "CLI Welcome Screen")

## Transfer Files with SCP

The user can also transfer files back and forth from his/her local hard drives to the folders on the remote Exabyte server. For this purpose, we recommend the **SCP file transfer protocol** [^7], which is also based on SSH.
    
### Windows Instructions

On Windows, we recommend the **WinSCP** graphical user interface program [^8]. A tutorial demonstrating how to operate it can be retrieved in Ref. [^9].

When using WinSCP, one would need to load the private key through its interface before connecting. Explanations on how to do so can be found in Ref. [^10].      
    
### Unix Instructions

The instructions for Unix-based operating systems can be found [in a separate page](actions/transfer-files-scp.md).

## Links to Clients Documentation

[^1]: [SSH keys, Website](https://wiki.archlinux.org/index.php/SSH_keys)

[^2]: [Putty Homepage, Website](https://www.putty.org/)

[^3]: [OpenSSH Homepage, Website](https://www.openssh.com/)

[^4]: [Puttygen - Key Generator for Putty on Windows, Website](https://www.ssh.com/ssh/putty/windows/puttygen)

[^5]: [SSH-keygen - Generate a New SSH Key, Website](https://www.ssh.com/ssh/keygen/)

[^6]: [How to Use Putty on Windows, Website](https://www.ssh.com/ssh/putty/windows/)

[^7]: [Wikipedia Secure Copy, Website](https://en.wikipedia.org/wiki/Secure_copy)

[^8]: [WinSCP homepage, Website](https://winscp.net/eng/index.php)

[^9]: [WinSCP Tutorial, Website](https://www.siteground.com/tutorials/ssh/winscp/)

[^10]: [WinSCP Authentication Page](https://winscp.net/eng/docs/ui_login_authentication#private_key)

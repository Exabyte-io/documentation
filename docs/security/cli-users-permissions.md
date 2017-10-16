<!-- by MM -->

## File system permissions

As a CLI user you have access to two main directories, `/home` and `/share`. 

### Home directory

When you connect to compute platform through a SSH terminal you are always redirected to your home directory. You have read and write permissions on your home directory. No one is able to access the content of your home directory.

### Share directory

Share directory (`/share`) is only accessible by organizations. When you create an organization, a directory with special permissions is created inside `/share/groups` directory. Please note that you should not modify permissions on `/share` directory, otherwise you would get permission denied while submitting organizational jobs to the system. An organization has an owner and may have a few projects and teams. Each team may have access to multiple projects. Members of a project and the organization owner are able to see the content of a project directory. For example, imagine you have created an organization named my-org and a project called my-project. If you connect to compute platform through a SSH terminal you would see `/share/groups/my-org/my-project` directory. You as an organization owner have read and write permissions on `/share/groups/my-org/my-project` directory. Also any member of my-project defined inside web application has read and write permissions on the project directory.

## On-premises installation

If you need a software or tool that is not currently installed and supported by Exabyte.io, you are welcome to install it inside your home directory. Please note that you can not install a software, tool or package through operating system package manager (YUM). You usually needs to download the source code of desired software, compile it along with its dependencies and install them inside your home directory.

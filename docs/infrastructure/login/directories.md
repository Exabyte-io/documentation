# Important Directories under Login Home 

Once the user enters his/her home folder under the login node (the so-called **Login Home**) via any of the possible [connection methods](../../remote-connection/overview.md), he/she will be presented with the following **directory structure**, which conforms to the conventions of the GNOME Desktop environment [^1] for the CentOS Linux distribution [^2] implemented on our platform.
 
```
.
├── cluster-001          => /cluster-001-home/<username>
├── cluster-007          => /cluster-007-home/<username>
├── Desktop
├── Documents
├── Downloads
├── dropbox              => /dropbox/<username>
├── job_script_templates => /export/compute/job_script_templates
├── Music
├── Pictures
├── Public
├── Templates
└── Videos
```

For the sake of the present discussion, the important folders that are worth noticing are the ones labelled with an arrow to their right, indicating that they represent shortcuts pointing to the full path specified to the right of the arrow. 

Each important folder is introduced in what follows, complementing the [general discussion](../../data-on-disk/directories.md) on the directory structure within our platform.

## Clusters Home Folders

Each [computing cluster](../clusters/overview.md) has its own distinct [home folder](../clusters/directories.md), referred to as the **Cluster Home**, which is mounted on the corresponding **Master Node** of the cluster.

We explain the contents of these cluster homes in a [separate section](../clusters/directories.md) of the documentation.

## Dropbox

Dropbox is a convenient way of sharing and transferring files across all nodes of the infrastructure. This functionality is narrated in detail in its own [dedicated page](../../data-in-objectstorage/dropbox.md).

## Jobscript Templates

The Login Home also contains a folder with [Job script](../../jobs-cli/batch-script.md) template examples, necessary for [submitting jobs via the Command Line Interface](../../jobs-cli/overview.md). 

## Links

[^1]: [Wikipedia GNOME, Website](https://en.wikipedia.org/wiki/GNOME)

[^2]: [Wikipedia CentOS, Website](https://en.wikipedia.org/wiki/CentOS)

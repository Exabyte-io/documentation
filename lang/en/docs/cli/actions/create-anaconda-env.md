# Create Anaconda Python Environment

Here, we explain how one can set up a custom python environment using Anaconda when using the [Command Line Interface](../overview.md)

## Loading Anaconda

Once logged into the command line interface, one must first load the anaconda module using the `module load` in the following way:

`module load python/anaconda3-5.2.0`

The user should see the message `The module python/anaconda3-5.2.0 is loaded` after executing the above command.
Furthermore, if the user executes `printenv`, they should see that their PATH environment variable has been prepended 
with the path to the anaconda binaries. For example, `/export/compute/software/pyenv/versions/anaconda3-5.2.0/bin:` 
in their `PATH` environment variable.

## Create Anaconda Environment

Now that Anaconda has been loaded, we can create a custom python environment using it. For demonstration purposes, we will now
create a custom python environment that uses Python version 3.7.

Before we go any further, let's first list any currently available conda environments. We can do so by executing:

`conda env list`

At the current moment, we should see that we have only 1 conda environment available to use, which is the `base` 
conda environment. To make a separate custom environment, we now execute the following command:

`conda create --name py37 python=3.7`

This will begin to create the py37 conda environment, which includes installing all required packages for python to 
execute properly. During the conda environment creation process, you will be prompted to proceed with the installation 
of the required packages for the creation of the py37 conda environment. At this prompt, you should type 'y'. The 
installation should finish shortly thereafter.

## Activating and Deactivating Conda Environment

Once the `py37` conda environment has been made, we can check i exists by again executing the command `conda env list`.
At this point, we should now see the `py37` environment in addition to the `base` environment. 

To activate the `py37` conda environment, execute the following command:

`source activate py37`

One should now see the `(py37)` environment loaded next to the command line prompt (look towards bottom left).

To switch from one conda environment to another, one can simply `activate` the other conda environment. For example,
to switch to the `base` conda environment, one executes the following.

`conda activate base`

to switch back to the `py37` environment, execute:

`conda activate py37`

The user should see the currently active environment (located at bottom left of screen, left of the command line prompt)
changing back and fourth between `py37` and `base` during this exercise. Finally, the user should be back in the `py37`
environment at this point.

To deactivate your conda environment, execute the following command

`conda deactivate py37`

## Installing packages into your custom conda environment:

While inside our custom `py37` conda environment, one can install packages using the following command:

`conda install <package_name>`

Alternatively, one can also install using `pip`:

`pip install <package_name>`

This is because conda installed `pip` during the creation of our custom `py37` conda environment.

To check which packages are currently installed in a certain custom conda environment, one executes:

`conda list`

## Final notes

If one wishes to have conda initialize automatically upon connecting to the command line interface, one executes:

`conda init`

after one has 'module loaded' Anaconda. The `conda init` command edits the users .bashrc file to initialize conda
when the user enters the command line interface. The default environment when using this approach is the `base`
conda environment.

Alternatively, the user can return to their home directory and execute the following command:

`source .bashrc`

For more great tips and tricks with Conda, we refer the users to this excellent 'conda cheat sheet'
[Conda Cheat Sheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)

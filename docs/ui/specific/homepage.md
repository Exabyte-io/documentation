# Account Homepage / Entry Gateway

When the user first logs into our platform using his/her username or email and password credentials, he/she is presented with the main **Homepage** of the Exabyte platform, otherwise known as the **Entry Gateway**.

This homepage is presented under the user's **default Account**, which can be modified through the [Account Switcher](/accounts/ui/switcher.md) by following the [standard defaulting procedure](/entities-general/actions/set-default.md). 

The initial screen of the Entry Gateway can be retrieved at all times by clicking the Exabyte Company logo in the [header](../header-footer.md). 

# Initial Options

Immediately after log-in, the user is first confronted with three main options, as displayed in the image below. 

![Entry Gateway](/images/entry-gateway.png "Entry Gateway")

These initial options can be navigated by the user by clicking their panels, or directly on the `Select` buttons. The overall result is a tree diagrams of sequential options, which will be reviewed throughout the rest of this documentation page. 

!!!note "Note: quick access to platform features"
    Numerous features can be accessed directly by opening either the [left-hand](../left-sidebar.md) or [right-hand](../right-sidebar.md) sidebars.

!!!note "Note: features not implemented yet"
    Many options are currently under development. Only features which are already enabled are reviewed in this page. Please [contact us](/ui/support.md) if you would like any of these features to  be given urgent attention for faster development. 


# Query Bar

A query bar <i class="zmdi zmdi-search zmdi-hc-border"></i> is present on top of the page, allowing the options to be searched at any level. 

## Search Tags

This Query bar is populated automatically with tags as the options are selected by the user. The search is performed under the level of the latest tag.

All tags can be removed simultaneously by clicking the "X" button on the right-hand side. This reverts the screen to its initial default appearance. Alternatively, each tag can be deleted in turn, which takes the interface up by one level each time.

## Search Suggestions

Suggestions are also displayed in real time under the query bar, as new search keywords are being entered. They can be added as tags to the query by clicking them. 

## Animation

The query functionality is demonstrated in the following animation. Here, we first navigate to the "Run Simulations" option under "Modeling and Simulations", and then we revert back to the original screen by deleting the corresponding tags.

<img data-gifffer="/images/gateway-query.gif" />


# Modeling and Simulations <i class="zmdi zmdi-cloud-outline-alt"></i>

The first option allows for the creation of simulation workflows for material modeling. They can be based on any of the supported theoretical [models](/models/overview.md), operated under the associated computational [methods](/methods/overview.md) and [applications](/applications/overview.md). 


!!!note "Note: labeling of options"
    In each flowchart presented in this page, a number or number-letter code is present inside each sub-component. It should be referred to in the headers of their dedicated explanation paragraphs.

![Modeling Flowchart](/images/modeling-flowchart.png "Modeling Flowchart")

## 1. Run Simulations 

Here, the user can choose to calculate [material properties](/materials/properties.md) of interest, through the selection of the corresponding workflow template. Examples of pre-defined templates may include total energy calculations, phonon or bandstructure dispersion calculations, as well as the possibility to relax and optimize the geometry of the crystal structure. 

At the moment, our platform only supports the [Density Functional Theory](/models/dft/overview.md) (DFT) theoretical framework for executing electronic structure calculations, as implemented by the [Quantum ESPRESSO](/applications/quantum-espresso.md) or [VASP](/applications/vasp.md) applications.

A sample of workflow templates included under this option is portrayed in the image below. Clicking any of these available templates creates a new job implementing the workflow, under the default Project of the user's Account.

![Workflow Templates](/images/workflow-templates.png "Workflow Templates")


## 2. Design Workflows 

Here, the possibility to design new computational workflows is offered to the users. 

### 2A. Density Functional Theory 

As mentioned previously, for the moment only the [DFT theoretical model]((/models/dft/overview.md)) is implemented under option "2A". Plans are however under way to expand the offer to new atomistic simulation approaches, such as the classical Molecular Dynamics and Multi-scale techniques. 

## 3. Connect Remotely 

In this section, users can connect to our computational engine through alternative channels, other than our graphical user interface-based platform. 

In future, further remote connection interfaces will be offered to our customers, including for example the Jupyter web-based python environment provided with a set of pre-loaded libraries and tools.

### 3A. Command Line Terminal 

The first remote connection method consists in the [Command Line interface](/compute/cli/login.md) (option "3A"). 

### 3B. Remote Desktop 

Alternatively, the [Remote Desktop environment](/compute/remote-desktop.md) (option "3B") can also be employed. 


# Machine Learning <i class="zmdi zmdi-graduation-cap"></i>

The Machine Learning functionality offered by our platform can be accessed as the second main option. Such functionality affords for the building of data-driven statistical models, based on results of materials simulations. The techniques implemented in our platform are the object of a [dedicated tutorial](/tutorials/ml/train-ml-model.md).

Machine Learning allows for example to predict new material properties by applying previously-trained models. In addition, new models can be trained by designing appropriate workflows, or use some of their pre-defined templates.

![Machine Learning Flowchart](/images/ml-flowchart.png "Machine Learning Flowchart")

## 2. Train New Model 

New models can be created under this option, by either designing new training workflows or using a pre-defined template.

### 2A. Regression linear 

This option allows for the building of a predictive model using the linear regression method. Selecting this option creates the corresponding workflow under a new job inside the default Project. 

# Data Analytics <i class="zmdi zmdi-search"></i>

The final main "Data analytics" option gives the user the possibility to import new materials from centralized databases into the Account-owned collection of materials. Alternatively, they can be uploaded directly from locally-stored files. In addition, advanced data analysis tools are provided. 

![Data Analytics Flowchart](/images/data-flowchart.png "Data Analytics Flowchart")

## 1. Upload/import 

Here, the user can upload or import a new material into the Account-owned collection from multiple external sources.

### 1A. Upload Material from File 

This option gives the user the possibility to [upload](/materials/actions/upload.md) one or multiple local files containing the relevant crystallographic information about the material under investigation. We support the CIF, POSCAR and XYZ crystal structure data formats.

### 1B. Import from Cloud Database 

We have made the third-party "Materials Project" repository of materials available to the users of our platform.  The materials contained there can thus be [imported](/materials/actions/import.md) into the Account-owned collection.

Support for other databases will be added in future.

## 2. Analyze Data 

This features allows materials to be [searched](/entities-general/actions/search.md) and inspected by the user. 

### 2A. Search my Materials 

This option searches only within the limits of the Account-owned collection of materials.

### 2B. Search all Materials 

Publicly available materials, originating from across the entire platform, can be searched and analyzed collectively with this option.
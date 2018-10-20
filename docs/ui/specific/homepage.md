# Account Homepage / Entry Gateway

When the user first logs into our platform using his/her username or email and password credentials, he/she will be presented with the main **Homepage** of the Exabyte platform, otherwise known as the **Entry Gateway**.

This homepage is always presented under the user's **default Account**, which can be modified through the [Explorer interface](/entities-general/ui/explorer.md) of the main [Account Switcher](/accounts/ui/switcher.md) by following the [standard defaulting procedure](/entities-general/actions/set-default.md). 

The initial screen of the Entry Gateway can be retrieved at all times during navigation of our platform by clicking on the Exabyte Company logo in the main top [header](../header-footer.md) of the user interface. 

# Options under Initial Screen

Immediately after log-in, within the initial screen of the Entry Gateway, the user will first be confronted with a set of three main options and associated descriptions, as displayed in the image below: 

![Entry Gateway](/images/entry-gateway.png "Entry Gateway")

These initial options can be navigated as desired by the user by clicking anywhere on their panels, or directly on their `Select` button. The overall result is a tree diagrams of sequential options, which will be reviewed throughout the rest of this documentation page. 

!!!note "Note: quick access to platform features"
    Instead of navigating progressively through this tree diagram, numerous features offered by our platform can be accessed directly by opening either of the [left-hand](../left-sidebar.md) or [right-hand](../right-sidebar.md) sidebars of the main [user interface](../overview.md).

!!!note "Note: features not implemented yet"
    Many options under the Entry Gateway have not been implemented yet and are still currently under development. Only the features which are already enabled are reviewed in this page, with occasional mentions of upcoming new features under development whenever applicable. Please [contact us](/ui/support.md) if you would like some of these features to  be given urgent attention for faster development. 


# Query Bar

As the reader may notice, a query bar <i class="zmdi zmdi-search zmdi-hc-border"></i> is also present on top of the Entry Gateway page, allowing the various computational tasks options outlined in the forthcoming paragraphs to be searched through at any level. 

## Search Tags

This Query bar will be populated automatically with tags as the options are progressively selected by the user, to help remind the user of their overall current sequence. The search will be performed under the level of the latest tag currently present in the query.

The possibility to remove all such tags is also offered via the "X" button on the right-hand side of the query bar, which reverts the screen to its initial default appearance. Alternatively, each tag can be deleted in turn by the user, which takes the interface up by one level each time.

## Search Suggestions

Suggestions are also displayed in real time under the query bar, as new search keywords are being entered by the user. These can be selected and added as tags to the query by clicking on them. 

## Animation

Some of the above-mentioned functionality of the query bar is demonstrated in the following animation, where we first navigate to the "Run Simulations" option under "Modeling and Simulations", and then revert back to the original screen by deleting the corresponding tags from the query bar:

<img data-gifffer="/images/gateway-query.gif" />


# Modeling and Simulations <i class="zmdi zmdi-cloud-outline-alt"></i>

The first option allows for the creation of simulation workflows in the general context of computational material modeling. These workflows can be based on any of the supported theoretical [models](/models/overview.md), operated under their corresponding computational [methods](/methods/overview.md) and [applications](/applications/overview.md). 


!!!note "Note: labeling of options"
    In each tree-diagram flowchart presented in this page, a number or number-letter code is present inside the various sub-components, to be referred to in the headers of their dedicated explanations following each diagram.

![Modeling Flowchart](/images/modeling-flowchart.png "Modeling Flowchart")

## 1. Run Simulations 

Here, the user can choose to calculate material properties of interest, through the selection of the corresponding workflow template. Examples of pre-defined workflow templates may include total energy calculations, phonon or bandstructure dispersion calculations, as well as the possibility to relax and optimize the geometry of a crystal structure. 

At the moment, our platform only supports the [Density Functional Theory](/models/dft/overview.md) (DFT) theoretical framework for executing such electronic structure calculations, as implemented by the [Quantum ESPRESSO](/applications/quantum-espresso.md) or [VASP](/applications/vasp.md) applications.

An example of selection of workflow templates included under this option is portrayed in the image below. Clicking and selecting any of these available templates will create a new job implementing the desired workflow, under the default Project of the user's Account.

![Workflow Templates](/images/workflow-templates.png "Workflow Templates")


## 2. Design Workflows 

In this branch, the possibility to perform  material modeling through the design of entirely new computational workflows, or through the use of pre-defined workflow templates, is offered to the users. 

### 2A. Density Functional Theory 

As mentioned previously, for the moment only the [DFT theoretical model]((/models/dft/overview.md)) is implemented under option "2A" in the above flowchart. Plans are however currently under way to expand the offer to new atomistic simulation approaches, such as the classical Molecular Dynamics and Multi-scale techniques. 

## 3. Connect Remotely 

Through this section, users can connect to our computational engine through alternative channels other than our standard graphical user interface-based platform. 

In future, further remote connection interfaces will be offered to our customers, including for example the Jupyter web-based python environment provided with a set of pre-loaded libraries and tools.

### 3A. Command Line Terminal 

The first available remote connection method consists in the [Command Line interface](/compute/cli/login.md) (option "3A"). 

### 3B. Remote Desktop 

Alternatively, the [Remote Desktop environment](/compute/remote-desktop.md) (option "3B") can also be employed to access our computational engine. 


# Machine Learning <i class="zmdi zmdi-graduation-cap"></i>

The Machine Learning functionality offered by our platform can be accessed as the second main option. Such functionality affords for the building of data-driven statistical models based on the actual results of computational simulations of materials. The various Machine Learning techniques implemented in our platform are the object of an [entire tutorial](/tutorials/ml/train-ml-model.md) within the present documentation manual.

Machine Learning allows for example to predict new material properties by applying previously-trained models, or to train new models altogether by designing training workflows or use some of their pre-defined templates.

![Machine Learning Flowchart](/images/ml-flowchart.png "Machine Learning Flowchart")

## 2. Train New Model 

New Machine Learning models can be created under this option, by either designing new training workflows or using a pre-defined template.

### 2A. Regression linear 

This option allows for the building of a predictive machine learning model using the linear regression method. Selecting this option will create the corresponding workflow under a new job inside the default Project of the Account currently being used. 

# Data Analytics <i class="zmdi zmdi-search"></i>

The final main "Data analytics" option gives the user the possibility to import new materials from centralized databases into the user's own collection of materials, or to upload them directly via locally-stored files. In addition, advanced data analysis tools are provided under this option. 

![Data Analytics Flowchart](/images/data-flowchart.png "Data Analytics Flowchart")

## 1. Upload/import 

Here, the user can upload or import a new material into the Account-owned collection from multiple external sources, through any of the following methods:

### 1A. Upload Material from File 

This option gives the user the possibility to [upload](/materials/actions/upload.md) one or multiple files, containing the relevant crystallographic information about the material under investigation, which are stored locally on the user's computer. The file formats which are currently supported by our platform include the CIF, POSCAR and XYZ crystal structure data formats.

### 1B. Import from Cloud Database 

We have made the third-party "Materials Project" online repository of materials available to the users of our platform. This allows all centrally-stored materials contained in this database to be [imported](/materials/actions/import.md) into the Account-owned collection of materials together with their corresponding metadata.

Support for other databases will be added in future.

## 2. Analyze Data 

This features allows materials stored on our platform and their associated properties to be [searched for](/entities-general/actions/search.md) and inspected by the user. Two types of materials collections can be searched through in this way:

### 2A. Search my Materials 

This option searches only within the limits of the Account-owned collection of materials.

### 2B. Search all Materials 

Under this option instead, all publicly available materials data originating from all Accounts of our platform combined can be searched and analyzed together, besides the items present in the Account-owned collection.


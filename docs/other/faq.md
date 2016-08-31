<!-- TODO by TB -->
<!--
other questions to add:
- how long does it take for my calculation to start?
- who else is using it?
- where can I leave a feature request?
- how do I know that you will exist tomorrow?
-->

# General

## What is exabyte.io?

Exabyte.io is the fastest way to design and discover new materials.

We believe that focusing on core materials science is the most effective way to speed things up. We merge together in a single environment: rigorous models, vast compute power, intuitive user interface and data management tools, in order to make your work on materials design highly efficient.

## Where does your name come from?

Exabyte is 2<sup>60</sup> bytes. Or 1 billion gigabytes. Or 1 million hard drives. Or 1 thousand datacenter storage units. It is a pretty big number and it illustrates the complexity and scale of the problem we solve. Rumor has it that our founding team together with the leading minds in the field had figured out that after surpassing 1 exabyte of accumulated materials data computers will be able to run simulations without needing humans...

## Why are you doing this?

The world of today is broken. Humans now face global challenges too many to count. We exist to solve the most fundamental and most important of these challenges by driving new generations of advanced materials. In our vision the world of tomorrow is created not through long and expensive tests by trial-and-error, but through fast, accurate and intelligent models.

## Why should I care?

Because you already know that the way materials design and discovery is done now is being rapidly transformed. There are multiple new initiatives started, you can feel that radical changes are soon to come, and you want to be among the first to know about them and extract benefits.

---

# Materials

## What do you classify as a material?

It is crucial to have a concise and informative way to describe materials and their properties in order to reach traceability, reproducibility and make results searchable.

We classify the data about materials into two main subcategories of properties: **descriptive** and **characteristic**.

- **Descriptive** data holds the parameters that are required to define a material in a way that prevent duplicates, eg. <a href="https://en.wikipedia.org/wiki/Bravais_lattice" target="_blank" class="text-muted">Bravais lattice vectors</a>.

- **Characteristic** data contains parameters that reflect on physical properties of materials, eg.
<a href="https://en.wikipedia.org/wiki/Electronic_band_structure" target="_blank" class="text-muted">
    electronic bandstructure
</a>,
<a href="https://en.wikipedia.org/wiki/Electron_mobility" target="_blank" class="text-muted">
    electron mobility
</a>,
<a href="http://www.researchgate.net/post/How_to_calculate_formation_energy_using_DFT" target="_blank" class="text-muted">
    formation energy
</a>.

Descriptive properties define materials uniquely (eg. Name/Lastname/Address/Title for a person), characteristic properties are extracted by simulations and tell us how good this materials is for certain applications (think Talents/Skills/Experience in the above analogy).

## Do you store my materials data?

We store the data about materials in a central database and every user has a copy that he/she can contribute to and modify at will. We support both private and public scenarios. By default all data you create is public and accessible to other users. You can choose to opt out and have your data in the private domain.

## Is my materials data viewable to the whole world?

Not unless you choose so. At current we only allow access from registered users, however in the future we plan on implementing a way to share your data with the outside world as well. Users of cloud storage services (google docs, dropbox, box etc.) can see why this could be handy.

## Why would I share my precious data with others?

This is more important for users in enterprise: you do **not** have to share data and have absolute control over it. We set up enterprise subscriptions such that data access is regulated by users with administrative permission at the organization level with fine-grained control.

There are also clear benefits that can be extracted from having others view materials that you work on when you care about traceability, reproducibility and validity of the simulation results. And when setting up a collaboration.

## How secure is my data in the cloud?

Chances are that these days your data may be more secure in the cloud than on your company's own servers. One look at the sheer number of case studies and companies that use cloud computing for their mission-critical activities serves as a better proof than thousand words: <a href="https://aws.amazon.com/solutions/case-studies/all/" target="_blank" class="text-muted">link</a>. If your enterprise is not on the list yet, you may be missing out.

---

# Models

## What models do you use @exabyte.io?

At current we support <a href="https://en.wikipedia.org/wiki/Density_functional_theory" target="_blank" class="text-muted">density functional theory</a> in the At current we support <a href="https://en.wikipedia.org/wiki/Basis_set_(chemistry)#Plane-wave_basis_sets" target="_blank" class="text-muted">planewave</a> At current we support <a href="https://en.wikipedia.org/wiki/Pseudopotential" target="_blank" class="text-muted">pseudopotential</a> approximation. We plan on adding more soon, however we want to make sure that everybody who uses us has an outstanding experience. That means gradually adding new models (users, methods, materials), instead of opening the floodgates all at once.

## What simulation engines do you support?

At current we support <a href="https://quantum-espresso.org" target="_blank" class="text-muted">Quantum ESPRESSO</a> for everyone. And also have enterprise users running proprietary and commercial codes. Reach our using the feedback form above or our email address at the bottom of the page to learn more.

We also plan to add support for <a href="https://berkeleygw.org" target="_blank" class="text-muted">BerkeleyGW</a> in the next few months.

## How did you choose the two?

Our founding team has profound experience with Quantum ESPRESSO (several publications produced, multiple material families studied, numerous modifications to the source code employed) from prior work, and is intimately aware of the great momentum and extensive development efforts behind the code.

We have roots at UC Berkeley, in fact our scientific advisors are Berkeley professors. We know what BerkeleyGW can do and see great potential in the application of advanced electronic structural methods to realistic materials.

## How do you make sure the models are accurate?

There are three main things that are important to achieve accuracy in predictions and we believe that our product has them all:

* rigorous models
* vast compute resources
* traceability, reproducibility

Rigorous models predict the nature well, compute resources let us employ such models, and traceability let us choose precision parameters and other method details properly.

---

# Infrastructure

## What cloud provider do you use?

We strive to be provider-agnostic and let our users select the details about the hardware.

Every provider has its strong and weak points and we would like to be able to leverage those appropriately to maximize the benefits for our users.

## What cloud providers do you support?

At current we fully support AWS and Rackspace, and have support for IBM SoftLayer and Azure coming in the nearest future.

## What exactly is "vast compute power"?

Our current customers routinely run their simulation workflows on ~1k CPU (central processing units, or processors). We have stress-tested the infrastructure to ~10k and have plans to extend it to ~100k and further beyond it in the next year or so.

## Can I run a simulation workflow on a thousand CPU in a couple of clicks?

Yes, you can. Although we are still in private beta, we have already scaled far beyond 1k CPU.

<!-- TODO by TB -->
<!--
other questions to add:
- how long does it take for my calculation to start?
- who else is using it?
- where can I leave a feature request?
- how do I know that you will exist tomorrow?
-->

# Frequently Asked Questions

> Last updated: Oct 29, 2019

## General

### What is Mat3ra?

Mat3ra is a comprehensive platform for materials design and discovery through modeling and simulations.

We believe that focusing on core science is the most effective way to speed things up. We merge together in a single environment: rigorous models, vast compute power, intuitive user interface and data management tools, in order to make your work on materials design highly efficient.

### I don't get it - what is it really?

OK, the animation below might help demonstrate our vision:

<img data-gifffer="https://exabyte.io/img/iron-man-creates-material.gif">

### Where does your name come from?

Exabyte is 2<sup>60</sup> bytes. Or 1 billion gigabytes. Or 1 million hard drives. Or 1 thousand datacenter storage units. It is a pretty big number and it illustrates the complexity and scale of the problem we solve. Rumor has it that our founding team together with the leading minds in the field had figured out that after surpassing 1 exabyte of accumulated materials data computers will be able to run simulations without needing humans...

### Why are you doing this?

The world of today is broken. Humans now face important global challenges. We exist to solve the most fundamental and most important of these challenges by driving new generations of advanced materials. In our vision the world of tomorrow is created not through long and expensive tests by trial-and-error, but through fast, accurate and intelligent models. Read more at [blog.exabyte.io](https://blog.exabyte.io).

### Why should I care?

Because you know that materials design and discovery is being rapidly transformed now. There are multiple new initiatives started, you can feel that radical changes are soon to come, and you want to be among the first to know and benefit from them.

---

## Materials

### Do you store my materials data?

We store the data about materials in a central database and every user has a copy that he/she can contribute to and modify at will. We support both private and public scenarios. By default all data you create under personal account is public and accessible to other users. You can choose to opt out and have your data in the private domain.

### Is my materials data viewable to the whole world?

Not unless you choose so. At current we only allow access from registered users, however in the future we plan on implementing a way to share your data with the outside world as well. Users of cloud storage services (google docs, dropbox, box etc.) can see why this could be handy.

### Why would I share my precious data with others?

This is more important for users in enterprise: you do **not** have to share data and have absolute control over it. We set up enterprise subscriptions such that data access is regulated by users with administrative permission at the organization level with fine-grained control.

There are also clear benefits that can be extracted from having others view materials that you work on when you care about traceability, reproducibility and validity of the simulation results. And when setting up a collaboration.

### How secure is my data in the cloud?

Chances are that these days your data may be more secure in the cloud than on your company's own servers. One look at the number of case studies and companies that use cloud computing for their mission-critical activities serves as a better proof than thousand words: <a href="https://aws.amazon.com/solutions/case-studies/all/" target="_blank" class="text-muted">link</a>. If your enterprise is not on the list yet, you may be missing out.

---

## Infrastructure

### What cloud providers do you use?

We strive to be provider-agnostic and let our users select the details about the hardware.

Every provider has its strong and weak points and we would like to be able to leverage those appropriately to maximize the benefits for our users.

### What cloud providers do you support?

At current we fully support AWS and Azure in production. We paused using Rackspace and IBM SoftLayer due to performance concerns, but they can be quickly re-added upon request.

### As far as I understand this project allows one to use supercomputing facilities by paying money. But I cannot find any information about prices?

For pricing, please see [the service levels pricing section](../pricing/service-levels.md), and the [service levels features explanation](../accounts/service-levels.md). The pricing is quite comprehensive and can be **as low as 2 cents per core hour** for [saving-category](../infrastructure/compute/overview.md) resources. 

### How much computational resources do you have? How much of them user can use for one job?

With the cloud, there is really no limit for high-throughput calculations. We have scaled to <a href="https://blog.exabyte.io/how-big-is-cloud-scale-9a3d891ced0" target="_blank">35,000 cores at most in test regime</a>, and regularly use ~10,000 cores in production. 

For a single communication-intensive job (ie. large cell, hybrid functionals, GW) the low-latency interconnect options on some cloud providers allow to scale to ~16-32 nodes (see Fig. 2 <a href="https://arxiv.org/pdf/1812.05257.pdf" target="_blank">from this recent manuscript</a>). Alternatively, there are large memory nodes that we found very helpful for GW, for example. We presently administratively limit each cluster to 200 nodes (each with 16-36 cores) and allow users to use 10 nodes per single job.


### Is it possible to just upload my own input file for QE and then use the interface to submit and make other post-processing with it?

We are covering this exact topic, and other similar ones in the webinar series. Here's the recording: <a href="https://youtu.be/FyBKlLQ2k9M">https://youtu.be/FyBKlLQ2k9M</a>. See links to video time in Description, part 4 "Jobs" in particular. It explains how to migrate existing work to Exabyte.

### Which software codes can we use? Only those installed on your machines? 

Here's the [list of installed software](../software-directory/overview.md), with many packages/versions accessible via command-line interface through [modules environment](../cli/modules.md). Users can also [install new software](../cli/actions/add-software.md) using the runtime libraries provided (or install them as well), and [set up a python environment](../cli/actions/create-python-env.md), for example. We can help install new packages globally too, of course.

### Can I use our own script or software to connect via ssh to your system and submit jobs?

> For example simultaneous submition of 200 jobs at a time (each job is 16 CPU for 2 hours). Then after these 2 hours resubmit another 200 jobs and so on. 

Absolutely. This is exactly what our [case study](../benchmarks/high-throughput-screening.md) speaks about here.

### Will there be a queue for these (200) calculations (from above)?

The beauty of the cloud is that it is elastic, so we can start all 200 jobs at once. Our system is dynamic and we run it well below the maximum capacity, so extra 200 jobs should take 5-15 min total to start as the computational nodes are provisioned and added to the system in parallel. This [benchmark](../benchmarks/high-throughput-screening.md) demonstrates it really well. The ability to "burst" - quickly run through a large number of jobs with little wait, is a nice value proposition of our system, compared to the shared use academic/gov supercomputers, for example.

### Another example: I have heavy QE calculations, which require disk space of about 100-300 GB, and runs continuously during at least a week. Is it possible to do that?

Yes, indeed - a job running for a week writing 100-300 Gb during that period is perfectly fine. We do not presently enforce maximum wall time, beyond what the account balance can accommodate. If you have 200 jobs like that running in parallel, we can accommodate with additional preparations. 

We enforce [quotas](../data-on-disk/quotas.md) on the accounts to avoid clashing, the exact amounts we can [set per account](../pricing/storage-quota.md) as desired.

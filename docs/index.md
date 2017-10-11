<!-- by TB -->

Exabyte.io is a cloud-based environment for materials modeling and simulations. This documentation explains how it works. You may search for your topic of interest by using the input field in the top left corner or read on.

The [links](#links) section below can direct reader to sources of more in-depth explanation about what we are building and why [[1]](#links), quick demonstration of our product capabilities [[2]](#links) and example case studies [[3]](#links).

# Quickstart

In case you feel impatient, you can skip straight to our tutorial summarizing
[first steps with exabyte.io](getting-started/run-first-simulation.md). You will learn how to create and save a material and run a simulation that predicts this material's electronic bandstructure.

# Contents

This documentation is divided into three main categories (present inside the sidebar on the left):

## Materials

* how to design, upload or import material geometries
* supported characteristic properties (eg. band gap, formation energy, electron mobility) supported
* advanced topics:
    * creation of combinatorial sets of materials for high-throughput screening,
    * overview of materials analytics (eg. how to make sense of all the characteristic properties)

## Models & Methods

* explanation of the models used to extract the properties of materials and their particular implementations (methods),
* how to apply these models and run simulations
* advanced topics:
    * editing simulation input,
    * dissecting convergence and relaxation algorithms,
    * calculation of compound characteristic properties (eg. formation energy)

## Compute

* how to submit a simulation job
* how to set compute resources
* job submission queues and urgency factors
* advanced topics:
    * benchmarks and scaling
    * limits per compute queue
    * alternate connection methods:
        * secure shell terminal:
        * web-browser terminal:
        * remote desktop via VNC

Other parts explain data security, sharing and collaboration, billing/pricing and our terminology.

## Highlighted features

### Materials Design/Upload/Import

We let one develop materials from scratch by designing new geometries or reuse/extend prior works by uploading structures from disk or importing from trusted database sources. More information on the topic available on this [page](/materials/upload-and-import.md).

### Distributed-memory calculations

Materials simulations are often computationally demanding. We put much attention to performance and scalability of our product. More information available [here](/compute/overview.md) and [here](/compute/benchmarks-and-scalability.md).

## How to get help

We have support team that is active 24/7 and will do our best to reply to your requests within 24 hours. Our support team can be contacted by phone, email, or the web during working hours Pacific Time:

- email: <a href="mailto:support@exabyte.io" target="_blank">support@exabyte.io</a>,
- phone: +1.510.473.7770,
- web: chat box at the bottom of our main <a href="https://platform.exabyte.io" target="_blank">web application</a>.

# Additional links

1. [What is materials discovery cloud, article](https://www.linkedin.com/pulse/how-we-design-world-tomorrow-what-materials-discovery-timur-bazhirov)
2. [How big is "cloud-scale", article](https://www.linkedin.com/pulse/how-big-cloud-scale-timur-bazhirov)
3. [High-throughput computer-aided discovery of new metallic alloys, case study](https://exabyte.io/#case-study)

# Notes

In case you find that something is missing or if you still have questions after reading this documentation, please <a class="text-muted" href="mailto:support@exabyte.io" target="_blank">contact us</a>.

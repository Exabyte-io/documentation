# How to incorporate spin-orbit coupling effect in Quantum ESPRESSO

In this tutorial, we walk you through the steps of incorporate spin-orbit
coupling effect in bandstructure calculation using Quantum ESPRESSO. We want to
calculate the electronic bandstructure of Bi<sub>2</sub>Se<sub>3</sub>, a
prototypical topological insulating material, featuring a insulating bulk and
conducting surface states. Spin-orbit coupling effect and presence of surface is
required for the existence to Topological Dirac surface states.

## 1. Creating slab structure
We will need to create a slab structure for this calculation. Density Functional
Theory calculation can only be performed on periodic systems. To get a surface,
we need to add sufficient vacuum between the layers.

Navigate to the materials designer from the left sidebar, and click create new
material. Set the lattice type (hexagonal in case of
Bi<sub>2</sub>Se<sub>3</sub>), original lattice constants, and atomic positions.
Then select **Preserve Interatomic Distance** and increase to lattice vector
**c** to add vacuum to the ab-plane.

![Bi2Se3 slab structure](/images/tutorials/soc/bi2se3-slab.webp "Bi2Se3 slab structure")


## 2. Create workflow
We need to specify the workflow following workflow steps to obtain the
bandstructure with Spin-orbit coupling effect:

1. Perform self-consistent field (SCF) calculation
2. Perform bands (NSCF) calculation along specific k-path
3. Post-processing of bands calculation

![Bandstructure with SOC workflow](/images/tutorials/soc/soc-workflow.webp "Bandstructure with SOC workflow")

Note that for SOC calculation, we need to select fully relativistic
pseudopotential.

![Relativistic pseudopotential](/images/tutorials/soc/relativistic-pseudo.webp "Relativistic pseudopotential")

### 2.1. Self-consistent field calculation
Add an execution unit, and select **pw_scf_soc** template, there are few other
SOC templates that you may explore, for example SOC in conjunction to the
Hubbard U calculation.

![SOC templates](/images/tutorials/soc/soc-flavors.webp "SOC templates")

### 2.2. PW Bands calculation
Add next execution unit for PW *bands* calculation. Here we select
**pw_bands_soc** template.

### 2.3. Bands.x postprocessing
Finally, we andd another unit for postprocessing of our bands data (optional).


## 3. Job designer
Navigate to the jobs designer page from the left sidebar and click create new
job. Select material and workflow. We can further edit the workflow units, and
set various parameters under **Important Settings** tab. Here we can set k-grid
density, starting magnetization, K-path, etc. SOC calculations are slower to
converge, it is possible to start a SOC calculation from a previously converged
SCF charge density that was performed without SOC.

![Important settings](/images/tutorials/soc/important-settings.webp "Important settings")

Navigate to the **Compute** and set various computer parameters, such as, time
limit for a given calculation, queue, number of nodes, and number of processor
cores per node.

![Compute parameters](/images/tutorials/soc/compute-parameters.webp "Compute parameters")

Save and exit job designer, now hover over the job, and click the run button to
submit job.


## 4. Results
Once the job is finished, click over the job to navigate to the **Results** tab
for the summary of various results including the bandstructure plot. All output
files are available under the **Files** tab.


## Step-by-step screenshare video

In the below video, we go through an example calculation.

<div class="video-wrapper">
<iframe class="gifffer" width="100%" height="100%" src="https://www.youtube.com/embed/Zr1jcalLYPU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

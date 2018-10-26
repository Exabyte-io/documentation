# Jobs Viewer Interface

!!!note "Note: restricted applicability"
    The Jobs Viewer is only relevant in the context of **Finished Jobs**. 

In order to inspect the contents of a finished Job, the user can [open it](/entities-general/actions/open-edit.md) from [Jobs Explorer](explorer.md). This action opens the Job under the corresponding Viewer. 

The image below shows how the Viewer contains two extra highlighted tabs, in addition to the three main tabs of [Designer](/jobs-designer/overview.md). They are labelled "Results" and "Files", and are reviewed in turn.

![Extra Jobs Viewer](/images/extra-jobs-viewer.png "Extra Jobs Viewer")

The name of the Job and that of the containing [Project](../projects.md) is also indicated at the top-left corner of the page, as shown above.

# Adjustments Not Allowed

The first key difference of Jobs Viewer compared to [Designer](/jobs-designer/overview.md) is the impossibility to make **any** kind of adjustments to either the [Materials](/jobs-designer/materials-tab.md), [Workflow](/jobs-designer/workflow-tab.md) or [Compute](/jobs-designer/compute-tab.md) settings contained in their respective tabs. The user might still be able to change manually such settings, but they cannot then be saved to the Job entry being inspected.

The only change which can be made to the Job under Viewer is the insertion of descriptive [metadata](/entities-general/data.md#metadata), under the corresponding button <i class="zmdi zmdi-info-outline zmdi-hc-border"></i> at the top-right corner of the interface.

# Results Tab

This tab displays the results of the job's computational tasks. They are presented in a user-friendly way, including graphics when applicable. 

The results for each computational [unit](/workflow-designer/unit-editor.md) contained across the [workflow](/workflow-designer/general-overview.md) operations of the Job are displayed in separate **panels**. They are named according to the format convention "Subworkflow Name - Unit Name". The name of the [application](/applications/overview.md) implemented in the current unit is also shown directly below the name of the corresponding panel. The option to collapse or expand a panel is offered at its top-right corner.

The panels contain the results for the computation of the [materials properties]((/materials/properties.md)) that were selected at the moment of the [creation of the subworkflow](/workflow-designer/subworkflow-editor/detailed-view.md).

# Example of Results
 
The images shown in this section correspond to the results of a standard electronic bandstructure calculation on a material sample consisting in the semiconductor "Aluminium Phosphide" (AlP), performed with the [VASP code](/applications/vasp.md). Other types of workflows might present some variations from the results presented herein, but the layout of such results remains similar for most calculations.

## Volume Relaxation

![1 jobs results](/images/1_jobs_results.png "1 jobs results")

This bandstructure workflow starts with an initial structural volume [relaxation](/workflows/addons/structural-relaxation.md). The end results of this first calculation are shown in the above panel image, and consist in the following physical properties, expressed in their corresponding units.

| Name    |  Icon      | Description | 
| :-------- |:----------- |:----------- |
| Total energy (eV) | <i class="zmdi zmdi-battery-flash"></i> | The internal potential energy of the crystal structure | 
| Pressure (kbar) | <i class="zmdi zmdi-square-down"></i> | The average pressure of the sample, rounded to the nearest integer | 
| Total force (eV/angstroms) | <i class="zmdi zmdi-arrows"></i> | The net sum of the inter-atomic forces | 
| Atomic forces (eV/angstroms) | N/A | The inter-atomic forces |
| Stress tensor (kbar) | N/A | The internal stress tensor of the material |
| Total energy contributions (eV) | N/A | Different contributions to the internal energy of the sample, such as the Ewald, Hartree and Exchange-correlation components |

Judging from the negligible values of both the inter-atomic forces and internal stress tensor of the material, we conclude that the relaxation has been effective in this case.

## Materials Viewer

![2 jobs results](/images/2_jobs_results.png "2 jobs results")

The material structure under consideration is also exhibited here for reference purposes, under the [Materials Viewer](/materials/ui/viewer.md) interface. 

## Fermi Energy

![3 jobs results](/images/3_jobs_results.png "3 jobs results")

Following the completion of the Relaxation Subworkflow, the bandstructure calculation Subworkflow now begins. It starts with a self-consistent field energy calculation, from which the Fermi energy is estimated.

## Bandstructure

![4 jobs results](/images/4_jobs_results.png "4 jobs results")

The main electronic bandstructure calculation is then performed. The results are portrayed in the form of a dispersion curve covering the [desired path](/workflow-designer/subworkflow-editor/important-settings.md) in the reciprocal space of the Brillouin Zone, with its corresponding Greek letter labels for special symmetry points. The energy vertical axis is scaled relative to the Fermi energy of the material (red dashed line), marking the highest occupied energy level.

The possibility to print or download the dispersion graph in different image formats is offered, under the button labelled with three horizontal bars at the top-right corner of the panel shown above.

### Band gap section

Numerical data about the size of the energy band-gap of the semiconductor is also displayed below the graph, in the "Band gap" section. This information is available for both the direct band-gap at the Gamma origin point, and for the indirect band-gap between the indicated valence and conduction k-points.

### Eigenvalues section

Finally, the list of energy eigenvalue solutions corresponding to each k-point eigenvector in the reciprocal path under investigation can be inspected by expanding the "Eigenvalues" section, using the three-dotted button at the bottom of the panel. Information about the weight, net electron spin, and electron occupation numbers for each solution is also included here.

## Density of States

![5 jobs results](/images/5_jobs_results.png "5 jobs results")

A second graph displaying the final results for the computed electronic density of states [[1](#links)] is also presented. The possibility to print or download the graph in different image formats is again offered under the top-right button.

In this graph, the total density of states is marked by the black line. Individual contributions are labelled with different colors, as explained in the legend below the graph. The Fermi level is again set by the red dashed line.

## Final Check

![6 jobs results](/images/6_jobs_results.png "6 jobs results")

A final check on the bandstructure is executed in the end, and the results are displayed in a similar format to the previous results (except for the lack of the dispersion plot). Results may differ from previously computed quantities due to possible differences in the choice of input parameters for the calculation.

# Files Tab

The additional "Files" tab under Jobs Viewer contains a list of all the files involved as part of the Job's computational tasks, both of input and output nature. This list is presented under the conventional [Explorer Interface](/entities-general/ui/explorer.md). The files specific to each computing unit in the workflow are grouped together in different [Sets](/entities-general/sets.md), under the same name as the unit.

## Properties and Actions

This items list provides information about the Cloud provider under which the Job was executed, and about the size and modification date of each listed file. 

The possibility to `Download` <i class="zmdi zmdi-download zmdi-hc-border"></i> each file is offered under its corresponding [actions drop-down](/entities-general/ui/explorer.md#actions-dropdown).

## Example Appearance

An example of appearance of this Files tab is portrayed below, for the same bandstructure run performed with [VASP](/applications/vasp.md) considered in previous sections. The user is referred to the code-specific documentation for an explanation of the contents of the files displayed in this example.

![Files Tab](/images/files-tab.png "Files Tab")

# Links

1. [Wikipedia Density of States, Website](https://en.wikipedia.org/wiki/Density_of_states)

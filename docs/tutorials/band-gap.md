<!-- TODO by MH -->

The [kpoint convergence tutorial](kpt-convergence) shows a calculation of the band gap as part of the calculation of the total energy.  Please refer to that tutorial for the band gap in the results section.

The relevant part of the results of that tutorial are shown below for Silicon:

<img data-gifffer="/images/BandGapStep1.png" />

!!! Note "DFT-LDA Band Gap error"
    Please note that this calculation will be performed using standard DFT-LDA and therefore underprediction of the band gap is to be expected.  Further modifications to the input files and settings to correctly predict the band gap are possible and will be explored in the future.

You will notice that we identify both the direct band gap and the indirect band gap.  This calculation is done during the self-consistent step of the calculation on the dense k-mesh.  As you can see the indirect band gap is significantly smaller than the smallest direct band gap.  The calculated value of 0.649 eV is significantly below the experimental band gap of Silicon of ~1.1 eV but this is expected with these types of potentials and algorithm as noted above.
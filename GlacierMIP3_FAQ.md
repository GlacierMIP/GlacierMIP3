# GlacierMIP3: Frequently Asked Questions (FAQ)

### What should I do if I want to participate in the experiments?

You should inform the [GlacierMIP core team](mailto:zharry@ethz.ch,fabien.maussion@uibk.ac.at). You will then be included in all communication regarding further information. Participants are expected to submit their model results by the given submission deadline (01 February 2022).

### Why are shuffled series of years used for the equilibration experiments instead of relying on continuously repeating a given 20-yr time period?

By relying on a shuffled series of years, possible trends within 20-yr time periods are minimized (e.g. a warming trend that is present in many of these time series). Moreover, possible unwanted effects related to a cyclic forcing are reduced.

### Why are shuffled series of years used for the equilibration experiments instead of relying on a constant forcing?

Using shuffled years instead of a constant forcing is more realistic, as in reality glaciers are subject to a forcing that experiences an interannual variability. Important information about this interannual variability is lost when forcing glaciers with a constant forcing (for example: how much does glacier length vary under a stable natural climate?).

### Why are the repeat years (‘shuffling key’) prescribed instead of allowing any random key?

The impact on the results is probably small but we prefer to standardize the experiments as much as possible for optimal comparability and thus prescribe the shuffling key.

### In my model, glaciers are not allowed to grow (or I don’t trust the results in the growing case). What should I do?

In this case, you may choose to not submit results for this particular experiment or region or glacier (not all past climate experiments may lead to the same temperature signal in each region). You can for example impose a growing threshold that your model is not allowed to reach and then stop the computation and discard that glacier / region ([see FAQ about upscaling](#faq-glacier-fail)).

### Why are not all relevant datasets (e.g. ice thickness, climate data sets used for calibration) strictly prescribed? Will this not complicate the comparison of results?

Although indeed complicating the model comparison, we allow for some flexibility to allow for more modeling groups to participate. For example, some models evolve the ice thickness and are not able to use the suggested ice thickness data set. Some participants may want to use their previously calibrated models for efficiency, and different groups use different past climate forcing data (e.g., CRU, ERA5).

<a id="faq-sim-expensive"></a>
### The simulations are computationally expensive. What can I do to reduce the computational time?

Ideally, participants should simulate the evolution of every glacier for the total time period of 2000/5000 years (depending on the region, [see Table 1 in the experimental protocol](https://github.com/GlacierMIP/GlacierMIP3/blob/main/GlacierMIP3_protocol.md#table-1)). However, if needed, participants can choose to shorten the simulations when:
- A given glacier has disappeared for more than a few years over a 20-year period. The simulation can then be stopped.
- A given criterion ('stop criterion') is met that identifies the glacier to be in equilibrium with the imposed climatic conditions. For this, we suggest to stop the simulation when the change in mass balance (calculated by dividing the volume change by the glacier area) is less than 10 mm w.e. over a period of 100 years. In any case, we strongly recommend participants to analyze the influence of the 'stop criterion' for specific model runs, e.g. by regionally comparing the outcome of the full 2000/5000 year simulations with those that rely on a 'stop criterion', and to potentially adapt the criterion where needed.

Please simulate all glaciers that your model is capable of simulating in a region (even smaller ones), as in some scenarios we expect glaciers to grow: missing these glaciers would make upscaling difficult. If absolutely necessary, you may choose to use a size threshold, in which case you may need to upscale your regional results ([see FAQ about upscaling](#faq-glacier-fail)).

<a id="faq-glacier-fail"></a>
### Some glaciers cannot be computed by my model: what should I do? 

For some reasons, some glaciers simply can’t be computed successfully: when the climate or boundary conditions are unrealistic, due to numerical errors, etc. This almost always happens. If the glacier area missed this way is negligible (< 1%), you can submit your results as is. For larger errors, we will ask you to upscale your results at the regional level the way you see fit (this is model dependent). Indeed, by experimental design, we expect all simulations to start with the same regional glacier area at year 0 (the RGI v6.0 area): if this is not the case, this may hint at problems in your simulation.

### I would like to join GlacierMIP3, but I won’t be able to perform all 80 experiments. Which experiments should I prioritize? 

If you encounter computational limitations, you may reduce the total computational time through several methods. For more information, refer to the [FAQ: “The simulations are computationally expensive. What can I do to reduce the computational expenses?](#faq-sim-expensive)”. If, after having opted for these solutions you still encounter computational limits, or if any other problems hinder you from performing all experiments, we ask you to follow the following priority list:
- GCMs: (1) ukesm1-0-ll_r1i1p1f2, (2) ipsl-cm6a-lr_r1i1p1f1, (3) mri-esm2-0_r1i1p1f1, (4) mpi-esm1-2-hr_r1i1p1f1 and (5) gfdl-esm4_r1i1p1f1
- SSPs: (1) ssp585, (2) historical, (3) ssp370 and (4) ssp126
This priority list was chosen by analyzing the climatic data at the global scale, with the goal to sample the largest spectrum of global mean temperature levels (vs. pre-industrial values). By defining a priority list, we aim to increase the overlap in the forcing products used by the various participants, allowing for a better intercomparison.

Use [github issues](https://github.com/GlacierMIP/GlacierMIP3/issues) if you'd like to make suggestions about the project or if you want us to address in this [FAQ] section

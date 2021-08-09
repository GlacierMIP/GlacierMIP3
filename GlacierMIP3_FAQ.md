# GlacierMIP3: Frequently Asked Questions (FAQ)

### What should I do if I want to participate in the experiments?

You should inform the [GlacierMIP core team](mailto:zharry@ethz.ch,fabien.maussion@uibk.ac.at) before Sept. 30, 2021, and let us know about your intention. You will then be included in all communication regarding further information. Participants are then expected to submit their model results by the given submission deadline.

### Why are shuffled series of years used for the equilibration experiments instead of relying on continuously repeating a given 20-yr time period?

By relying on a shuffled series of years, possible trends within 20-yr time periods are removed (e.g. a warming trend that is present in many of these time series). Moreover, possible unwanted effects related to a cyclic forcing are reduced.

### Why are shuffled series of years used for the equilibration experiments instead of relying on a constant forcing?

Using shuffled years instead of a constant forcing is more realistic, as in reality glaciers are subject to a forcing that experiences an interannual variability. Important information about this interannual variability is lost when forcing glaciers with a constant forcing (for example: how much does glacier length vary under a stable natural climate?).

### In my model, glaciers are not allowed to grow (or I don’t trust the results in the growing case). What should I do?

In this case, you may choose to not submit results for this particular experiment or region or glacier (not all past climate experiments may lead to the same temperature signal in each region). You can for example impose a growing threshold that your model is not allowed to reach and then stop the computation and discard that glacier / region ([see FAQ about upscaling](#faq-glacier-fail)).

<a id="faq-sim-expensive"></a>
### The simulations are computationally expensive. What can I do to reduce the computational time?

Ideally, participants should simulate the evolution of every glacier for the total time period of 2000/5000 years (depending on the region, [see Table 1 in the experimental protocol](https://github.com/GlacierMIP/GlacierMIP3/blob/main/GlacierMIP3_protocol.md#table-1)). However, if needed, participants can choose to shorten the simulations when:
- A given glacier has disappeared for >20 years. The simulation can then be stopped.
- A given criterion is met that identifies the glacier to be in equilibrium with the imposed climatic conditions. **This criterion will be clarified very soon in the experimental protocol. Please do not start your simulations yet.**

Please simulate all glaciers as your model allows in a region (even smallers ones) because in some scenarios, we expect glaciers to grow: missing these glaciers would make upscaling difficult. If absolutely necessary, you may choose to use a size threshold, in which case you may need to upscale your regional results ([see FAQ about upscaling](#faq-glacier-fail)).

<a id="faq-glacier-fail"></a>
### Some glaciers cannot be computed by my model: what should I do? 

For some reasons, some glaciers simply can’t be computed successfully: when the climate or boundary conditions are unrealistic, due to numerical errors, etc. This almost always happens. If the glacier area missed this way is negligible (< 1%), you can submit your results as is. For larger errors, we will ask you to upscale your results at the regional level the way you see fit (this is model dependent). Indeed, by experimental design, we expect all simulations to start with the same regional glacier area at year 0 (the RGI area): if this is not the case, this hints at problems in your simulation.


### I would like to join GlacierMIP3, but I won’t be able to perform all 80 experiments. Which experiments should I prioritize? 

If you encounter computational limitations, you may reduce the total computational time through several methods. For more information, refer to the [FAQ: “The simulations are computationally expensive. What can I do to reduce the computational expenses?](#faq-sim-expensive)”. If, after having opted for these solutions you still encounter computational limits, or if any other problems hinder you from performing all experiments, we ask you to [contact the GlacierMIP3 core team](mailto:zharry@ethz.ch,fabien.maussion@uibk.ac.at).

### Why are the repeat years (‘shuffling key’) imposed? Will the impact on the results not be limited as long as the year selection is randomized?

It is indeed true that the effect of shuffling the years in a different order is likely to be very small to almost nonexistent. However, while preparing the experimental protocol for GlacierMIP3, we found out that it was not straightforward to determine whether every year should be 'picked' at least once every 20 years (length of reference time period for every experiment), or whether this could be totally random (i.e. possibility to have a single year occuring more than once in 20-year time sequence). We decided to go for the former option (i.e. a single year cannot be 'picked' more than once every 20 years), and to avoid any possible confusion, we opted to impose this 'shuffling key' (thereby also limiting the effect of the 'order of the picking', even if very small).

### Why are reference datasets (e.g. for ice thickness and for past climatology) not imposed? Will this not complicate the comparison of results?

Imposing the datasets to be used does indeed allow for a more straightforward comparison of the model output. However, imposing certain datasets to the participants would likely be a limiting factor for some groups to participate, as this would result in (a lot of) additional work (e.g. to recalibrate the model to new ice thickness or climate dataset). The present 'open' formulation, where we leave this up to the participant to decide, will indeed have the disadvantage that a direct comparison between the models is less straightforward. However, the 'open' approach has the advantage that groups can use their (calibrated) models 'as is' (e.g. as used in GlacierMIP2), which will likely save a lot of time and efforts for the participants (e.g. for the past climate forcing, some groups typically use CRU, others ERA5,..etc).


Use [github issues](https://github.com/GlacierMIP/GlacierMIP3/issues) if you'd like to make suggestions about the project or if you want us to address in this [FAQ] section

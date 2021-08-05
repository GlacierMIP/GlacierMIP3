# GlacierMIP3: Frequently Asked Questions (FAQ)

## I am interested in joining GlacierMIP, should I inform the core team?

Yes! It is of large importance for the core team to know who will join the experiments. This will allow us to inform you about the progress of the simulations and keep you updated in case parts of the protocol are reformulated (e.g. for clarification). Therefore, if you intend to join GlacierMIP3, please let us know as soon as possible. Even if you are unsure about joining (potential interest), or if you’d simply like to be updated about the progress of the experiments, [please let us know](mailto:zharry@ethz.ch,fabien.maussion@uibk.ac.at) as soon as possible.

## Why are shuffled series of years used for the equilibration experiments instead of relying on continuously repeating a given 20-yr time period?

By relying on a shuffled series of years, possible trends within 20-yr time periods are removed (e.g. a warming trend that is present in many of these time series). Moreover, possible unwanted effects related to a cyclic forcing are reduced.

<a id="faq-shuffled-not-cte"></a>
## Why are shuffled series of years used for the equilibration experiments instead of relying on a constant forcing?

Using shuffled years instead of a constant forcing is generally more realistic, as in reality glaciers are subject to a forcing that experiences an interannual variability. Information about this interannual variability is lost when forcing glaciers with a constant forcing. Moreover, utilizing a series of shuffled years is more straightforward (and computationally less demanding), as forcing the model with a constant mass balance forcing, requires the mass balance to be computed at a regular basis (typically annually) for the entire 20-yr time period, after which a mean value can be taken (this is required, as the glacier geometry is continuously evolving). 

Also note that an alternative approach (perhaps more intuitive at first sight), which relies on computing the mean climatology of a given period and then computing the mass balance from this climatology, is not possible. Indeed, the average of the model chain “Forcing data -> Impact model” is NOT equivalent to the model chain “Average(Forcing data) -> Impact model”. If you are curious about why, visit [this blog post](https://oggm.org/2021/08/05/mean-forcing/).

## In my model, glaciers are not allowed to grow (or I don’t trust the results in the growing case). What should I do?

In this case, you may choose to not submit results for this particular experiment or region or glacier (not all past climate experiments may lead to the same temperature signal in each region). You can for example impose a growing threshold that your model is not allowed to reach and then stop the computation and discard that glacier / region ([see FAQ below about upscaling](#faq-sim-expensive)).

<a id="faq-sim-expensive"></a>
## The simulations are computationally expensive. What can I do to reduce the computational time?   

Ideally, participants should simulate the evolution of every glacier for the total time period of 2000/5000 years (depending on the region, [see Table 1 in the experimental protocol](https://github.com/GlacierMIP/GlacierMIP3/blob/main/GlacierMIP3_protocol.md#table-1)). However, if needed, participants can choose to shorten the simulations when:
- A given glacier has disappeared for >20 years. The simulation can then be stopped.
- A given criterion is met that identifies the glacier to be in equilibrium with the imposed climatic conditions. A full equilibrium will never be reached (as shuffled time series are used), but by considering e.g. the evolution change over a longer time period, one can possibly identify a point at which the glacier is very close to equilibrium. Note that the experimental protocol does not provide a universal criterion to be used for when glaciers are in steady state, as this depends among others on the model used and the glaciers considered. Participants are asked to provide time series of volume and area at the regional level for the entire 2000/5000 yr time series: i.e. also when (a part of the) glacier simulations are stopped earlier.

To reduce computational efforts, we do not recommend making a glacier selection (e.g. larger than a chosen size threshold) because in some scenarios, we expect glaciers to grow: missing these glaciers would make upscaling difficult. If absolutely necessary, you may choose to use a size threshold, in which case you may need to upscale your regional results ([see FAQ below](#faq-glacier-fail)).

Also, forcing with the model with mean mass balance conditions or a mean climatology is not advisable, as addressed in the response to the [FAQ: “Why are shuffled series of years used for the equilibration experiments instead of relying on a constant forcing?”](#faq-shuffled-not-cte)

<a id="faq-glacier-fail"></a>
## Some glaciers cannot be computed by my model: what should I do? 

For some reasons, some glaciers simply can’t be computed successfully: when the climate or boundary conditions are unrealistic, due to numerical errors, etc. This almost always happens. If the glacier area missed this way is negligible (< 1%), you can submit your results as is. For larger errors, we will ask you to upscale your results at the regional level the way you see fit (this is model dependent). Indeed, by experimental design, we expect all simulations to start with the same regional glacier area at year 0 (the RGI area): if this is not the case, this hints at problems in your simulation.


## I would like to join GlacierMIP3, but I won’t be able to perform all 80 experiments. Which experiments should I prioritize? 

If you encounter computational limitations, you may reduce the total computational time through several methods. For more information, refer to the [FAQ: “The simulations are computationally expensive. What can I do to reduce the computational expenses?](#faq-sim-expensive)”. If, after having opted for these solutions you still encounter computational limits, or if any other problems hinder you from performing all experiments, we ask you to [contact the GlacierMIP3 core team](mailto:zharry@ethz.ch,fabien.maussion@uibk.ac.at). We will then inform you about which experiments to prioritize.


## Why are the repeat years (‘shuffling key’) imposed? Will the impact on the results not be limited as long as the year selection is randomized?

It is indeed true that the effect of shuffling the years in a different order is likely to be very small to almost nonexistent. However, while preparing the experimental protocol for GlacierMIP3, we found out that it was not straightforward to determine whether every year should be 'picked' at least once every 20 years (length of reference time period for every experiment), or whether this could be totally random (i.e. possibility to have a single year occuring more than once in 20-year time sequence). We decided to go for the former option (i.e. a single year cannot be 'picked' more than once every 20 years), and to avoid any possible confusion, we opted to impose this 'shuffling key' (thereby also limiting the effect of the 'order of the picking', even if very small).

## Why are reference datasets (e.g. for ice thickness and for past climatology) not imposed? Will this not complicate the comparison of results?

Imposing the datasets to be used does indeed allow for a more straightforward comparison of the model output. However, ‘forcing’ the participants to use a given datasets would likely be a limiting factor for some groups to participate, as this would result in (a lot of) additional work (e.g. to recalibrate the model to new ice thickness or climate dataset). The present 'open' formulation, where we leave this up to the participant to decide, will indeed have the disadvantage that a direct comparison between the models is less straightforward. However, the 'open' approach has the advantage that groups can use their (calibrated) models 'as is' (e.g. as used in GlacierMIP2), which will likely save a lot of time and efforts for the participants (e.g. for the past climate forcing, some groups typically use CRU, others ERA5,..etc).


Use [github issues](https://github.com/GlacierMIP/GlacierMIP3/issues) if you'd like to make suggestions about the project or if you want us to address in this [FAQ] section

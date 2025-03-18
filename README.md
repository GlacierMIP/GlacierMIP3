# GlacierMIP3

[GlacierMIP](https://climate-cryosphere.org/glaciermip/) is a framework for a coordinated intercomparison of global-scale glacier mass change models to foster model improvements and reduce uncertainties in global glacier projections. It is running as a 'Targeted Activity' under the auspices of the Climate and Cryosphere Project [CliC](https://www.climate-cryosphere.org/), a core project of the World Climate Research Programme (WCRP).

GlacierMIP3 and its experimental design and protocol were developed in 2020/2021 by Harry Zekollari (chair), Fabien Maussion, Lilian Schuster, Regine Hock and Ben Marzeion. 

This repository holds the description of the experimental protocol and other documents relevant for the third phase of GlacierMIP launched in 2021: **GlacierMIP3: Equilibration of glaciers under different climate states (GlacierMIP3 - Equi)** together with the code for the analysis of the resulting community estimate paper. 

This repository is archived under Zenodo, but the README and code is best readable directly at GitHub: [https://github.com/GlacierMIP/GlacierMIP3](https://github.com/GlacierMIP/GlacierMIP3) 

All instructions of how to perform the experiments can be found in the [GlacierMIP3 protocol](GlacierMIP3_protocol.md). Everything that was necessary for the GMIP3 submission is in the folder [0_experimental_protocol_files](0_experimental_protocol_files). The submission file names and format conventions are described in [netcdf file format notebook](0_experimental_protocol_files/netcdf_templates/netcdf_file_format.ipynb) with some sample files available in the [netcdf_templates](0_experimental_protocol_files/netcdf_templates) folder. A list of [Frequently Asked Questions (FAQ)](GlacierMIP3_FAQ.md) on the GlacierMIP3 submission is also available. If you have other questions, or if you'd like to make suggestions about the project, use 
[github issues](https://github.com/GlacierMIP/GlacierMIP3/issues).

This community estimate manuscript resulted out of GlacierMIP3:

> Zekollari\*, H., Schuster\*, L., Maussion, F., Hock, R., Marzeion, B., Rounce, D. R., Compagno, L., Fujita, K., Huss, M., James, M., Kraaijenbrink, P. D. A., Lipscomb, W. H., Minallah, S., Oberrauch, M., Van Tricht, L., Champollion, N., Edwards, T., Farinotti, D., Immerzeel, W., Leguy, G., Sakai, A. (under review): Glacier preservation doubled by limiting warming to 1.5°C. Preprint available at [https://doi.org/10.31223/X51T5W](https://doi.org/10.31223/X51T5W), 2024.
>
> \* *These authors contributed equally.*


Code for the community estimate paper above is in the following folders with these respective READMEs:
- [0_pre_post_processing](0_pre_post_processing) documented in [README_0_pre_post_processing.md](README_0_pre_post_processing.md)
- [A_community_estimate_paper_analysis](A_community_estimate_paper_analysis) documented in [README_A_community_estimate_paper_analysis.md](README_A_community_estimate_paper_analysis.md)
   - The main figures are currently only available in the manuscript. However, figure variants (figure simplifications of the Fig. 3 worldmap that are useful for presentations and outreach), a variant of Fig. 2 showing the entire y-range, a variant of Supplementary Fig. S6 for 500 instead of 100 simulation years and variants of Supplementary Fig. S12 are included in this [folder](A_community_estimate_paper_analysis/figures/supplements/only_github_supplements).


The regional GlacierMIP3 glacier projections for the different glacier models and experiments are available and documented via the [Zenodo dataset (Schuster, Zekollari et al., 2024)](https://doi.org/10.5281/zenodo.14045268). In addition, postprocessed data for the community estimate manuscript are included there. The data documentation is also available in [README_data.md](README_data.md).


When using the GlacierMIP3 dataset, please cite both the [Zenodo dataset](https://doi.org/10.5281/zenodo.14045268) and the [preprint](https://doi.org/10.31223/X51T5W) above. Note that we are working currently on potentially another study to analyse more the glacier model differences. 


For data and technical questions contact:
- [Harry Zekollari](mailto:zharry@ethz.ch)
- [Lilian Schuster](mailto:Lilian.Schuster@uibk.ac.at)
- [Fabien Maussion](mailto:fabien.maussion@bristol.ac.uk)

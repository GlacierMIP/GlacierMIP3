# README for the Glacier Model Intercomparison Project 3 Data Publication

This document provides data documentation for the Glacier Model Intercomparison Project 3 (GlacierMIP3), which focused on global glacier mass change equilibration experiments.

[GlacierMIP](https://www.climate-cryosphere.org/mips/glaciermip/about-glaciermip) is a framework for a coordinated intercomparison of global-scale glacier mass change models to foster model improvements and reduce uncertainties in global glacier projections. It is running as a 'Targeted Activity' under the auspices of the Climate and Cryosphere Project [CliC](https://www.climate-cryosphere.org/), a core project of the World Climate Research Programme (WCRP).

For detailed information about the GlacierMIP3 experimental design, please refer to the GlacierMIP3 protocol.

The dataset includes the regional per-glacier-model simulations as submitted by the modeling groups, encapsulated in the main file `GMIP3_reg_glacier_model_data/glacierMIP3_Feb12_2024_models_all_rgi_regions_sum.nc`. Additionally, it features post-processed and aggregated data derived from GlacierMIP3, or in combination with other studies, which is used for the analyses and visualisations presented in the manuscript.

> Zekollari*, H., Schuster*, L., Maussion, F., Hock, R., Marzeion, B., and the GlacierMIP3 consortium ...TODO-add all names (submitted). Current climate policies will affect multi-century global glacier change. (link to preprint will be added once available), 2024.
*These authors contributed equally

When using this dataset, please cite both the Zenodo dataset and the submitted study above. Note that we are working currently on another study to analyse more the glacier model differences. 

To assist potential data users, we have included a jupyter notebook (`gmip3_data_example_use_cases.ipynb`) that guides you through some simple use cases. We may adapt the data structure and improve the documentation during the review phase. If you have any questions or suggestions, please [contact us](mailto:lilian.schuster@uibk.ac.at,harry.zekollari@vub.be).


Please note that the data described is only available through the published Zenodo dataset (link will be added). The code used to generate this data and to conduct the analyses for the manuscript mentioned above is available at [https://github.com/GlacierMIP/GlacierMIP3](https://github.com/GlacierMIP/GlacierMIP3). We have retained this README_data also in the GitHub repository for reference. 

Below you will find the documentation for the different individual datasets.


## GMIP3_reg_glacier_model_data/
Here the regionally aggregated glacier model projections (volume and area) are given in different postprocessing steps. 

All files within the `GMIP3_reg_glacier_model_data` folder are netCDF files with data for volume in m³ (`volume_m3`) and area in m² (`area_m2`) which have the following dimensions:

| Variable          | Dimension | Description                                                                                                                                                                                                                                                 |
|-------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `model_author`    | 8 (10)        | One of the eight model authors from the list: ['PyGEM-OGGM_v13', 'GloGEMflow', 'GloGEMflow3D', 'OGGM_v16', 'GLIMB', 'Kraaijenbrink', 'GO', 'CISM2']. In the non-final postprocessed files, we included two OGGM variants which we might only use for a more technical model intercomparison study (more in `gmip3_data_example_use_cases.ipynb`)                                                                                                   |
| `simulation_year` | 5001      | Simulation year from 0 to 5000 (estimates may be NaNs after 2000)                                                                                                                             |
| `gcm`             | 5         | ISIMIP3b climate model: ['gfdl-esm4', 'ipsl-cm6a-lr', 'mpi-esm1-2-hr', 'mri-esm2-0', 'ukesm1-0-ll'] (corresponding warming level available in climate_input_data/).                                                                             |
| `period_scenario` | 16        | One of the 16 climate scenarios (combining time periods and scenarios): ['1851-1870_hist', '1901-1920_hist', '1951-1970_hist', '1995-2014_hist', '2021-2040_ssp126', '2021-2040_ssp370', '2021-2040_ssp585', '2041-2060_ssp126', '2041-2060_ssp370', '2041-2060_ssp585', '2061-2080_ssp126', '2061-2080_ssp370', '2061-2080_ssp585', '2081-2100_ssp126', '2081-2100_ssp370', '2081-2100_ssp585'] |
| `rgi_reg`         | 19        | One of the 19 RGI6 regions, from '01' to '19'.                                                                                                                                                                                                           |

**The following different regional glacier model projections are available (ordered from the least to the most postprocessed):**
`GMIP3_reg_glacier_model_data/glacierMIP3_Feb12_2024_models_all_rgi_regions_sum.nc`
- unprocessed dataset with the "raw" regional files as submitted by the glacier model groups. Not used directly in any of the analysis, but of most interest for model comparison analyses
- > in the first manuscript, this file was only used to create the next dataset.

`GMIP3_reg_glacier_model_data/glacierMIP3_Feb12_2024_models_all_rgi_regions_sum_scaled.nc`
- same as previous file but each climate scenario and model time series (experiment) but the volume is scaled to perfectly match the Farinotti et al. (2019) multi-model ice thickness estimate at the beginning and the area is scaled to match the RGI6 area (in many cases this is already true, except for some very cold experiments, where glaciers may fail for some regions)
- > only used to estimate the amount of years until steady state is reached (in `A_community_estimate_paper_analysis/2b_find_equilibrium_steady_state_yr.ipynb` for Supplementary Fig. S8)

`GMIP3_reg_glacier_model_data/glacierMIP3_Feb12_2024_models_all_rgi_regions_sum_scaled_extended_repeat_last_101yrs.nc`
- same as previous file but where necessary, the experiments are extended from the year 2000 to the year 5000
- > used in some notebooks for the steady-state estimates (note that the steady-state estimates are the same as in the below shifted dataset)
       
`GMIP3_reg_glacier_model_data/all_shifted_glacierMIP3_Feb12_2024_models_all_rgi_regions_sum_scaled_extended_repeat_last_101yrs_via_5yravg.nc`
- same as previous file but the timeseries were shifted so that the initial state of the new timeseries match better the glacier mass estimate of the year 2020  
- dimension changed to  (from -50 to 5000)
- `area_m2` removed here, as not analysed in the first GlacierMIP3 study
- here `simulation_year` is the initial simulation year as given by the unshifted version (and dimension changed to `year_after_2020`, see below)
- additional variables:
   - `year_after_2020`  : new dimension which describes now the "year" after having reached the 2020 state - unit: year
   - `volume_rel_2020_%` : scaled and then shifted glacier volume/mass relative to 2020 - unit: %
   - `yrs_w_most_similar_state_to_2020`: year with a glacier volume/mass similar to the estimated state in 2020 - unit: year
- > used for the LOWESS fits later, but also to estimate the response timescales, and also directly for e.g. Fig. 1,2; Supplementary Fig. S5, S7


## climate_input_data/

Warming above pre-industrial for the different experiments (either on a global mean average or regional). 

| Column Name                               | Description                                                                                             |
|-------------------------------------------|---------------------------------------------------------------------------------------------------------|
| `gcm`                                     | ISIMIP3b climate model                                                                                 |
| `period_scenario`                         | One of the 16 climate scenarios (combining time periods and scenarios, e.g. `2041-2060_ssp126`)       |
| `region`                                  | Aggregated region over which the warming was estimated. Global mean average (`global`),                |
|                                           | global glacier-area weighted mean (`global_glacier`), regional glacier-area weighted mean (e.g. `RGI11_glacier`)  |
|                                           | `temp_ch_ipcc_ar6_isimip3b` does not have this column as all entries are `global`                     |
| `temp_ch_ipcc`                           | Warming above pre-industrial (1850-1900) using the IPCC AR6 definition (i.e. assume +0.69°C between 1850 and 1986-2005 - unit: °C                                                                    |

**The following different csv files are available:** 
`climate_input_data/temp_ch_ipcc_ar6_isimip3b.csv`: only the global mean average warming
- > used in most figures and analysis

`climate_input_data/temp_ch_ipcc_ar6_isimip3b_glacier_regionally.csv`: all regions
- Attention: here we assume regionally equally +0.69°C of warming between 1850 and 1986 to 2005. For the warming ratio computation that is shown in e.g. Fig. 2 or Fig. 4, we substract the 0.69°C again to instead just show the regional warming ratio to the actual regional 1986 to 2005 estimates. 
- > used e.g. for Supplementary Fig. 1, Fig. 2, 


## LOWESS fits
The different relative glacier mass changes were LOWESS fitted with respective temperature changes of the 80 climate scenarios. The LOWESS fit results, 
here given in steps of 0.05°C, are given in the `lowess_fit_rel_2020*.csv` files for different variants

All `lowess_fit_rel_2020*.csv` files have the following columns:

| Variable         | Description                                                                                                                                                                                          |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `temp_ch`        | Warming level above pre-industrial in °C.                                                                                                                                                         |
| `0.5`, `0.17`, `0.83` (and others) | Quantiles of fitted remaining glacier mass in % relative to 2020 (21- or 101-year rolling average) for the respective region and warming level.                                                  |
| `region`         | The 19 RGI6 regions ('01' to '19') or all regions together ('All'), which corresponds to the global estimates.                                                                                     |
| `year`           | 100, 500, or 5000 - Year of analysis.                                                                                                                                                             |
| `frac`           | Chosen frac parameter (hyperparameter of how much data points are applied for the local regression, see MOEPY package documentation).                                                                 |
|                  | Note: frac is only valid for the median values in case of `region=='All'`.                                                                                                                    |
| `it`             | Number of iterations for the lowess fit (see MOEPY package).                                                                                                                                     |
| `N`              | Repetitions (see MOEPY package).                                                                                                                                                             |


**The following different LOWESS fitted data files are available:** 
`lowess_fit_rel_2020_101yr_avg_steady_state_Feb12_2024.csv`
- fit uses relative remaining mass at steady-state (101-year rolling average of the last simulation years, either after 5000 or 2000 years) together with global mean warming above preindustrial
- year is here 5000 (although for some regions simulations were only done for 2000 years)
- > used for Fig. 1-4, Extended Data Fig. 1-XX, Extended Table 1, and several supplementary figures XX

`lowess_fit_rel_2020_21yr_avg_after{YEAR}yr_Feb12_2024.csv` with YEAR=100 or YEAR=500
- similar to `lowess_fit_rel_2020_101yr_avg_steady_state_Feb12_2024.csv`, but for the estimates after 100 or 500 simulation years. Here the quantiles were LOWESS-fitted with 21-year centered rolling average glacier mass estimates
- year is here 100 or 500
- > used for Fig. 3, Supplementary Fig. S3

`lowess_fit_rel_2020_101yr_avg_steady_state_Feb12_2024_only_global_models.csv`
- similar to `lowess_fit_rel_2020_101yr_avg_steady_state_Feb12_2024.csv`, but using for the LOWESS fit only globally available glacier models
- year is here 5000
> used for e.g. Supplementary Fig. S7

`lowess_fit_rel_2020_101yr_avg_steady_state_Feb12_2024_rel_regional_glacier_temp_ch.csv`
- similar to `lowess_fit_rel_2020_101yr_avg_steady_state_Feb12_2024.csv`, but using instead regional glacier-area weighted warming
> used for e.g. Extended Data Fig. 2

`lowess_fit_rel_2020_101yr_avg_steady_state_Feb12_2024_per_glac_model.csv`
- similar to `lowess_fit_rel_2020_101yr_avg_steady_state_Feb12_2024.csv`, but doing a LOWESS fit for every glacier model individually.
- note that the fit performs not  well for some glacier models below 1.5°C, and should thus not be used in that range. However, to just estimate the spread in the committed ice loss sensitivity between 1.5 and 3.0°C, it is ok
- > used to estimate the spread/uncertainties in the committed ice loss sensitivity (e.g. shown in Extended Data Table 1, Supplementary Fig. S2)


 
## other files
**response timescale dataset csv-file**: `resp_time_shifted_X%_threshold25%_for_deltaT_rgi_reg_roll_volume_21yravg.csv` with the following columns
| Column Name                          | Description                                                                 |
|--------------------------------------|-----------------------------------------------------------------------------|
| `rgi_reg`                            | RGI region (e.g. 'RGI11') or global ('All')                                   |
| `model_author`                       | Model name (e.g. 'GLIMB')                                                   |
| `temp_ch_ipcc`                       | Global warming above pre-industrial for that experiment - unit: °C           |
| `gcm_period_scenario`                | One of the 80 experiments, e.g. in the format: 'ipsl-cm6a-lr_2081-2100_ssp370' |
| `min_perc_change`                    | Minimum shrinkage/growing limit to estimate a "response timescale", here everywhere 25% to reduce noise from interannual variability - unit: % |
| `resp_time_-50%`                     | Response timescale for -50% of the total changes to occur (here only if changes are losses) - unit: years |
| `resp_time_-80%`                     | Response timescale for -80% of the total changes to occur (here only if changes are losses) - unit: years |
| `resp_time_-90%`                     | Response timescale for -90% of the total changes to occur (here only if changes are losses) - unit: years |
| `diff_resp_time_-50%`                | Difference of that model's response time scale to the median glacier model response time scale) - unit: years |
| `diff_resp_time_-80%`                | Difference of that model's response time scale to the median glacier model response time scale) - unit: years |
| `diff_resp_time_-90%`                | Difference of that model's response time scale to the median glacier model response time scale) - unit: years |

> this dataset is used e.g. for the following figures or tables: Extended Data Fig. 6, Supplementary Fig. S6
     


**aggregated regional characteristics summary csv-file**: `3_shift_summary_region_characteristics.csv` with the following columns
| Column Name                                          | Description                                                                 |
|------------------------------------------------------|-----------------------------------------------------------------------------|
| `rgi_reg`, `region`                                  | Regions e.g. ('11'), all regions together described as `All` in `rgi_reg` and as `global` in `region` |
| *Climate Indices (data from ISIMIP3a (GSWP3-W5E5)):* |                                                                             |
| `temp_ch_avg_2000-2019_vs_1901-1920`                | ΔTemp 2000-2019 - 1901-1920 (reg-aw) - unit: °C                             |
| `temp_avg_2000-2019`                                 | Temp 2000-2019 (reg-aw) - unit: °C                                          |
| `prcp_avg_2000-2019`                                 | Prcp 2000-2019 (reg-aw) - unit: kg m-2 s-1                                  |
| `continentality_index_avg_2000-2019`                 | Continentality index 2000-2019 (temp difference between coldest/warmest     |
|                                                      | month same year, reg-aw) - unit: °C                                        |
| `median_reg_vs_glob_ch`                              | Ratio reg vs global ΔTemp to pre-industrial (median, reg-aw) - no unit      |
| `median_reg_vs_glob_temp_ch_1.5_3.0`                 | Same as `median_reg_vs_glob_ch` but only with experiments between 1.5°C    |
|                                                      | and 3.0°C - no unit                                                         |
| `median_reg_vs_glob_ch_ref_1986-2005`                | Ratio reg vs global ΔTemp to 1986-2005 (median, reg-aw) - no unit           |
| `median_reg_vs_glob_temp_ch_1.5_3.0_ref_1986-2005`   | Same as `median_reg_vs_glob_ch_ref_1986-2005` but only with experiments     |
|                                                      | between 1.5°C and 3.0°C - no unit                                           |
| `slope_fit_reg_vs_glob_ch`                           | Fitted linear fit slope regional vs global temp change (aw) - no unit       |
| *Glacier topography (data from RGI6):*               |                                                                             |
| `slope_weighted_area_avg`                            | Glacier surface slope (reg-aw) - unit: °                                    |
| `lat_absolute_weighted_area_avg`                     | Latitude (absolute, reg-aw) - unit: °                                       |
| `lat_weighted_area_avg`                              | Latitude (reg-aw) - unit: °                                                 |
| `marine_term_ratio_hundredlargest_glac`              | Ratio marine-terminating (100 largest glaciers) - no unit                   |
| `mean_vol_ten_largest_glac`                          | Mean volume (10 largest glaciers by area) - unit: km3                       |
| `elev_diff_area_weighted`                            | Elevation range (reg-aw) - unit: m                                          |
| `ice_cap_ratio_hundredlargest_glac`                  | Ratio ice caps (100 largest glaciers) - no unit                             |
| `max_elev_area_weighted`                             | Maximum elevation (reg-aw) - unit: m                                        |
| `min_elev_area_weighted`                             | Minimum elevation (reg-aw) - unit: m                                        |
| `mean_area_ten_largest_glac`                         | Mean area (10 largest glaciers by area) - unit: km2                         |
| *Observed glacier changes and states in past (data from Hugonnet et al. 2021 & Farinotti et al. 2019):* |  |
| `geodetic_obs_area_weighted`                         | Observed geodetic MB (2000-2019, reg) from Hugonnet et al. (2021) - unit: m w.e. year-1 |
| `dvoldt_m3_hugonnet`                                 | Observed ΔVolumeΔt (2000-2019, reg) from Hugonnet et al. (2021) - unit: m3 per year |
| `20yr_regional_dvol_dt_2000_2019_vs_2000_vol_%`      | Observed ΔMassΔt (2000-2019 relative to 2000 Mass, reg) - unit: %           |
| `regional_volume_m3_itmix`                           | Glacier volume as given by Farinotti et al. (2019) (reg) - unit: m3         |
| `regional_volume_m3_2020_via_5yravg`                 | Glacier volume in 2020 (est. from Farinotti et al. 2019 & Hugonnet et al.,  |
|                                                      | 2021) (reg) - unit: m3                                                      |
| `regional_volume_m3_itmix_vs_2020`                   | Ratio of glacier volume at RGI6 inventory date vs volume in 2020 (est.     |
|                                                      | from Farinotti et al. 2019 & Hugonnet et al., 2021) (reg) - no unit       |
| `rgi_year_weighted_median`                           | RGI year (reg-aw) - unit: year                                              |
| *Glacier simulation change estimates (data from GlacierMIP3):* |                                                                    |
| `resp_time_-50%_1_5_deg`                             | Response timescale (~1.5°C, 50%, reg) - unit: years                        |
| `resp_time_-50%_3_0_deg`                             | Response timescale (~3.0°C, 50%, reg) - unit: years                        |
| `resp_time_-80%_1_5_deg`                             | Response timescale (~1.5°C, 80%, reg) - unit: years                        |
| `resp_time_-80%_3_0_deg`                             | Response timescale (~3.0°C, 80%, reg) - unit: years                        |
| `resp_time_-50%_1_5_deg_only_global_models`          | Same as above but only considering glacier models with global simulations   |
| `resp_time_-50%_3_0_deg_only_global_models`          | Same as above                                                               |
| `resp_time_-80%_1_5_deg_only_global_models`          | Same as above                                                               |
| `resp_time_-80%_3_0_deg_only_global_models`          | Same as above                                                               |
| `ice_loss_1.2°C_%_rel_2020`                          | Committed glacier mass loss at ΔTemp=+1.2°C (rel. to 2020) - unit: %       |
| `ice_loss_slope_1.5_to_3.0_per_tenth_degC_rel_2020` | Sensitivity of committed glacier mass loss (ΔTemp=1.5 to 3.0°C) - unit : % per 0.1°C  |

*Abbreviations: “10/100 largest” refers to the 10/100 glaciers with the largest initial glacier mass at inventory date according to the estimate by Farinotti et al. 2021. ”reg-aw” refers to regionally glacier-area weighted, “reg” refers to regional, “avg” refers to average, “Temp” refers to temperature, “Prcp” refers to precipitation.*
> used for Extended Data Table 1 and 3, and for Fig. 4, Extended Data Fig. 2, Supplementary Fig. 4, and many other figures


-------
**Some additional notes**
We also use for a few supplementary figures data from other studies. Sometimes we got the data via personal communication or by aggregating raw files from published datasets. These files are shortly described in `data_from_others/README_data_from_others.md`. However, they are only available via [https://cluster.klima.uni-bremen.de/~lschuster/GlacierMIP3/data/data_from_others](https://cluster.klima.uni-bremen.de/~lschuster/GlacierMIP3/data/data_from_others). 

The per-glacier model glacier volume and area estimates are at the moment only available for the models `PyGEM-OGGM_v13` and `OGGM_v16`. If you have interest in that data, please [contact us](mailto:lilian.schuster@uibk.ac.at,harry.zekollari@vub.be). 
# 0: Preprocessing and postprocessing of climatic data, glacier model projections, and LOWESS fits with temperature changes

Note that you need the package versions as in mamba_packages_oggm_gmip3_sept20_2024.yml (pandas 2.1.3, xarray 2023.11.0, numpy 1.24.4). For some postprocessing, you also need to install oggm (e.g. v1.6.2) /progressbar2 and for the lowess fits, you need moepy (e.g. v1.1.4). That means you could do the following steps:
> mamba create --name <gmip3_env> --file <mamba_packages_oggm_gmip3_sept20_2024.yml> 
> mamba activate gmip3_env
> pip install --user --no-deps moepy oggm progressbar2

## 00: Download climate data, preprocess and extract statistics

`000_wget-isimip3b_prcp_temp.sh` 
- download script of the daily ISIMIP3b files
- if you want to repeat the download (~1TB of data), run the following bash file:
  - `bash 000_wget-isimip3b_prcp_temp.sh -H` (you need to registrate to esg and login via terminal)
  
`00a_isimip3b_postprocessing_analysis/isimip3b_postprocess_to_monthly.ipynb`
- postprocesses ISIMIP3b precipitation and temperature data:
  - merging and creating monthly means (those monthly files were used as input for most glacier models)
  - the processed monthly ISIMIP3b version 2.5 data are available under: https://cluster.klima.uni-bremen.de/~lschuster/isimip3b/ 
- produces global mean temperature change estimates for every climate scenarios (°C above pre-industrial, as defined by IPCC AR6 report)
  - **Output:** `../data/climate_input_data/temp_ch_ipcc_ar6_isimip3b.csv` 

`00b_extract_isimip3a_gswp3-w5e5_glacier_climate_change.ipynb`:
- gets past and current temperature and precipitation from ISIMIP3a GSWP3-W5E5 for the different glacier regions
- **Output:** `../data/climate_input_data/temp_prcp_past_gswp3-w5e5_glacier_regionally.csv`

`00c_extract_isimip3b_glacier_climate_change.ipynb`: 
- **Output:** `../data/climate_input_data/temp_ch_ipcc_ar6_isimip3b_glacier_regionally.csv`

## 0a-c: Postprocess (aggregate, scale, check, extend, shift) the glacier model projections of the individual glacier models
`0a_analysis_regional_model_dataset_merging_and_initial_state_comparison.ipynb`
- merges all regional volume and area glacier runs of the different models into two netCDF files
- these datasets also include OGGM_v153 and OGGM_VAS. These model options are not part of the first GlacierMIP3 study, but might be used for a study focusing on the glacier model differences. 
    - **Output A:** non-postprocessed aggregated file `../data/GMIP3_reg_glacier_model_data/glacierMIP3_Feb12_2024_models_all_rgi_regions_sum.nc`
        - (interesting for testing, understanding the models workflow, or specific model intercomparison)
    - **Output B:** volume/area scaling applied so that all models start at the exact same initial state (i.e., Farinotti et al. 2019 volume and RGI6 area): `../data/GMIP3_reg_glacier_model_data/glacierMIP3_Feb12_2024_models_all_rgi_regions_sum_scaled.nc`
- also plots amount of experiments per glacier model and checks initial state before having applied volume/area scaling

 
`0a1_test_for_duplicates_and_other_errors.ipynb`
- checks if there are duplicates in the data of the submitted groups (tests are running now without errors)
    
`0b_create_extended_5000yr_timeseries.ipynb`
- extends each region’s simulations to year 5000 by repeating the last 101 years and using the scaled netCDF file from the previous notebook. This extension is useful for plotting timeseries or steady-state estimates.
- **Output:** `../data/GMIP3_reg_glacier_model_data/glacierMIP3_Feb12_2024_models_all_rgi_regions_sum_scaled_extended_repeat_last_101yrs.nc`
    
`0c_correction_regional_volume_change_until_2020.ipynb`
- shifts all time series to roughly begin with a 2020 volume (by finding a simulation year near to the 2020 volume, and redefining this to be the `year_after_2020` zero state)
- creates the Hugonnet et al. 2021 / Farinotti et al. 2019 summary statistics that also includes the estimated median RGI year and the 2020 regional volume/mass:
    - saved as an intermediate output file in `../data/0_rgi_vs_2020_volume_hugonnet_estimates.csv`
- test figures created to show how much simulation years are shifted and how well the 2020 volume is matched
- creates the shifted timeseries dataset that is used later in most analysis (eight glacier models are included here, not anymore OGGM-VAS or OGGM_v153):
    - **Output:** `../data/GMIP3_reg_glacier_model_data/all_shifted_glacierMIP3_Feb12_2024_models_all_rgi_regions_sum_scaled_extended_repeat_last_101yrs_via_5yravg.nc`

## 0d-f, lowess_fits_scripts/, per_glac_model_lowess_fits_scripts/: LOWESS fits of glacier model mass vs temperature changes 

`lowess_fits_scripts/lowess_percentile_interval_fit_per_region_added_uncertainties.py` 
- you need to execute the lines of `lowess_fits_scripts/commandos_slurm.txt` which will run the python scripts to create the lowess fits with uncertainties 
- creates preliminary csv files with the lowess best frac fits: 
    - e.g.: `lowess_fits_scripts/_raw_fits/fitted_lowess_best_frac_shift_years_rel_2020_101yr_avg_period_lowess_added_quantiles_added_current12deg_5000_Feb12_2024_ipcc_ar6.csv`
- creates preliminary csv files with the exponential fit (just for comparison), here the "shifted variant":
    - e.g.: `lowess_fits_scripts/_raw_fits/fitted_lowess_best_frac_shift_years_rel_2020_101yr_avg_period_lowess_added_quantiles_added_current12deg_5000_Feb12_2024_ipcc_ar6.csv`
- creates preliminary rather complex figure variants of Fig.2 of the manuscript (figures are in `lowess_fits_scripts/_test_figs`) :
    - those are simplified later in `A_community_estimate_paper_analysis/2a_glacier_vs_climate_change_evolution.ipynb`

`per_glac_model_lowess_fits_scripts/lowess_percentile_interval_fit_per_model_per_region.py` :
- python script to create the per-glacier lowess fits (necessary to assess glacier model uncertainties of the temperature sensitivities)
          
`0d_lowess_fit_advanced_aggregation_uncertainty.ipynb`
- aggregates all different LOWESS fits to summary CSVs files. 
- **Output:** `../data/lowess_fit_rel_2020_*.csv` (more in `README_data.md`)

## 0e-f : Summarise different regional GMIP3 model estimates together with glacier region characteristic
`0e_response_timescale_estimates.ipynb`
- estimates the response timescale for every glacier model and experiment (for the shifted simulations) at volume changes of -50%, -80% and -90% and saves them
- **Output:** `../data/resp_time_shifted_X%_threshold25%_for_deltaT_rgi_reg_roll_volume_21yravg.csv` (more in `README_data.md`)

`0f_extract_regional_climatic_glacier_median_response_time_characteristics.ipynb`
-  extracts all the regional glacier/climate and some median response timescale/lowess fit characteristics (uses some intermediately saved files from notebooks above)
- **Output:** `3_shift_summary_region_characteristics.csv` (more in `README_data.md`)
  
---
The pre- and postprocessing was done on the OGGM cluster in Bremen. Intermediate or preliminary data / test figures or raw data from the individual groups are only available at the OGGM cluster, and not available in the GitHUB reposity or the Zenodo data repository. These additional files are mostly in [https://cluster.klima.uni-bremen.de/~lschuster/GlacierMIP3/](https://cluster.klima.uni-bremen.de/~lschuster/GlacierMIP3/) or available by changing respectively the url path as given by the notebooks. In case of questions, please ask [Lilian Schuster](mailto:lilian.schuster@uibk.ac.at).  


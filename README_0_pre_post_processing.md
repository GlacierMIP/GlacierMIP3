# Preprocessing and postprocessing of climatic data, glacier model projections, and LOWESS fits with temperature changes

Most recent postprocessing date: `DATE = "Feb12_2024"`

> environemnt saved via:
> (oggm_gmip3_working) mamba list --export > mamba_packages_oggm_gmip3_sept17_2024.yml
> install the packages of that environment, then also install moepy and oggm 
> pip install --user --no-deps moepy oggm progressbar2

## 00: Download climate data, preprocess and extract statistics

`000_wget-isimip3b_prcp_temp.sh` 
- if you want to repeat the download of the daily ISIMIP3b files (~1TB of data), run the following bash file:
  - `bash 000_wget-isimip3b_prcp_temp.sh -H` (you need to registrate to esg and login via terminal)
  
`00a_isimip3b_postprocessing_analysis/isimip3b_postprocess_to_monthly.ipynb`
- postprocesses ISIMIP3b precipitation and temperature data:
  - merging and creating monthly means (those monthly files were used as input for most glacier models)
  - the processed monthly ISIMIP3b version 2.5 data are available under: https://cluster.klima.uni-bremen.de/~lschuster/isimip3b/ 
- produces global mean temperature change estimates for every climate scenarios (°C above pre-industrial, as defined by IPCC AR6 report)
  - creates `../data/climate_input_data/temp_ch_ipcc_ar6_isimip3b.csv` 

`00b_extract_isimip3a_gswp3-w5e5_glacier_climate_change.ipynb`:
- gets past and current temperature and precipitation from ISIMIP3a GSWP3-W5E5 for the different glacier regions
- creates `../data/climate_input_data/temp_prcp_past_gswp3-w5e5_glacier_regionally.csv`

`00c_extract_isimip3b_glacier_climate_change.ipynb`: 
- creates `../data/climate_input_data/temp_ch_ipcc_ar6_isimip3b_glacier_regionally.csv`

## 0a-c: Postprocess (aggregate, scale, check, extend, shift) the glacier model projections of the individual glacier models
`0a_analysis_regional_model_dataset_merging_and_initial_state_comparison.ipynb`
- merges all regional volume and area glacier runs of the different models into one netCDF file 
- option A: volume/area scaling applied so that all models start at the same initial state (i.e., Farinotti et al. 2019 volume and RGI6 area):
    - creates `../data/GMIP3_reg_glacier_model_data/glacierMIP3_Feb12_2024_models_all_rgi_regions_sum_scaled.nc`
      
      also available at: https://cluster.klima.uni-bremen.de/~lschuster/glacierMIP3_analysis/glacierMIP3_Feb12_2024_models_all_rgi_regions_sum_scaled.nc
- same as A, but in option B no volume/area scaling applied (just interesting for testing, understanding the models workflow, or model intercomparison)
    - creates `../data/GMIP3_reg_glacier_model_data/glacierMIP3_Feb12_2024_models_all_rgi_regions_sum.nc`

      also available at: https://cluster.klima.uni-bremen.de/~lschuster/glacierMIP3_analysis/glacierMIP3_Feb12_2024_models_all_rgi_regions_sum.nc
- also plots amount of experiments per glacier model and checks initial state before having applied volume/area scaling
- these datasets also include OGGM_v153 and OGGM_VAS. These model options are not part of the first GlacierMIP3 study, but might be used for a study focusing on the glacier model differences. 
 

`0a1_test_for_duplicates_and_other_errors.ipynb`
- checks if there are duplicates in the data of the submitted groups (now all duplicates were removed/resubmitted, so the tests are running without errors)
    
`0b_create_extended_5000yr_timeseries.ipynb`
- uses the scaled netCDF file from the previous notebook and creates an extended dataset where for each region all simulations go until simulation year 5000
    - applied option: repeat the values of the last 101 years
- creates `../data/GMIP3_reg_glacier_model_data/glacierMIP3_{DATE}_models_all_rgi_regions_sum_scaled_extended_repeat_last_101yrs.nc`
      - also available at: https://cluster.klima.uni-bremen.de/~lschuster/glacierMIP3_analysis/glacierMIP3_Feb12_2024_models_all_rgi_regions_sum_scaled_extended_repeat_last_101yrs.nc
      - dataset useful for plotting timeseries or steady-state estimates
    
`0c_correction_regional_volume_change_until_2020.ipynb`
- shifts all time series to roughly the 2020 volume
- creates the hugonnet 2021 / Farinotti et al. 2019 summary statistics that also includes the estimated median RGI year and the 2020 regional volume:
    - `../data/rgi_vs_2020_volume_hugonnet_estimates.csv`
- creates the shifted timeseries dataset that is used later in most analysis (eight glacier models are included here, not anymore OGGM-VAS or OGGM_v153):
    - `../data/GMIP3_reg_glacier_model_data/all_shifted_glacierMIP3_Feb12_2024_models_all_rgi_regions_sum_scaled_extended_repeat_last_101yrs_via_5yravg.nc`
    - also available at: https://cluster.klima.uni-bremen.de/~lschuster/glacierMIP3_analysis/all_shifted_glacierMIP3_Feb12_2024_models_all_rgi_regions_sum_scaled_extended_repeat_last_101yrs_via_5yravg.nc
- creates some test figures to show how much simulation years are shifted and how well the 2020 volume is matched

## 0d-f, lowess_fits_scripts/, per_glac_model_lowess_fits_scripts/: LOWESS fits of glacier model mass vs temperature changes 

`lowess_fits_scripts/lowess_percentile_interval_fit_per_region_added_uncertainties.py` 
- need to execute the lines of `lowess_fits_scripts/commandos_slurm.txt` which will run the python scripts to create the lowess fits with uncertainties 
- creates preliminary csv files with the lowess best frac fits: 
    - e.g.: `lowess_fits_scripts/_raw_fits/fitted_lowess_best_frac_shift_years_rel_2020_101yr_avg_period_lowess_added_quantiles_added_current12deg_5000_{DATE}_ipcc_ar6.csv`
- creates preliminary csv files with the exponential fit (just for comparison), here the "shifted variant":
    - e.g.: `lowess_fits_scripts/_raw_fits/fitted_lowess_best_frac_shift_years_rel_2020_101yr_avg_period_lowess_added_quantiles_added_current12deg_5000_{DATE}_ipcc_ar6.csv`
- creates preliminary rather complex figure variants of Fig.2 of the manuscript (figures are in `lowess_fits_scripts/_test_figs`) :
    - those are simplified later in `A_community_estimate_paper_analysis/2a_glacier_vs_climate_change_evolution.ipynb`

`per_glac_model_lowess_fits_scripts/lowess_percentile_interval_fit_per_model_per_region.py` :
- python script to create the per-glacier lowess fits 
    - (necessary to assess glacier model uncertainties of the temperature sensitivities)
          
`0d_lowess_fit_advanced_aggregation_uncertainty.ipynb`
- aggregates all different lowess fits to better summary csv files. These files are available in `data/lowess_fit_rel_2020_*` (more in `README_data.md`)

## Summarise different regional GMIP3 model estimates together with glacier region characteristic
`0e_response_timescale_estimates.ipynb`
- estimates the response timescale for every glacier model and experiment (for the shifted simulations) at volume changes of -50%, -80% and -90% and saves them in this csv file: `../data/resp_time_shifted_X%_threshold25%_for_deltaT_rgi_reg_roll_volume_21yravg.csv` (more in `README_data.md`)

`0f_extract_regional_climatic_glacier_median_response_time_characteristics.ipynb`
-  extracts all the regional glacier/climate and median response time/lowess fit characteristics and saves them under: `3_shift_summary_region_characteristics.csv` (more in `README_data.md`) 



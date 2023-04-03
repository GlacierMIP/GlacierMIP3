# Notebook overview:


### 0: Preprocessing, create datasets that can be analysed:
- `0_extract_isimip3b_glacier_climate_change.ipynb`: 
    - creates glacier-area global and regional temperature change averages `../data/temp_ch_ipcc_isimip3b_glacier_regionally.csv` and `figures/0_temp_change_global_regional_glacier_hist_{scenario}.png`
    - Only get global mean temperature changes for each of the experiments (time periods and scenarios) and GCMs: inside of `../isimip3b_postprocessing_analysis/isimip3b_postprocess_to_monthly.ipynb`
- `0_analysis_regional_model_dataset_merging_and_initial_state_comparison.ipynb`
    - merges all regional glacier runs of the different models into one netCDF file 
    - creates: https://cluster.klima.uni-bremen.de/~lschuster/glacierMIP3_analysis/glacierMIP3_mar14_models_all_rgi_regions_sum_scaled.nc
    - (there might be a more recent date available)
    - volume/area scaling applied so that all models start at the same initial state
    
- `0_individual_glacier_check.ipynb`
    - checks if individual glacier interannual variability coincides between glacier models
    - looks at per-glacier files!!!
    - PyGEM' interannual variability coincides well with the one from OGGM, but GloGEMFlow' interannual variability does not coincide at all with them 
    
- `00_test_for_duplicates_and_other_errors.ipynb`:
    - checks if there are duplicates in the data of the submitted groups (now all duplicates were removed, so the tests are running without errors)
    
 
### 1: First Analysis without using temperature data
> these notebooks can be run also without being on the OGGM cluster, if you change th path for the `glacierMIP3_{DATE}_models_all_rgi_regions_sum_scaled.nc` file

- `1_overview_timeseries_plots.iypnb`
    - creates simple volume time series plots for every RGI region, and then also for every GCM separately (plots inside of `figures/1_overview_timeseries_plot`)
- `1b_annual_variability.ipynb`
    - shows the differences in the interannual regional volume variability between the glacier models (some models, specifically GloGEM-family, do not correlate with the other models)
    

### 2: Also include temp. change data
> these notebooks can be run also without being on the OGGM cluster, if you change th path for the `glacierMIP3_{DATE}_models_all_rgi_regions_sum_scaled.nc` file

- `2_analysis_regional_glacier_vs_climate_change.ipynb`
    - comparison of glacier changes to global or glacier regional climate changes 
- `2_glacier_vs_climate_change_evolution.ipynb`
    - work in process: for every region, all 80 experiments as lines dependent on the warming scenario (blue to red), either with global warming or regional warming 
    
### Plans
- analyse runaway effect ...

- plot the difference period - ref_peroid for each glacier model -> filter out downscaling difference 
    - look at differences between time series to reduce the downscaling influence  (as downscaling is different for every glacier model)

    
    
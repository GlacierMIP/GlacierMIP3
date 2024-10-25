# Community estimate paper analysis and figure creation - Notebook overview:
Most recent postprocessing date: `DATE = "Feb12_2024"`

Pre and postprocessing is described in [README_0_pre_post_processing](README_0_pre_post_processing).


- `00a_gmt_climate_scenarios_figure.ipynb`
    - creates the extended data figure that shows the climate timeseries 
      - `fig_ED_XX_climate.png`


### Compare dta relative to temp. change data 

- `2a_glacier_vs_climate_change_evolution.ipynb` 
    - global plot, and for every RGI region, showing results by always using median (and quantiles) of glacier models 
    - creates figures inside of `2_timeseries_temp_ch_reg_glob` and the Fig. `2_condensed_rgi_region_analysis.png` 
         - manuscript figure 1, 2 (TODO: need to update the figure to show LOWESS fit with uncertainties instead of exp. fit)
         - actually Fig. 1 needs the fits that are shown in 
    - creates figures of global vs regional warming (for supplements)
    - creates supplemental figures with x-axis the RGI regions and as y-axis ... (allow to also show uncertainties): 
        - steady-state statistics with uncertainties (1.2°C ice loss, temp. sensitvities - TODO _> update and add uncertainties)
    
- `2b_find_equilibrium_steady_state_yr.ipynb`
    - find steady-state year (used at the moment for one supplemental figure)



    
### 3: further analysis of steady state, time to reach 50 or 80% of the total changes, and of regional characteristics related to these regional differences

- `3a_response_time_analysis_with_2020_shift.ipynb`
    - time to reach 50 or 80% of the total changes
        - creates supplemental figures of "Time to reach 50%/80 % of the changes statistics" 

- `3c_lowess_shifted_fit_region_characteristics_glacier_response.ipynb`
   - creates additional file that is currently only? used within 3x_create Fig. 4 ??? (`_intermediate_data/lowess_fit_cluster...`)
   - creates Extended Data Fig. about correlation coefficients ...
   - TODO: check which files are actually still used, maybe we can now merge 3c and 3x_create fig. 4 together???  

- `3x_create_fig4.ipynb`
    - creates Fig. 4
       - **TODO**: notebook still needs the dataset where the k-means clustering is applied (just because of historical reasons)
       - todo: `_intermediate_data/lowess_fit_cluster...` -> update so that it does not need that anymore!!!


### 4: further aggregated figures such as the world map

- `4_world_map_figure.ipynb`
    - world map plot created, figure variants are in `figures/supplements/only_github_supplements/fig3_worldmap_variants`

### discussion analysis
- `5_comparison_to_marzeion_et_al_2018.ipynb`
    - Comparison of the GlacierMIP3 results (relative to inventory date) to those from Marzeion et al., (2018)
    - creates extended data fig. 3
    - compares also the temperature sensitivities between Marzeion et al. 2018 and GMIP3 (number possibly mentioned in main text)
    
- `5_comparison_to_zekollari_et_al_2024_rounce_et_al_2023.ipynb`
    - comparison to the 2100 projections of other studies
    - computed the glacier mass loss sensitivity to temperature changes by using the 2100 projection of rounce et al. 2023 (estimate mentioned in main manuscript)
    - creates extended data Fig. 4: comparison plot of regional glacier mass loss from transient glacier projections until the year 2100 (Zekollari et al., 2024) versus the GlacierMIP3 steady state glacier mass losses

- `5x_RGI04_barnes_ice_cap_analysis.ipynb`
    - analysis of per-glacier files just for the Barnes Ice cap RGI IDs

- `5_conversion_to_SLR_equivalent.ipynb`
    - creates a fit of how much glacier volume below sea-level is lost vs total volume (by using OGGM data). This fit is used later in `6_csv_tables_creation.ipynb`.
    - also creates supplementary figure to show the relationship of the ratio to the total volume (and the applied fit from the OGGM data)

### suppl analysis
- `XX_suppl_per_glacier_model_fit.ipynb`
    - creates suppl. figure with per glacier model LOWESS fits
    - uses the per-glacier model LOWESS fit (saved at the moment here: 0_pre_post_processing/per_glac_model_lowess_fits_scripts/fitted_per_model_lowess_best_frac_shift_years_rel_2020_101yr_avg_period_lowess_added_current12deg_5000_Feb12_2024_ipcc_ar6.csv)
      - todo: eventually extract important data and  move that to the `data` folder... 

### Supplementary Data
- `6_csv_tables_creation.ipynb`
    - creates table for suppl. information about current and past volume changes (+ some regional characteristics, such as regional glacier surface slope)
    - creates aswell table with steady-state regional glacier volume estimates with uncertainties ...
    - ... what other tables do we need ? 
        - TODO: maybe time to reach 80% of the total changes for the different regions??? 
    - tables are saved as .csv file, and directly exported as `.docx` file for the manuscript and then some minor formatting adjustments were manually done

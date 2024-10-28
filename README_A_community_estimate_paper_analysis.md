# Community estimate paper analysis and figure creation - Notebook overview:
Most recent postprocessing date: `DATE = "Feb12_2024"`

Pre and postprocessing is described in [README_0_pre_post_processing](README_0_pre_post_processing).


### 1: Visualise the 80 steady-state constant climate experiments
`1_gmt_climate_scenarios_figure.ipynb`
- creates **supplementary figure XX** that shows the climate timeseries
  - `fig_ED_XX_climate.png`
- to run the code, you need additional climate data from ISIMIP3b that are available here: https://cluster.klima.uni-bremen.de/~lschuster/isimip3b/isimip3b_tasAdjust_monthly 


### 2: Compare dta relative to temp. change data 

`2a_glacier_vs_climate_change_evolution.ipynb` 
- creates **Figure 1, 2 and several supplementary figures XX (variants of Fig. 2)**
- global plot, and for every RGI region, showing results by always using median (and quantiles) of glacier models 
- creates figures of global vs regional warming (for supplements)

`2b_find_equilibrium_steady_state_yr.ipynb`
- computes steady-state year and visualises it -> **supplementary figure XX**

    
### 3: Further analysis of steady state, time to reach 50 or 80% of the total changes, and of regional characteristics related to these regional differences

`3a_response_time_analysis_with_2020_shift.ipynb`
- time to reach 50 or 80% of the total changes
    - creates timeseries for each region/glacier model and all experiments with global warming >=1.2°C. Example time series in **supplementary figure XX**, remaining variants are in `figures/supplements/only_github_supplements/figS5_variants`
    - creates **supplementary figure XX,XX** of "Time to reach 50%/80 % of the changes statistics" 

`3b_create_fig4_plus_regional_correlations.ipynb`
- creates **Figure 4, Supplementary figure XX,XX** on regional correlation coefficients and different reponse timescale definitions...

### 4: further aggregated figures: world map
`4_world_map_figure.ipynb`
- creates **Figure 3 world map**, figure variants are in `figures/supplements/only_github_supplements/fig3_worldmap_variants`

### 5: Discussion analysis with just supplementary/extended data figures
`5_comparison_to_marzeion_et_al_2018.ipynb`
- creates extended data fig. 3
- Comparison of the GlacierMIP3 results (relative to inventory date) to those from Marzeion et al., (2018)
- compares also the temperature sensitivities between Marzeion et al. 2018 and GMIP3 (number possibly mentioned in main text)

`5_comparison_to_zekollari_et_al_2024_rounce_et_al_2023.ipynb`
- comparison to the 2100 projections of other studies
- computed the glacier mass loss sensitivity to temperature changes by using the 2100 projection of rounce et al. 2023 (estimate mentioned in main manuscript)
- creates extended data Fig. 4: comparison plot of regional glacier mass loss from transient glacier projections until the year 2100 (Zekollari et al., 2024) versus the GlacierMIP3 steady state glacier mass losses

`5_conversion_to_SLR_equivalent.ipynb`
- creates a fit of how much glacier volume below sea-level is lost vs total volume (by using OGGM data). This fit is used later in `6_csv_tables_creation.ipynb`.
- also creates supplementary figure to show the relationship of the ratio to the total volume (and the applied fit from the OGGM data)

`5_suppl_per_glacier_model_fit.ipynb`
- creates suppl. figure with per glacier model LOWESS fits
- uses the per-glacier model LOWESS fit (saved at the moment here: 0_pre_post_processing/per_glac_model_lowess_fits_scripts/fitted_per_model_lowess_best_frac_shift_years_rel_2020_101yr_avg_period_lowess_added_current12deg_5000_Feb12_2024_ipcc_ar6.csv)
  - todo: eventually extract important data and  move that to the `data` folder...

`5x_RGI04_barnes_ice_cap_analysis.ipynb`
- analysis of some per-glacier files just for the Barnes Ice cap RGI IDs
- this needs per-glacier model files (ask us to get these files)


### 6: Create supplementary data tables
`6_csv_tables_creation.ipynb`
- creates table for suppl. information about current and past volume changes (+ some regional characteristics from RGI6, such as regional glacier surface slope)
- creates table with steady-state regional glacier mass and response timescale estimates with uncertainties ...
- tables are saved as .xlsx files for the manuscript and then some minor formatting adjustments were manually done

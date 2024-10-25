
import seaborn as sns
import numpy as np 
import pandas as pd
import xarray as xr

# sns.color_palette('colorblind')
# color blind seaborn palette, but want the two Glogemflow  types w. similar color
pal_models = [(0.33725490196078434, 0.7058823529411765, 0.9137254901960784), # Rounce
               (0.8705882352941177, 0.5607843137254902, 0.0196078431372549), # Compagno
             (0.00784313725490196, 0.6196078431372549, 0.45098039215686275), # Zekollari
              (0.8, 0.47058823529411764, 0.7372549019607844), # OGGM_v16
             (0.984313725490196, 0.6862745098039216, 0.8941176470588236),  # GLIMB not good to have grey !(0.5803921568627451, 0.5803921568627451, 0.5803921568627451), # GLIMB
             (0.8352941176470589, 0.3686274509803922, 0.0), # 'Kraaijenbrink'
              (0.9254901960784314, 0.8823529411764706, 0.2), # JAMES
              sns.color_palette('dark')[5], # CISM2
            (0.5803921568627451, 0.5803921568627451, 0.5803921568627451),# sns.color_palette('dark')[6],   # this is for the OGGM_v153 (which will be removed again anyways)
            (0.5803921568627451, 0.5803921568627451, 0.5803921568627451),#(0.984313725490196, 0.6862745098039216, 0.8941176470588236),  # OGGM-VAS
            (0.5803921568627451, 0.5803921568627451, 0.5803921568627451),#(0.00392156862745098, 0.45098039215686275, 0.6980392156862745), #Huss
             ]
pal_models = sns.color_palette(pal_models)
model_order = ['PyGEM-OGGM_v13', 'GloGEMflow', 'GloGEMflow3D',
               'OGGM_v16', 'GLIMB', 'Kraaijenbrink', 'GO', 'CISM2','OGGM_v153','OGGM-VAS', 'Huss']
model_order_anonymous = {'PyGEM-OGGM_v13': 'model 1', 'GloGEMflow': 'model 2',  'GloGEMflow3D' : 'model 3' , 
                         'OGGM_v16': 'model 4',  'GLIMB': 'model 5', 'Kraaijenbrink': 'model 6', 
                        'GO': 'model 7', 'CISM2': 'model 8', 'OGGM_v153': 'model 9', 'OGGM-VAS': 'model 10', 'Huss': 'model 11'}



glac_models_sel = ['PyGEM-OGGM_v13', 'GloGEMflow', 'GloGEMflow3D', 'OGGM_v16', 'GLIMB', 'Kraaijenbrink', 'GO', 'CISM2']

d_reg_num_name = {}
d_reg_num_name['01'] = 'Alaska'
d_reg_num_name['02'] = 'W Canada & US' # Western Canada & USA
d_reg_num_name['03'] = 'Arctic Canada N'
d_reg_num_name['04'] = 'Arctic Canada S'
d_reg_num_name['05'] = 'Greenland Periphery' # maybe rather call it Greenland Periphery as in Rounce et al., 2023???
d_reg_num_name['06'] = 'Iceland'
d_reg_num_name['07'] = 'Svalbard & Jan Mayen'
d_reg_num_name['08'] = 'Scandinavia'
d_reg_num_name['09'] = 'Russian Arctic'
d_reg_num_name['10'] = 'North Asia'
d_reg_num_name['11'] = 'Central Europe'
d_reg_num_name['12'] = 'Caucasus & Middle East'
d_reg_num_name['13'] = 'Central Asia'
d_reg_num_name['14'] = 'South Asia W' #West
d_reg_num_name['15'] = 'South Asia E' # EAST
d_reg_num_name['16'] = 'Low Latitudes'
d_reg_num_name['17'] = 'Southern Andes'
d_reg_num_name['18'] = 'New Zealand'
d_reg_num_name['19'] = 'Subantarctic & Antarctic Islands' ## NEW name!!!

d_reg_num_name_sh = {}
d_reg_num_name_sh['01'] = 'Alaska'
d_reg_num_name_sh['02'] = 'W Canada & US'
d_reg_num_name_sh['03'] = 'Arctic Canada N'
d_reg_num_name_sh['04'] = 'Arctic Canada S'
d_reg_num_name_sh['05'] = 'Greenland'
d_reg_num_name_sh['06'] = 'Iceland'
d_reg_num_name_sh['07'] = 'Svalbard and\nJan Mayen'
d_reg_num_name_sh['08'] = 'Scandinavia'
d_reg_num_name_sh['09'] = 'Russian Arctic'
d_reg_num_name_sh['10'] = 'North Asia'
d_reg_num_name_sh['11'] = 'Central Europe'
d_reg_num_name_sh['12'] = 'Caucasus and\nMiddle East'
d_reg_num_name_sh['13'] = 'Central Asia'
d_reg_num_name_sh['14'] = 'South Asia W'
d_reg_num_name_sh['15'] = 'South Asia E'
d_reg_num_name_sh['16'] = 'Low Latitudes'
d_reg_num_name_sh['17'] = 'Southern Andes'
d_reg_num_name_sh['18'] = 'New Zealand'
d_reg_num_name_sh['19'] = 'Subantarctic and\nAntarctic Islands'



def compute_steady_state_yr(ds_sel, option='relative_to_total_change', threshold_total_change=0, xperc=1, minimum_period=20, test=False):
    
    if len(ds_sel.simulation_year)==0:
        # just set NaN values everywhere
        equilibrium_yr_lower_xperc_ch = pd.DataFrame(index=ds_sel.experiments.to_dataframe().index, 
             columns=['simulation_year'],
             )['simulation_year']
        #print('NaN')
    else:
        end_yr = ds_sel.simulation_year[-1].values
        begin_yr = ds_sel.simulation_year[0].values
        # for the total change, we have to be sure to get a "stable" estimate, thus we
        # use the average over the last 200 years 
        end_state = ds_sel.sel(simulation_year=slice(end_yr-300,end_yr)).mean(dim='simulation_year')
        total_change = np.abs(100 - end_state)  # (Vyr=0 - Yyr steady-state)
        total_change[total_change<threshold_total_change] = np.NaN
        # minimum is 33yrs in region 16, so maybe ok to use a 20-yr average (but normally not a 100-year average)
        testi = ds_sel.sel(simulation_year=slice(minimum_period+begin_yr,end_yr))  # V_yr
        testi_b = ds_sel.sel(simulation_year=slice(begin_yr,end_yr-minimum_period)).values  # V_yr-20/60/100 years

        # important to set here values, as we do not want to substract the same years!!!
        # (V_roll(t) - V_roll(t-50) )/(2*((V_roll(t) + V_roll(t-50) ))
        # v_diff_20_yr = 100*np.abs((testi-testi_b))/(0.5*(testi+testi_b))
        # divide instead by total_change (otherwise we do have a problem if the volume gets very small... )
        # on the other hand, if total chane is small, we also get an issue 
        # v_diff_20_yr = 100*np.abs((testi-testi_b))/total_change
        # lets only do the difference 
        # ??? should we divide by the total change ???
        if option =='relative_to_total_change':
            v_diff_avg_yrs = 100*np.abs((testi-testi_b))/total_change
        elif option == 'relative_to_initial_state':
            v_diff_avg_yrs = np.abs((testi-testi_b))

        v_diff_avg_yrs = v_diff_avg_yrs.reset_coords()

        if test:
            v_diff_avg_yrs_abovexperc = v_diff_avg_yrs.volume_m3.where(np.abs(testi-testi_b)>xperc).to_dataframe(f'volume_diff_after_XX_yrs').dropna()
        else:
            v_diff_avg_yrs_abovexperc = v_diff_avg_yrs.volume_m3.where(v_diff_avg_yrs.volume_m3>xperc).to_dataframe(f'volume_diff_after_XX_yrs').dropna()
        try:
            v_diff_avg_yrs_abovexperc = v_diff_avg_yrs_abovexperc.drop(columns=['period_scenario','gcm'])
        except:
            pass
        v_diff_avg_yrs_abovexperc = v_diff_avg_yrs_abovexperc.reset_index()

        v_diff_avg_yrs_last_yr_above_xperc = v_diff_avg_yrs_abovexperc.groupby(['gcm', 'period_scenario']).max()['simulation_year']

        # if it is the end of the timeseries (i.e. 1990 or 4990), it means that no equilibrium within the limits was reached , we set it to np.NaN
        # for the moment just set a larger number and then we need to check what to do!
        v_diff_avg_yrs_last_yr_above_xperc.loc[v_diff_avg_yrs_last_yr_above_xperc>=end_yr] = 100000
        # we need to add +1 (as we computed the last year where it was above 1)
        equilibrium_yr_lower_xperc_ch = v_diff_avg_yrs_last_yr_above_xperc + 1
    return equilibrium_yr_lower_xperc_ch
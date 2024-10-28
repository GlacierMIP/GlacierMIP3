
import seaborn as sns
import numpy as np 
import pandas as pd
import xarray as xr

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
             ]
pal_models = sns.color_palette(pal_models)
model_order = ['PyGEM-OGGM_v13', 'GloGEMflow', 'GloGEMflow3D',
               'OGGM_v16', 'GLIMB', 'Kraaijenbrink', 'GO', 'CISM2','OGGM_v153','OGGM-VAS']
model_order_anonymous = {'PyGEM-OGGM_v13': 'model 1', 'GloGEMflow': 'model 2',  'GloGEMflow3D' : 'model 3' , 
                         'OGGM_v16': 'model 4',  'GLIMB': 'model 5', 'Kraaijenbrink': 'model 6', 
                        'GO': 'model 7', 'CISM2': 'model 8', 'OGGM_v153': 'model 9', 'OGGM-VAS': 'model 10'}

# actually used glacier models for the community estimate manuscript
glac_models_sel = ['PyGEM-OGGM_v13', 'GloGEMflow', 'GloGEMflow3D', 'OGGM_v16', 'GLIMB', 'Kraaijenbrink', 'GO', 'CISM2']

d_reg_num_name = {}
d_reg_num_name['01'] = 'Alaska'
d_reg_num_name['02'] = 'W Canada & US' # Western Canada & USA
d_reg_num_name['03'] = 'Arctic Canada N'
d_reg_num_name['04'] = 'Arctic Canada S'
d_reg_num_name['05'] = 'Greenland Periphery' 
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



########################### get the correct colorscale ... will just import cmap and scaler to the individual notebooks
from matplotlib.colors import LinearSegmentedColormap
from sklearn.preprocessing import MinMaxScaler
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt

# get the global mean average temperatures of the experiments... 
pd_avg_exps= pd.read_csv('../data/climate_input_data/temp_ch_ipcc_ar6_isimip3b.csv', index_col=[0])
glob_temp_ch = pd_avg_exps.set_index(['gcm', 'period_scenario']).values

only_12_range = False
if only_12_range:
    colors_icci_l3 = ['#70B8FF', '#FABB00', '#F25100', '#D42300', '#B3001E', '#800040', '#550066', '#2B084D']
    cmap_icci_3 = LinearSegmentedColormap.from_list('bins_100', colors_icci_l3, N=1000)
    # IDEA --> Let's scale from 1.2 onwards
    scaler = MinMaxScaler()
    temp_ch_sel = np.arange(1.2,glob_temp_ch.max(),0.25)
    scaler.fit(temp_ch_sel.reshape(-1,1))
    cmap = cmap_icci_3
else:
    ## '#306BAF', '#1A488A', '#002966'
    ## '#4D8ED6',
    colors_full_temp_range = ['#002966', '#306BAF', '#70B8FF','#FABB00', '#F25100', '#D42300', '#B3001E', '#800040', '#550066', '#2B084D']
    cmap_full_temp_range = LinearSegmentedColormap.from_list('bins_100', colors_full_temp_range, N=1000)
    # IDEA --> Let's scale from the entire range onwards onwards
    scaler = MinMaxScaler()
    temp_ch_sel = np.arange(-0.36,glob_temp_ch.max(),0.25)# need to manually set the minimum to a lower value to have a light blue color at ~1.2°C
    scaler.fit(temp_ch_sel.reshape(-1,1))
    cmap = cmap_full_temp_range

norm = plt.Normalize(vmin=-0.36, vmax=glob_temp_ch.max())
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
assert sm.cmap == cmap

t = 1.2
# just want to make sure that 1.2°C is this color here: '#70B8FF'
hex_color = '#70B8FF'
rgba_color = mcolors.to_rgba(hex_color)
c1=sm.cmap(scaler.transform(np.array(t).reshape(-1,1))).squeeze()
c2=cmap(scaler.transform(np.array(t).reshape(-1,1))).squeeze()
np.testing.assert_allclose(c1,c2)
np.testing.assert_allclose(c1,rgba_color)

###################


def get_glob_temp_exp(region='global'):
    pd_global_temp_exp_glac = pd.read_csv('../data/climate_input_data/temp_ch_ipcc_ar6_isimip3b_glacier_regionally.csv', index_col = 0)
    _p = pd_global_temp_exp_glac.loc[pd_global_temp_exp_glac.region == region]
    _p = _p.set_index(['gcm','period_scenario'])
    return _p

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
        # need to increase the int type as it gives an error otherwise
        v_diff_avg_yrs_last_yr_above_xperc = v_diff_avg_yrs_last_yr_above_xperc.astype('int32')
        v_diff_avg_yrs_last_yr_above_xperc.loc[v_diff_avg_yrs_last_yr_above_xperc>=end_yr] = 100000
        # we need to add +1 (as we computed the last year where it was above 1)
        equilibrium_yr_lower_xperc_ch = v_diff_avg_yrs_last_yr_above_xperc + 1
    return equilibrium_yr_lower_xperc_ch
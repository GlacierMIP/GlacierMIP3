% Code to shuffle annual temperature time series following the
% 'shuffle-key' (provided in 'shuffled_years_GlacierMIP3.csv') 
% for the 'GlacierMIP3 - Equi' experiments

%% 
close all
clear
clc

%% User input. Which glacier 
glacier='RGI60-16.02207' % 'RGI60-11.00897' = Hintereisferner; 'RGI60-16.02207' = Shallap glacier

%% Glacier lon-lat (nearest grid cell GCM)
if glacier=='RGI60-11.00897' % Hintereisferner (Austria)
    lat=46.75
    lon=10.75
elseif glacier=='RGI60-16.02207' % Glaciar  Shallap (Peru)
    lat=-77.25
    lon=-9.25
end

%% Loading the data (ISIMIP3b: ipsl-cm6a-lr_r1i1p1f1_w5e5)
% Monthly climate data (tasAdjust) for historical time period (1850-2014)
% and future projections (evolution under ssp585). 
data_monthly_historical=ncread('tasAdjust/ipsl-cm6a-lr_r1i1p1f1_w5e5_historical_tasAdjust_global_monthly_1850_2014.nc','tasAdjust');
data_monthly_future=ncread('tasAdjust/ipsl-cm6a-lr_r1i1p1f1_w5e5_ssp585_tasAdjust_global_monthly_2015_2100.nc','tasAdjust');
% Gridded longitude and latitude
GCM_lon=ncread('tasAdjust/ipsl-cm6a-lr_r1i1p1f1_w5e5_historical_tasAdjust_global_monthly_1850_2014.nc','lon');
GCM_lat=ncread('tasAdjust/ipsl-cm6a-lr_r1i1p1f1_w5e5_historical_tasAdjust_global_monthly_1850_2014.nc','lat');
% time series with shuffled years
shuffled_series_years=readmatrix('shuffled_years_GlacierMIP3.csv');
shuffled_series_years(1,:)=[]; % Remove the first row (= index)
shuffled_series_years(:,1)=[]; % Remove the first column (= years)

%% Merge the 'historical' and 'future' temperature series into a single time series
data_monthly = cat(3,data_monthly_historical,data_monthly_future); % cat = to concatenate. 3 = along the third dimension

%% Take the data at the glacier location:
col=find(GCM_lon==lon); % Find the 'row' in the 2D array
row=find(GCM_lat==lat); % Find the 'column' in the 2D array
data_monthly_glacier=squeeze(data_monthly(col,row,:)); % 'squeeze' is used to go from 3-D to 1-D array

%% Convert the time series to annual time series (note: no weighting per month duration is performed here)
data_annual_glacier=nan([251 1]); % 251 = years from 1850 to 2100
for i=1:length(data_monthly)/12
    data_annual_glacier(i)=mean(data_monthly_glacier((i-1)*12+1:i*12));
end

%% Shuffle for the various time series (8 in total):
data_shuffled=nan([8 5000]); % 8 time series in total (1851-1870, 1901-1920, 1951-1970, 1995-2014, 2021-2040, 2041-2060, 2061-2080, 2081-2100), these have a length of 5000 years
for i=1:8 % 8 time series
    for j=1:5000 % each time series is 5000 years long
        year=shuffled_series_years(i,j);
        data_shuffled(i,j)=data_annual_glacier(year-1849); % '-1849', as index 1 = year 1850
    end
end

% Write out the files: same as on GitHub, but without the first row (index) and columns (years)
% if glacier=='RGI60-11.00897' % Hintereisferner
%     writematrix(data_shuffled,'test_RGI60-11.00897_ipsl-cm6a-lr_tasAdjust_ssp585_shuffled.csv') 
% elseif glacier=='RGI60-16.02207' % Shallap
%     writematrix(data_shuffled,'test_RGI60-16.02207_ipsl-cm6a-lr_tasAdjust_ssp585_shuffled.csv') 
% end
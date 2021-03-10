import pandas as pd
import geopandas as gpd
import numpy as np
from geosupport import Geosupport

pd.set_option('display.max_columns', None)
path='C:/Users/mayij/Desktop/DOC/GITHUB/td-walkshed/'



g=Geosupport()
df=pd.read_csv(path+'RTCORRIDOR.csv',dtype=str)
df['X']=np.nan
df['Y']=np.nan
df['LAT']=np.nan
df['LONG']=np.nan

for i in df.index:
    borocode='5'
    street1=str(df.loc[i,'INT1'])
    street2=str(df.loc[i,'INT2'])
    intersection=g['2']({'borough_code':borocode,
                         'street_1':street1,
                         'street_2':street2,
                         'compass_direction':'N'})
    df.loc[i,'X']=pd.to_numeric(intersection['SPATIAL COORDINATES']['X Coordinate'])
    df.loc[i,'Y']=pd.to_numeric(intersection['SPATIAL COORDINATES']['Y Coordinate'])
df=gpd.GeoDataFrame(df,geometry=gpd.points_from_xy(df['X'],df['Y']),crs=6539)
df=df.to_crs(4326)
df=df[['INT2','geometry']].reset_index(drop=True)
df.columns=['intersection','geometry']
df.to_file(path+'RTCORRIDOR.shp')

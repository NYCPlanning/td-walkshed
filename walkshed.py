import pandas as pd
import geopandas as gpd
import numpy as np

pd.set_option('display.max_columns', None)
path='C:/Users/mayij/Desktop/DOC/DCP2021/WALKSHED/'



lion=gpd.read_file(path+'lion.geojson')
lion=lion.to_crs('epsg:4326')



lvl={'A':-12,'B':-11,'C':-10,'D':-9,'E':-8,'F':-7,'G':-6,'H':-5,'I':-4,'J':-3,'K':-2,'L':-1,'M':0,
     'N':1,'O':2,'P':3,'Q':4,'R':5,'S':6,'T':7,'U':8,'V':9,'W':10,'X':11,'Y':12,'Z':13}



liondiff=lion[np.isin(lion['SegmentTyp'],['B','R','T','C','U','S'])].reset_index(drop=True)
liondiff=liondiff[np.isin(liondiff['FeatureTyp'],['0','6','C','W','A'])].reset_index(drop=True)
liondiff=liondiff[liondiff['NonPed']!='V'].reset_index(drop=True)
liondiff=liondiff[(liondiff['NodeLevelF']!='M')|(liondiff['NodeLevelT']!='M')].reset_index(drop=True)
liondiff['LvlF']=liondiff['NodeLevelF'].map(lvl)
liondiff['LvlF']=liondiff['LvlF'].fillna(0)
liondiff['LvlT']=liondiff['NodeLevelF'].map(lvl)
liondiff['LvlT']=liondiff['LvlT'].fillna(0)
liondiff=liondiff[['SegmentID','LvlF','LvlT','geometry']].reset_index(drop=True)
liondiff=liondiff.drop_duplicates(['SegmentID','LvlF','LvlT'],keep='first').reset_index(drop=True)
liondiff.to_file(path+'liondiff.geojson',driver='GeoJSON')



liongrade=lion[np.isin(lion['SegmentTyp'],['B','R','T','C','S','U'])].reset_index(drop=True)
liongrade=liongrade[np.isin(liongrade['FeatureTyp'],['0','6','C','W','A'])].reset_index(drop=True)
liongrade=liongrade[liongrade['NonPed']!='V'].reset_index(drop=True)
liongrade=liongrade[(liongrade['NodeLevelF']=='M')&(liongrade['NodeLevelT']=='M')].reset_index(drop=True)
liongrade['LvlF']=liongrade['NodeLevelF'].map(lvl)
liongrade['LvlF']=liongrade['LvlF'].fillna(0)
liongrade['LvlT']=liongrade['NodeLevelF'].map(lvl)
liongrade['LvlT']=liongrade['LvlT'].fillna(0)
liongrade=liongrade[['SegmentID','LvlF','LvlT','geometry']].reset_index(drop=True)
liongrade=liongrade.drop_duplicates(['SegmentID','LvlF','LvlT'],keep='first').reset_index(drop=True)
liongrade.to_file(path+'liongrade.geojson',driver='GeoJSON')







import pandas as pd
import geopandas as gpd
import shapely

pd.set_option('display.max_columns', None)
path='C:/Users/mayij/Desktop/DOC/DCP2021/WALKSHED/'


# OSM based
osm=gpd.read_file(path+'osm.shp')
osm.crs=4326
osm=osm[~osm['code'].isin([5111,5112,5131,5132,5133,5134])].reset_index(drop=True)

df=[]
for i in sorted(osm['layer'].unique()):
    tp=osm[osm['layer']==i].reset_index(drop=True)
    tp=pd.DataFrame(shapely.ops.unary_union(tp['geometry']))
    tp.columns=['geom']
    tp['layer']=i
    tp=gpd.GeoDataFrame(tp,geometry=tp['geom'],crs=4326)
    tp=tp.drop('geom',axis=1)
    df+=[tp]
df=pd.concat(df,axix=0,ignore_index=True)
    



df=shapely.ops.unary_union(df['geometry'])
df=pd.DataFrame(df)
df.columns=['geom']
df=gpd.GeoDataFrame(df,geometry=df['geom'],crs=4326)
df=df.drop('geom',axis=1)
df.to_file(path+'test.shp')















# # Backup
# # LION based 
# lion=gpd.read_file(path+'lion.shp')
# lion.crs=4326


# lvl={'A':-12,'B':-11,'C':-10,'D':-9,'E':-8,'F':-7,'G':-6,'H':-5,'I':-4,'J':-3,'K':-2,'L':-1,'M':0,
#      'N':1,'O':2,'P':3,'Q':4,'R':5,'S':6,'T':7,'U':8,'V':9,'W':10,'X':11,'Y':12,'Z':13}


# liondiff=lion[np.isin(lion['SegmentTyp'],['B','R','T','C','U','S'])].reset_index(drop=True)
# liondiff=liondiff[np.isin(liondiff['FeatureTyp'],['0','6','C','W','A'])].reset_index(drop=True)
# liondiff=liondiff[np.isin(liondiff['RB_Layer'],['R','B'])].reset_index(drop=True)
# liondiff=liondiff[liondiff['NonPed']!='V'].reset_index(drop=True)
# liondiff=liondiff[(liondiff['NodeLevelF']!='M')|(liondiff['NodeLevelT']!='M')].reset_index(drop=True)
# liondiff['LvlF']=liondiff['NodeLevelF'].map(lvl)
# liondiff['LvlF']=liondiff['LvlF'].fillna(0)
# liondiff['LvlT']=liondiff['NodeLevelF'].map(lvl)
# liondiff['LvlT']=liondiff['LvlT'].fillna(0)
# liondiff=liondiff[['SegmentID','LvlF','LvlT','geometry']].reset_index(drop=True)
# liondiff=liondiff.drop_duplicates(['SegmentID','LvlF','LvlT'],keep='first').reset_index(drop=True)
# liondiff.to_file(path+'liondiff.shp')


# liongrade=lion[np.isin(lion['SegmentTyp'],['B','R','T','C','S','U'])].reset_index(drop=True)
# liongrade=liongrade[np.isin(liongrade['FeatureTyp'],['0','6','C','W','A'])].reset_index(drop=True)
# liongrade=liongrade[np.isin(liongrade['RB_Layer'],['R','B'])].reset_index(drop=True)
# liongrade=liongrade[liongrade['NonPed']!='V'].reset_index(drop=True)
# liongrade=liongrade[(liongrade['NodeLevelF']=='M')&(liongrade['NodeLevelT']=='M')].reset_index(drop=True)
# liongrade['LvlF']=liongrade['NodeLevelF'].map(lvl)
# liongrade['LvlF']=liongrade['LvlF'].fillna(0)
# liongrade['LvlT']=liongrade['NodeLevelF'].map(lvl)
# liongrade['LvlT']=liongrade['LvlT'].fillna(0)
# liongrade=liongrade[['SegmentID','LvlF','LvlT','geometry']].reset_index(drop=True)
# liongrade=liongrade.drop_duplicates(['SegmentID','LvlF','LvlT'],keep='first').reset_index(drop=True)
# liongrade.to_file(path+'liongrade.shp')

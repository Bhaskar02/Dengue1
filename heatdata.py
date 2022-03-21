import streamlit as st
#import pandas as pd # pip install pandas
#from matplotlib import pyplot as plt # pip install matplotlib
import time
import datetime
from glob import glob
import numpy as np
#import coiled
#import dask
#import dask.dataframe as dd
#import folium
import streamlit as st
#from dask.distributed import Client
#from folium.plugins import HeatMap
from streamlit_folium import folium_static
from streamlit_folium.plugins import HeatMap
import pandas as pd
import streamlit as st
import leafmap.foliumap as leafmap

import streamlit as st
import plotly.express as px
import plotly.graph_objs as go
plt.style.use("ggplot")


rad =st.sidebar.radio("Navigation",["HeatMap2","HeatMap1"])

if rad == "HeatMap2":
    st.title('heatmap with Date')
    df = pd.read_csv('https://raw.githubusercontent.com/Bhaskar02/dengueapp/main/data/dengue11f.csv')
    df['dat'] = pd.to_datetime(df['dat'], format='%Y-%m-%d')
    m = leafmap.Map(location=[20.5937, 78.9629],zoom_start=5,tiles="stamentoner")
    #m = folium.Map([20.5937, 78.9629], tiles='stamentoner', zoom_start=5)
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    today=today - datetime.timedelta(days=200)
    start_date = st.date_input('Start date', today)
    end_date = st.date_input('End date', tomorrow)
    data=df[(df.dat>=str(start_date)) & (df.dat<=str(end_date))]
    st.write('', data)
    data=data[['lat','lon','cases']]
    HeatMap(data).add_to(m)#(folium.FeatureGroup(name='Heat Map').add_to(m))
    #st.write('', data)
    #folium.LayerControl().add_to(m)
    m.to_streamlit(width=700, height=700)
if(rad=="HeatMap1"):
    st.title('Heatmaps')

    filepath = "https://raw.githubusercontent.com/Bhaskar02/dengueapp/main/data/denguelatdata.csv"
    url = 'https://raw.githubusercontent.com/Bhaskar02/dengueapp/main/data/denguelatdata.csv'
    df1 = pd.read_csv(url)
    columns1 = df1.columns.tolist()
    selected_columns = st.multiselect("select column", columns1, default='2012')
    #selected_columns =st.selectbox('Select the year',('2010', '2011', '2012','2013','2014','2015','2016','2017','2018'))
    filepath = "https://raw.githubusercontent.com/Bhaskar02/dengueapp/main/data/"+selected_columns[0]+".csv"
    s = df1[selected_columns[0]]
    m = leafmap.Map(location=[20.5937, 78.9629],zoom_start=5,tiles="stamentoner")
    m.add_heatmap(
        url,
        latitude='lat',
        longitude='long',
        value=selected_columns[0],
        name="Heat map",
        radius=20,
    )
    m.to_streamlit(width=700, height=700)

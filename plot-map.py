import streamlit as st
import numpy as np
import pandas as pd

map_data= pd.DataFrame(
        np.random.randn(10, 2)/ [1000,1000] + [19.030377273432197, -98.19039231871928], 
        columns = ['lat', 'lon'])

st.map(map_data)
st.dataframe(map_data)

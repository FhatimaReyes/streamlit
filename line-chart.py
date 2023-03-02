import streamlit as st
import numpy as np
import pandas as pd

chart_data = pd.DataFrame(
        np.random.randn(200000,6),
        columns = ['a', 'b', 'c', 'd', 'e', 'f'])

st.line_chart(chart_data)

st.dataframe(chart_data)

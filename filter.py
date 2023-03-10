import streamlit as st
import pandas as pd

st.title("Streamlit - Filter by sex")
DATA_URL =  "https://firebasestorage.googleapis.com/v0/b/streamlit-77149.appspot.com/o/storage%2Fdataset.csv?alt=media&token=bcb86c4a-8350-4e0a-8666-5ceb8aa327f2"

@st.cache
def load_data():
    data = pd.read_csv(DATA_URL) #read csv
    return data

@st.cache
def load_data_bysex(sex):
   data = pd.read_csv(DATA_URL)
   filtered_data_bysex = data[data['sex'] == sex]

   return filtered_data_bysex

data = load_data()
selected_sex = st.selectbox("Select Sex", data['sex'].unique())
btnFilterbySex = st.button('Filter by sex')

if (btnFilterbySex):
    filterbysex = load_data_bysex(selected_sex)
    count_row = filterbysex.shape[0]
    st.write(f"Total items : {count_row}")

st.dataframe(filterbysex)

import streamlit as st
import pandas as pd

st.title("Streamlit - Search ranges")
DATA_URL =  "https://firebasestorage.googleapis.com/v0/b/streamlit-77149.appspot.com/o/storage%2Fdataset.csv?alt=media&token=bcb86c4a-8350-4e0a-8666-5ceb8aa327f2"

@st.cache
def load_data_byrange(startid, endid):
    data = pd.read_csv(DATA_URL) #read csv
    filtered_data_byrange = data[ (data["index"] >= startid) & (data["index"] <= endid) ]

    return filtered_data_byrange #return the data frame

startid = st.text_input("Start index :" )
endid = st.text_input("End index :" )
btnRange = st.button("Search by range")


if (btnRange):
    filterbyrange = load_data_byrange(int(startid), int(endid)) #call the function
    count_row = filterbyrange.shape[0] #
    st.write(f"Total names : {count_row}")

    st.dataframe(filterbyrange)

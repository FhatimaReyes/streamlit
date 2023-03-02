import streamlit as st
import pandas as pd
import codecs

st.title('Netflix App')
name_link ='movies.csv'

@st.cache
def load_data(nrows):
    name_link = codecs.open('movies.csv', mode='r', encoding=None, errors='strict', buffering=- 1)

    data = pd.read_csv(name_link, nrows=nrows)
    return data

data_load_state = st.text('cargando')
data = load_data(500)
data_load_state.text('netflix app!! (using st.cache)')
st.text('Fhatima Reyes Alejandre - zS20006773')
st.dataframe(data)


sidebar = st.sidebar
st.sidebar.image("https://raw.githubusercontent.com/FhatimaReyes/streamlit/master/FhatimaReyes.jpeg")
sidebar.title("Filtro")

agree = st.sidebar.checkbox("Mostrar todos los filmes")
if agree:
  load_data(500)
sidebar.write("Nombre de la pelicula que desea buscar:")
sidebar.text_input("movie: ")
 

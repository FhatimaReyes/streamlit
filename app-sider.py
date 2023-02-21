import streamlit as st

st.title("Mi primera app con streamlit")

sidebar = st.sidebar

sidebar.title("Esta es la barra lateral.")

sidebar.write("Aqui van los elementos de entrada.")

st.header("información sobre el conjunto de Datos")
st.header("Descripcion de los datos")

st.write("""
        ESte es un simple ejemplo de una app para predecir
        ¡Esta app predice mis datos!
        """)



import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

bicicletas='https://raw.githubusercontent.com/Manuel1928/NYC/main/citibike-tripdata.csv'
DATE_COLUMN = 'started_at'

sidebar = st.sidebar
sidebar.title("Menu")

@st.cache
def load_data(nrows):
    data = pd.read_csv(bicicletas, nrows=nrows, encoding_errors='ignore')
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

Mostrar_todo = sidebar.checkbox("Mostrar todos los datos?")
if Mostrar_todo:
  data = load_data(500)
  st.text("Todos los datos:")
  st.dataframe(data)

RecPorHora = sidebar.checkbox("Mostrar los recorridos por hora?")
if RecPorHora:
  data = load_data(500)
  st.subheader('Numero de recorridos por hora')
  grafica = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
  st.bar_chart

hour_tofilter = sidebar.slider('HORA', 0, 23, 9)
if hour_tofilter:
  data = load_data(500)
  data_rename = data.rename(columns = {'start_lat': 'lat', 'start_lng': 'lon'}, inplace = False)

  filtered_data = data_rename[data_rename[DATE_COLUMN].dt.hour == hour_tofilter]

  st.subheader('Mapa de los recorridos iniciados a las %s:00' % hour_tofilter)
  st.map(filtered_data)



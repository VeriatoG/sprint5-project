import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles.csv')

st.header('Dashboard de Anúncios de Veículos')

hist_checkbox = st.checkbox('Mostrar histograma')

if hist_checkbox:
    st.write('Distribuição da quilometragem dos veículos')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

scatter_checkbox = st.checkbox('Mostrar gráfico de dispersão')

if scatter_checkbox:
    st.write('Relação entre preço e quilometragem')
    fig = px.scatter(
        car_data,
        x='odometer',
        y='price'
    )
    st.plotly_chart(fig, use_container_width=True)

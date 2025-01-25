import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

st.header('Elige tu proximo vehículo') # Titulo de la app

st.write('Con nuestra aplicacion puedes ver los detalles de tu nuevo vehículo ideal') # Descripción de la app

casilla_transmision = st.checkbox('Transmisión') # crear casilla transmisión
casilla_color = st.checkbox('Color') # crear casilla color
casilla_cuentakilómetros = st.checkbox('cuentakilómetros') #crear casilla cuentakilómetros

if casilla_transmision: # si la casilla de verificación está seleccionada
    st.write('Acá puedes ver la cantidad de vehículos que cuentan con transmisión automática o manual')
    fig = px.histogram(car_data, x="transmission",labels={"transmission": "Tipo de Transmisión"},title="Transmisión") # crear el gráfico
    st.plotly_chart(fig, use_container_width=True)

if casilla_color:
    st.write('Revisa los colores disponibles')
    fig = px.histogram(car_data,x= 'paint_color',labels={"paint_color": "Colores Disponibles"},title="Colores") # crear el gráfico
    st.plotly_chart(fig,use_container_width=True)

if casilla_cuentakilómetros:
    st.write('Revisa el cuentakilómetros de nuestros vehículos')
    fig = px.histogram(car_data,x= 'odometer',y='price',labels={"odometer": "Cuentakilómetros de los vehículos"},title="Cuentakilómetros de Nuestros Vehículos") #crear el gráfico
    st.plotly_chart(fig, use_container_width=True)
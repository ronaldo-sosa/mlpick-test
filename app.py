import streamlit as st
from datetime import datetime

# Añadir estilo CSS para el logo en la esquina superior derecha
st.markdown(
    """
    <style>
    .logo-container {
        display: flex;
        justify-content: flex-end;
        position: fixed;
        top: 60px; /* Ajusta el top si el logo no es visible */
        right: 35px; /* Ajusta el right si el logo no es visible */
        padding: 10px;
        z-index: 1; /* Asegúrate de que esté sobre otros elementos */
    }
    .logo-container img {
        height: 50px; /* Ajusta el tamaño del logo aquí */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# URL del logo desde GitHub
logo_url = "https://github.com/ronaldo-sosa/mlpick-test/blob/main/boldr.png?raw=true"

# Insertar el logo en la esquina superior derecha usando la URL
st.markdown(
    f"""
    <div class="logo-container">
        <img src="{logo_url}" alt="Logo">
    </div>
    """,
    unsafe_allow_html=True
)
# Título de la aplicación
st.title("Date Selection")

# Mostrar el calendario y permitir al usuario seleccionar una fecha
fecha_seleccionada = st.date_input(
    "Choose a date:", 
    value=datetime.today(),  # Fecha predeterminada es la fecha actual
    min_value=datetime(2024, 10, 1),  # Fecha mínima
    max_value=datetime(2024, 10, 31)  # Fecha máxima
)

# Mostrar la fecha seleccionada
st.write("You selected:", fecha_seleccionada)


# Título de la aplicación
st.title("Pilot Selection")

# Lista de opciones para el dropdown
opciones = ['Dan', 'Eman', 'Rich', 'Ron', 'Leon']

# Crear el widget de selección múltiple
opciones_seleccionadas = st.multiselect(
    'Select one or option(s):',  # Etiqueta del dropdown
    opciones,  # Lista de opciones disponibles

)

# Mostrar las opciones seleccionadas
st.write("You Chosen:", opciones_seleccionadas)

import pandas as pd
import requests

# URL del archivo de Google Sheets (asegúrate de que el enlace tenga el formato correcto)
drive_url = "https://docs.google.com/spreadsheets/d/1xPgPtX41jZOcsvtzrU_ImaTOh-WBcfZ6/export?format=xlsx"

# Descargar el archivo usando requests
@st.cache_data
def load_data(url):
    try:
        # Descargar el archivo de Google Drive
        response = requests.get(url)
        response.raise_for_status()  # Verifica que la descarga sea exitosa

        # Guardar el archivo temporalmente y leerlo como DataFrame
        with open("kpis.xlsx", "wb") as file:
            file.write(response.content)
        
        st.write("Archivo descargado y guardado temporalmente")
        
        # Cargar el archivo como DataFrame
        df = pd.read_excel("kpis.xlsx")
        st.write("Archivo leído correctamente como DataFrame")
        
        return df
    except Exception as e:
        st.error(f"Error al descargar o leer el archivo: {e}")
        return None

# Cargar los datos
df = load_data(drive_url)

# Mostrar el DataFrame en la aplicación Streamlit
if df is not None:
    st.write("Datos cargados desde Google Drive:")
    st.dataframe(df)
else:
    st.write("No se pudo cargar el DataFrame. Verifica el enlace y el formato del archivo.")

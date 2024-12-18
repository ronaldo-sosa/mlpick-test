import streamlit as st
from datetime import datetime
import pandas as pd
import gdown

# Añadir estilo CSS para los logos en las esquinas
st.markdown(
    """
    <style>
    .logo-container {
        display: flex;
        position: fixed;
        top: 60px; /* Ajusta el top si el logo no es visible */
        padding: 10px;
        z-index: 1; /* Asegúrate de que esté sobre otros elementos */
    }
    .logo-right {
        right: 35px; /* Ajusta el espacio desde la derecha */
    }
    .logo-left {
        left: 35px; /* Ajusta el espacio desde la izquierda */
    }
    .logo-container img {
        height: 50px; /* Ajusta el tamaño del logo aquí */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# URL del logo desde GitHub
logo_url_right = "https://github.com/ronaldo-sosa/mlpick-test/blob/main/boldr.png?raw=true"
logo_url_left = "https://github.com/ronaldo-sosa/mlpick-test/blob/main/ocado.png?raw=true"  # Cambia esta URL por la de tu logo

# Insertar el logo en la esquina superior derecha
st.markdown(
    f"""
    <div class="logo-container logo-right">
        <img src="{logo_url_right}" alt="Logo Derecho">
    </div>
    """,
    unsafe_allow_html=True
)

# Insertar el logo en la esquina superior izquierda
st.markdown(
    f"""
    <div class="logo-container logo-left">
        <img src="{logo_url_left}" alt="Logo Izquierdo">
    </div>
    """,
    unsafe_allow_html=True
)
# Título de la aplicación
st.title("MLPICK - Key Performance Indicator Tracker")

# Mostrar el calendario y permitir al usuario seleccionar una fecha
st.header('Date Selection')
fecha_seleccionada = st.date_input(
    "Choose a date:", 
    value=datetime.today(),  # Fecha predeterminada es la fecha actual
    min_value=datetime(2024, 10, 1),  # Fecha mínima
    max_value=datetime(2024, 10, 31)  # Fecha máxima
)
fecha_formateada = fecha_seleccionada.strftime('%m-%d-%Y')

# Mostrar la fecha seleccionada
st.write("You selected:", fecha_formateada)


# Título de la aplicación
st.header("Pilot Selection")

# Lista de opciones para el dropdown
opciones = ['Dan', 'Eman', 'Rich', 'Ron', 'Leon']

# Crear el widget de selección múltiple
opciones_seleccionadas = st.multiselect(
    'Select one or option(s):',  # Etiqueta del dropdown
    opciones,  # Lista de opciones disponibles

)

# Mostrar las opciones seleccionadas
st.write("You Chosen:", opciones_seleccionadas)



# URL del archivo de Google Sheets en formato Excel
drive_url = "https://docs.google.com/spreadsheets/d/1xPgPtX41jZOcsvtzrU_ImaTOh-WBcfZ6/export?format=xlsx"

@st.cache_data  # Cachear para que se descargue solo una vez
def load_data(url):
    gdown.download(url, 'kpis.xlsx', quiet=False)
    return pd.read_excel('kpis.xlsx')

# Cargar y mostrar el DataFrame
df = load_data(drive_url)
filtered_df = df[df['DATE'] == fecha_formateada]
st.write("Datos cargados desde Google Drive:")
st.dataframe(filtered_df)


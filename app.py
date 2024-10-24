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
        top: 0;
        right: 0;
        padding: 10px;
    }
    .logo-container img {
        height: 50px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Cargar una imagen local y convertirla a bytes
logo_path = "https://github.com/ronaldo-sosa/mlpick-test/blob/main/boldr.png?raw=true"
logo = open(logo_path, "rb").read()

# Insertar el logo usando HTML
st.markdown(
    f"""
    <div class="logo-container">
        <img src="{logo_url}" alt="Logo">
    </div>
    """,
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



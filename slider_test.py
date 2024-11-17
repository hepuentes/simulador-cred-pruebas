import streamlit as st

# Configuración inicial
st.set_page_config(
    page_title="Simulador de Crédito",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Función para formatear números
def format_number(number):
    return "{:,.0f}".format(number).replace(",", ".")

# Datos de créditos
LINEAS_DE_CREDITO = {
    "LoansiFlex": {
        "descripcion": "Crédito de libre inversión para empleados, independientes, personas naturales y pensionados.",
        "monto_min": 1000000,
        "monto_max": 20000000,
        "plazo_min": 12,
        "plazo_max": 60,
        "tasa_mensual": 1.9715,
        "tasa_anual_efectiva": 26.4,
        "aval_porcentaje": 0.10,
        "seguro_vida_base": 150000
    },
    "Microflex": {
        "descripcion": "Crédito rotativo para personas en sectores informales.",
        "monto_min": 50000,
        "monto_max": 500000,
        "plazos": [4, 6, 8],
        "tasa_mensual": 2.0718,
        "tasa_anual_efectiva": 27.9,
        "aval_porcentaje": 0.12
    }
}

# Aquí va el estilo que te compartí antes
st.markdown("""
    <style>
        /* Tema general y fuentes */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        
        .stApp {
            background-color: #1E1E1E;
            font-family: 'Inter', sans-serif;
        }
        
        /* ... resto de los estilos ... */
    </style>
""", unsafe_allow_html=True)

# Título principal
st.markdown("<h1>Simulador de Crédito LOANSI</h1>", unsafe_allow_html=True)


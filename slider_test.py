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

# Datos de líneas de crédito
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

# Estilos
st.markdown("""
    <style>
        .stApp {
            background-color: #1E1E1E;
        }

        .stSelectbox {
            margin-top: 0.2rem !important;
        }
        
        .stSelectbox > div > div {
            pointer-events: auto;
            background-color: #2D2D2D !important;
            border: 1px solid #404040 !important;
            color: #FFFFFF !important;
            cursor: pointer;
        }

        /* Campo de entrada con símbolo $ */
        .currency-input-container {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            margin: 1rem 0 2.5rem 0;
        }

        .currency-symbol {
            font-size: 1.3rem;
            color: #FFFFFF;
            font-weight: 500;
            padding-top: 0.5rem;
        }

        /* Input ajustado */
        .stNumberInput > div > div > input {
            padding-left: 1rem !important;
            height: 3rem !important;
            background-color: #2D2D2D !important;
            color: white !important;
            border: 1px solid #404040 !important;
        }

        /* Espaciado del plazo */
        .plazo-text {
            color: #FFFFFF !important;
            font-size: 1.2rem !important;
            font-weight: 600 !important;
            margin: 2rem 0 1rem 0 !important;
        }

        .stSlider {
            padding-top: 0.5rem !important;
            margin-bottom: 2rem !important;
        }

        /* Resto de estilos... */
    </style>
""", unsafe_allow_html=True)

# Título
st.markdown("<h1 style='color: white; text-align: center; font-size: 2.2rem; margin: 2rem 0;'>Simulador de Crédito Loansi</h1>", unsafe_allow_html=True)

# Selección de línea de crédito
st.markdown("<p style='color: #FFFFFF; font-size: 1.4rem; font-weight: 700; margin-bottom: 0.2rem;'>Selecciona la Línea de Crédito</p>", unsafe_allow_html=True)
tipo_credito = st.selectbox("", options=LINEAS_DE_CREDITO.keys(), index=0)
detalles = LINEAS_DE_CREDITO[tipo_credito]

# Entrada del monto
st.markdown("<p style='color: #FFFFFF; font-size: 1.4rem; font-weight: 700; margin: 1.5rem 0 0.2rem;'>Escribe el valor del crédito</p>", unsafe_allow_html=True)
st.markdown(f"<p style='color: #B0B0B0; font-size: 1.1rem;'>Ingresa un valor entre $ {format_number(detalles['monto_min'])} y $ {format_number(detalles['monto_max'])} COP</p>", unsafe_allow_html=True)

# Contenedor del monto
st.markdown('<div class="currency-input-container">', unsafe_allow_html=True)
col1, col2 = st.columns([0.5,20])
with col1:
    st.markdown('<div class="currency-symbol">$</div>', unsafe_allow_html=True)
with col2:
    monto = st.number_input("", 
                           min_value=detalles["monto_min"],
                           max_value=detalles["monto_max"],
                           step=1000,
                           format="%d")
st.markdown('</div>', unsafe_allow_html=True)

# ¿Quieres que siga con el resto del código?

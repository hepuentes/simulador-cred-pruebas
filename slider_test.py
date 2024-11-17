import streamlit as st

# Configuración inicial
st.set_page_config(page_title="Simulador Crédito", layout="centered", initial_sidebar_state="collapsed")

# Función para formatear números con separadores de miles
def format_number(number):
    return "{:,.0f}".format(number).replace(",", ".")

# Datos para cada línea de crédito
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
        "descripcion": "Crédito rotativo para personas en sectores informales, orientado a cubrir necesidades de liquidez rápida con pagos semanales.",
        "monto_min": 50000,
        "monto_max": 500000,
        "plazo_min": 4,
        "plazo_max": 8,
        "tasa_mensual": 2.0718,
        "tasa_anual_efectiva": 27.9,
        "aval_porcentaje": 0.12,
    }
}

# Estilos personalizados
st.markdown("""
<style>
    .stApp {
        background-color: #1E1E1E;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .main-container {
        max-width: 600px;
        width: 100%;
        margin: 0 auto;
        padding: 20px;
    }
    .titulo {
        color: white;
        font-size: 1.5rem;
        text-align: center;
        margin-bottom: 1rem;
    }
    .valor-seleccionado {
        color: #3B82F6;
        font-size: 2.5rem;
        font-weight: bold;
        margin: 1.5rem 0;
    }
    .stSlider {
        margin: 2rem 0 !important;
    }
    .stSlider > div > div > div {
        background: linear-gradient(to right, #FF4B4B var(--progress), #4B5563 var(--progress)) !important;
        height: 6px !important;
    }
    div[role="slider"] {
        width: 24px !important;
        height: 24px !important;
        background: #3B82F6 !important;
        border: 2px solid white !important;
        border-radius: 50% !important;
        top: -10px !important;
    }
    .valores-minmax {
        display: flex;
        justify-content: space-between;
        color: white;
        font-size: 1rem;
        margin-top: 1rem;
        padding: 0 10px;
    }
    .currency-symbol {
        font-size: 1.5rem;
        color: #FFFFFF;
        text-align: right;
        margin-right: 10px;
    }
    .number-input {
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# Contenedor principal
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Título
st.markdown('<div class="titulo">Simulador de Crédito Loansi</div>', unsafe_allow_html=True)

# Entrada del monto con símbolo de peso
col1, col2 = st.columns([0.1, 0.9])
with col1:
    st.markdown('<div class="currency-symbol">$</div>', unsafe_allow_html=True)
with col2:
    monto = st.number_input(
        "Ingresa un valor entre $ 1.000.000 y $ 20.000.000 COP",
        min_value=1000000,
        max_value=20000000,
        step=50000,
        format="%d",
        label_visibility="collapsed",
        key="monto"
    )

# Espacio adicional para separación
st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)

# Slider de plazo
st.markdown('<p class="titulo">Plazo en Meses</p>', unsafe_allow_html=True)
plazo = st.slider("", min_value=12, max_value=60, step=12, key="plazo")

# Espaciado entre elementos
st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)

# Resultado de la simulación
st.markdown(f"""
<div class="valor-seleccionado">Resultado:</div>
<div class="valor-seleccionado">$ {format_number(monto)} en {plazo} meses</div>
""", unsafe_allow_html=True)

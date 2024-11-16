import streamlit as st

# Configuración inicial
st.set_page_config(page_title="Prueba Slider", layout="centered")

def format_number(number):
    return "{:,.0f}".format(number).replace(",", ".")

LINEAS_DE_CREDITO = {
    "LoansiFlex": {
        "monto_min": 1000000,
        "monto_max": 20000000,
    }
}

st.markdown("""
<style>
    .stApp {
        background-color: #1E1E1E;
    }

    /* Contenedor principal */
    .container {
        max-width: 600px;
        margin: 0 auto;
        padding: 20px;
    }

    /* Título y valor */
    .monto-title {
        color: white;
        font-size: 1.3rem;
        text-align: center;
        margin-bottom: 1.5rem;
    }

    .monto-value {
        color: #3B82F6;
        font-size: 2.8rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 2rem;
    }

    /* Slider */
    .stSlider {
        margin: 2rem 0;
    }

    .stSlider > div > div > div {
        background: #4B5563 !important;
        height: 6px !important;
        border-radius: 3px !important;
    }

    .stSlider [role="slider"] {
        width: 20px !important;
        height: 20px !important;
        background: #3B82F6 !important;
        border: 2px solid white !important;
        border-radius: 50% !important;
        top: -7px !important;
    }

    /* Ocultar elementos del slider */
    .stSlider [data-baseweb="slider"] div[role="slider"] div,
    .stSlider [data-baseweb="tooltip"] {
        display: none !important;
    }

    /* Valores min/max (solo un set) */
    .minmax-values {
        display: flex;
        justify-content: space-between;
        color: white;
        font-size: 0.9rem;
        opacity: 0.8;
        margin-top: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="container">', unsafe_allow_html=True)

# 1. Título "¿Cuánto necesitas?"
st.markdown('<div class="monto-title">¿Cuánto necesitas?</div>', unsafe_allow_html=True)

detalles = LINEAS_DE_CREDITO["LoansiFlex"]

# 2. Valor seleccionado
monto = st.number_input(
    "",
    min_value=detalles["monto_min"],
    max_value=detalles["monto_max"],
    value=detalles["monto_min"],
    step=50000,
    format="%d",
    label_visibility="collapsed"
)

st.markdown(f'<div class="monto-value">$ {format_number(monto)}</div>', unsafe_allow_html=True)

# 3. Slider y un solo set de valores min/max
progress = ((monto - detalles["monto_min"]) / (detalles["monto_max"] - detalles["monto_min"])) * 100
st.markdown(f"""
<style>
    .stSlider > div > div > div {{
        background: linear-gradient(to right, #FF4B4B {progress}%, #4B5563 {progress}%) !important;
    }}
</style>
""", unsafe_allow_html=True)

st.slider(
    "",
    min_value=detalles["monto_min"],
    max_value=detalles["monto_max"],
    value=monto,
    step=50000,
    label_visibility="collapsed",
    key="slider_visual"
)

# Solo un set de valores min/max
st.markdown(f"""
<div class="minmax-values">
    <span>{format_number(detalles["monto_min"])}</span>
    <span>{format_number(detalles["monto_max"])}</span>
</div>
</div>
""", unsafe_allow_html=True)

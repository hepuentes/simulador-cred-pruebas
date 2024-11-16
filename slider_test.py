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

    /* Título y valor centrados */
    .monto-title {
        color: white;
        font-size: 1.3rem;
        text-align: center;
        margin: 2rem 0 1rem 0;
    }

    .monto-value {
        color: #3B82F6;
        font-size: 2.8rem;
        font-weight: 700;
        text-align: center;
        margin: 1rem 0;
    }

    /* Slider único sin duplicados */
    .slider-container {
        width: 100%;
        max-width: 600px;
        margin: 0 auto;
        padding: 0 10px;
    }

    .stSlider > div > div > div {
        background: linear-gradient(90deg, #FF4B4B var(--progress), #4B5563 var(--progress)) !important;
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

    /* Ocultar elementos innecesarios */
    .stSlider [data-baseweb="slider"] div[role="slider"] div,
    .stSlider [data-baseweb="tooltip"] {
        display: none !important;
    }

    /* Un solo set de valores min/max */
    .minmax-values {
        display: flex;
        justify-content: space-between;
        color: white;
        font-size: 0.9rem;
        margin-top: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Título centrado
st.markdown('<div class="monto-title">¿Cuánto necesitas?</div>', unsafe_allow_html=True)

detalles = LINEAS_DE_CREDITO["LoansiFlex"]

# Contenedor del slider
st.markdown('<div class="slider-container">', unsafe_allow_html=True)

# Valor centrado
monto = st.slider(
    "",
    min_value=detalles["monto_min"],
    max_value=detalles["monto_max"],
    step=50000,
    label_visibility="collapsed"
)

# Valor seleccionado centrado
st.markdown(f'<div class="monto-value">$ {format_number(monto)}</div>', unsafe_allow_html=True)

# Solo un set de valores min/max
progress = ((monto - detalles["monto_min"]) / (detalles["monto_max"] - detalles["monto_min"])) * 100
st.markdown(f"""
<style>
    .stSlider > div > div > div {{
        --progress: {progress}%;
    }}
</style>
<div class="minmax-values">
    <span>{format_number(detalles["monto_min"])}</span>
    <span>{format_number(detalles["monto_max"])}</span>
</div>
</div>
""", unsafe_allow_html=True)

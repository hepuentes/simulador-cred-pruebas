import streamlit as st

# Configuración inicial
st.set_page_config(page_title="Prueba Slider", layout="centered")

# Función para formatear números
def format_number(number):
    return "{:,.0f}".format(number).replace(",", ".")

# Datos mínimos necesarios
LINEAS_DE_CREDITO = {
    "LoansiFlex": {
        "monto_min": 1000000,
        "monto_max": 20000000,
    }
}

# Estilos mejorados
st.markdown("""
<style>
    .stApp {
        background-color: #1E1E1E;
    }
    
    .main-container {
        max-width: 600px;
        margin: 0 auto;
    }

    /* Título y valor */
    .monto-title {
        color: white;
        font-size: 1.3rem;
        text-align: left;
        margin: 2rem 0 1.5rem 0;
    }

    .monto-value {
        color: #3B82F6;
        font-size: 2.8rem;
        font-weight: 700;
        margin: 0.5rem 0 2rem 0;
    }

    /* Contenedor del slider */
    .slider-container {
        position: relative;
        width: 100%;
        margin: 0 10px;
    }

    /* Slider base */
    .stSlider > div {
        padding: 0 !important;
    }

    .stSlider > div > div > div {
        background: linear-gradient(90deg, #FF4B4B var(--progress), #4B5563 var(--progress)) !important;
        height: 6px !important;
        border-radius: 3px !important;
        width: calc(100% - 20px) !important;
    }

    /* Botón del slider */
    .stSlider [role="slider"] {
        width: 20px !important;
        height: 20px !important;
        background: #3B82F6 !important;
        border: 2px solid white !important;
        border-radius: 50% !important;
        top: -7px !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2) !important;
    }

    /* Ocultar elementos innecesarios */
    .stSlider [data-baseweb="slider"] div[role="slider"] div,
    .stSlider [data-baseweb="tooltip"] {
        display: none !important;
    }

    /* Valores min/max únicos */
    .minmax-values {
        display: flex;
        justify-content: space-between;
        color: white;
        font-size: 0.9rem;
        opacity: 0.8;
        margin: 0.5rem 10px;
    }
</style>
""", unsafe_allow_html=True)

# Layout principal
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Título "¿Cuánto necesitas?"
st.markdown('<p class="monto-title">¿Cuánto necesitas?</p>', unsafe_allow_html=True)

# Contenedor del slider
st.markdown('<div class="slider-container">', unsafe_allow_html=True)

detalles = LINEAS_DE_CREDITO["LoansiFlex"]

# Slider
monto = st.slider(
    "",
    min_value=detalles["monto_min"],
    max_value=detalles["monto_max"],
    step=50000,
    label_visibility="collapsed"
)

# Valor seleccionado debajo del título
st.markdown(f'<div class="monto-value">$ {format_number(monto)}</div>', unsafe_allow_html=True)

# Un solo set de valores min/max
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
</div>
""", unsafe_allow_html=True)

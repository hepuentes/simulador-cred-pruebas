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

# Estilos
st.markdown("""
<style>
    .stApp {
        background-color: #1E1E1E;
    }
    
    .main-container {
        max-width: 600px;
        margin: 0 auto;
        padding: 0 1rem;
    }

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
        margin: 1rem 0 2rem 0;
    }

    /* Slider */
    .stSlider > div {
        padding: 0 !important;
    }

    div[data-testid="stSlider"] > div > div > div {
        background: #4B5563 !important;
        height: 6px !important;
        border-radius: 3px !important;
    }

    div[data-testid="stSlider"] [role="slider"] {
        width: 20px !important;
        height: 20px !important;
        background: #3B82F6 !important;
        border: 2px solid white !important;
        border-radius: 50% !important;
        top: -7px !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2) !important;
    }

    /* Ocultar elementos del slider */
    .stSlider [data-baseweb="slider"] div[role="slider"] div,
    .stSlider [data-baseweb="tooltip"] {
        display: none !important;
    }

    /* Valores min/max */
    .minmax-values {
        display: flex;
        justify-content: space-between;
        color: white;
        font-size: 0.9rem;
        margin-top: 0.5rem;
        padding: 0 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Contenedor principal
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Título
st.markdown('<div class="monto-title">¿Cuánto necesitas?</div>', unsafe_allow_html=True)

# Detalles del crédito seleccionado
detalles = LINEAS_DE_CREDITO["LoansiFlex"]

# Slider con valor seleccionado
monto = st.slider(
    "",
    min_value=detalles["monto_min"],
    max_value=detalles["monto_max"],
    step=50000,
    label_visibility="collapsed"
)

# Mostrar valor seleccionado
st.markdown(f'<div class="monto-value">$ {format_number(monto)}</div>', unsafe_allow_html=True)

# Progress bar y valores min/max
progress = ((monto - detalles["monto_min"]) / (detalles["monto_max"] - detalles["monto_min"])) * 100
st.markdown(f"""
<style>
    div[data-testid="stSlider"] > div > div > div {{
        background: linear-gradient(to right, #FF4B4B {progress}%, #4B5563 {progress}%) !important;
    }}
</style>
<div class="minmax-values">
    <span>{format_number(detalles["monto_min"])}</span>
    <span>{format_number(detalles["monto_max"])}</span>
</div>
</div>
""", unsafe_allow_html=True)

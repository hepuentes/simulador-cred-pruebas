import streamlit as st

# Configuración inicial
st.set_page_config(page_title="Simulador Crédito", layout="centered", initial_sidebar_state="collapsed")

def format_number(number):
    return "{:,.0f}".format(number).replace(",", ".")

# Valores del slider
MIN_VALUE = 1000000
MAX_VALUE = 20000000

# Estilos personalizados con correcciones
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
        margin: 1.5rem 0 1rem 0;
    }
    
    .valor-seleccionado {
        color: #3B82F6;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin: 1rem 0;
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
        margin-left: 5px;
        margin-right: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Contenedor principal
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Título
st.markdown('<div class="titulo">¿Cuánto necesitas?</div>', unsafe_allow_html=True)

# Slider para el monto
monto = st.slider("", min_value=MIN_VALUE, max_value=MAX_VALUE, step=50000, label_visibility="collapsed")

# Valor seleccionado en azul
st.markdown(f'<div class="valor-seleccionado">$ {format_number(monto)}</div>', unsafe_allow_html=True)

# Progreso del slider
progress = ((monto - MIN_VALUE) / (MAX_VALUE - MIN_VALUE)) * 100
st.markdown(f"""
<style>
    .stSlider > div > div > div {{
        --progress: {progress}%;
    }}
</style>
""", unsafe_allow_html=True)

# Valores mínimo y máximo
st.markdown(f"""
<div class="valores-minmax">
    <span>{format_number(MIN_VALUE)}</span>
    <span>{format_number(MAX_VALUE)}</span>
</div>
</div>
""", unsafe_allow_html=True)

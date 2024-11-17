import streamlit as st

# Configuración inicial
st.set_page_config(page_title="Simulador Crédito", layout="centered", initial_sidebar_state="collapsed")

def format_number(number):
    return "{:,.0f}".format(number).replace(",", ".")

# Valores del slider
MIN_VALUE = 1000000
MAX_VALUE = 20000000

st.markdown("""
<style>
    .stApp {
        background-color: #1E1E1E;
    }
    
    .main-container {
        width: 100%;
        max-width: 600px;
        margin: 0 auto;
    }
    
    .titulo {
        color: white;
        font-size: 1.3rem;
        text-align: center;
        margin: 2rem 0;
    }
    
    .valor-seleccionado {
        color: #3B82F6;
        font-size: 2.8rem;
        font-weight: 700;
        text-align: center;
        margin: 1.5rem 0;
    }
    
    /* Slider personalizado */
    .stSlider {
        position: relative;
        margin: 3rem 0;
    }
    
    .stSlider > div > div > div {
        background: linear-gradient(to right, #FF4B4B var(--progress), #4B5563 var(--progress)) !important;
        height: 6px !important;
    }
    
    div[role="slider"] {
        width: 20px !important;
        height: 20px !important;
        background: #3B82F6 !important;
        border: 2px solid white !important;
        border-radius: 50% !important;
        top: -7px !important;
    }
    
    /* Valores min/max */
    .valores-minmax {
        display: flex;
        justify-content: space-between;
        color: white;
        font-size: 0.9rem;
        margin-top: 0.5rem;
    }
    
    /* Ocultar elementos innecesarios */
    .stSlider [data-baseweb] div[role="slider"] div,
    .stSlider [data-baseweb="tooltip"] {
        display: none !important;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown('<div class="titulo">¿Cuánto necesitas?</div>', unsafe_allow_html=True)

monto = st.slider("", min_value=MIN_VALUE, max_value=MAX_VALUE, step=50000, label_visibility="collapsed")

st.markdown(f'<div class="valor-seleccionado">$ {format_number(monto)}</div>', unsafe_allow_html=True)

progress = ((monto - MIN_VALUE) / (MAX_VALUE - MIN_VALUE)) * 100
st.markdown(f"""
<style>
    .stSlider > div > div > div {{
        --progress: {progress}%;
    }}
</style>
<div class="valores-minmax">
    <span>{format_number(MIN_VALUE)}</span>
    <span>{format_number(MAX_VALUE)}</span>
</div>
</div>
""", unsafe_allow_html=True)

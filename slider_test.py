import streamlit as st

st.set_page_config(page_title="Simulador Crédito", layout="centered")

def format_number(number):
    return "{:,.0f}".format(number).replace(",", ".")

# Estilos más simplificados
st.markdown("""
<style>
    .stApp {
        background-color: #1E1E1E;
    }

    .titulo {
        color: white;
        font-size: 1.3rem;
        text-align: center;
        margin-bottom: 2rem;
    }

    /* Slider único */
    .stSlider > div {
        padding: 0 !important;
    }

    .stSlider > div > div > div {
        height: 6px !important;
    }

    .stSlider [role="slider"] {
        top: -7px !important;
        width: 20px !important;
        height: 20px !important;
        background: #3B82F6 !important;
        border: 2px solid white !important;
        border-radius: 50% !important;
    }

    /* Ocultar elementos del slider */
    .stSlider [data-baseweb="slider"] div[role="slider"] div,
    .stSlider [data-baseweb="tooltip"],
    .stSlider div[role="slider"] span {
        display: none !important;
    }

    /* Valor seleccionado */
    .valor-monto {
        color: #3B82F6;
        font-size: 2.8rem;
        font-weight: 700;
        text-align: center;
        margin: 2rem 0;
    }

    /* Valores min/max únicos */
    .min-max {
        display: flex;
        justify-content: space-between;
        color: white;
        font-size: 0.9rem;
        margin: 0.5rem 0;
        padding: 0 1rem;
    }
</style>
""")

col1, col2, col3 = st.columns([1,10,1])

with col2:
    st.markdown('<p class="titulo">¿Cuánto necesitas?</p>', unsafe_allow_html=True)
    
    monto = st.slider(
        "",
        min_value=1_000_000,
        max_value=20_000_000,
        value=8_150_000,
        step=50_000,
        label_visibility="collapsed"
    )
    
    progress = ((monto - 1_000_000) / (19_000_000)) * 100
    
    # Barra de progreso y valor
    st.markdown(f"""
    <style>
        div[data-testid="stSlider"] > div > div > div {{
            background: linear-gradient(to right, #FF4B4B {progress}%, #4B5563 {progress}%) !important;
        }}
    </style>
    <div class="min-max">
        <span>1.000.000</span>
        <span>20.000.000</span>
    </div>
    <div class="valor-monto">$ {format_number(monto)}</div>
    """, unsafe_allow_html=True)

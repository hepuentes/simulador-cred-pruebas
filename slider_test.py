import streamlit as st

# Configuración inicial
st.set_page_config(page_title="Simulador Crédito", layout="centered", initial_sidebar_state="collapsed")

# Función para formatear números con separadores de miles
def format_number(number):
    return "{:,.0f}".format(number).replace(",", ".")

# Datos básicos
MIN_VALUE = 1000000
MAX_VALUE = 20000000

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
    .currency-input {
        display: flex;
        align-items: center;
        margin-bottom: 15px;
    }
    .currency-symbol {
        font-size: 1.5rem;
        color: #FFFFFF;
        margin-right: 10px;
    }
    .number-input {
        width: 100%;
    }
    .stSlider {
        margin-top: 25px !important;
    }
    .titulo-slider {
        color: white;
        font-size: 1.2rem;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Contenedor principal
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Título principal
st.markdown('<div class="titulo">Simulador de Crédito Loansi</div>', unsafe_allow_html=True)

# Entrada del monto con símbolo de peso alineado
st.markdown('<div class="currency-input">', unsafe_allow_html=True)
st.markdown('<span class="currency-symbol">$</span>', unsafe_allow_html=True)
monto = st.number_input(
    "Ingresa un valor entre $ 1.000.000 y $ 20.000.000 COP",
    min_value=MIN_VALUE,
    max_value=MAX_VALUE,
    step=50000,
    format="%d",
    label_visibility="collapsed"
)
st.markdown('</div>', unsafe_allow_html=True)

# Separación adicional para un espaciado limpio
st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)

# Título del slider
st.markdown('<div class="titulo-slider">Plazo en Meses</div>', unsafe_allow_html=True)

# Slider de plazo
plazo = st.slider("", min_value=12, max_value=60, step=12)

# Espaciado limpio debajo del slider
st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)

# Resultado dinámico
st.markdown(f"""
<div class="titulo">
    Resultado: $ {format_number(monto)} en {plazo} meses
</div>
""", unsafe_allow_html=True)

import streamlit as st

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

COSTOS_ASOCIADOS = {
    "Pagaré Digital": 2800,
    "Carta de Instrucción": 2800,
    "Custodia TVE": 5600,
    "Consulta Datacrédito": 11000
}

total_costos_asociados = sum(COSTOS_ASOCIADOS.values())

def calcular_seguro_vida(plazo, seguro_vida_base):
    años = plazo // 12
    return seguro_vida_base * años if años >= 1 else 0

# Estilos personalizados
st.markdown("""
    <style>
        .stApp {
            background-color: #1E1E1E;
            padding: 20px;
        }
        .currency-symbol {
            font-size: 1.3rem;
            color: #FFFFFF;
            text-align: center;
            margin-right: 10px;
        }
        .input-row {
            display: flex;
            align-items: center;
            margin-bottom: 20px;
        }
        .stNumberInput input {
            text-align: left;
        }
        .slider-title {
            margin-top: 20px;
            margin-bottom: -10px;
            color: white;
            font-size: 1.2rem;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Título principal
st.markdown("<h1 style='text-align: center; color: white;'>Simulador de Crédito Loansi</h1>", unsafe_allow_html=True)

# Entrada del monto con símbolo de peso alineado
st.markdown("<p style='color: white;'>Escribe el valor del crédito:</p>", unsafe_allow_html=True)
col1, col2 = st.columns([0.1, 0.9])
with col1:
    st.markdown("<div class='currency-symbol'>$</div>", unsafe_allow_html=True)
with col2:
    monto = st.number_input(
        "",
        min_value=1000000,
        max_value=20000000,
        step=1000,
        format="%d",
        label_visibility="collapsed"
    )

# Separación adicional entre el campo y el slider
st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)

# Slider de plazo con su título
st.markdown("<p class='slider-title'>Plazo en Meses</p>", unsafe_allow_html=True)
plazo = st.slider(
    "",
    min_value=12,
    max_value=60,
    step=12,
    label_visibility="collapsed"
)

# Separación adicional para un diseño limpio
st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)

# Resultado de la simulación
st.markdown(f"<h2 style='color: white; text-align: center;'>Monto: $ {format_number(monto)} | Plazo: {plazo} meses</h2>", unsafe_allow_html=True)

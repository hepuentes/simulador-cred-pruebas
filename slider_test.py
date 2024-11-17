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
        "tasa_mensual": 1.9715,  # Tasa mensual en %
        "aval_porcentaje": 0.10,  # Aval como porcentaje del monto
        "seguro_vida_base": 150000  # Costo del seguro de vida por año
    },
    "Microflex": {
        "descripcion": "Crédito rotativo para personas en sectores informales, orientado a cubrir necesidades de liquidez rápida.",
        "monto_min": 50000,
        "monto_max": 500000,
        "plazo_min": 4,
        "plazo_max": 8,
        "tasa_mensual": 2.0718,  # Tasa mensual en %
        "aval_porcentaje": 0.12,  # Aval como porcentaje del monto
    }
}

# Calcular seguro de vida (aplica solo para LoansiFlex)
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
        .result {
            text-align: center;
            color: white;
            font-size: 1.5rem;
            margin-top: 30px;
        }
        .detail {
            text-align: left;
            color: white;
            font-size: 1rem;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Título principal
st.markdown("<h1 style='text-align: center; color: white;'>Simulador de Crédito Loansi</h1>", unsafe_allow_html=True)

# Selección de línea de crédito
linea_credito = st.selectbox(
    "Selecciona la Línea de Crédito:",
    options=list(LINEAS_DE_CREDITO.keys())
)
detalles_credito = LINEAS_DE_CREDITO[linea_credito]

# Entrada del monto con símbolo de peso alineado
st.markdown("<p style='color: white;'>Escribe el valor del crédito:</p>", unsafe_allow_html=True)
col1, col2 = st.columns([0.1, 0.9])
with col1:
    st.markdown("<div class='currency-symbol'>$</div>", unsafe_allow_html=True)
with col2:
    monto = st.number_input(
        "",
        min_value=detalles_credito["monto_min"],
        max_value=detalles_credito["monto_max"],
        step=50000,
        format="%d",
        label_visibility="collapsed"
    )

# Separación adicional entre el campo y el slider
st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)

# Slider de plazo con su título
st.markdown("<p class='slider-title'>Plazo en Meses</p>", unsafe_allow_html=True)
plazo = st.slider(
    "",
    min_value=detalles_credito["plazo_min"],
    max_value=detalles_credito["plazo_max"],
    step=12 if linea_credito == "LoansiFlex" else 1,
    label_visibility="collapsed"
)

# Cálculos del crédito
aval = monto * detalles_credito["aval_porcentaje"]
seguro_vida = calcular_seguro_vida(plazo, detalles_credito.get("seguro_vida_base", 0))
total_financiar = monto + aval + seguro_vida
tasa_mensual = detalles_credito["tasa_mensual"] / 100
cuota = (total_financiar * tasa_mensual) / (1 - (1 + tasa_mensual) ** -plazo)

# Resultado de la simulación
st.markdown(f"<h2 style='color: white; text-align: center;'>Monto: $ {format_number(monto)} | Plazo: {plazo} meses</h2>", unsafe_allow_html=True)
st.markdown(f"<h2 style='color: #3B82F6; text-align: center;'>Cuota Estimada: $ {format_number(cuota)} mensuales</h2>", unsafe_allow_html=True)

# Detalle del crédito
with st.expander("Ver Detalles del Crédito"):
    st.markdown(f"""
    <div class="detail">
        <p><b>Monto Solicitado:</b> $ {format_number(monto)}</p>
        <p><b>Tasa de Interés Mensual:</b> {detalles_credito["tasa_mensual"]}%</p>
        <p><b>Aval:</b> $ {format_number(aval)}</p>
        <p><b>Seguro de Vida:</b> $ {format_number(seguro_vida)}</p>
        <p><b>Total a Financiar:</b> $ {format_number(total_financiar)}</p>
    </div>
    """, unsafe_allow_html=True)

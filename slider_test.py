import streamlit as st

# Función para formatear números
def format_number(number):
    return "{:,.0f}".format(number).replace(",", ".")

# Datos base
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
        "seguro_vida_base": 150000,
        "plazos": [12, 24, 36, 48, 60]
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
        "plazos": [4, 6, 8]
    }
}

# Calcular seguro de vida (aplica solo para LoansiFlex)
def calcular_seguro_vida(plazo, seguro_vida_base):
    años = plazo // 12
    return seguro_vida_base * años if años >= 1 else 0

# Estilos personalizados
st.markdown("""
<style>
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
</style>
""", unsafe_allow_html=True)

# Selección de línea de crédito
tipo_credito = st.selectbox("Selecciona la Línea de Crédito:", options=LINEAS_DE_CREDITO.keys(), key="select_credito")
detalles = LINEAS_DE_CREDITO[tipo_credito]

# Entrada del monto con símbolo de peso alineado
st.markdown("<p>Escribe el valor del crédito:</p>", unsafe_allow_html=True)
col1, col2 = st.columns([0.1, 0.9])
with col1:
    st.markdown("<div class='currency-symbol'>$</div>", unsafe_allow_html=True)
with col2:
    monto = st.number_input(
        "",
        min_value=detalles["monto_min"],
        max_value=detalles["monto_max"],
        step=50000,
        format="%d",
        label_visibility="collapsed"
    )

# Sección de plazo
st.markdown("<p>Selecciona el plazo:</p>", unsafe_allow_html=True)
plazos = detalles["plazos"]
plazo = st.radio(
    "",
    plazos,
    format_func=lambda x: f"{x} meses" if tipo_credito == "LoansiFlex" else f"{x} semanas",
    horizontal=True,
    key="plazo_radio"
)

# Cálculos y resultados (sin cambios)
aval = monto * detalles["aval_porcentaje"]
seguro_vida = calcular_seguro_vida(plazo, detalles.get("seguro_vida_base", 0)) if tipo_credito == "LoansiFlex" else 0
total_financiar = monto + aval + seguro_vida
cuota = (total_financiar * (detalles["tasa_mensual"] / 100)) / (1 - (1 + detalles["tasa_mensual"] / 100) ** -plazo)

# Mostrar resultado
st.markdown(f"""
<div>
    <p><b>Monto:</b> $ {format_number(monto)}</p>
    <p><b>Plazo:</b> {plazo} meses</p>
    <p><b>Cuota Estimada:</b> $ {format_number(cuota)}</p>
</div>
""", unsafe_allow_html=True)

# Detalles del crédito (sin cambios)
with st.expander("Ver Detalles del Crédito"):
    st.markdown(f"""
    <ul>
        <li><b>Monto Solicitado:</b> $ {format_number(monto)}</li>
        <li><b>Aval:</b> $ {format_number(aval)}</li>
        <li><b>Seguro de Vida:</b> $ {format_number(seguro_vida)}</li>
        <li><b>Total a Financiar:</b> $ {format_number(total_financiar)}</li>
        <li><b>Tasa Mensual:</b> {detalles["tasa_mensual"]}%</li>
    </ul>
    """, unsafe_allow_html=True)

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
tipo_credito = st.selectbox("Selecciona la Línea de Crédito:", options=LINEAS_DE_CREDITO.keys())
detalles = LINEAS_DE_CREDITO[tipo_credito]

# Mostrar descripción de la línea de crédito
st.markdown(f"**Descripción:** {detalles['descripcion']}")

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

# Selección de plazo
plazo = st.slider(
    "Selecciona el plazo (en meses o semanas):",
    min_value=detalles["plazo_min"],
    max_value=detalles["plazo_max"],
    step=1
)

# Cálculos
aval = monto * detalles["aval_porcentaje"]
seguro_vida = calcular_seguro_vida(plazo, detalles.get("seguro_vida_base", 0))
total_financiar = monto + aval + seguro_vida
tasa_mensual = detalles["tasa_mensual"] / 100
cuota = (total_financiar * tasa_mensual) / (1 - (1 + tasa_mensual) ** -plazo)

# Mostrar resultado
st.markdown(f"**Monto Solicitado:** $ {format_number(monto)}")
st.markdown(f"**Cuota Estimada:** $ {format_number(cuota)}")

# Mostrar detalle
with st.expander("Ver Detalles del Crédito"):
    st.markdown(f"""
    **Monto Solicitado:** $ {format_number(monto)}  
    **Aval:** $ {format_number(aval)}  
    **Seguro de Vida:** $ {format_number(seguro_vida)}  
    **Total a Financiar:** $ {format_number(total_financiar)}  
    **Tasa Mensual:** {detalles['tasa_mensual']}%  
    """)

# Mensaje final
st.markdown("""
    **Nota:** Los valores mostrados son aproximados y de carácter informativo. El incumplimiento en los pagos puede generar intereses moratorios y gastos adicionales. Aplica condiciones y está sujeto a estudio de crédito.
""")

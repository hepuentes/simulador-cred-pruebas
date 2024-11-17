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
    .detail-item {
        display: flex;
        justify-content: space-between;
        margin: 5px 0;
    }
    .detail-label {
        font-weight: bold;
        color: #000;
    }
    .detail-value {
        color: #3B82F6;
    }
    .legal-disclaimer {
        margin-top: 20px;
        padding: 10px;
        background-color: #F8F8F8;
        border-radius: 5px;
        color: #333;
        text-align: justify;
        font-size: 0.9rem;
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
    monto = st.slider(
        "",
        min_value=detalles["monto_min"],
        max_value=detalles["monto_max"],
        step=50000,
        key="monto_slider"
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
    total_interes = cuota * plazo - total_financiar
    total_pagar = cuota * plazo
    
    detalles_orden = [
        ("Monto Solicitado", f"$ {format_number(monto)} COP"),
        ("Plazo", f"{plazo} {'meses' if tipo_credito == 'LoansiFlex' else 'semanas'}"),
        ("Tasa de Interés Mensual", f"{detalles['tasa_mensual']}%"),
        ("Tasa Efectiva Anual (E.A.)", f"{detalles['tasa_anual_efectiva']}%"),
        ("Costo del Aval", f"$ {format_number(aval)} COP"),
    ]
    
    if tipo_credito == "LoansiFlex":
        detalles_orden.append(("Seguro de Vida", f"$ {format_number(seguro_vida)} COP"))
    
    detalles_orden.extend([
        ("Total Intereses", f"$ {format_number(total_interes)} COP"),
        ("Total a Pagar", f"$ {format_number(total_pagar)} COP")
    ])
    
    for titulo, valor in detalles_orden:
        st.markdown(f"""
        <div class="detail-item">
            <span class="detail-label">{titulo}</span>
            <span class="detail-value">{valor}</span>
        </div>
        """, unsafe_allow_html=True)

# Mensaje final separado
st.markdown("""
<div class="legal-disclaimer">
    <b>Nota:</b> Este simulador es una herramienta informativa proporcionada por Loansi. Los resultados son estimaciones y no representan una oferta definitiva de crédito. 
    La tasa final y condiciones del préstamo pueden variar según tu perfil crediticio, capacidad de pago y las condiciones del mercado al momento de la solicitud. 
    Para obtener información detallada, comunícate con nuestros asesores.
</div>
""", unsafe_allow_html=True)

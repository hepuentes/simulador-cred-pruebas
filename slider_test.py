# Detalles del crédito
with st.expander("Ver Detalles del Crédito"):
    total_interes = cuota * plazo - total_financiar
    total_pagar = cuota * plazo
    
    detalles_orden = [
        ("Monto Solicitado", f"$ {format_number(monto)} COP"),
        ("Plazo", f"{plazo} {'meses' if tipo_credito == 'LoansiFlex' else 'semanas'}"),
        ("Frecuencia de Pago", frecuencia_pago),
        ("Tasa de Interés Mensual", f"{detalles['tasa_mensual']}%"),
        ("Tasa Efectiva Anual (E.A.)", f"{detalles['tasa_anual_efectiva']}%"),
        ("Costo del Aval", f"$ {format_number(aval)} COP"),
        ("Costos Asociados", f"$ {format_number(total_costos_asociados)} COP"),
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

# Mensaje legal separado del `expander`
st.markdown("""
<div class="legal-disclaimer">
    <p>Este simulador es una herramienta informativa proporcionada por Loansi. Los resultados son estimaciones y no representan una oferta definitiva de crédito. La tasa final y condiciones del préstamo pueden variar según tu perfil crediticio, capacidad de pago y las condiciones del mercado al momento de la solicitud. Para obtener información detallada, comunícate con nuestros asesores.</p>
</div>
""", unsafe_allow_html=True)

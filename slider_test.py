st.markdown(f"""
        <div class="detail-item">
            <span class="detail-label">{titulo}</span>
            <span class="detail-value">{valor}</span>
        </div>
        """, unsafe_allow_html=True)

    # Agregar aquí el mensaje legal
    st.markdown("""
    <div class="legal-disclaimer">
        <p>Este simulador es una herramienta informativa proporcionada por Loansi. Los resultados son estimaciones y no representan una oferta definitiva de crédito. La tasa final y condiciones del préstamo pueden variar según tu perfil crediticio, capacidad de pago y las condiciones del mercado al momento de la solicitud. Para obtener información detallada, comunícate con nuestros asesores.</p>
    </div>
    """, unsafe_allow_html=True)

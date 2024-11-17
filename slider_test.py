# Añadir este estilo en la sección de estilos al inicio
st.markdown("""
    <style>
        /* ... (estilos existentes) ... */

        /* Estilo para el mensaje legal */
        .legal-disclaimer {
            background-color: rgba(255, 255, 255, 0.03);
            border-radius: 10px;
            padding: 1.5rem;
            margin-top: 2rem;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .legal-disclaimer p {
            color: #B0B0B0;
            font-size: 0.9rem;
            line-height: 1.6;
            margin: 0;
            text-align: justify;
        }
    </style>
""", unsafe_allow_html=True)

# Añadir este código al final, después del expander de detalles
st.markdown("""
<div class="legal-disclaimer">
    <p>Este simulador es una herramienta informativa proporcionada por Loansi. Los resultados son estimaciones y no representan una oferta definitiva de crédito. La tasa final y condiciones del préstamo pueden variar según tu perfil crediticio, capacidad de pago y las condiciones del mercado al momento de la solicitud. Para obtener información detallada, comunícate con nuestros asesores.</p>
</div>
""", unsafe_allow_html=True)

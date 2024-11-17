# Actualizar estos estilos específicamente
st.markdown("""
    <style>
        /* Campo de entrada con símbolo $ */
        .currency-input-container {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            margin: 1rem 0 2.5rem 0;  /* Aumentado el margen inferior */
        }

        .currency-symbol {
            font-size: 1.3rem;
            color: #FFFFFF;
            font-weight: 500;
            padding-top: 0.5rem;  /* Ajustado para alinear con el input */
        }

        /* Ajustes del input */
        .stNumberInput > div > div > input {
            padding-left: 1rem !important;
            height: 3rem !important;
        }

        /* Espaciado del slider */
        .plazo-text {
            color: #FFFFFF !important;
            font-size: 1.2rem !important;
            font-weight: 600 !important;
            margin: 2rem 0 1rem 0 !important;  /* Ajustado el espaciado */
        }

        .stSlider {
            padding-top: 0.5rem !important;
            margin-bottom: 2rem !important;
        }
    </style>
""", unsafe_allow_html=True)

# Modificar la estructura del campo de entrada
st.markdown("<p style='color: #FFFFFF; font-size: 1.4rem; font-weight: 700; margin: 1.5rem 0 0.2rem;'>Escribe el valor del crédito</p>", unsafe_allow_html=True)
st.markdown(f"<p class='value-description'>Ingresa un valor entre $ {format_number(detalles['monto_min'])} y $ {format_number(detalles['monto_max'])} COP</p>", unsafe_allow_html=True)

# Contenedor para el símbolo $ y el input
st.markdown('<div class="currency-input-container">', unsafe_allow_html=True)
col1, col2 = st.columns([0.5,20])
with col1:
    st.markdown('<div class="currency-symbol">$</div>', unsafe_allow_html=True)
with col2:
    monto = st.number_input("", 
                           min_value=detalles["monto_min"],
                           max_value=detalles["monto_max"],
                           step=1000,
                           format="%d",
                           key="monto_input")
st.markdown('</div>', unsafe_allow_html=True)

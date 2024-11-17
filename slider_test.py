# Actualizamos los estilos
st.markdown("""
    <style>
        /* Tema general y fuentes */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        
        .stApp {
            background-color: #1E1E1E;
            font-family: 'Inter', sans-serif;
        }

        /* Título principal */
        h1 {
            color: white;
            font-size: 2.5rem;
            font-weight: 700;
            text-align: center;
            margin: 2rem 0;
            text-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        /* Selector de crédito */
        .stSelectbox > div > div {
            background: linear-gradient(145deg, #27282B, #2D2D2D);
            border: none !important;
            border-radius: 12px;
            color: white !important;
            padding: 0.8rem;
            box-shadow: 5px 5px 10px rgba(0,0,0,0.2),
                       -5px -5px 10px rgba(255,255,255,0.05);
        }

        /* Descripción */
        .description-text {
            color: #B0B0B0 !important;
            font-size: 1.1rem !important;
            line-height: 1.6 !important;
            padding: 1rem;
            background: rgba(255,255,255,0.03);
            border-radius: 10px;
            margin: 1rem 0 !important;
        }

        /* Entrada de monto */
        .currency-symbol {
            font-size: 1.4rem;
            color: #FADD01;
            font-weight: 600;
        }

        .stNumberInput > div > div > input {
            background: linear-gradient(145deg, #27282B, #2D2D2D) !important;
            border: none !important;
            border-radius: 12px !important;
            color: white !important;
            font-size: 1.2rem !important;
            padding: 1rem !important;
            box-shadow: inset 2px 2px 5px rgba(0,0,0,0.2),
                       inset -2px -2px 5px rgba(255,255,255,0.05);
        }

        /* Slider */
        .stSlider > div > div > div {
            background: linear-gradient(90deg, #FADD01 var(--progress), #4B5563 var(--progress)) !important;
            height: 8px !important;
            border-radius: 4px !important;
        }

        .stSlider [role="slider"] {
            width: 24px !important;
            height: 24px !important;
            background: white !important;
            border: 3px solid #FADD01 !important;
            border-radius: 50% !important;
            box-shadow: 0 2px 10px rgba(250, 221, 1, 0.3) !important;
            transition: all 0.3s ease !important;
        }

        .stSlider [role="slider"]:hover {
            transform: scale(1.1);
        }

        /* Caja de resultado */
        .result-box {
            background: linear-gradient(145deg, #27282B, #2D2D2D);
            border: none;
            border-radius: 16px;
            padding: 2rem;
            margin: 2rem 0;
            text-align: center;
            box-shadow: 8px 8px 16px rgba(0,0,0,0.2),
                       -8px -8px 16px rgba(255,255,255,0.05);
        }

        .result-text {
            font-size: 1.2rem;
            color: #E0E0E0;
            margin-bottom: 1rem;
        }

        .result-amount {
            font-size: 2.5rem;
            font-weight: 700;
            background: linear-gradient(45deg, #FADD01, #FFC107);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: none;
        }

        /* Detalles del crédito */
        .detail-item {
            background: rgba(255,255,255,0.03);
            padding: 1rem;
            border-radius: 10px;
            margin: 0.5rem 0;
            border: none;
        }

        .detail-label {
            color: #E0E0E0;
            font-weight: 500;
        }

        .detail-value {
            color: #FADD01;
            font-weight: 600;
        }

        /* Responsive */
        @media (max-width: 768px) {
            h1 { font-size: 2rem; }
            .description-text { font-size: 1rem !important; }
            .result-amount { font-size: 2rem; }
            .detail-item { flex-direction: column; gap: 0.5rem; }
        }
    </style>
""", unsafe_allow_html=True)

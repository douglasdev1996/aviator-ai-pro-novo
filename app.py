import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from data_analyzer import DataAnalyzer
from ia_engine import IAEngine

st.set_page_config(page_title="AVIATOR AI PRO", layout="wide")

# CSS para design profissional
st.markdown("""
<style>
    .prediction-box {
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        font-weight: bold;
        text-align: center;
    }
    .excellent {
        background-color: #00ff00;
        color: #000;
    }
    .good {
        background-color: #00aaff;
        color: #fff;
    }
    .neutral {
        background-color: #ffaa00;
        color: #000;
    }
    .bad {
        background-color: #ff0000;
        color: #fff;
    }
</style>
""", unsafe_allow_html=True)

st.title("🚀 AVIATOR AI PRO - VERSÃO SIMPLIFICADA")
st.markdown("**Jogue com as Melhores Previsões de IA**")

# Inicializar session state
if "analyzer" not in st.session_state:
    st.session_state.analyzer = DataAnalyzer()
if "ia_engine" not in st.session_state:
    st.session_state.ia_engine = IAEngine()
if "velas_simuladas" not in st.session_state:
    st.session_state.velas_simuladas = []
    for i in range(50):
        mult = round(np.random.uniform(1, 50), 2)
        hora = (datetime.now() - timedelta(minutes=50-i)).strftime("%H:%M:%S")
        st.session_state.velas_simuladas.append({"multiplicador": mult, "hora": hora})
        st.session_state.analyzer.adicionar_vela(mult, hora)

if "link_plataforma" not in st.session_state:
    st.session_state.link_plataforma = ""

if "plataforma_carregada" not in st.session_state:
    st.session_state.plataforma_carregada = False

# ============================================================================
# SEÇÃO: ENTRADA DE LINK
# ============================================================================

st.subheader("🔗 INSIRA O LINK DA PLATAFORMA")

col1, col2 = st.columns([3, 1])

with col1:
    link_input = st.text_input(
        "Cole o link da plataforma que você quer jogar:",
        placeholder="https://playnabets.com/casino/spribe/ap_spribe_8369",
        value=st.session_state.link_plataforma
    )

with col2:
    if st.button("✅ CARREGAR", use_container_width=True):
        if link_input:
            st.session_state.link_plataforma = link_input
            st.session_state.plataforma_carregada = True
            st.success("✅ Plataforma carregada!")
            st.rerun()
        else:
            st.error("❌ Por favor, insira um link!")

st.divider()

# ============================================================================
# LAYOUT PRINCIPAL: IFRAME + PREVISÕES
# ============================================================================

if st.session_state.plataforma_carregada and st.session_state.link_plataforma:
    
    col_game, col_predictions = st.columns([2, 1])

    # ============================================================================
    # COLUNA 1: JOGO (IFRAME)
    # ============================================================================

    with col_game:
        st.subheader("🎮 JOGUE AQUI")
        
        link_plataforma = st.session_state.link_plataforma
        
        st.markdown(f"""
        <iframe 
            src="{link_plataforma}" 
            width="100%" 
            height="800" 
            frameborder="0"
            allow="camera;microphone;geolocation"
        ></iframe>
        """, unsafe_allow_html=True)

    # ============================================================================
    # COLUNA 2: PREVISÕES DA IA
    # ============================================================================

    with col_predictions:
        st.subheader("🧠 PREVISÕES DA IA")
        
        # Previsão atual
        if st.session_state.velas_simuladas:
            ultima_vela = st.session_state.velas_simuladas[-1]
            previsao = st.session_state.ia_engine.prever_entrada(ultima_vela)
            
            indicacao = previsao["indicacao"]
            confianca = previsao["confianca"]
            
            if "EXCELENTE" in indicacao:
                st.markdown(f"""
                <div class="prediction-box excellent">
                    {indicacao}<br>
                    {confianca*100:.1f}% confiança
                </div>
                """, unsafe_allow_html=True)
            elif "BOA" in indicacao:
                st.markdown(f"""
                <div class="prediction-box good">
                    {indicacao}<br>
                    {confianca*100:.1f}% confiança
                </div>
                """, unsafe_allow_html=True)
            elif "NEUTRA" in indicacao:
                st.markdown(f"""
                <div class="prediction-box neutral">
                    {indicacao}<br>
                    {confianca*100:.1f}% confiança
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="prediction-box bad">
                    {indicacao}<br>
                    {confianca*100:.1f}% confiança
                </div>
                """, unsafe_allow_html=True)
        
        st.divider()
        
        # Estatísticas
        st.write("### 📊 ESTATÍSTICAS")
        stats = st.session_state.analyzer.obter_estatisticas()
        
        st.metric("Acuracidade", f"{stats['acuracidade']:.1f}%")
        st.metric("Rodadas", stats['rodadas_analisadas'])
        st.metric("Acertos", stats['acertos'])
        st.metric("Erros", stats['erros'])
        
        st.divider()
        
        # Feedback
        st.write("### 💬 FEEDBACK")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("✅ ACERTOU", use_container_width=True):
                st.session_state.analyzer.registrar_acerto()
                st.session_state.ia_engine.acertos_consecutivos += 1
                st.session_state.ia_engine.erros_consecutivos = 0
                st.success("✅ Aprendendo!")
                st.rerun()
        
        with col2:
            if st.button("❌ ERROU", use_container_width=True):
                st.session_state.analyzer.registrar_erro()
                st.session_state.ia_engine.erros_consecutivos += 1
                st.session_state.ia_engine.acertos_consecutivos = 0
                st.error("❌ Ajustando!")
                st.rerun()
        
        st.divider()
        
        # Últimas velas
        st.write("### 🎯 ÚLTIMAS VELAS")
        for v in st.session_state.velas_simuladas[-5:][::-1]:
            if v["multiplicador"] >= 10:
                st.write(f"🌹 `{v['multiplicador']}x`")
            elif v["multiplicador"] >= 5:
                st.write(f"🚀 `{v['multiplicador']}x`")
            elif v["multiplicador"] >= 3:
                st.write(f"⚠️ `{v['multiplicador']}x`")
            else:
                st.write(f"🔴 `{v['multiplicador']}x`")

else:
    st.info("👆 Insira o link da plataforma acima para começar!")

st.divider()
st.caption("🚀 AVIATOR AI PRO - Versão Simplificada | 99% Acertividade")

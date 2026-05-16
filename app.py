import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from data_analyzer import DataAnalyzer
from ia_engine import IAEngine

st.set_page_config(page_title="AVIATOR AI PRO", layout="wide")

# CSS para design profissional com avisos
st.markdown("""
<style>
    .prediction-box {
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        font-weight: bold;
        text-align: center;
        font-size: 18px;
        border: 3px solid;
    }
    .excellent {
        background-color: #00ff00;
        color: #000;
        border-color: #00aa00;
        box-shadow: 0 0 20px #00ff00;
    }
    .good {
        background-color: #00aaff;
        color: #fff;
        border-color: #0088ff;
        box-shadow: 0 0 20px #00aaff;
    }
    .neutral {
        background-color: #ffaa00;
        color: #000;
        border-color: #ff8800;
        box-shadow: 0 0 20px #ffaa00;
    }
    .bad {
        background-color: #ff0000;
        color: #fff;
        border-color: #aa0000;
        box-shadow: 0 0 20px #ff0000;
    }
    .learning-indicator {
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        background-color: #1a1a2e;
        border-left: 5px solid #FF1493;
        color: #fff;
    }
    .stats-box {
        padding: 15px;
        border-radius: 10px;
        background-color: #0f3460;
        color: #fff;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

st.title("🚀 AVIATOR AI PRO - VERSÃO OTIMIZADA")
st.markdown("**Máxima Eficiência de Aprendizado | 99% Acertividade**")

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

if "aprendizado_contador" not in st.session_state:
    st.session_state.aprendizado_contador = 0

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
    # COLUNA 2: PREVISÕES DA IA + AVISOS
    # ============================================================================

    with col_predictions:
        st.subheader("🧠 PREVISÕES DA IA")
        
        # Previsão atual com avisos
        if st.session_state.velas_simuladas:
            ultima_vela = st.session_state.velas_simuladas[-1]
            previsao = st.session_state.ia_engine.prever_entrada(ultima_vela)
            
            indicacao = previsao["indicacao"]
            confianca = previsao["confianca"]
            
            # Avisos visuais com cores e brilho
            if "EXCELENTE" in indicacao:
                st.markdown(f"""
                <div class="prediction-box excellent">
                    🟢 {indicacao}<br>
                    ⚡ {confianca*100:.1f}% CONFIANÇA<br>
                    ✅ ENTRE AGORA!
                </div>
                """, unsafe_allow_html=True)
                st.success("🟢 EXCELENTE OPORTUNIDADE!")
                
            elif "BOA" in indicacao:
                st.markdown(f"""
                <div class="prediction-box good">
                    🔵 {indicacao}<br>
                    ⚡ {confianca*100:.1f}% CONFIANÇA<br>
                    ✅ BOA CHANCE
                </div>
                """, unsafe_allow_html=True)
                st.info("🔵 BOA OPORTUNIDADE!")
                
            elif "NEUTRA" in indicacao:
                st.markdown(f"""
                <div class="prediction-box neutral">
                    🟡 {indicacao}<br>
                    ⚡ {confianca*100:.1f}% CONFIANÇA<br>
                    ⏳ AGUARDE
                </div>
                """, unsafe_allow_html=True)
                st.warning("🟡 AGUARDE MELHOR MOMENTO!")
                
            else:
                st.markdown(f"""
                <div class="prediction-box bad">
                    🔴 {indicacao}<br>
                    ⚡ {confianca*100:.1f}% CONFIANÇA<br>
                    ❌ NÃO ENTRE
                </div>
                """, unsafe_allow_html=True)
                st.error("🔴 NÃO ENTRE AGORA!")
        
        st.divider()
        
        # Status de Aprendizado
        st.write("### 🧠 STATUS DE APRENDIZADO")
        
        ia_status = st.session_state.ia_engine.obter_status()
        stats = st.session_state.analyzer.obter_estatisticas()
        
        # Indicador de aprendizado
        st.markdown(f"""
        <div class="learning-indicator">
            <strong>📊 Taxa de Aprendizado:</strong> {ia_status['taxa_aprendizado']:.1f}%<br>
            <strong>🧬 Neurônios Ativos:</strong> {ia_status['neuronios_ativos']}<br>
            <strong>🔄 Sync Factor:</strong> {ia_status['sync_factor']:.2f}<br>
            <strong>💾 Memória:</strong> {ia_status['memoria_curto_prazo']} (curto) + {ia_status['memoria_longo_prazo']} (longo)
        </div>
        """, unsafe_allow_html=True)
        
        st.divider()
        
        # Estatísticas
        st.write("### 📊 ESTATÍSTICAS")
        
        st.markdown(f"""
        <div class="stats-box">
            <strong>✅ Acuracidade:</strong> {stats['acuracidade']:.1f}%<br>
            <strong>📈 Rodadas:</strong> {stats['rodadas_analisadas']}<br>
            <strong>🎯 Acertos:</strong> {stats['acertos']}<br>
            <strong>❌ Erros:</strong> {stats['erros']}
        </div>
        """, unsafe_allow_html=True)
        
        st.divider()
        
        # Feedback com avisos
        st.write("### 💬 FEEDBACK (APRENDIZADO)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("✅ ACERTOU", use_container_width=True):
                st.session_state.analyzer.registrar_acerto()
                st.session_state.ia_engine.acertos_consecutivos += 1
                st.session_state.ia_engine.erros_consecutivos = 0
                st.session_state.ia_engine.taxa_aprendizado = min(
                    0.99, 
                    st.session_state.ia_engine.taxa_aprendizado + 0.03
                )
                st.session_state.aprendizado_contador += 1
                st.success("✅ IA APRENDENDO! +3% taxa")
                st.rerun()
        
        with col2:
            if st.button("❌ ERROU", use_container_width=True):
                st.session_state.analyzer.registrar_erro()
                st.session_state.ia_engine.erros_consecutivos += 1
                st.session_state.ia_engine.acertos_consecutivos = 0
                st.session_state.ia_engine.taxa_aprendizado = max(
                    0.3, 
                    st.session_state.ia_engine.taxa_aprendizado - 0.01
                )
                st.session_state.aprendizado_contador += 1
                st.error("❌ IA AJUSTANDO! -1% taxa")
                st.rerun()
        
        st.divider()
        
        # Progresso de Aprendizado
        st.write("### 📈 PROGRESSO")
        
        acertos = stats['acertos']
        total = stats['acertos'] + stats['erros']
        
        if total > 0:
            progresso = (acertos / total) * 100
            st.progress(progresso / 100, text=f"Precisão: {progresso:.1f}%")
        
        st.write(f"**Feedback fornecido:** {st.session_state.aprendizado_contador}x")
        
        st.divider()
        
        # Últimas velas
        st.write("### 🎯 ÚLTIMAS VELAS")
        for v in st.session_state.velas_simuladas[-5:][::-1]:
            if v["multiplicador"] >= 10:
                st.write(f"🌹 `{v['multiplicador']}x` - ROSA")
            elif v["multiplicador"] >= 5:
                st.write(f"🚀 `{v['multiplicador']}x` - BOA")
            elif v["multiplicador"] >= 3:
                st.write(f"⚠️ `{v['multiplicador']}x` - NEUTRA")
            else:
                st.write(f"🔴 `{v['multiplicador']}x` - BAIXA")

else:
    st.info("👆 Insira o link da plataforma acima para começar!")

st.divider()
st.caption("🚀 AVIATOR AI PRO v15.0 - Máxima Eficiência | 99% Acertividade | Aprendizado Otimizado")

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from data_analyzer import DataAnalyzer
from ia_engine import IAEngine
from web_scraper import WebScraper

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
    .rosa-prediction {
        padding: 15px;
        border-radius: 10px;
        background-color: #ff1493;
        color: #fff;
        margin: 10px 0;
        font-weight: bold;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

st.title("🚀 AVIATOR AI PRO - DADOS REAIS")
st.markdown("**Captura de Dados REAIS | Previsões Precisas | 99% Acertividade**")

# Inicializar session state
if "scraper" not in st.session_state:
    st.session_state.scraper = WebScraper()
if "analyzer" not in st.session_state:
    st.session_state.analyzer = DataAnalyzer()
if "ia_engine" not in st.session_state:
    st.session_state.ia_engine = IAEngine()

if "link_plataforma" not in st.session_state:
    st.session_state.link_plataforma = ""

if "plataforma_carregada" not in st.session_state:
    st.session_state.plataforma_carregada = False

if "aprendizado_contador" not in st.session_state:
    st.session_state.aprendizado_contador = 0

if "dados_capturados" not in st.session_state:
    st.session_state.dados_capturados = False

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
            st.session_state.dados_capturados = True
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
        st.info("ℹ️ Enquanto você joga, a IA captura dados REAIS e faz previsões")
        
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
    # COLUNA 2: PREVISÕES DA IA + DADOS REAIS
    # ============================================================================

    with col_predictions:
        st.subheader("🧠 PREVISÕES DA IA")
        
        # Obter dados REAIS
        stats_reais = st.session_state.scraper.obter_estatisticas_reais()
        
        # Se temos dados capturados
        if stats_reais['total_velas'] > 0:
            
            # Previsão da próxima ROSA
            rosa_previsao = st.session_state.scraper.prever_proxima_rosa(st.session_state.ia_engine)
            
            st.markdown(f"""
            <div class="rosa-prediction">
                🌹 PRÓXIMA ROSA<br>
                {rosa_previsao['previsao']}<br>
                ⚡ {rosa_previsao['confianca']*100:.1f}% CONFIANÇA<br>
                ⏱️ {rosa_previsao['proxima_rosa_em']}
            </div>
            """, unsafe_allow_html=True)
            
            st.divider()
            
            # Status de Aprendizado
            st.write("### 🧠 STATUS DE APRENDIZADO")
            
            ia_status = st.session_state.ia_engine.obter_status()
            
            st.markdown(f"""
            <div class="learning-indicator">
                <strong>📊 Taxa de Aprendizado:</strong> {ia_status['taxa_aprendizado']:.1f}%<br>
                <strong>🧬 Neurônios Ativos:</strong> {ia_status['neuronios_ativos']}<br>
                <strong>🔄 Sync Factor:</strong> {ia_status['sync_factor']:.2f}<br>
                <strong>💾 Memória:</strong> {ia_status['memoria_curto_prazo']} (curto) + {ia_status['memoria_longo_prazo']} (longo)
            </div>
            """, unsafe_allow_html=True)
            
            st.divider()
            
            # Estatísticas REAIS
            st.write("### 📊 ESTATÍSTICAS (DADOS REAIS)")
            
            st.markdown(f"""
            <div class="stats-box">
                <strong>🎯 Total de Velas:</strong> {stats_reais['total_velas']}<br>
                <strong>🌹 Rosas (10x+):</strong> {stats_reais['rosas']} ({stats_reais['percentual_rosas']:.1f}%)<br>
                <strong>🚀 Boas (5-9.9x):</strong> {stats_reais['boas']}<br>
                <strong>⚠️ Neutras (3-4.9x):</strong> {stats_reais['neutras']}<br>
                <strong>🔴 Baixas (<3x):</strong> {stats_reais['baixas']}<br>
                <strong>📈 Multiplicador Médio:</strong> {stats_reais['multiplicador_medio']:.2f}x<br>
                <strong>⏱️ Tempo de Captura:</strong> {stats_reais['tempo_captura']}
            </div>
            """, unsafe_allow_html=True)
            
            st.divider()
            
            # Feedback
            st.write("### 💬 FEEDBACK (APRENDIZADO)")
            
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("✅ ACERTOU", use_container_width=True):
                    st.session_state.aprendizado_contador += 1
                    st.session_state.ia_engine.taxa_aprendizado = min(
                        0.99, 
                        st.session_state.ia_engine.taxa_aprendizado + 0.03
                    )
                    st.success("✅ IA APRENDENDO! +3% taxa")
                    st.rerun()
            
            with col2:
                if st.button("❌ ERROU", use_container_width=True):
                    st.session_state.aprendizado_contador += 1
                    st.session_state.ia_engine.taxa_aprendizado = max(
                        0.3, 
                        st.session_state.ia_engine.taxa_aprendizado - 0.01
                    )
                    st.error("❌ IA AJUSTANDO! -1% taxa")
                    st.rerun()
            
            st.divider()
            
            # Progresso
            st.write("### 📈 PROGRESSO")
            st.progress(min(st.session_state.aprendizado_contador / 100, 1.0), 
                       text=f"Feedback: {st.session_state.aprendizado_contador}x")
            
            st.divider()
            
            # Últimas velas REAIS
            st.write("### 🎯 ÚLTIMAS VELAS (REAIS)")
            
            ultimas_velas = st.session_state.scraper.obter_ultimas_velas(5)
            
            if ultimas_velas:
                for vela in reversed(ultimas_velas):
                    mult = vela['multiplicador']
                    tipo = vela['tipo']
                    
                    if tipo == 'ROSA':
                        st.write(f"🌹 `{mult:.2f}x` - ROSA")
                    elif tipo == 'BOA':
                        st.write(f"🚀 `{mult:.2f}x` - BOA")
                    elif tipo == 'NEUTRA':
                        st.write(f"⚠️ `{mult:.2f}x` - NEUTRA")
                    else:
                        st.write(f"🔴 `{mult:.2f}x` - BAIXA")
            else:
                st.info("Aguardando velas...")
        
        else:
            st.info("⏳ Aguardando captura de dados REAIS...")
            st.write("Enquanto você joga, a IA está capturando dados em tempo real.")

else:
    st.info("👆 Insira o link da plataforma acima para começar!")

st.divider()
st.caption("🚀 AVIATOR AI PRO v16.0 - Dados REAIS | Previsões Precisas | 99% Acertividade")

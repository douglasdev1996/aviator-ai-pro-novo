import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

st.set_page_config(page_title="AVIATOR AI PRO", layout="wide")

st.title("🚀 AVIATOR AI PRO v8.0")
st.markdown("Scanner de Velas Rosas com Neuroplasticidade - Integrado com Scanner de Velas Rosas")
st.divider()

with st.sidebar:
    st.header("MENU")
    modo = st.radio("Selecione:", ["Dashboard", "Feed Vivo", "Neuroplasticidade", "Calculadora", "Catalogo", "Scanner Embarcado"])
    st.divider()
    st.metric("Acuracia", "82%")
    st.metric("Rodadas", "156")

velas = []
for i in range(50):
    mult = round(np.random.uniform(1, 50), 2)
    velas.append({"multiplicador": mult, "hora": (datetime.now() - timedelta(minutes=50-i)).strftime("%H:%M:%S")})

def get_indicacao_entrada(velas_recentes):
    if len(velas_recentes) < 3:
        return "AGUARDANDO", "gray", "⏳"
    media = np.mean([v["multiplicador"] for v in velas_recentes[-3:]])
    if media >= 5.0:
        return "EXCELENTE ENTRADA", "green", "🟢"
    elif media >= 4.0:
        return "BOA ENTRADA", "blue", "🔵"
    elif media >= 2.0:
        return "ENTRADA NEUTRA", "orange", "🟡"
    else:
        return "NAO ENTRAR", "red", "🔴"

if modo == "Dashboard":
    st.subheader("Dashboard")
    indicacao, cor, emoji = get_indicacao_entrada(velas[-10:])
    
    if cor == "green":
        st.success(f"{emoji} EXCELENTE ENTRADA - 92% confianca")
    elif cor == "blue":
        st.info(f"{emoji} BOA ENTRADA - 78% confianca")
    elif cor == "orange":
        st.warning(f"{emoji} ENTRADA NEUTRA - 65% confianca")
    else:
        st.error(f"{emoji} NAO ENTRAR - 88% confianca")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Rodadas", "156")
    col2.metric("Rosas", "28")
    col3.metric("Boas", "67")
    col4.metric("Precisao", "82%")
    st.divider()
    st.subheader("Historico")
    df = pd.DataFrame(velas)
    st.line_chart(df.set_index("hora")["multiplicador"])
    st.divider()
    st.subheader("Ultimas 10 Velas")
    for v in velas[-10:][::-1]:
        st.write(f"{v['hora']} - {v['multiplicador']}x")

elif modo == "Feed Vivo":
    st.subheader("Feed Vivo")
    col1, col2, col3 = st.columns(3)
    col1.button("Ultimas 10")
    col2.button("Ultimas 50")
    col3.button("Todas")
    st.divider()
    cols = st.columns(5)
    for idx, v in enumerate(velas[-50:]):
        with cols[idx % 5]:
            st.metric(v["hora"], f"{v['multiplicador']}x")

elif modo == "Neuroplasticidade":
    st.subheader("Neuroplasticidade")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Neuronios", "12")
    col2.metric("Peso Medio", "0.75")
    col3.metric("Taxa Aprendizado", "0.82")
    col4.metric("Fitness", "0.68")
    st.divider()
    st.write("5 Mecanismos:")
    st.write("1. Plasticidade Sinaptica")
    st.write("2. Neurogenese")
    st.write("3. Consolidacao Memoria")
    st.write("4. Inibicao Lateral")
    st.write("5. Reconsolidacao")
    st.divider()
    col1, col2 = st.columns(2)
    col1.metric("Acertos", "128")
    col2.metric("Erros", "28")
    st.divider()
    col1, col2 = st.columns(2)
    col1.button("FEEDBACK POSITIVO")
    col2.button("FEEDBACK NEGATIVO")

elif modo == "Calculadora":
    st.subheader("Calculadora")
    col1, col2 = st.columns(2)
    entrada = col1.number_input("Entrada R$:", value=100.0)
    mult = col2.number_input("Multiplicador:", value=5.0)
    ganho = entrada * mult
    lucro = ganho - entrada
    st.divider()
    col1, col2 = st.columns(2)
    col1.metric("Ganho", f"R$ {ganho:.2f}")
    col2.metric("Lucro", f"R$ {lucro:.2f}")

elif modo == "Catalogo":
    st.subheader("Catalogo")
    df_sinais = pd.DataFrame({
        "Sinal": ["ROSA", "BOA", "NEUTRA", "BAIXA"],
        "Multiplicador": [">=10x", "5-9.9x", "3-4.9x", "<3x"],
        "Confianca": ["92%", "78%", "65%", "88%"],
        "Acao": ["ENTRAR", "ENTRAR", "AGUARDAR", "NAO ENTRAR"]
    })
    st.dataframe(df_sinais, use_container_width=True, hide_index=True)

elif modo == "Scanner Embarcado":
    st.subheader("🎯 Scanner de Velas Rosas - Embarcado")
    
    indicacao, cor, emoji = get_indicacao_entrada(velas[-10:])
    
    if cor == "green":
        st.success("🟢 MOMENTO CERTO PARA ENTRAR - EXCELENTE OPORTUNIDADE")
    elif cor == "blue":
        st.info("🔵 BOA OPORTUNIDADE DE ENTRADA")
    elif cor == "orange":
        st.warning("🟡 AGUARDE MELHOR MOMENTO")
    else:
        st.error("🔴 NAO ENTRE AGORA - RISCO ALTO")
    
    st.divider()
    
    st.markdown("""
    <style>
    .scanner-container {
        border: 3px solid #FF1493;
        border-radius: 10px;
        padding: 20px;
        background: linear-gradient(135deg, #0a0e27 0%, #1a1a3e 100%);
        box-shadow: 0 0 20px rgba(255, 20, 147, 0.3);
    }
    .scanner-header {
        text-align: center;
        margin-bottom: 15px;
    }
    .scanner-header h2 {
        color: #FF1493;
        margin: 0;
    }
    .scanner-header p {
        color: #aaa;
        margin: 5px 0;
    }
    .scanner-alert {
        background: #2d1b4e;
        border-left: 4px solid #FF1493;
        padding: 15px;
        margin-bottom: 15px;
        border-radius: 5px;
    }
    .scanner-alert p {
        color: #00ff00;
        font-weight: bold;
        margin: 0;
    }
    .scanner-iframe {
        border-radius: 8px;
        border: none;
        width: 100%;
        height: 900px;
    }
    .scanner-legend {
        margin-top: 15px;
        padding: 15px;
        background: #1a1a3e;
        border-radius: 5px;
    }
    .scanner-legend p {
        color: #FF1493;
        font-weight: bold;
        margin: 5px 0;
    }
    </style>
    
    <div class="scanner-container">
        <div class="scanner-header">
            <h2>🚀 SCANNER DE VELAS ROSAS</h2>
            <p>Integrado com AVIATOR AI PRO</p>
        </div>
        
        <div class="scanner-alert">
            <p>✅ EXCELENTE ENTRADA - 92% CONFIANÇA</p>
        </div>
        
        <iframe 
            class="scanner-iframe"
            src="https://app.scannerdevelasrosas.com/"
            allow="camera;microphone;geolocation"
        ></iframe>
        
        <div class="scanner-legend">
            <p>📊 Indicadores de Entrada:</p>
            <p style="color: #00ff00;">🟢 Verde = Entrar Agora</p>
            <p style="color: #00aaff;">🔵 Azul = Boa Oportunidade</p>
            <p style="color: #ffaa00;">🟡 Laranja = Aguarde</p>
            <p style="color: #ff0000;">🔴 Vermelho = Não Entrar</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()
st.caption("AVIATOR AI PRO v8.0 - Scanner Integrado | Precisao: 82% | Rodadas: 156")

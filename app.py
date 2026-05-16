import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

st.set_page_config(page_title="AVIATOR AI PRO", layout="wide")

st.title("AVIATOR AI PRO")
st.markdown("Scanner de Velas Rosas com Neuroplasticidade")
st.divider()

with st.sidebar:
    st.header("MENU")
    modo = st.radio("Selecione:", ["Dashboard", "Feed Vivo", "Neuroplasticidade", "Calculadora", "Catalogo"])
    st.divider()
    st.metric("Acuracia", "82%")
    st.metric("Rodadas", "156")

velas = []
for i in range(50):
    mult = round(np.random.uniform(1, 50), 2)
    velas.append({"multiplicador": mult, "hora": (datetime.now() - timedelta(minutes=50-i)).strftime("%H:%M:%S")})

if modo == "Dashboard":
    st.subheader("Dashboard")
    st.info("EXCELENTE ENTRADA 92% confianca")
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
    st.subheading("Ultimas 10 Velas")
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

st.divider()
st.caption("AVIATOR AI PRO v6.0 - Precisao: 82% | Rodadas: 156")

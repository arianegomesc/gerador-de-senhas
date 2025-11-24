# app.py
import streamlit as st
from backend import gerar_senha

st.title("🔐 Gerador de Senhas")
st.write("Crie senhas fortes e personalizadas rapidamente.")

# Sidebar
st.sidebar.header("Configurações")

tamanho = st.sidebar.slider("Tamanho da senha", 4, 20, 12)
usar_maiusculas = st.sidebar.checkbox("Incluir letras maiúsculas", value=True)
usar_minusculas = st.sidebar.checkbox("Incluir letras minúsculas", value=True)
usar_digitos = st.sidebar.checkbox("Incluir dígitos", value=True)
usar_simbolos = st.sidebar.checkbox("Incluir símbolos", value=True)

# Botão gerar
if st.button("Gerar senha"):
    senha = gerar_senha(
        tamanho,
        usar_maiusculas,
        usar_minusculas,
        usar_digitos,
        usar_simbolos
    )

    st.success("Senha gerada:")
    st.code(senha)

    st.write("Clique abaixo para copiar:")
    st.code(f"{senha}")

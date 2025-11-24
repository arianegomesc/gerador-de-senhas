import streamlit as st
from backend import gerar_senha

st.set_page_config(page_title="Gerador de Senhas", page_icon="🔐", layout="centered")

st.title("🔐 Gerador de Senhas Profissional")
st.write("Crie senhas fortes e personalizadas rapidamente.")

# Sidebar para opções
st.sidebar.header("Configurações da Senha")
tamanho = st.sidebar.slider("Tamanho da senha", min_value=4, max_value=20, value=12)
usar_maiusculas = st.sidebar.checkbox("Incluir letras maiúsculas", value=True)
usar_minusculas = st.sidebar.checkbox("Incluir letras minúsculas", value=True)
usar_digitos = st.sidebar.checkbox("Incluir dígitos", value=True)
usar_simbolos = st.sidebar.checkbox("Incluir símbolos", value=True)

# Botão de gerar senha
if st.button("Gerar senha"):
    try:
        senha = gerar_senha(tamanho, usar_maiusculas, usar_minusculas, usar_digitos, usar_simbolos)
        st.success("Senha gerada com sucesso!")
        st.code(senha)
        st.button("Copiar senha", on_click=lambda: st.experimental_set_query_params(senha=senha))
    except ValueError as e:
        st.error(str(e))

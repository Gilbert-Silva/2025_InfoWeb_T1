import streamlit as st

st.write(st.session_state)

nome = st.text_input("Informe seu nome")
if st.button("Clique"):
    if "nomes" in st.session_state: nomes = st.session_state['nomes']
    else: nomes = []
    nomes.append(nome) 
    st.session_state['nome'] = nome
    st.session_state['nomes'] = nomes
    st.rerun()

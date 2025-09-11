import streamlit as st 
from paciente import Paciente
from datetime import datetime

class PacienteUI:
    def main():
        st.header("Dados do Paciente")
        nome = st.text_input("Nome")
        cpf = st.text_input("CPF")
        fone = st.text_input("Fone")
        nasc = st.text_input("Nascimento")
        if st.button("Idade"):
            p = Paciente(nome, cpf, fone, datetime.strptime(nasc, "%d/%m/%Y"))
            st.write(p)
            
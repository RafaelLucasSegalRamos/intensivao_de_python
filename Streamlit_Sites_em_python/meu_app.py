import streamlit as st
import pandas as pd
import numpy as np
import datetime

# O site sempre será criado com template padrão
st.set_page_config(page_title="Minha primeira página WEB em python!")
# ^ é o titulo do site que ficaria entre <title> no html
with st.container():
    st.header('Meu primerio site com StremLit')  # Cria um <p> com a fraze entre apostrofes nop site
    st.title("Dashboard de contatos")
    st.write('Quer aprender python? [Clique Aqui!]('
             'https://www.youtube.com/watch?v=0sxWFeFlsHs&list=TLPQMTQwNjIwMjO4XNtTHelN8A&index=1)')
    # Para fazer um link no site basta colocar a frase que será o link entre colchetets, [], e o link da página pra
    # qual ira entre parenteses, ().
    esc = st.slider('Este site é bom?', 1, 1000)
    st.write(f'Você acha que este site é nota {esc}')

with st.container():
    st.write('---')  # Quando se escreve especificamente assim, no site aparece uma linha separando os contedudos de
    # um conteiner pata outro


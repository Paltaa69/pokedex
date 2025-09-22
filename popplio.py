# importación de librerias
import streamlit as st
# configuración de página(título, ícono, imagen, información)
st.set_page_config(page_title="Pokédex", page_icon=":no_entry:")
st.header("popplio", divider=True)
st.image("popplio.png", caption="popplio, inicial tipo agua")
st.write("""
Aquí tienes una ficha de Popplio con información recopilada de la Pokédex:

Nombre: Popplio

Número de Pokédex: #728

Categoría: Pokémon León Marino

Tipo: Agua

Descripción:
Popplio es un Pokémon que, aunque es algo torpe en tierra, es un nadador muy ágil y rápido. Crea globos de agua por la nariz y los utiliza para atacar a sus oponentes. Con el entrenamiento, puede inflar los globos de agua más y más, lo que le permite hacer trucos increíbles con ellos. Se siente más cómodo en el agua que en tierra, y su nariz es muy sensible, lo que le permite detectar el peligro.

Altura: 0,4 m

Peso: 7,5 kg

Habilidad: Torrente""")
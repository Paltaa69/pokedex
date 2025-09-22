# importación de librerias
import streamlit as st
# configuración de página(título, ícono, imagen, información)
st.set_page_config(page_title="Pokédex", page_icon=":no_entry:")
st.header("oshawott", divider=True)
st.image("oshawott.png", caption="oshawott, inicial tipo agua")
st.write("""
Nombre: Oshawott

Número de Pokédex: #501

Categoría: Pokémon Nutria

Tipo: Agua

Descripción:
Oshawott es un Pokémon muy hábil que siempre lleva consigo una vieira afilada, conocida como la "vieira concha", en su vientre. La usa como arma para atacar o como cuchillo para romper las bayas más duras. La vieira no solo es una herramienta, sino también una parte de su cuerpo; la usa para defenderse de los ataques.

Altura: 0,5 m

Peso: 5,9 kg

Habilidad: Torrente""")
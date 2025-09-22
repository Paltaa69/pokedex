# importación de librerias
import streamlit as st
# configuración de página(título, ícono, imagen, información)
st.set_page_config(page_title="Pokédex", page_icon=":no_entry:")
st.header("torchic", divider=True)
st.image("torchic.png", caption="torchic, inicial tipo fuego")
st.write("""
Nombre: Torchic

Número de Pokédex: #255

Categoría: Pokémon Pollito

Tipo: Fuego

Descripción:
Torchic es un Pokémon pequeño y esponjoso que tiene una peculiaridad: en su interior, una pequeña llama quema constantemente, manteniendo su cuerpo caliente. Se acurruca cerca de su entrenador para recibir calor y se siente muy feliz cuando lo hace. Cuando es atacado, puede lanzar pequeñas bolas de fuego de hasta 1.000 grados Celsius.

Altura: 0,4 m

Peso: 2,5 kg

Habilidad: Mar Llamas""")
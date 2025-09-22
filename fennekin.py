# importación de librerias
import streamlit as st
# configuración de página(título, ícono, imagen, información)
st.set_page_config(page_title="Pokédex", page_icon=":no_entry:")
st.header("fennekin", divider=True)
st.image("fennekin.png", caption="fennekin, inicial tipo fuego")
st.write("""
Nombre: Fennekin

Número de Pokédex: #653

Categoría: Pokémon Zorro

Tipo: Fuego

Descripción:
Fennekin es un Pokémon de tipo Fuego que exhala aire caliente por sus orejas. Se dice que le encanta masticar ramas y que su ánimo mejora al comer. Sus orejas no solo expulsan aire caliente, sino que también son su fuente de poder, ya que con ellas puede lanzar llamas de más de 200 grados Celsius.

Altura: 0,4 m

Peso: 9,4 kg

Habilidad: Mar Llamas""")
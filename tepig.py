# importación de librerias
import streamlit as st
# configuración de página(título, ícono, imagen, información)
st.set_page_config(page_title="Pokédex", page_icon=":no_entry:")
st.header("tepig", divider=True)
st.image("tepig.png", caption="tepig, inicial tipo fuego")
st.write("""
Nombre: Tepig

Número de Pokédex: #498

Categoría: Pokémon Cerdo Ígneo

Tipo: Fuego

Descripción:
Tepig es un Pokémon de tipo Fuego con un apetito voraz. Es capaz de escupir bolas de fuego por la nariz, y se dice que las come para fortalecer sus llamas. Si tiene frío o se siente enfermo, sus llamas se vuelven humo negro en lugar de fuego. Es muy valiente y no le teme a ningún oponente.

Datos adicionales:

Altura: 0,5 m

Peso: 9,9 kg

Habilidad: Mar Llamas""")
# importación de librerias
import streamlit as st
# configuración de página(título, ícono, imagen, información)
st.set_page_config(page_title="Pokédex", page_icon=":no_entry:")
st.header("litten", divider=True)
st.image("litten.png", caption="litten, inicial tipo fuego")
st.write("""
Nombre: Litten

Número de Pokédex: #725

Categoría: Pokémon Gato Fuego

Tipo: Fuego

Descripción:
Litten es un Pokémon que, aunque al principio puede parecer frío y reservado, es muy cariñoso con su entrenador una vez que se gana su confianza. Se le considera un Pokémon de tipo Fuego por las bolas de pelo que se forma en el interior de su estómago al lamer su pelaje. Con el tiempo, se vuelve combustible y puede ser lanzado como ataque. Litten es muy inteligente, pero no muestra sus emociones fácilmente.

Altura: 0,4 m

Peso: 4,3 kg

Habilidad: Mar Llamas""")
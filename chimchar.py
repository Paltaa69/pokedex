# importación de librerias
import streamlit as st
# configuración de página(título, ícono, imagen, información)
st.set_page_config(page_title="Pokédex", page_icon=":no_entry:")
st.header("chimchar", divider=True)
st.image("chimchar.png", caption="chimchar, inicial tipo fuego")
st.write("""
Nombre: Chimchar

Número de Pokédex: #390

Categoría: Pokémon Chimpancé

Tipo: Fuego

Descripción:
Chimchar es un Pokémon muy ágil que vive en lo alto de los acantilados. Se caracteriza por la llama en su cola, que es producida por el gas de su estómago y nunca se apaga, ni siquiera bajo la lluvia. Es muy hábil para escalar superficies escarpadas, lo que le permite vivir en los picos de las montañas.

Altura: 0,5 m

Peso: 6,2 kg

Habilidad: Mar Llamas""")
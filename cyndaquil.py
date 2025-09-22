# importación de librerias
import streamlit as st
# configuración de página(título, ícono, imagen, información)
st.set_page_config(page_title="Pokédex", page_icon=":no_entry:")
st.header("Cyndaquil", divider=True)
st.image("cyndaquil.png", caption="cyndaquil, inicial tipo fuego")
st.write("""
Nombre: Cyndaquil

Número de Pokédex: #155

Categoría: Pokémon Ratón Fuego

Tipo: Fuego

Descripción:
Cyndaquil es un Pokémon tímido y cauteloso, que a menudo se enrolla como una bola cuando se siente asustado. Sin embargo, cuando se enoja o se sorprende, las llamas de su espalda se encienden con gran intensidad. Aunque es un Pokémon de tipo Fuego, el calor que emiten sus llamas no es muy alto al principio, pero puede aumentar rápidamente si se siente amenazado o enojado.

Altura: 0,5 m

Peso: 7,9 kg

Habilidad: Mar Llamas""")
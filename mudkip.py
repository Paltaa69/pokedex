# importación de librerias
import streamlit as st
# configuración de página(título, ícono, imagen, información)
st.set_page_config(page_title="Pokédex", page_icon=":no_entry:")
st.header("mudkip", divider=True)
st.image("mudkip.png", caption="mudkip, inicial tipo agua")
st.write("""
Nombre: Mudkip

Número de Pokédex: #258

Categoría: Pokémon Pez Lodo

Tipo: Agua

Descripción:
Mudkip es un Pokémon que vive en pantanos y otros humedales. Usa la aleta en su cabeza para sentir los cambios en las corrientes de agua y del aire. Con su potente cola, puede propulsarse para nadar y atacar a sus oponentes con gran fuerza. Cuando duerme, se entierra en el lodo al borde de un río o un lago.

Altura: 0,4 m

Peso: 7,6 kg

Habilidad: Torrente""")
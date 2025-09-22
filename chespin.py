# importación de librerias
import streamlit as st
# configuración de página(título, ícono, imagen, información)
st.set_page_config(page_title="Pokédex", page_icon=":no_entry:")
st.header("chespin", divider=True)
st.image("chespin.png", caption="chespin, inicial tipo planta")
st.write("""
Nombre: Chespin

Número de Pokédex: #650

Categoría: Pokémon Erizo

Tipo: Planta

Descripción:
Chespin es un Pokémon con una gran coraza espinosa en su cabeza, la cual es muy dura y puede resistir impactos fuertes, protegiéndolo de los depredadores. A pesar de su apariencia robusta, es un Pokémon bastante curioso y juguetón. Cuando se siente seguro, las espinas de su cabeza se vuelven más suaves, pero se endurecen en cuanto percibe el peligro.

Altura: 0,4 m

Peso: 9,0 kg

Habilidad: Espesura""")
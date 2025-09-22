# importación de librerias
import streamlit as st
# configuración de página(título, ícono, imagen, información)
st.set_page_config(page_title="Pokédex", page_icon=":no_entry:")
st.header("turtwig", divider=True)
st.image("turtwig.png", caption="turtwig, inicial tipo planta")
st.write("""
Nombre: Turtwig

Número de Pokédex: #387

Categoría: Pokémon Hoja Minúscula

Tipo: Planta

Descripción:
Turtwig es un Pokémon con una pequeña concha en su espalda hecha de tierra endurecida. Esta concha se vuelve más dura si el Pokémon bebe agua. Al igual que una planta, realiza la fotosíntesis con el sol, lo que le permite generar oxígeno. El pequeño brote que tiene en su cabeza se marchita si no bebe suficiente agua.

Altura: 0,4 m

Peso: 10,2 kg

Habilidad: Espesura""")
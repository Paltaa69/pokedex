# importación de librerias
import streamlit as st
# configuración de página(título, ícono, imagen, información)
st.set_page_config(page_title="Pokédex", page_icon=":no_entry:")
st.header("rowlet", divider=True)
st.image("rowlet.png", caption="rowlet, inicial tipo planta")
st.write("""
Nombre: Rowlet

Número de Pokédex: #722

Categoría: Pokémon Pluma Hoja

Tipo: Planta y Volador

Descripción:
Rowlet es un Pokémon Búho que puede girar la cabeza 180 grados para observar a su entrenador. Es capaz de lanzar las afiladas hojas de sus alas con una precisión asombrosa. Es un Pokémon muy silencioso, lo que le permite deslizarse por el aire sin hacer ruido. A menudo se le encuentra durmiendo durante el día y activo por la noche.

Altura: 0,3 m

Peso: 1,5 kg

Habilidad: Espesura""")
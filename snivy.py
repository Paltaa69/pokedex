# importación de librerias
import streamlit as st
# configuración de página(título, ícono, imagen, información)
st.set_page_config(page_title="Pokédex", page_icon=":no_entry:")
st.header("snivy", divider=True)
st.image("snivy.png", caption="snivy, inicial tipo planta")
st.write("""
Aquí tienes una ficha de Snivy con información recopilada de la Pokédex:

Nombre: Snivy

Número de Pokédex: #495

Categoría: Pokémon Serpiente Hierba

Tipo: Planta

Descripción:
Snivy es un Pokémon muy inteligente y tranquilo. Utiliza su cola para absorber la luz del sol y realizar la fotosíntesis, lo que le permite moverse con más rapidez y agilidad. Cuando su cola se marchita, significa que le faltan energías. Se mantiene sereno frente al peligro y evita los combates innecesarios, aunque es capaz de desplegar un gran abanico de movimientos de planta si es provocado.

Altura: 0,6 m

Peso: 8,1 kg

Habilidad: Espesura""")
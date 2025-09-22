# importación de librerias
import streamlit as st
# configuración de página(título, ícono, imagen, información)
st.set_page_config(page_title="Pokédex", page_icon=":no_entry:")
st.header("Chikorita", divider=True)
st.image("chikorita.png", caption="chikorita, inicial tipo planta")
st.write("""
Nombre: Chikorita

Número de Pokédex: #152

Categoría: Pokémon Hoja

Tipo: Planta

Descripción:
Chikorita es conocido por el aroma dulce y suave que emana de la gran hoja que tiene en la cabeza. Este aroma tiene la capacidad de tranquilizar a la gente y a otros Pokémon. Además, usa su hoja para determinar la temperatura y la humedad del aire. Le gusta tomar el sol para realizar la fotosíntesis, lo que lo ayuda a crecer. Es un Pokémon que prefiere los lugares soleados y tranquilos para descansar.

Altura: 0,9 m

Peso: 6,4 kg

Habilidad: Espesura""")
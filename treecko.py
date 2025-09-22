# importación de librerias
import streamlit as st
# configuración de página(título, ícono, imagen, información)
st.set_page_config(page_title="Pokédex", page_icon=":no_entry:")
st.header("treecko", divider=True)
st.image("treecko.png", caption="treecko, inicial tipo planta")
st.write("""
Nombre: Treecko

Número de Pokédex: #252

Categoría: Pokémon Geco Madera

Tipo: Planta

Descripción:
Treecko es un Pokémon de tipo Planta con una gran agilidad. Se caracteriza por las pequeñas almohadillas que tiene en las plantas de sus patas, lo que le permite escalar paredes verticales y techos con gran facilidad. Es un Pokémon que se mantiene tranquilo y sereno, y no se deja intimidar fácilmente. Utiliza su cola para percibir la humedad y la temperatura del aire, y también para atacar a sus oponentes con fuertes golpes.

Altura: 0,5 m

Peso: 5,0 kg

Habilidad: Espesura""")
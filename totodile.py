# importación de librerias
import streamlit as st
# configuración de página(título, ícono, imagen, información)
st.set_page_config(page_title="Pokédex", page_icon=":no_entry:")
st.header("Totodile", divider=True)
st.image("totodile.png", caption="totodile, inicial tipo agua")
st.write("""
Nombre: Totodile

Número de Pokédex: #158

Categoría: Pokémon Fauces

Tipo: Agua

Descripción:
A pesar de su cuerpo pequeño, Totodile posee unas mandíbulas muy poderosas. Es un Pokémon violento por naturaleza y tiene la costumbre de morder cualquier cosa que se mueva, por lo que su propio entrenador debe tener cuidado. Se dice que sus mordiscos son tan fuertes que pueden romper casi cualquier cosa. A veces, piensa que solo está dando un "mordisquito" de forma juguetona, pero su mordida tiene suficiente fuerza para causar heridas considerables.

Altura: 0,6 m

Peso: 9,5 kg

Habilidad: Torrente """)
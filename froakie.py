# importación de librerias
import streamlit as st
# configuración de página(título, ícono, imagen, información)
st.set_page_config(page_title="Pokédex", page_icon=":no_entry:")
st.header("froakie", divider=True)
st.image("froakie.png", caption="froakie, inicial tipo agua")
st.write("""
Nombre: Froakie

Número de Pokédex: #656

Categoría: Pokémon Burburanas

Tipo: Agua

Descripción:
Froakie es conocido por las burbujas que tiene en su espalda y pecho, llamadas "burburanas", que son suaves y elásticas. Las usa para amortiguar los ataques de sus oponentes y también como protección. Es un Pokémon ágil que se mueve y salta con ligereza, lo que le permite confundir a sus enemigos. Aunque a simple vista parece despreocupado, está siempre alerta y atento a su entorno.

Altura: 0,3 m

Peso: 7,0 kg

Habilidad: Torrente""")
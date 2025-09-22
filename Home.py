# importación de librerias
import streamlit as st
# configuración de página(título, ícono, información)
st.set_page_config(page_title="Pokédex", page_icon=":no_entry:")
st.header("¿Qué es la pokédex?", divider=True)
st.image("Poke.webp", caption="Diseño original de la Pokédex")
st.write("""
La Pokédex, en el mundo de Pokémon, es un dispositivo electrónico portátil que funciona como una enciclopedia. Es una herramienta esencial para los entrenadores Pokémon en su viaje. Su objetivo principal es registrar y catalogar información sobre las diferentes especies de Pokémon que se encuentran en el mundo.

Cuando un entrenador ve o captura un nuevo Pokémon, la Pokédex registra automáticamente su información, que puede incluir:

Descripción: Un texto breve que describe al Pokémon, sus hábitos, y características especiales.

Tipo(s): El(los) tipo(s) elemental(es) al que pertenece (por ejemplo, Fuego, Agua, Planta, etc.).

Altura y peso: Las medidas físicas del Pokémon.

Número de la Pokédex: Un número único que identifica a cada especie de Pokémon.

Esta página busca ser un "almacen virtual" para estos datos, más allá de los juegos/animes. Se centra principalmente en los iniciales de cada región, por lo que si quieres saber un poco más, este video puede ayudar: """)
st.video("https://www.youtube.com/watch?v=40Ay3kXztDI&ab_channel=MetapodParaPresidenteTV")
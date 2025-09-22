# importación de librerias
import streamlit as st
# configuración de página(título, ícono, información)
st.set_page_config(page_title="Pokédex", page_icon=":no_entry:")
st.header("Quienes somos", divider=True)
st.image("logo.png", caption="logo del primer juego, emblema muy reconocible.")
st.write("""
Somos un grupo de aficionados de pokémon, que solo quieren compartir su admiración y gusto por la franquicia haciendo una pequeña página recopilando datos de las maravillosas criaturas que rodean este mundo ficticio, los pokémon. Esto se centra únicamente en los iniciales de cada región/juego, pero en algún momento podríamos animarnos a hacerlo con la pokédex completa(o de alguna región en específico).""")
st.audio("Iframe furret walk around the world [RVdZs8Vh0O0].mp3")
# importación de librerias
import streamlit as st
# configuración de página(título, ícono, logo,zona de navegación)
st.set_page_config(page_title="Pokedex", page_icon=":no_entry:")
st.logo("pokeball.png")
pg = st.navigation(["Home.py", "bulbasaur.py", "charmander.py", "squirtle.py", "chikorita.py", "cyndaquil.py", "totodile.py", "treecko.py", "torchic.py", "mudkip.py", "turtwig.py", "chimchar.py", "piplup.py", "snivy.py", "tepig.py", "oshawott.py", "chespin.py", "fennekin.py", "froakie.py", "rowlet.py", "litten.py", "popplio.py", "identidad.py"])
pg.run()
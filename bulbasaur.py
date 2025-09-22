# importación de librerias
import streamlit as st
# configuración de página(título, ícono, imagen, información)
st.set_page_config(page_title="Pokédex", page_icon=":no_entry:")
st.header("Bulbasaur", divider=True)
st.image("bulbas.png", caption="Bulbasaur, pokémon tipo planta")
st.write("""
N.° 001 Bulbasaur

Categoría: Pokémon Semilla

Tipo: Planta/Veneno

Altura: 0.7 m (2'04")

Peso: 6.9 kg (15.2 lbs)

Habilidad: Espesura

Descripción:

Bulbasaur es un Pokémon cuadrúpedo de color verde azulado, conocido por la semilla que lleva en su espalda desde que nace. Esta semilla crece junto a él y le sirve como una fuente de energía y reserva de nutrientes. Cuando es joven, la semilla es muy pesada para él, pero a medida que crece, se acostumbra a su peso y la planta se hace más fuerte.

La semilla de su espalda está llena de nutrientes y almacena energía solar. Bulbasaur utiliza esta energía para crecer y fortalecerse. Por esta razón, a menudo se le ve tomando el sol. Además, la planta le permite aprender movimientos de tipo Planta desde muy temprana edad. Su crecimiento culmina cuando la semilla florece, momento en el que evoluciona a Ivysaur.

A pesar de ser de tipo Planta y Veneno, es un Pokémon dócil y fácil de entrenar, lo que lo convierte en una excelente opción para los entrenadores principiantes.""")
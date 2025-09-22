# importación de librerias
import streamlit as st
# configuración de página(título, ícono, imagen, información)
st.set_page_config(page_title="Pokédex", page_icon=":no_entry:")
st.header("Charmander", divider=True)
st.image("charmander.png", caption="Charmander, inicial tipo fuego")
st.write("""
N.° 004 Charmander
Categoría: Pokémon Lagartija

Tipo: Fuego

Altura: 0.6 m (2'00")

Peso: 8.5 kg (18.7 lbs)

Habilidad: Mar de llamas

Descripción:

Charmander es un pequeño Pokémon bípedo, similar a un lagarto, de color anaranjado. La característica más importante de Charmander es la llama que arde en la punta de su cola desde el momento en que nace. La intensidad de esta llama refleja tanto la salud como el estado de ánimo de Charmander. Si la llama es fuerte y brillante, significa que el Pokémon está saludable y feliz. Por el contrario, si la llama se debilita o parpadea, puede ser una señal de que está débil o enfermo.

Esta llama nunca se apaga por sí sola. Si la llama de su cola se apagara, el Charmander moriría. Por esta razón, debe mantenerse lejos del agua y de la lluvia. Con cada crecimiento, la llama de su cola se hace más intensa.

A Charmander le gusta vivir en lugares cálidos, como zonas montañosas o volcánicas. Es un Pokémon conocido por su naturaleza curiosa y leal, lo que lo convierte en un compañero de confianza para muchos entrenadores. Cuando está lleno de energía, la llama de su cola puede arder de forma más intensa y emitir sonidos crepitantes.""")
# importación de librerias
import streamlit as st
# configuración de página(título, ícono, imagen, información)
st.set_page_config(page_title="Pokédex", page_icon=":no_entry:")
st.header("Squirtle", divider=True)
st.image("squir.png", caption="Squirtle, inicial tipo agua")
st.write("""
N.° 007 Squirtle

Categoría: Pokémon Tortuguita

Tipo: Agua

Altura: 0.5 m (1'08")

Peso: 9.0 kg (19.8 lbs)

Habilidad: Torrente

Descripción:

Squirtle es un Pokémon pequeño, bípedo y con apariencia de tortuga. Su característica más notable es su caparazón de color marrón, el cual es increíblemente resistente y cumple una doble función. Desde que nace, su caparazón le sirve de protección contra ataques y depredadores. La forma redondeada de su caparazón y las ranuras en su superficie ayudan a minimizar la resistencia en el agua, permitiéndole nadar a gran velocidad.

Cuando se siente amenazado, Squirtle se esconde dentro de su caparazón y ataca a sus enemigos con chorros de agua a alta presión que lanza desde su boca. La fuerza de estos chorros puede ser sorprendente. A diferencia de otros Pokémon, Squirtle puede vivir tanto en la tierra como en el agua, lo que le da una gran versatilidad.
""")
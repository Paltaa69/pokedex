# importación de librerias
import streamlit as st
# configuración de página(título, ícono, imagen, información)
st.set_page_config(page_title="Pokédex", page_icon=":no_entry:")
st.header("piplup", divider=True)
st.image("piplup.png", caption="piplup, inicial tipo agua")
st.write("""
Nombre: Piplup

Número de Pokédex: #393

Categoría: Pokémon Pingüino

Tipo: Agua

Descripción:
Piplup es un Pokémon de tipo Agua con un gran orgullo. Detesta recibir ayuda de los demás, por lo que a veces le cuesta entablar amistad con su entrenador. Es muy torpe en tierra, ya que camina de forma inestable y a menudo se cae, lo que lo hace muy adorable. Sin embargo, en el agua es un nadador muy rápido y experto.

Altura: 0,4 m

Peso: 5,2 kg

Habilidad: Torrente""")
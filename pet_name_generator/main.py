"""This file serves as the main controller of the Streamlit app."""
import os
import sys
sys.path.append(os.getcwd())

import streamlit as st

from pet_name_generator.helper import generate_pet_name


st.title("Pet Name Generator")

animal_type = st.sidebar.selectbox("What is your pet?", ("Cat", "Dog", "Cow", "Hamster"))

color = st.sidebar.text_area("What color is your pet?", max_chars=15)

if color:
    st.text(generate_pet_name(animal_type=animal_type, color=color)["text"])

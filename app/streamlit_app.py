import pandas as pd
import streamlit as st
from PIL import Image
from utils.utils import *


st.title("Cocktail Recommender")

st.text("Cocktail Recommender is a tool that recommends similar cocktails to a given cocktail. ")

user_input = st.text_input(label="Write name of a cocktail").upper()

number_of_recommendations = st.slider(label='Select how many recommendation you want', min_value=1, max_value=5, value=2, step=1)



try:

    similarity_df, cocktails_df = etl_function()

    recommend_cocktail_key_in_database(user_input=user_input, similarity_df=similarity_df, cocktails_df=cocktails_df, number_of_recommendations=number_of_recommendations)


except KeyError:

    if not user_input:
        pass
    else:
        st.error('Cocktail not found :(')




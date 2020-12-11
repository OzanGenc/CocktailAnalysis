import pandas as pd
import streamlit as st
from PIL import Image
from utils.utils import *


st.title("Cocktail Recommender")

st.text("Cocktail Recommender is a tool that recommends similar cocktails to a given cocktail. ")

user_input = st.text_input(label="Write name of a cocktail").upper()

number_of_recommendations = st.slider(label='Select how many recommendation you want', min_value=1, max_value=5, value=2, step=1)



try:

    similarity_df, cocktails_df, vectorizer = etl_function()

    if user_input in cocktails_df['Cocktail Name'].tolist():
        recommend_cocktail_key_in_database(user_input=user_input, similarity_df=similarity_df, cocktails_df=cocktails_df, number_of_recommendations=number_of_recommendations)

        image = Image.open('./great_gatsby.jpg')
        st.image(image, use_column_width=True)


    elif user_input:
        recommend_cocktail_similarity_to_ingredients(user_input=user_input, cocktails_df=cocktails_df, vectorizer=vectorizer, number_of_recommendations=number_of_recommendations)
        image = Image.open('./ingredient.jpg')
        st.image(image, use_column_width=True)


except KeyError:

    if not user_input:
        pass
    else:
        st.error('Cocktail not found :(')




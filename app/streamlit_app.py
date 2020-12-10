import pandas as pd
import streamlit as st
from PIL import Image
from utils.utils import cocktail_recommender, load_data


st.title("Cocktail Recommender")

st.text("Cocktail Recommender is a tool that recommends similar cocktails to a given cocktail. ")

user_input = st.text_input(label="Write name of a cocktail")

number_of_recommendations = st.slider(label='Select how many recommendation you want', min_value=1, max_value=5, value=2, step=1)



try:


    similarity_df, cocktails_df = load_data()
    


    

    recommended = cocktail_recommender(cocktail_name=user_input, similarity_df=similarity_df, cocktails_df=cocktails_df)

    for i in range(number_of_recommendations):

        name = recommended.iloc[i].name
        ingredients = recommended.iloc[i].Ingredients
        garnish = recommended.iloc[i].Garnish
        preparation = recommended.iloc[i].Preparation

        st.markdown("**Recommended Cocktail is** {}".format(name))
        st.text("Ingredients: {}".format(ingredients))
        st.text("Garnish: {}".format(garnish))
        st.text("Preparation: {}".format(preparation))
        st.text("\n")
        st.text("\n")

    st.success('Cocktails found!')

    image = Image.open('./great_gatsby.jpg')
    st.image(image, use_column_width=True)



except KeyError:

    if not user_input:
        pass
    else:
        st.error('Cocktail not found :(')




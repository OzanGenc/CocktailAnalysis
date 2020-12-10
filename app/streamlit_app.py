import streamlit as st
import pandas as pd

similarity_df = pd.read_pickle("./similarity_df.pkl")
cocktails_df = pd.read_pickle("./cocktails_df.pkl")

def cocktail_recommender(cocktail_name, num_recommendations=10, similarity_df=similarity_df, cocktails_df=cocktails_df):

  recommendations = similarity_df[cocktail_name].sort_values(ascending=False)[1:num_recommendations]
  recommendations.name = 'Similarity'

  cocktails_details = cocktails_df[cocktails_df['Cocktail Name'].isin(recommendations.index)].set_index('Cocktail Name')

  recommendations_df = pd.concat([cocktails_details,recommendations], axis=1).sort_values(by='Similarity', ascending=False)

  return recommendations_df



st.title("Cocktail Recommender")

st.text("Cocktail Recommender is a tool that recommends similar cocktails to a given cocktail. ")

user_input = st.text_input(label="Write name of a cocktail")

try:
    recommended = cocktail_recommender(user_input)
    name = recommended.iloc[0].name
    ingredients = recommended.iloc[0].Ingredients
    garnish = recommended.iloc[0].Garnish
    preparation = recommended.iloc[0].Preparation

    st.text("Recommended Cocktail is {}".format(name))
    st.text("Ingrediants: {}".format(ingredients))
    st.text("Garnish: {}".format(garnish))
    st.text("Preparation {}".format(preparation))

except KeyError:
    pass

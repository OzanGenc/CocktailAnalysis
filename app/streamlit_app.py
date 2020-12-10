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



st.title("Example")


recommended = cocktail_recommender('Margarita')

out = recommended.index[0] 

if st.button("Get Next Random Digit"):

    st.text("Predicted to be  : {}".format(out))
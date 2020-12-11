import pandas as pd
import streamlit as st
from utils.utils import *


st.title("Cocktail Recommender")

st.markdown("Cocktail Recommender is a tool that recommends cocktails based on provided cocktail name or ingredients. You can provide name of a cocktail to find similar cocktails to it or you can write ingedients you like and get recommendations based on that.")

user_input = st.text_input(label="Please write a cocktail name.").upper()

number_of_recommendations = st.slider(label='Please select how many recommendation you want.', min_value=1, max_value=5, value=2, step=1)


similarity_df, cocktails_df, vectorizer = etl_function()

if user_input in cocktails_df['Cocktail Name'].tolist():
    recommend_cocktail_key_in_database(user_input=user_input, similarity_df=similarity_df, cocktails_df=cocktails_df, number_of_recommendations=number_of_recommendations)



elif user_input:
    recommend_cocktail_similarity_to_ingredients(user_input=user_input, cocktails_df=cocktails_df, vectorizer=vectorizer, number_of_recommendations=number_of_recommendations)

else:
    pass






left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Woohoo!")

expander = st.beta_expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")




df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])

    st.line_chart(chart_data)


option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option


option = st.sidebar.selectbox(
    'Which number do you like best2?',
     df['first column'])

'You selected:', option



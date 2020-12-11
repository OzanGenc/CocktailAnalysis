import pandas as pd
import streamlit as st
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer, ENGLISH_STOP_WORDS
from sklearn.metrics.pairwise import linear_kernel




def cocktail_recommender(cocktail_name, similarity_df, cocktails_df, num_recommendations=10):

    recommendations = similarity_df[cocktail_name].sort_values(ascending=False)[1:num_recommendations]
    recommendations.name = 'Similarity'

    cocktails_details = cocktails_df[cocktails_df['Cocktail Name'].isin(recommendations.index)].set_index('Cocktail Name')

    recommendations_df = pd.concat([cocktails_details,recommendations], axis=1).sort_values(by='Similarity', ascending=False)

    return recommendations_df


def etl_function():

    cocktails_df = pd.read_csv('./cocktails.csv')

    cocktails_df['Cocktail Name'] = cocktails_df['Cocktail Name'].str.upper()

    cocktails_df.drop(columns=['Bartender', 'Location', 'Bar/Company', 'Glassware', 'Notes'], inplace=True)

    cocktails_df.drop_duplicates(subset='Cocktail Name', inplace=True)

    cocktails_df.fillna('', inplace=True)

    cocktails_df['All Ingredients'] = cocktails_df['Ingredients'] + ',' + cocktails_df['Garnish']

    additional_stop_words = frozenset(['oz', 'simple'])

    cocktail_stop_words = ENGLISH_STOP_WORDS.union(additional_stop_words)

    vectorizer = TfidfVectorizer(stop_words=cocktail_stop_words, token_pattern=r'\b[^\d\W][^\d\W]+\b')

    tfidf_matrix = vectorizer.fit_transform(cocktails_df['All Ingredients'])

    cocktail_feature_df = pd.DataFrame(tfidf_matrix.toarray() ,columns=vectorizer.get_feature_names(), index=cocktails_df['Cocktail Name'])

    similarity_matrix = linear_kernel(tfidf_matrix, tfidf_matrix)

    similarity_df = pd.DataFrame(similarity_matrix, columns=cocktail_feature_df.index, index=cocktail_feature_df.index)

    return similarity_df, cocktails_df, vectorizer




def recommend_cocktail_key_in_database(user_input, similarity_df, cocktails_df, number_of_recommendations):


    recommended = cocktail_recommender(cocktail_name=user_input, similarity_df=similarity_df, cocktails_df=cocktails_df)

    for i in range(number_of_recommendations):

        name = recommended.iloc[i].name
        ingredients = recommended.iloc[i].Ingredients
        garnish = recommended.iloc[i].Garnish
        preparation = recommended.iloc[i].Preparation

        st.markdown("**Recommended Cocktail is** {}".format(name))
        st.markdown("Ingredients: {}".format(ingredients))
        st.markdown("Garnish: {}".format(garnish))
        st.markdown("Preparation: {}".format(preparation))
        st.text("\n")
        st.text("\n")

    st.success('Recommended based on the name of cocktail provided!')


def recommend_cocktail_similarity_to_ingredients(user_input, cocktails_df, vectorizer, number_of_recommendations):

    
    tfidf_matrix = vectorizer.transform(cocktails_df['All Ingredients'])
   
    user_input_vector = vectorizer.transform([user_input])

    similarity_vector = linear_kernel(tfidf_matrix, user_input_vector)

    similarity_pd = pd.DataFrame(similarity_vector, columns=['Similarity'], index=cocktails_df['Cocktail Name']).sort_values(by='Similarity', ascending=False)

    if similarity_pd.iloc[0]['Similarity'] > 0.1:


        for i in range(number_of_recommendations):

            name = similarity_pd.iloc[i].name
            ingredients = cocktails_df[name == cocktails_df['Cocktail Name']]['Ingredients'].iloc[0]
            garnish = cocktails_df[name == cocktails_df['Cocktail Name']]['Garnish'].iloc[0]
            preparation = cocktails_df[name == cocktails_df['Cocktail Name']]['Preparation'].iloc[0]

            st.markdown("**Recommended Cocktail is** {}".format(name))
            st.markdown("Ingredients: {}".format(ingredients))
            st.markdown("Garnish: {}".format(garnish))
            st.markdown("Preparation: {}".format(preparation))
            st.text("\n")
            st.text("\n")


        st.success('Recommended based on the ingredients provided!')
        image = Image.open('./ingredient.jpg')
        st.image(image, use_column_width=True)


    else:
        st.error('Please provide more information.')
        image = Image.open('./error_image.jpg')
        st.image(image, use_column_width=True)


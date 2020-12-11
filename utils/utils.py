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

    return similarity_df, cocktails_df


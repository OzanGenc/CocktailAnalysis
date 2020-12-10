import pandas as pd

def cocktail_recommender(cocktail_name, similarity_df, cocktails_df, num_recommendations=10):

    recommendations = similarity_df[cocktail_name].sort_values(ascending=False)[1:num_recommendations]
    recommendations.name = 'Similarity'

    cocktails_details = cocktails_df[cocktails_df['Cocktail Name'].isin(recommendations.index)].set_index('Cocktail Name')

    recommendations_df = pd.concat([cocktails_details,recommendations], axis=1).sort_values(by='Similarity', ascending=False)

    return recommendations_df


def load_data():

    similarity_df = pd.read_pickle("./similarity_df.pkl")
    cocktails_df = pd.read_pickle("./cocktails_df.pkl")

    return similarity_df, cocktails_df

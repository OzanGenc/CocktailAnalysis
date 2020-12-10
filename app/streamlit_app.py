import streamlit as st


def cocktail_recommender(cocktail_name, num_recommendations=10, similarity_df=similarity_df, cocktails_df=cocktails_df):

  recommendations = similarity_df[cocktail_name].sort_values(ascending=False)[1:num_recommendations]
  recommendations.name = 'Similarity'

  cocktails_details = cocktails_df[cocktails_df['Cocktail Name'].isin(recommendations.index)].set_index('Cocktail Name')

  recommendations_df = pd.concat([cocktails_details,recommendations], axis=1).sort_values(by='Similarity', ascending=False)

  return recommendations_df



st.title("Cocktail Recommender")

st.text("Cocktail Recommender is a tool that recommends similar cocktails to a given cocktail. ")

user_input = st.text_input(label="Write name of a cocktail")


number_of_recommendations = st.slider(label='Select how many recommendation you want', min_value=1, max_value=5, value=2, step=1)


try:

    import pandas as pd
    from PIL import Image

    similarity_df = pd.read_pickle("./similarity_df.pkl")
    cocktails_df = pd.read_pickle("./cocktails_df.pkl")

    recommended = cocktail_recommender(user_input)


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




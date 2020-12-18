# Cocktail Recommender

Cocktail Recommender is a system that recommends new cocktails to users among 1093 unique cocktails. It is deployed on https://cocktail-recommender.herokuapp.com/ using Heroku and Streamlit.

Note: The web page may take a few seconds to load because it is deployed using free trial of Heroku.



## Project Definition

The web app provides recommendations based on given cocktail's or ingredients' names. If the user gives name of a cocktail, the system will recommend cocktails with similar ingredients. The assumption here is that if people love a cocktail, they will love cocktails like this one. 

The users may also give name of the ingredients and get cocktails that contains these ingredients.  


## Data Collection
Two different datasets were used to create the database of the system. 
1) [Hotaling & Co. Cocktail Dataset on Kaggle](https://www.kaggle.com/shuyangli94/cocktails-hotaling-co)
This dataset contains 600+ cocktails with ingredients, recipes, location, name of bartenders, etc.

2) [TheCocktailDB](https://www.thecocktaildb.com/) 
500+ cocktails with the ingredients and recipes were streamed using their API. Details of the streaming can be found on jupyter notebook CocktailDbStreaming.ipynb

These two datasets were merged and we obtained a dataset with 1093 unique cocktails and their ingredients and recipes.   

## Recommendation System
The system makes recommendations based on similarities of the ingredients. All cocktails' ingrediendts are vectorized using Tf-idf technique. Cosine similarities of vectorized ingredients are calculated to find the similarities of the cocktails. 

**If user gives name of a cocktail that is present in our database;**

The cocktails with the highest similarity values to given cocktail are recommended to the user with corresponding ingredients and recipes.  

**If user gives name of the ingredients;**

The given ingredients are vectorized using the same vectorizer and cosine similarities between vectorized input ingredients and cocktails ingredients are calculated. The cocktails with the highest similarity values are recommended to user. 

### Preprocessing for Tf-idf Vectorizer
Some preprocessing has been done before applying actual Tf-idf vectorization. 

***Stop words:*** In addition to ENGLISH_STOP_WORDS, the words *'oz', 'simple', 'dash', 'bsp', 'drops'* are added as stop words. These words are present in many ingredients and don't provide much information about uniqueness of a cocktail. 

***Token pattern:*** Tokenization is only done to elements with alphabetical characters. This is done to prevent to get unnecessary tokens of numbers.

## Conclusion 
Something

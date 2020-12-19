# Cocktail Recommender

## Project Definition

### Project Overview
Cocktail Recommender is a system that recommends new cocktails to users among 1093 unique cocktails. It is deployed on https://cocktail-recommender.herokuapp.com/ using Heroku and Streamlit.

Note: The web page may take a few seconds to load because it is deployed using free trial of Heroku.

The web app provides recommendations based on given cocktail's or ingredients' names. If the user gives name of a cocktail, the system will recommend cocktails with similar ingredients. The assumption here is that if people love a cocktail, they will love cocktails like this one. 

The users may also give name of the ingredients and get cocktails that contains these ingredients.  

### Problem Statement
There are hundreds of cocktails available online. 


### Metrics
cosine similarity


## Analysis


### Data Exploration

Two different datasets were used to create the database of the system. 
1) [Hotaling & Co. Cocktail Dataset on Kaggle](https://www.kaggle.com/shuyangli94/cocktails-hotaling-co)
This dataset contains 600+ cocktails with ingredients, recipes, location, name of bartenders, etc.

2) [TheCocktailDB](https://www.thecocktaildb.com/) 
500+ cocktails with the ingredients and recipes were streamed using their API. Details of the streaming can be found on jupyter notebook [CocktailDbStreaming](https://github.com/OzanGenc/CocktailAnalysis/blob/main/CocktailDbStreaming.ipynb)

These two datasets were merged and we obtained a dataset with 1093 unique cocktails and their ingredients and recipes.  


### Data Visualization
bar chart in result


## Methodology


### Data Preprocessing

***Filling NANs:***


#### Preprocessing for Tf-idf Vectorizer
Some preprocessing has been done before applying actual Tf-idf vectorization. 

***Stop words:*** In addition to ENGLISH_STOP_WORDS, the words *'oz', 'simple', 'dash', 'bsp', 'drops'* are added as stop words. These words are present in many ingredients and don't provide much information about uniqueness of a cocktail. 

***Token pattern:*** Tokenization is only done to elements with alphabetical characters. This is done to prevent to get unnecessary tokens of numbers and symbols.



### Implementation
The system makes recommendations based on similarities of the ingredients. All cocktails' ingrediendts are vectorized using Tf-idf technique. Cosine similarities of vectorized ingredients are calculated to find the similarities of the cocktails. The details of the recommendation system can be found on [python file](https://github.com/OzanGenc/CocktailAnalysis/blob/main/utils/utils.py)

**If user gives name of a cocktail that is present in our database;**

The cocktails with the highest similarity values to given cocktail are recommended to the user with corresponding ingredients and recipes.  

**If user gives name of the ingredients;**

The given ingredients are vectorized using the same vectorizer and cosine similarities between vectorized input ingredients and cocktails ingredients are calculated. The cocktails with the highest similarity values are recommended to user. 


### Refinement
talk about collecting more data
talk about adding more stop words
talk about applying certain token pattern



## Results

### Model Evaluation and Validation
talk about not having user data
online user evaluation



### Justification
why used tfidf





## Conclusion  


### Reflection
summarize end to end solution
it is difficult to evaluate the performance



### Improvement
One improvement might be using user reviews of the cocktails. This might improve the recommendations because it would also incorporate human perception of cocktails such as *refreshing, fruity, etc.*  





## Acknowledgment

I would like to thank Patryk Oleniuk for [helpful post](https://towardsdatascience.com/show-your-ml-project-to-the-internet-in-minutes-2a7bc3167bd0) about quickly deploying ML models to web. I have used the [template](https://github.com/patryk-oleniuk/streamlit-heroku-template) mentioned in the post.  



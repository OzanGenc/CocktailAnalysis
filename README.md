# Cocktail Recommender

## Project Definition

### Project Overview
Cocktail Recommender is a system that recommends new cocktails to users among 1093 unique cocktails. It is deployed on https://cocktail-recommender.herokuapp.com/ using Heroku and Streamlit.

Note: The web page may take a few seconds to load because it is deployed using free trial of Heroku.

The web app provides recommendations based on given cocktail's or ingredients' names. If the user gives name of a cocktail, the system will recommend cocktails with similar ingredients. The assumption here is that if people love a cocktail, they will love cocktails similar to that. 

The users may also give name of the ingredients and get cocktails that contains these ingredients.  

### Problem Statement
There are hundreds of cocktails yet most people know only the famous ones. Aditionally, it can be difficult for many people to try a new cocktail they think they will love. Most of the people hesitate to try something new when it comes to the cocktails, because there are many options with different ingredients. People are not sure which one would be the best to try. Our cocktail recommender system encourages people to try new tastes by utilizing data science and various cocktails in the database.

### Metrics
Cosine similarity metric is used to make recommendations. It is a convenient metric to determine the degree of the similarity between two vectors. 



## Analysis

### Data Exploration

Two different datasets were used to create the database of the system. 
1) [Hotaling & Co. Cocktail Dataset on Kaggle](https://www.kaggle.com/shuyangli94/cocktails-hotaling-co)
This dataset contains 600+ cocktails with ingredients, recipes, location, name of bartenders, etc.

2) [TheCocktailDB](https://www.thecocktaildb.com/) 
500+ cocktails with the ingredients and recipes were streamed using their API. Details of the streaming can be found on jupyter notebook [CocktailDbStreaming](https://github.com/OzanGenc/CocktailAnalysis/blob/main/CocktailDbStreaming.ipynb)

These two datasets were merged and we obtained a dataset with 1093 unique cocktails and their ingredients and recipes.  


### Data Visualization
When a user provides a cocktail name that is present in the database, a bar chart showing cocktail names with corresponding similarities come up.

![](https://github.com/OzanGenc/CocktailAnalysis/blob/main/cocktail_recommendations_example.png)



## Methodology


### Data Preprocessing

#### Preprocessing for Tf-idf Vectorizer
Some preprocessing has been done before applying actual Tf-idf vectorization. 

***Stop words:*** In addition to ENGLISH_STOP_WORDS, the words *'oz', 'simple', 'dash', 'bsp', 'drops'* are added as stop words. These words are present in many ingredients and don't provide much information about uniqueness of a cocktail. 

***Token pattern:*** Tokenization is only done to elements with alphabetical characters. This is done to prevent to get unnecessary tokens of numbers and symbols.


### Implementation
The system makes recommendations based on similarities of the ingredients. All cocktails' ingrediendts are vectorized using Tf-idf technique. Cosine similarities of vectorized ingredients are calculated to find the similarities of the cocktails. The details of the recommendation system can be found on [python file](https://github.com/OzanGenc/CocktailAnalysis/blob/main/utils/utils.py)

**If the user gives name of a cocktail that is present in our database;**

The cocktails with the highest similarity values to given cocktail are recommended to the user with corresponding ingredients and recipes.  

**If the user gives name of the ingredients;**

The given ingredients are vectorized using the same vectorizer and cosine similarities between vectorized input ingredients and cocktails ingredients are calculated. The cocktails with the highest similarity values are recommended to user. 


### Refinement
In the first version of the system, only Hotaling & Co. Cocktail Dataset on Kaggle were used. Despite this dataset has many original cocktails, it lacks some well known ones. It is essential for our database to include popular cocktails because most of the time users will provide these ones. TheCocktailDB is a great website having data of both popular and rare cocktails. Therefore, data from TheCocktailDB has been scraped by using their API and merged with the initial dataset.

Another refinement was adding stop words of *'oz', 'simple', 'dash', 'bsp', 'drops'* to the default stop words in english. These words are present in most of the ingredients and don't provide valuable information in recommendation. Additionally, it is observed that they degrade the performance of the system. For example, if two cocktails have words of drops and oz alot, the calculated similarity between them is inflated than the actual value.

The final refinement is that using a token pattern to only tokenize alphabetical elements. In this way, unnecesary tokens such as numbers and symbols are eliminated.  


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



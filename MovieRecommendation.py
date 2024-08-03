import os 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 


user_ratings_df = pd.read_csv("../input/the-movies-dataset/ratings.csv")
user_ratings_df.head()


movie_metadata = pd.read_csv("../input/the-movies-dataset/movies_metadata.csv")
movie_metadata = movie_names[['title', 'genres']]
movie_metadata.head()


movie_data = user_ratings_df.merge(movie_metadata, on='movieId')
movie_data.head()


user_item_matrix = ratings_data.pivot(index=['userId'], columns=['movieId'], values='rating').fillna(0) """fillna(0): null values with zero"""
user_item_matrix

# Define a KNN model on cosine similarity
cf_knn_model= NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=10, n_jobs=-1)


# Fitting the model on our matrix
cf_knn_model.fit(user_item_matrix)

""" This specifies that a brute-force search algorithm will be used. 
Brute-force search calculates the distance between each pair of points,
which can be computationally intensive but is simple to implement."""

"""n_jobs=-1: This specifies that all available CPU cores should be used 
to perform the computation, which can significantly speed up the process.
"""

def movie_recommender_engine(movie_name, matrix, cf_model, n_recs):
    # Fit model on matrix
    cf_knn_model.fit(matrix) """fit the model on the matrix"""
    
    # Extract input movie ID
    movie_id = process.extractOne(movie_name, movie_names['title'])[2] 
    
    """Uses process.extractOne (probably from the fuzzywuzzy library) 
    to find the most similar movie title in the movie_names['title'] list and extract its corresponding movie ID."""

    """[2] returns the index of the best match"""
    
    # Calculate neighbour distances
    distances, indices = cf_model.kneighbors(matrix[movie_id], n_neighbors=n_recs)
    movie_rec_ids = sorted(list(zip(indices.squeeze().tolist(),distances.squeeze().tolist())),key=lambda x: x[1])[:0:-1]

    """The matrix is likely a 2D array where each row corresponds to a movie and each column corresponds to a feature."""
    """n_neighbors=n_recs: Specifies the number of neighbors to find, 
    where n_recs is the number of recommendations you want to generate."""

    """distances.squeeze().tolist(): Converts the distances array from a multi-dimensional format to a 1D list."""

    """sorted(..., key=lambda x: x[1]): Sorts the list of tuples 
    based on the second element of each tuple (the distance) in ascending order."""

    """[:0:-1]: Slices the sorted list to exclude the first item and reverse the order"""
    """[:0:-1] slicing means starting from the end of the list to the first element (excluding the very first element). 
    This ensures that the recommendations do not include the input movie itself and are sorted in descending order of distance."""
    
    # List to store recommendations
    cf_recs = [] """This list will store the movie recommendations."""
    for i in movie_rec_ids:
        cf_recs.append({'Title':movie_names['title'][i[0]],'Distance':i[1]})

        """'Title': The title of the movie, accessed from movie_names['title'][i[0]].
        'Distance': The distance or similarity score, accessed from i[1]."""

        """So, each item i in movie_rec_ids is a tuple or list where:
            The first element (i[0]) is the movie’s index or ID.
            The second element (i[1]) is the similarity score."""
    
    # Select top number of recommendations needed
    df = pd.DataFrame(cf_recs, index = range(1,n_recs))

    """This converts the list of dictionaries into a pandas DataFrame, with the index ranging from 1 to n_recs."""
     
    return df
from dataclasses import dataclass
import pandas as pd 


@dataclass
class SearchResult:
    """Dataclass to store search results"""
    genres: list = None 
    year: int = None
    rating: int = None


class Recommender:
    """Recommender class to search movies by genre, year and rating"""
    def __init__(self):
        self.data = pd.read_csv('imdb_top_1000.csv')

    def filter_movies(self, search_result):
        """Filter movies based on search results"""
        movies = self.data

        # Apply genre filter
        if search_result.genres:
            movies = movies.loc[movies["Genre"].apply(lambda g: all(genre in g for genre in search_result.genres))]

        # Apply year filter
        if search_result.year:
            movies = movies.loc[movies["Released_Year"] == search_result.year]

        # Apply rating filter
        if search_result.rating:
            movies = movies.loc[movies["Meta_score"] > int(search_result.rating)]

        # Return filtered movie titles
        movies_titles = movies["Series_Title"].tolist()
        return movies_titles if movies_titles else None
        
    def filtered_data(self, movie):
        """Returns the filtered data for a movie"""
        filtered_data = self.data.query(f'Series_Title == "{movie}"')
        columns_to_show = [self.data.columns[i] for i in [1, 2, 4, 8, 9, 10]]
        return filtered_data[columns_to_show]
    
   
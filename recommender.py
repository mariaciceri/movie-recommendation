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

    def search_movies_by_genre(self, search_result):
        """Searches for movies by genre"""
        movies = self.data

        if search_result.genres:
            search_result.genres.sort()
            genre_pattern = ', '.join(search_result.genres) #Converting list to string
            movies_found = movies.loc[movies["Genre"].str.contains(genre_pattern, case=False, na=False)]
            movies_titles = movies_found["Series_Title"].tolist() #Converting series to list
            return movies_titles if movies_titles else 'No movies found'


    def search_movies_by_year(self, search_result):
        """Searches for movies by year"""
        movies = self.data

        if search_result.year:
            movies_found = movies.loc[movies["Released_Year"] == search_result.year]
            movies_titles = movies_found["Series_Title"].tolist() 
            return movies_titles if movies_titles else 'No movies found'



    def search_movies_by_rating(self, search_result):
        """Searches for movies by rating"""
        movies = self.data

        if search_result.rating:
            movies_found = movies.loc[movies["Meta_score"] > int(search_result.rating)]
            movies_titles = movies_found["Series_Title"].tolist()
            return movies_titles if movies_titles else 'No movies found'
        
    def filtered_data(self, movie):
        """Returns the filtered data for a movie"""
        filtered_data = self.data.query(f'Series_Title == "{movie}"')
        columns_to_show = [self.data.columns[i] for i in [1, 2, 4, 5, 8, 9, 10]]
        return filtered_data[columns_to_show]
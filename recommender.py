from dataclasses import dataclass
import pandas as pd 

@dataclass
class SearchResult:
    genres: list = None 
    year: int = None
    rating: int = None

class Recommender:
    def __init__(self):
        self.data = pd.read_csv('imdb_top_1000.csv')

    def search_movies_by_genre(self, search_result):
        movies = self.data

        if search_result.genres:
            search_result.genres.sort()
            genre_pattern = ', '.join(search_result.genres) #Converting list to string
            movies_found = movies.loc[movies["Genre"].str.contains(genre_pattern, case=False, na=False)]
            movies_titles = movies_found["Series_Title"].tolist() #Converting series to list
            return movies_titles if movies_titles else 'No movies found'


    def search_movies_by_year(self, search_result):
        movies = self.data

        if search_result.year:
            movies_found = movies.loc[movies["Released_Year"] == search_result.year]
            movies_titles = movies_found["Series_Title"].tolist() 
            return movies_titles if movies_titles else 'No movies found'



    def search_movies_by_rating(self, search_result):
        movies = self.data

        if search_result.rating:
            movies_found = movies.loc[movies["Meta_score"] > int(search_result.rating)]
            movies_titles = movies_found["Series_Title"].tolist()
            return movies_titles if movies_titles else 'No movies found'
        
    def filtered_data(self, movie):
        filtered_data = self.data.query(f'Series_Title == "{movie}"')
        columns_to_show = [self.data.columns[i] for i in [1, 2, 4, 5, 8, 9, 10]]
        return filtered_data[columns_to_show]
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

    def search_movies(self, search_result):
        movies = self.data
        if search_result.genres:
            search_result.genres.sort()
            genre_pattern = ', '.join(search_result.genres)
            movies = movies.loc[movies["Genre"].str.contains(genre_pattern, case=False, na=False)]
            movies_titles = movies["Series_Title"].tolist()
            print(f"Movies with genres {search_result.genres}: {movies_titles if movies_titles else 'No movies found'}")

        if search_result.year:
            movies = movies.loc[movies["Year"] == search_result.year]
        if search_result.rating:
            movies = movies.loc[movies["IMDB_Rating"] > search_result.rating]
        return movies
    

test = SearchResult(genres=["War", "Comedy", "Fantasy"])
recommender = Recommender()
print(recommender.search_movies(test))

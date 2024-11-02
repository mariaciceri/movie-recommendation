from dataclasses import dataclass
import pandas as pd 

@dataclass
class SearchResult:
    genres: list = None 
    year: int = None
    rating: int = None

class Recommender:
    def __innit__(self):
        self.data = pd.read_csv('imdb_top_1000.csv')

    
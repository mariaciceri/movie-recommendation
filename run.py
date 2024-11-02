from InquirerPy import prompt
from InquirerPy.base.control import Choice
import recommender as rec


def ask_genre_question():
    movies_genre = [
        "Film-Noir",
        "Drama",
        "Mystery",
        "Adventure",
        "Comedy",
        "Action",
        "Crime",
        "Biography",
        "Horror",
        "Fantasy",
        "Animation",
        "Sci-Fi",
        "Thriller",
        "Family",
        "Romance",
        "Western",
        "War",
        "History",
        "Music",
        "Sport",
        "Musical",
        "Documentary",
    ]

    genre_questions = prompt(
        [
            {
                "type": "checkbox",
                "message": "Choose a genre",
                "choices": movies_genre,
                "instruction": "(Press up/down arrows to see more options. Press 'space' to select, 'enter' to confirm)",
            }
        ]
    )

    return genre_questions[0]

def validate_year(year):
    """Validate if the year is between 1920 and 2020 or not provided"""
    try:
        if year == "":
            return True
        year = int(year)
        if year < 1920 or year > 2020:
            return False
        return True
    except ValueError:
        return False
    
def ask_year_question():
    year_questions = prompt(
        [
            {
                "type": "input",
                "message": "Enter a year between 1920 and 2020",
                "instruction": "(Type your answer and press enter to confirm)",
                "validate": lambda result: validate_year(result),
                "invalid_message": "Year must be between 1920 and 2020",
            }
        ]
    )

    return year_questions[0]
    
def validate_rating(rating):
    """Validate if the rating is between 0 and 100 or not provided"""
    try:
        if rating == "":
            return True
        rating = int(rating)
        if rating < 0 or rating > 100:
            return False
        return True
    except ValueError:
        return False
    
def ask_rating_question():
    rating_questions = prompt(
        [
            {
                "type": "input",
                "message": "Enter a rating between 0 and 100",
                "instruction": "(Type your answer and press enter to confirm)",
                "validate": lambda result: validate_rating(result),
                "invalid_message": "Rating must be between 0 and 100",
            }
        ]
    )

    return rating_questions[0]
    
def ask_another_filter_question():
    another_filter_question = prompt(
        [
            {
                "type": "confirm",
                "message": "Do you want to choose another filter?",
                "default": False,
            }
        ]
    )

    return another_filter_question[0]

def ask_continue_question():
    continue_question = prompt(
        [
            {
                "type": "confirm",
                "message": "Do you want to search anew?",
                "default": True,
            }
        ]
    )

    return continue_question[0]

def main():
    print("Welcome to the IMDB Top 1000 Movies Finder")

    search_result = rec.SearchResult()
    while True:
        filter, result = gather_search_params()
        #search_results = search_movies(search_params)
        #display_search_results(search_results)
        if filter == "genre":
            search_result.genres = result
        elif filter == "year":
           search_result.year = result
        elif filter == "rating":
            search_result.rating = result

        another_filter = ask_another_filter_question()

        if not another_filter:
            print(search_result) #show the results
            continue_search = ask_continue_question()
            if not continue_search:
                break

def gather_search_params():

    questions = [
        {
            "type": "list",
            "message": "Choose one of the below options to filter your search",
            "choices": [
                Choice("genre", "Genre"),
                Choice("year", "Year"),
                Choice("rating", "Rating"),
            ],
            "instruction": "(Press 'enter' to confirm)",
        }
    ]

    filter = prompt(questions=questions)[0]
    result = None
    if filter == "genre":
        result = ask_genre_question()
    elif filter == "year":
        result = ask_year_question()
    elif filter == "rating":
        result = ask_rating_question()

    return filter, result

    



if __name__ == "__main__":
    main()




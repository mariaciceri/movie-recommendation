from InquirerPy import prompt
from InquirerPy.base.control import Choice
import recommender as rec
import random
from tabulate import tabulate


def ask_genre_question():
    """Ask user to choose a genre"""
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
                "validate": lambda result: len(result) < 4,
                "invalid_message": "You can only choose up to 3 genres",
            },
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
    """Ask user to enter a year between 1920 and 2020"""
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
    """Ask user to enter a rating between 0 and 100"""
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
    """Ask user if they want to choose another filter"""
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
    """Ask user if they want to continue searching"""
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
    """Main function to run the program"""
    print("Welcome to the Top 1000 Movies Finder \n")
    data = rec.Recommender()
    search_result = rec.SearchResult()
    
    # Ask user to choose a filter to search movies
    while True:
        filter, result = gather_search_params()
        if filter == "genre":
            search_result.genres = result
            list_of_titles = data.filter_movies(search_result)
            display_search_results(list_of_titles, data)
        elif filter == "year":
            search_result.year = result
            list_of_titles = data.filter_movies(search_result)
            display_search_results(list_of_titles, data)
        elif filter == "rating":
            search_result.rating = result
            list_of_titles = data.filter_movies(search_result)
            display_search_results(list_of_titles, data)

        # Ask user if they want to choose another filter
        another_filter = ask_another_filter_question()

        # If user wants to choose another filter, continue the loop
        if not another_filter:
            display_search_results(list_of_titles, data)
            continue_search = ask_continue_question()
            # If user wants to start a new search, reset search_result and continue the loop
            if continue_search:
                search_result = rec.SearchResult()
            if not continue_search:
                print("\nThank you for using the IMDB Top 1000 Movies Finder")
                break

def gather_search_params():
    """Prompt user to choose a filter to search movies"""
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

def display_search_results(list_of_titles, data):
    """Display search results and prompt user to choose a movie"""
    if isinstance(list_of_titles, list):
        five_random_movies = random.sample(list_of_titles, min(5, len(list_of_titles)))
        choices = five_random_movies + ["Back to search"] + ["Exit"]
        questions = [
        {
            "type": "list",
            "message": "Choose a movie",
            "choices": choices,
            "instruction": "(Press 'enter' to see full details)",
        }
    ]
    else:
        print("No movies found")
        return

    movie = prompt(questions=questions)[0]
    if movie == "Back to search":
        return
    if movie == "Exit":
        print("\nThank you for using the Top 1000 Movies Finder")
        return exit()


    print(tabulate(data.filtered_data(movie), headers='keys', tablefmt='pretty', showindex=False))



if __name__ == "__main__":
    main()




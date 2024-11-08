import random
from InquirerPy import prompt
from InquirerPy.base.control import Choice
from tabulate import tabulate
from colored import fore, style
import recommender as rec

# Set up colors for the text
_GREEN = fore('green')
_L_MAGENTA = fore('light_magenta')
_RED = fore('red')
_L_YELLOW = fore('light_yellow')
_RESET = style('reset')


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
    ]

    print(f"\n{_GREEN}Choose up to 3 genres to filter your search{_RESET}")
    instructions_genre = """
Press up/down arrows to see more options.
Press 'SPACE' to select, 'ENTER' to confirm"""
    genre_questions = prompt(
        [
            {
                "type": "checkbox",
                "message": ">",
                "choices": movies_genre,
                "instruction": instructions_genre,
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

    print(f"\n{_GREEN}Enter a year between 1920 and 2020{_RESET}")
    year_questions = prompt(
        [
            {
                "type": "input",
                "message": ">",
                "instruction": "Type your answer and press enter to confirm",
                "validate": lambda result: validate_year(result),
                "invalid_message": "Year must be a whole number between 1920 and 2020",
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

    print(f"\n{_GREEN}Enter a rating between 0 and 100{_RESET}")
    rating_questions = prompt(
        [
            {
                "type": "input",
                "message": ">",
                "instruction": "Type your answer and press enter to confirm",
                "validate": lambda result: validate_rating(result),
                "invalid_message": "Rating must be a whole number between 0 and 100",
            }
        ]
    )

    return rating_questions[0]


def ask_another_filter_question():
    """Ask user if they want to choose another filter"""

    print(f"\n{_GREEN}Do you want to choose another filter?{_RESET}")
    another_filter_question = prompt(
        [
            {
                "type": "confirm",
                "message": "Yes or No",
                "default": False,
            }
        ]
    )

    return another_filter_question[0]


def ask_continue_question():
    """Ask user if they want to continue searching"""

    print(f"\n{_GREEN}Do you want to search anew?{_RESET}")
    continue_question = prompt(
        [
            {
                "type": "confirm",
                "message": "Yes or No",
                "default": True,
            }
        ]
    )

    return continue_question[0]


def gather_search_params():
    """Prompt user to choose a filter to search movies"""

    print(f"{_GREEN}Choose a filter to search movies{_RESET}")
    questions = [
        {
            "type": "list",
            "message": ">",
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


def display_search_results(list_of_titles, data, extra_options):
    """Display search results and prompt user to choose a movie"""
    if isinstance(list_of_titles, list):
        five_random_movies = random.sample(list_of_titles,
                                           min(5, len(list_of_titles)))
        choices = five_random_movies + extra_options.split(", ")

        print(f"{_GREEN}Choose a title below to see full details{_RESET}")
        questions = [
            {
                "type": "list",
                "message": ">",
                "choices": choices,
                "instruction": "(Press 'enter' to select)",
            }
        ]
    else:
        print(f"{_RED}No movies found, try changing your filters{_RESET}")
        return

    answer = prompt(questions=questions)[0]

    if answer == "Back to search" or answer == "Start over":
        return
    if answer == "Exit":
        print(f"""{_L_MAGENTA}
Thank you for using the Top 1000 Movies Finder{_RESET}""")

        return exit()

    print(tabulate(data.filtered_data(answer),
                   headers=[
                       "Title",
                       "Year",
                       "Runtime",
                       "Meta Score",
                       "Director",
                       "Star"],
                   tablefmt='fancy_grid',
                   maxcolwidths=8,
                   numalign="center",
                   stralign="center",
                   showindex=False))
    

def main():
    """Main function to run the program"""

    print(f"\n{_L_MAGENTA}Welcome to the Top 1000 Movies Finder{_RESET}")
    data = rec.Recommender()
    search_result = rec.SearchResult()

    # Ask user to choose a filter to search movies
    while True:
        filter, result = gather_search_params()
        list_of_titles = None
        if filter == "genre":
            search_result.genres = result
            list_of_titles = data.filter_movies(search_result)
            message = (
                f"""Displaying up to 5 random movies with the following genres:
{', '.join(search_result.genres)}""")
        elif filter == "year":
            search_result.year = result
            list_of_titles = data.filter_movies(search_result)
            if (search_result.year == "2020"):
                message = (
                    f"""Displaying up to 5 random movies released in the year:
{search_result.year}.""")
            elif (search_result.year == ""):
                message = (
                    f"""Displaying up to 5 random movies released between 1920
and 2020.""")
            else:
                message = (
                    f"""Displaying up to 5 random movies released in the year:
{search_result.year} until the end of the decade.""")
        elif filter == "rating":
            search_result.rating = result
            list_of_titles = data.filter_movies(search_result)
            if (search_result.rating == ""):
                message =(
                    f"""Displaying up to 5 random movies with a rating equal or
greater than 0.""")
            else:
                message = (
                    f"""Displaying up to 5 random movies with a rating equal
or greater than: {search_result.rating}""")

        if list_of_titles:
            print(f"\n{_L_YELLOW}{message}{_RESET}")
            display_search_results(
                list_of_titles, data, "Back to search, Exit"
                )
        else:
            print(f"{_RED}No movies found, try changing your filters{_RESET}")

        # Ask user if they want to choose another filter
        another_filter = ask_another_filter_question()

        # If user doesn't want to choose another filter, show the final filters
        # and display the search results
        if not another_filter:

            final_display = (
                (f'Genres: {", ".join(search_result.genres)};'
                 if search_result.genres else "") +
                (f" Year: {search_result.year};"
                 if search_result.year else "") +
                (f" Rating: {search_result.rating}."
                 if search_result.rating else "")
                )

            print(f"""\n{_L_YELLOW}Your last (up to) 5 random movies filtered by
{final_display} are:{_RESET}""")
            display_search_results(list_of_titles, data, "Start over, Exit")

            continue_search = ask_continue_question()
            # If user wants to start a new search,
            # _RESET search_result and continue the loop
            if continue_search:
                search_result = rec.SearchResult()
            else:
                print(f"""{_L_MAGENTA}
Thank you for using the IMDB Top 1000 Movies Finder{_RESET}""")
                break


if __name__ == "__main__":
    main()

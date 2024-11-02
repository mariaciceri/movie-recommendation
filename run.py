from InquirerPy import prompt


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
    

def main():
    
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
                "instruction": "(Use arrow up/down to see more genre options. Use space to select, enter to confirm)",
            }
        ]
    )

    chosen_genres = genre_questions[0]


    year_questions = prompt(
        [
            {
                "type": "input",
                "message": "Enter a year between 1920 and 2020",
                "instruction": "(Press enter to confirm)",
                "validate": lambda result: validate_year(result),
                "invalid_message": "Year must be between 1920 and 2020",
            }
        ]
    )

    chosen_year = year_questions[0]

    

main()


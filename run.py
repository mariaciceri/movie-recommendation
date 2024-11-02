from InquirerPy import prompt


def genres_question():
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
    
def year_question():
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
    
def rating_question():
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
    

def main():
    
    chosen_genres = genres_question()

    chosen_year = year_question()
    
    chosen_rating = rating_question()
    
    print(chosen_genres, chosen_year, chosen_rating)

if __name__ == "__main__":
    main()


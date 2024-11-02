from InquirerPy import prompt


def main():
    
    movies_categories = [
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
                "choices": movies_categories,
                "instruction": "(Use arrow up/down to see more genre options. Use space to select, enter to confirm)",
            }
        ]
    )



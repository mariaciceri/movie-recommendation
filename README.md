# Top 1000 Movies Finder

Top 1000 Movies Finder is a Python program that suggests movies based on filters selected by the user. It runs in the Code Institute mock terminal on Heroku.

User can choose to filter movies by genre (up to three), year (between 1920 and 2020) and/or rating (between 0 and 100).

[Check the project here!](https://best-1000-movie-finder-37b039113a18.herokuapp.com/)

![Am I responsive screenshot](/docs/images/am-i-responsive.png)

## How to Use

When coming to the page, the user is welcomed and prompted to choose a filter to start the search. Then they must use arrow up or down to select one of the three options (Genre, Year, Rating) and press enter.

If "Genre" selected, a list with all the genres available are displayed and the user must use arrow up or down to navigate through the options and press space to select up to three genres and then press enter to confirm.

If "Year" selected, the user must type their answer (a year between 1920 and 2020) and press enter to confirm.

If "Rating" selected, the user must type their answer (a number between 0 and 100) and press enter to confirm.

After each input, the user will have a list of up to 5 movie titles to select to see full details and a "Back to search" and "Exit" option.

The "Back to search" option takes the user to the filter selection part and the "Exit" ends the program.

If the user do not wish to filter further, a last list of movies will be displayed and they will be asked if they want to restart the search, if "Yes" answered, the filters are emptied and they can start over the search, otherwise the program will end and a message thanking them for using the program will be displayed.

None of the filter are mandatory, meaning that if the user selects a filter and regrets choosing it, a simple enter will make a random movie list appear without being affected by that specific filter. 

## Features
### Existing Features

+ Interactive menu to choose filter;

![Filter selection menu](/docs/images/welcome-message.png)

+ Checkbox style genre selection;

![Genre selection manu](/docs/images/genre-selection.png)

+ Movie titles displayed in a interactive menu:

![Movie titles display](/docs/images/movie-title-display.png)

+ Movie details displayed in a table for readability:

![Table with movie information](/docs/images/full-details-display.png)

+ Possibility to filter movies using one, two or all categories;
+ Possibility to start over the search;


### Future Features

+ Allow user to mark movies as seen and not display them anymore;

## Technologies

+ [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) is the language used in the program;
+ [InquirerPy](https://inquirerpy.readthedocs.io/en/latest/) is the Python Package used to create the interactive command-line interface;
+ [Pandas](https://pandas.pydata.org/) is the library used to read and retrieve data from the dataset;
+ [Tabulate](https://pypi.org/project/tabulate/) is the library used to style the table with movie information to the user;
+ [Colored](https://pypi.org/project/colored/) is used to style the print statements in the program;
+ [Python Classes](https://docs.python.org/3/tutorial/classes.html) is used to manage dealing with dataset requests;
+ [Data Class](https://docs.python.org/3/library/dataclasses.html) is used to store filters chosen by the user.

## Deployment

+ The project was deployed using Code Institute's mock terminal for Heroku, following this steps:
    + On the terminal, paste `kaggle datasets download harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows`;
    + On the terminal, create a .kaggle directory (`mkdir .kaggle`) on your main directory
    + Move the downloaded file(named 'kaggle') into .kaggle using the command `mv {source_path} {destination_path}`;
    + Clone the [repository](https://github.com/mariaciceri/movie-recommendation) from GitHub page;
    + Create a new Heroku app;
    + In the Settings tab, set the buildpacks to Python and NodeJS in that order;
    + In the Settings tab, set two the Config Vars:
        + CREDS(key): The information inside the kaggle file you downloaded previously(value)
        + PORT(key): 8000(value)
    + In the Deploy tab, scroll down to Manual Deploy, confirm that you are deploying from main and click on "Deploy Branch"
    + Alternatively, enable "Enable Automatic Deploys"

## Testing
### Manual Testing
+ The project was manually tested by doing the following:
    + When selecting filters: press arrow up/down key to movie the cursor:
        + It moves the cursor up and down, changing the color of the selected filter.
    + Press enter when filter is selected:
        + Displays the input area, giving instructions on how to do it.
    + Insert wrong input (too many genres or year/rating out of range or invalid):
        + Displays a message at the bottom stating what is expected for input, not allowing to do anything else until the input is correct.
    + Press "Back to search" buttom:
        + Prompts users if they would like to choose another filter.
    + Press "Exit":
        + Ends the program and display thank you message.
    + Press "Start over":
        + Prompts the user if want to start anew.
    + Select one of the movie titles displayed:
        + Display a table with information about the movie and prompts if the user wants to choose anothe filter.


### Bugs
#### Solved Bugs

+ Bug: When searching for rating, a TypeError was raised indicating that it was trying to compare string and integer.
    + Fix: Convert the user input into integer to match the value from the dataset.
+ Bug: After calculating how long until the end of the decade, retrieving data was raising a TypeError.
    + Fix: Convert the year into string to match the value from the dataset.
+ Bug: When "Exit" pressed, it was not ending the program but instead asking if user wanted t start over:
    + Fix: Return exit() method to break the loop.
+ Bug: When more than one genre was selected and not in the same order as in the dataset, no movie was returned.
    + Fix: use aapply() method to search with lambda function using all() to check if each genre was in the whole genre string in the dataset.

#### Unsolved Bugs

+ No known unsolved bug is present in the project.

#### Validator Testing

+ No errors were found by the PEP8.

## Credits

+ Video on how to use [Pandas](https://www.youtube.com/watch?v=DkjCaAMBGWM&ab_channel=RobMulla) is from Rob Mulla channel;
+ Post on how to use [Tabulate](https://www.datacamp.com/tutorial/python-tabulate?dc_referrer=https%3A%2F%2Fwww.google.com%2F) is from Datacamp;
+ Dataset is taken from [Kaggle](https://www.kaggle.com/);


# Top 1000 Movies Finder

Top 1000 Movies Finder is a Python program that suggests movies based on the user's selected filters. It runs in the Code Institute mock terminal on Heroku.

The user can choose to filter movies by genre (up to three), year (between 1920 and 2020), and/or rating (between 0 and 100).

[Check the project here!](https://best-1000-movie-finder-37b039113a18.herokuapp.com/)

![Am I responsive screenshot](/docs/images/am-i-responsive.png)

## How to Use

+ When coming to the page, the user is welcomed and prompted to choose a filter to start the search. Then they must use the arrow up or down to select one of the three options (Genre, Year, Rating) and press enter.

+ If "Genre" is selected, a list with all the genres available is displayed. The user must use the arrow keys up or down to navigate through the options, press space to select up to three genres, and then press enter to confirm.

+ If "Year" is selected, the user must type their answer (a year between 1920 and 2020) and press enter to confirm.

+ If "Rating" is selected, the user must type their answer (a number between 0 and 100) and press enter to confirm.

+ After each input, the user will have a list of up to 5 movie titles to select to see full details and a "Back to search" and "Exit" option.

+ The user is asked if they want to choose another filter and they must type "Y"(yes) or "N"(no) to answer. This is insensitive to capitalization.

+ The "Back to search" option takes the user to the filter selection part and the "Exit" ends the program.

+ If the user does not wish to filter further, a last list of movies will be displayed and they will be asked if they want to restart the search, if "Y" is answered, the filters are emptied and they can start over the search, otherwise, "N" is press, the program will end and a message thanking them for using the program will be displayed.

+ None of the filters are mandatory, meaning that if the user selects a filter and regrets choosing it, a simple "enter" will make a random movie list appear without being affected by that specific filter. 

+ This flow chart demonstrates how the program runs:
![Flow chart of the program](/docs/images/flowchart.png)

## Features
### Existing Features

+ Interactive menu to choose filter;

![Filter selection menu](/docs/images/welcome-message.png)

+ Checkbox style genre selection;

![Genre selection manu](/docs/images/genre-selection.png)

+ Movie titles displayed in an interactive menu:

![Movie titles display](/docs/images/movie-title-display.png)

+ Movie details displayed in a table for readability:

![Table with movie information](/docs/images/full-details-display.png)

+ Possibility to filter movies using one, two, or all categories;
+ Possibility to start over the search;

+ Clear error messages and no possibility to continue until the error is fixed:

![Too many genres selected error message](/docs/images/genre-validation.png)
![Year out of range error messa](/docs/images/year-validation.png)
![Rating out of range error message](/docs/images/rating-validation.png)

+ No movie found message when there is no movie available in the database that matches the filters:

![No movies found message](/docs/images/no-movies-found.png)

### Future Features

+ Allow the user to mark movies as seen and not display them anymore;

## Technologies

+ [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) is the language used in the program;
+ [InquirerPy](https://inquirerpy.readthedocs.io/en/latest/) is the Python Package used to create the interactive command-line interface;
+ [Pandas](https://pandas.pydata.org/) is the library used to read and retrieve data from the dataset;
+ [Tabulate](https://pypi.org/project/tabulate/) is the library used to style the table with movie information for the user;
+ [Colored](https://pypi.org/project/colored/) is used to style the print statements in the program;
+ [Python Classes](https://docs.python.org/3/tutorial/classes.html) is used to structure code in a way that makes it more readable, reusable, and maintainable. By modeling real-world entities and concepts, classes help encapsulate data and behavior, making code more intuitive and easier to manage.
In this project, the OOP principles of encapsulation and separation of concerns are applied as the main class "Recommender" was created to separate the logic that handles the dataset from the code that manages user interactions. This allowed the project to be much easier to debug.
+ [Data Class](https://docs.python.org/3/library/dataclasses.html) is used to store filters chosen by the user.
+ [Gitpod](https://gitpod.io/) with [VSCode](https://code.visualstudio.com/) desktop extension is the IDE for the project;
+ [Git](https://git-scm.com/) is used for version control;
+ [Github](https://github.com/) is used for hosting the page;
+ [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) is used as the start script to run the Code Institute mock terminal on the browser;

## Deployment

+ The project was deployed using Code Institute's mock terminal for Heroku.

### Deployment to Heroku

+ Clone the repository from GitHub page by running the command `git clone https://github.com/mariaciceri/movie-recommendation.git`;
+ Save the project on your own GitHub account by using the command `git push`
+ Create a new Heroku app by clicking on "New" and then "Create new app" on their page;
![Heroku menu with new app creating menu](/docs/images/heroku-new-app.png)
+ In the Deploy tab, look for "Deployment method" and select GitHub;
![Heroku menu with deploy selected](/docs/images/heroku-deploy.png)
+ Connect to your GitHub account if not done already and right below it, find your repository and connect to Heroku;
![Heroku Deployment method and App connected to GitHub](/docs/images/heroku-github.png)
+ Give your app a unique name and set the region accordingly. Click create app.
+ In the Settings tab, add to the buildpacks Python and NodeJS scripts in that order;
![Heroku menu after creating a new app with "Settings" selected](/docs/images/heroku-settings.png)
![Heroku buildpacks](/docs/images/heroku-buildpacks.png)
+ In the Settings tab, set one Config Vars:
    + PORT(key): 8000(value)
![Heroku config vars](/docs/images/heroku-config-vars.png)
+ In the Deploy tab, scroll down to Manual Deploy, confirm that you are deploying from "main" and click on "Deploy Branch";
![Heroku Manual deploy](/docs/images/heroku-manual-deploy.png)
+ Alternatively, enable "Enable Automatic Deploys";
![Heroku Automatic deploy](/docs/images/heroku-automatic-deploy.png)
+ It may take a couple of minutes to deploy, after completed, a "View" button will be available and it will take you to the deployed page.

### Run locally

+ If Python ins't installed, download from the [official webpage](https://www.python.org/downloads/).
+ For this project to run with all its functionalities, install:
    + `pip install colored InquirerPy pandas tabulate`
+ Clone the repository from GitHub page by running the command `git clone https://github.com/mariaciceri/movie-recommendation.git` 
+ Alternatively, download it as a ZIP file from `https://github.com/mariaciceri/movie-recommendation` and extract it to a chosen location in your computer;

## Testing
### Manual Testing
+ The project was manually tested by doing the following:
    + When selecting filters: press the arrow up/down key to move the cursor:
        + It moves the cursor up and down, changing the color of the selected filter.
    + Press enter when the filter is selected:
        + Displays the input area, giving instructions on how to do it.
    + Insert wrong input (too many genres or year/rating out of range or invalid):
        + Displays a message at the bottom stating what is expected for input, not allowing to do anything else until the input is correct.
    + Press "Back to search":
        + Prompts users if they would like to choose another filter.
    + Press "Exit":
        + Ends the program and displays a thank you message.
    + Press "Start over":
        + Prompts the user if want to start anew.
    + Select one of the movie titles displayed:
        + Display a table with information about the movie and prompts if the user wants to choose another filter.

### Validator Testing

+ No errors were found by the PEP8 in both Python files.
![Screenshot of Code Institute's Python Style Validator for the run.py file](/docs/images/run-py-validator.png)
![Screenshot of Code Institute's Python Style Validator for the recommender.py file](/docs/images/recommender-validator.png)

### Bugs
#### Solved Bugs

+ Bug: When searching for rating, a TypeError was raised indicating that it was trying to compare string and integer.
    + Fix: Convert the user input into integer to match the value from the dataset.
+ Bug: After calculating how long until the end of the decade, retrieving data was raising a TypeError.
    + Fix: Convert the year into string to match the value from the dataset.
+ Bug: When "Exit" was pressed, it did not end the program but instead asked if the user wanted to start over:
    + Fix: Return exit() method to break the loop.
+ Bug: When more than one genre was selected and not in the same order as in the dataset, no movie was returned.
    + Fix: use apply() method to search with lambda function using all() to check if each genre was in the whole genre string in the dataset.

#### Unsolved Bugs

+ No known unsolved bug is present in the project.

## Credits

+ Video on how to use [Pandas](https://www.youtube.com/watch?v=DkjCaAMBGWM&ab_channel=RobMulla) is from Rob Mulla channel;
+ Post on how to use [Tabulate](https://www.datacamp.com/tutorial/python-tabulate?dc_referrer=https%3A%2F%2Fwww.google.com%2F) is from Datacamp;
+ Dataset is taken from [Kaggle](https://www.kaggle.com/) and all the information on how to use install it;
+ Deployed template was provided by Code Institute;
+ Deployment to Heroku step-by-step was taken from Love Sandwiches walkthrough project from Code Institute; 

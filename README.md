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

+ 

### Future Filters


## Technologies



## Data Model

## Deployment


## Testing

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

#### Unsolved Bugs

#### validator Testing


## Credits


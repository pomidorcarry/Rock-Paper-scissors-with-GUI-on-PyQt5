# ROCK PAPER SCISSORS with GUI on PyQt5
## TO DO 
 - Tests
 - Rearrange project architecture
 - add interest api for random pictures
#### Description:


This project was made to learn basics of PyQt5 python framework, while creating a simple gui window application.
The application itself is a classic rock paper scissors game

- project.py - top level script that runs the program;

- main_window.py - file containing a MainWindow class, inheriting from QMainWindow, that handles drawing essentail main window with a PyQt stacked layout and swtiches between pages with .setCurrentIndex method;

- project.spce - pyinstaller specification to create exe files;
- requirements.txt - list of necessary 3rd party modules to run source code

- pages/ folder contains pages or sub windows, each file is responsible only for it's own page
    - page1.py - file containing the first page with the title and name input textbox, options to quit or start the game;
    - page2.py - file containing the second page with the game itself, allowing the player to chose rock paper or scissors button;
    - page3.py - file containing the third page with a loading gif that's set on timer;
    - page4.py - file containing the forth page with the result of a round, asking player wether he'd like to play again or quit;
- widgets/ folder contains all custom widgets created for the app
    - custom_dialog.py - file containing CustomDialog(QDialog) class that creates a dialog window showing an error message;

 - utility/ folder contains utility modules that are used for inner logic in the project;
     - game.py - file with the Game class with methods handling player's interactions;
     - player.py - file with the Player class with attributes and methods to represent a player;
     - service.py - file with methods used only for injecting specific universal logic;
- assets/ - folder with all images or other assets necessary for the game, such as picures, gifs and fonts



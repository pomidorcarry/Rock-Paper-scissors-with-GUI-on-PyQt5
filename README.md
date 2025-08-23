    # ROCK PAPER SCISSORS with GUI on PyQt5
    
    #### Description:
    TODO
    Make page 2 and apge 3
    Make the score in the top right corner
    Make the basic game loop

    This project was made to learn basics of PyQt5 python framework, while creating a simple gui window application.
    The application itself is a classic rock paper scissors game

    project.py - top level script that runs the program
    main_window.py - file containing a MainWindow class, inheriting from QMainWindow, that handles drawing essentail main window with a PyQt stacked layout and swtiches between pages with .setCurrentIndex method.
    pages/ folder contains pages or sub windows, each file is responsible only for it's own page
    page1.py - file containing the first page with the title and name input textbox
    page2.py - file containing the second page with the game itself, allowing the player to chose rock paper or scissors button
    page3.py - file containing the third page with the result of a round, asking player wether he'd like to play again or quit
    widgets/ folder contains all custom widgets created for the app
    custom_dialog.py - file containing CustomDialog(QDialog) class that creates a dialog window showing an error message
    assets/ - folder with all images or other assets necessary for the game



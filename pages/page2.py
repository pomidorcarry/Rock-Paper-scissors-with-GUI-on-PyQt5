from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMainWindow, QPushButton,  QDesktopWidget, QButtonGroup, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, QLineEdit, QLabel, QApplication, QMessageBox, QDialog, QDialogButtonBox, QRadioButton

from PyQt5.QtCore import Qt, QSize

# from main_window import MainWindow

class Page2(QWidget):
    def __init__(self,main_window):
        super().__init__()
        self.main_window = main_window

        self.horizontal_layout = QHBoxLayout()
        self.verical_layout = QVBoxLayout()
        self.grid_layout = QGridLayout()

        self.initUI_horizontal_layout(self.horizontal_layout)
        self.initUI_grid_layout(self.grid_layout)
        self.initUI_vertical_layout(self.verical_layout)
        # verical_layout.addLayout(horizontal_layout)

        self.setStyleSheet("""
                                QWidget{
                                font-size: 25px;
                                font-family: Garamond;
                                            }
                                QLabel#title{
                                font-size: 50px;
                                font-weight: bold;
                                            }
                                QLineEdit{
                                font-size: 25px;
                                border-radius: 10;
                                            }
                                QPushButton{
                                font-weight: bold;
                                background-color: #f0a860;
                                border-radius: 15;
                                            }
                                QPushButton:hover{
                                font-weight: bold;
                                background-color: #faddc0;
                                border-radius: 15;
                                            }
                                                """)

        self.setLayout(self.verical_layout)

    def initUI_horizontal_layout(self,horizontal_layout:QHBoxLayout):
        pass

    def initUI_vertical_layout(self,vertical_layout:QVBoxLayout):
        score = QLabel(f"{self.main_window.player.name}:{self.main_window.player.score}\ncpu:{self.main_window.cpu.score}")
        title = QLabel("Choose one")
        vertical_layout.addWidget(score,alignment=Qt.AlignRight)
        vertical_layout.addWidget(title,alignment=Qt.AlignHCenter)
        vertical_layout.addLayout(self.grid_layout)
        button = QPushButton("I've made my choice")
        button.clicked.connect(self.make_option_choice)
        # verical_layout.addWidget(title,alignment=Qt.AlignHCenter)
        vertical_layout.addWidget(button,alignment=Qt.AlignHCenter)

    def initUI_grid_layout(self,grid_layout:QGridLayout):
        picture_rock = QLabel("Rock")
        picture_paper = QLabel("Paper")
        picture_scissors = QLabel("Scissors")

        button_rock = QRadioButton("Rock")
        button_paper = QRadioButton("Paper")
        button_scissors = QRadioButton("Scissors")

        button_rock.toggled.connect(self.radio_button_changed)
        button_paper.toggled.connect(self.radio_button_changed)
        button_scissors.toggled.connect(self.radio_button_changed)

        game_buttons_group = QButtonGroup()
        game_buttons_group.addButton(button_rock)
        game_buttons_group.addButton(button_paper)
        game_buttons_group.addButton(button_scissors)


        grid_layout.addWidget(picture_rock,0,0)
        grid_layout.addWidget(picture_paper,0,1)
        grid_layout.addWidget(picture_scissors,0,2)

        grid_layout.addWidget(button_rock,1,0)
        grid_layout.addWidget(button_paper,1,1)
        grid_layout.addWidget(button_scissors,1,2)

        grid_layout.setAlignment(Qt.AlignHCenter)

    def radio_button_changed(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            self.main_window.player.choice = radio_button.text()
        # print(self.main_window.player_option_choice)

    def make_option_choice(self):
        if self.main_window.player.choice:
            self.main_window.switch_to_page_3()
        else:
            print("error")
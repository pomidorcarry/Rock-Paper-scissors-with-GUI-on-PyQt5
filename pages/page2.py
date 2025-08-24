from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMainWindow, QPushButton,  QDesktopWidget, QButtonGroup, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, QLineEdit, QLabel, QApplication, QMessageBox, QDialog, QDialogButtonBox, QRadioButton

from PyQt5.QtCore import Qt, QSize

from utility.player import Player
from utility.game import Game
# from main_window import MainWindow

class Page2(QWidget):
    def __init__(self,main_window):
        super().__init__()
        self.main_window = main_window

        self.local_player_choice = None

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
        self.score = QLabel(f"{self.main_window.player.name}:{self.main_window.player.score}\ncpu:{self.main_window.cpu.score}")
        title = QLabel("Choose one")
        vertical_layout.addWidget(self.score,alignment=Qt.AlignRight)
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

        self.button_rock = QRadioButton("Rock")
        self.button_paper = QRadioButton("Paper")
        self.button_scissors = QRadioButton("Scissors")

        self.button_rock.toggled.connect(self.radio_button_changed)
        self.button_paper.toggled.connect(self.radio_button_changed)
        self.button_scissors.toggled.connect(self.radio_button_changed)

        self.game_buttons_group = QButtonGroup()
        # self.game_buttons_group.setExclusive(False)
        self.game_buttons_group.addButton(self.button_rock)
        self.game_buttons_group.addButton(self.button_paper)
        self.game_buttons_group.addButton(self.button_scissors)


        grid_layout.addWidget(picture_rock,0,0)
        grid_layout.addWidget(picture_paper,0,1)
        grid_layout.addWidget(picture_scissors,0,2)

        grid_layout.addWidget(self.button_rock,1,0)
        grid_layout.addWidget(self.button_paper,1,1)
        grid_layout.addWidget(self.button_scissors,1,2)

        grid_layout.setAlignment(Qt.AlignHCenter)

    def radio_button_changed(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            self.local_player_choice = radio_button.text()
        # print(self.local_player_choice)

    def make_option_choice(self):
        if self.local_player_choice:
            self.main_window.player.choice = self.local_player_choice
            self.main_window.cpu.choice = Player.cpu_make_choice()
            # self.main_window.game_result = Game.game_result(cpu=self.main_window.cpu,player=self.main_window.player)
            # print(self.main_window.player.choice)
            self.main_window.switch_to_page_3()
            # print(self.main_window.player.choice)
        else:
            print("error")
    
    def update_values(self):
        self.game_buttons_group.setExclusive(False)
        for button in self.game_buttons_group.buttons():
            button.setChecked(False)
        self.game_buttons_group.setExclusive(True)
        # self.button_paper.setChecked(False)
        # self.button_rock.setChecked(False)
        # self.button_scissors.setChecked(False)
        self.score.setText(f"{self.main_window.player.name}:{self.main_window.player.score}\ncpu:{self.main_window.cpu.score}")
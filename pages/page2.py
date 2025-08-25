from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import (
    QMainWindow,
    QPushButton,
    QDesktopWidget,
    QButtonGroup,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QStackedLayout,
    QLineEdit,
    QLabel,
    QApplication,
    QMessageBox,
    QDialog,
    QDialogButtonBox,
    QRadioButton,
)
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt, QSize

from utility.player import Player
from utility.game import Game
from widgets.custom_dialog import CustomDialog

# from main_window import MainWindow


class Page2(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.resource_path = self.main_window.resource_path
        self.local_player_choice = None

        self.horizontal_layout = QHBoxLayout()
        self.verical_layout = QVBoxLayout()
        self.grid_layout = QGridLayout()

        self.initUI_horizontal_layout(self.horizontal_layout)
        self.initUI_grid_layout(self.grid_layout)
        self.initUI_vertical_layout(self.verical_layout)

        self.title.setObjectName("title")
        self.setStyleSheet(
            """
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
                            border-radius: 10px;
                                        }
                            QPushButton{
                            font-weight: bold;
                            background-color: #f0a860;
                            border-radius: 15px;
                                        }
                            QPushButton:hover{
                            font-weight: bold;
                            background-color: #faddc0;
                            border-radius: 15px;
                                        }
                                            """
        )

        self.setLayout(self.verical_layout)

    def initUI_horizontal_layout(self, horizontal_layout: QHBoxLayout):
        pass

    def initUI_vertical_layout(self, vertical_layout: QVBoxLayout):
        self.title = QLabel("Choose one")
        self.score = QLabel(
            f"{self.main_window.player.name}:{self.main_window.player.score}\ncpu:{self.main_window.cpu.score}"
        )
        button = QPushButton("I've made my choice")
        button.setFixedSize(QSize(260, 60))
        button.clicked.connect(self.make_option_choice)

        vertical_layout.setSpacing(50)
        vertical_layout.addWidget(self.score, alignment=Qt.AlignRight)
        vertical_layout.addWidget(self.title, alignment=Qt.AlignHCenter)
        vertical_layout.addLayout(self.grid_layout)
        vertical_layout.addWidget(button, alignment=Qt.AlignHCenter)
        vertical_layout.addSpacing(50)

    def initUI_grid_layout(self, grid_layout: QGridLayout):
        pics = []
        self.picture_rock = QLabel()
        self.picture_paper = QLabel()
        self.picture_scissors = QLabel()
        rock_pic = self.resource_path("assets/picture_3.jpg")
        rock_pic = rock_pic.replace("\\", "/")
        paper_pic = self.resource_path("assets/picture_2.jpg")
        paper_pic = paper_pic.replace("\\", "/")
        scissors_pic = self.resource_path("assets/picture_4.jpg")
        scissors_pic = scissors_pic.replace("\\", "/")
        self.picture_rock.setStyleSheet(
            f"""
            border-image: url({rock_pic});
            border-radius: 15px;
        """
        )
        self.picture_paper.setStyleSheet(
            f"""
            border-image: url({paper_pic});
            border-radius: 15px;
        """
        )
        self.picture_scissors.setStyleSheet(
            f"""
            border-image: url({scissors_pic});
            border-radius: 15px;
        """
        )

        self.picture_rock.setMinimumSize(QSize(200, 200))
        self.picture_rock.setScaledContents(True)
        self.picture_paper.setMinimumSize(QSize(200, 200))
        self.picture_paper.setScaledContents(True)
        self.picture_scissors.setMinimumSize(QSize(200, 200))
        self.picture_scissors.setScaledContents(True)

        self.button_rock = QRadioButton("Rock")
        self.button_paper = QRadioButton("Paper")
        self.button_scissors = QRadioButton("Scissors")

        self.button_rock.toggled.connect(self.radio_button_changed)
        self.button_paper.toggled.connect(self.radio_button_changed)
        self.button_scissors.toggled.connect(self.radio_button_changed)

        self.game_buttons_group = QButtonGroup()

        self.game_buttons_group.addButton(self.button_rock)
        self.game_buttons_group.addButton(self.button_paper)
        self.game_buttons_group.addButton(self.button_scissors)

        grid_layout.addWidget(self.picture_rock, 0, 0)
        grid_layout.addWidget(self.picture_paper, 0, 1)
        grid_layout.addWidget(self.picture_scissors, 0, 2)

        grid_layout.addWidget(self.button_rock, 1, 0, alignment=Qt.AlignHCenter)
        grid_layout.addWidget(self.button_paper, 1, 1, alignment=Qt.AlignHCenter)
        grid_layout.addWidget(self.button_scissors, 1, 2, alignment=Qt.AlignHCenter)

        grid_layout.setAlignment(Qt.AlignHCenter)

    def radio_button_changed(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            self.local_player_choice = radio_button.text()

    def make_option_choice(self):
        if self.local_player_choice:
            self.main_window.player.choice = self.local_player_choice
            self.main_window.cpu.choice = Player.cpu_make_choice()
            # self.main_window.game_result = Game.game_result(player=self.main_window.player,cpu=self.main_window.cpu)
            # print()
            self.main_window.switch_to_page_3()
        else:
            CustomDialog.error_dialog("Please choose one")

    def update_values(self):
        self.game_buttons_group.setExclusive(False)
        for button in self.game_buttons_group.buttons():
            button.setChecked(False)
        self.game_buttons_group.setExclusive(True)
        self.local_player_choice = None
        self.score.setText(
            f"{self.main_window.player.name}:{self.main_window.player.score}\ncpu:{self.main_window.cpu.score}"
        )

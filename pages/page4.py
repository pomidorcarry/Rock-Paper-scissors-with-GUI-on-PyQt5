from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import (
    QMainWindow,
    QPushButton,
    QDesktopWidget,
    QButtonGroup,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QStackedLayout,
    QLineEdit,
    QLabel,
    QApplication,
    QMessageBox,
    QDialog,
    QDialogButtonBox,
)

from PyQt5.QtCore import Qt, QSize

# from page2 import Page2
from utility.game import Game


class Page4(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.result = self.main_window.game_result
        self.score = QLabel(
            f"{self.main_window.player.name}:{self.main_window.player.score}\ncpu:{self.main_window.cpu.score}"
        )
        self.vertical_layout = QVBoxLayout()
        self.horizontal_layout_1 = QHBoxLayout()
        self.horizontal_layout_2 = QHBoxLayout()

        self.initUI_horizontal_layout_1(horizontal_layout=self.horizontal_layout_1)
        self.initUI_horizontal_layout_2(horizontal_layout=self.horizontal_layout_2)
        self.initUI_vertical_layout(vertical_layout=self.vertical_layout)
        self.title.setObjectName("title")
        self.setStyleSheet(
            """
                                QWidget{
                                font-size: 35px;
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
                                                """
        )
        self.setLayout(self.vertical_layout)

    def initUI_horizontal_layout_1(self, horizontal_layout: QHBoxLayout):
        self.player_choice = QLabel(f"You chose\n {self.main_window.player.choice}")
        self.cpu_choice = QLabel(f"Cpu chose\n {self.main_window.cpu.choice}")
        vs_label = QLabel("VS")
        vs_label.setStyleSheet(
            """
                                font-size: 25px;
                                font-family: Garamond;
                                font-weight: bold;
                            """
        )
        horizontal_layout.setSpacing(20)
        horizontal_layout.addWidget(self.player_choice)
        horizontal_layout.addWidget(vs_label)
        horizontal_layout.addWidget(self.cpu_choice)
        horizontal_layout.setAlignment(Qt.AlignHCenter)

    def initUI_vertical_layout(self, vertical_layout: QVBoxLayout):

        self.title = QLabel("Game results!")

        self.game_result = QLabel(f"{self.result}")

        vertical_layout.addWidget(self.score, alignment=Qt.AlignRight)
        vertical_layout.addWidget(self.title, alignment=Qt.AlignHCenter)

        vertical_layout.addLayout(self.horizontal_layout_1)

        vertical_layout.addWidget(self.game_result, alignment=Qt.AlignHCenter)
        vertical_layout.addLayout(self.horizontal_layout_2)

    def initUI_horizontal_layout_2(self, horizontal_layout: QHBoxLayout):
        self.start_button = QPushButton("Play again")
        self.quit_button = QPushButton("Exit")

        self.start_button.setFixedSize(200, 60)
        self.start_button.clicked.connect(self.play_again)

        self.quit_button.setFixedSize(200, 60)
        self.quit_button.clicked.connect(self.main_window.close)

        horizontal_layout.addWidget(self.start_button)
        horizontal_layout.addWidget(self.quit_button)

    def play_again(self):
        self.main_window.switch_to_page_2()

    def update_values(self):
        self.player_choice.setText(f"You chose {self.main_window.player.choice}")
        self.cpu_choice.setText(f"Cpu chose {self.main_window.cpu.choice}")
        self.game_result.setText(
            f"{Game.game_result(player=self.main_window.player,cpu=self.main_window.cpu)}"
        )
        self.score.setText(
            f"{self.main_window.player.name}:{self.main_window.player.score}\ncpu:{self.main_window.cpu.score}"
        )

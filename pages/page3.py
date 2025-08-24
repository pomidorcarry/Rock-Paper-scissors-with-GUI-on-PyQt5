
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMainWindow, QPushButton,  QDesktopWidget, QButtonGroup, QWidget, QVBoxLayout, QHBoxLayout, QStackedLayout, QLineEdit, QLabel, QApplication, QMessageBox, QDialog, QDialogButtonBox

from PyQt5.QtCore import Qt, QSize

# from page2 import Page2
from utility.game import Game

class Page3(QWidget):
    def __init__(self,main_window):
        super().__init__()
        self.main_window = main_window
        self.main_window.cpu.choice = Game.cpu_make_choice()
        self.result = Game.game_result(cpu=self.main_window.cpu,player=self.main_window.player)
        self.score = QLabel(f"{self.main_window.player.name}:{self.main_window.player.score}\ncpu:{self.main_window.cpu.score}")
        self.vertical_layout = QVBoxLayout()
        self.horizontal_layout = QHBoxLayout()

        self.initUI_horizontal_layout(horizontal_layout=self.horizontal_layout)
        self.initUI_vertical_layout(vertical_layout=self.vertical_layout)
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
        self.setLayout(self.vertical_layout)


    def initUI_vertical_layout(self,vertical_layout:QVBoxLayout):

        title = QLabel("This is page 3")
        player_choice = QLabel(f"You chose {self.main_window.player.choice}")
        cpu_choice = QLabel(f"Cpu chose {self.main_window.cpu.choice}")
        game_result = QLabel(f"{self.result}")
        # page_3_button.clicked.connect(switch_to_page_1)



        vertical_layout.addWidget(self.score,alignment=Qt.AlignHCenter)
        vertical_layout.addWidget(title,alignment=Qt.AlignHCenter)
        # page_3_layout.addWidget(page_3_button,alignment=Qt.AlignHCenter)
        vertical_layout.addWidget(cpu_choice,alignment=Qt.AlignHCenter)
        vertical_layout.addWidget(player_choice,alignment=Qt.AlignHCenter)
        vertical_layout.addWidget(game_result,alignment=Qt.AlignHCenter)
        vertical_layout.addLayout(self.horizontal_layout)

        
    def initUI_horizontal_layout(self,horizontal_layout:QHBoxLayout):
        self.start_button = QPushButton("Play again")
        self.quit_button = QPushButton("Exit")

        self.start_button.setFixedSize(200,60)
        self.start_button.clicked.connect(self.play_again)

        self.quit_button.setFixedSize(200,60)
        self.quit_button.clicked.connect(self.main_window.close_window)

        horizontal_layout.addWidget(self.start_button)
        horizontal_layout.addWidget(self.quit_button)

    def play_again(self):
        
        self.main_window.switch_to_page_2()

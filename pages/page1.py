import re

from PyQt5.QtWidgets import QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QPixmap

from widgets.custom_dialog import CustomDialog

class Page1(QWidget):
    def __init__(self,main_window):
        super().__init__()
        self.main_window = main_window


        self.name_is_filled = False

        horizontal_layout = QHBoxLayout()
        vertical_layout = QVBoxLayout()

        self.initUI_horizontal_layout(horizontal_layout=horizontal_layout)

        self.initUI_vertical_layout(vertical_layout)

        vertical_layout.addLayout(horizontal_layout)
        vertical_layout.addSpacing(20)

        self.title.setObjectName("title")
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

        self.setLayout(vertical_layout)

    def initUI_horizontal_layout(self,horizontal_layout:QHBoxLayout)->None:
        self.start_button = QPushButton("Start the game")
        self.quit_button = QPushButton("Exit")

        self.start_button.setFixedSize(200,60)
        self.start_button.clicked.connect(self.start_game)

        self.quit_button.setFixedSize(200,60)
        self.quit_button.clicked.connect(self.main_window.close_window)

        horizontal_layout.addWidget(self.start_button)
        horizontal_layout.addWidget(self.quit_button)

    def initUI_vertical_layout(self,vertical_layout:QVBoxLayout)->None:
        self.title = QLabel("Rock paper scissors")
        self.picture = QLabel()
        self.picture.setPixmap(QPixmap("rock_paper_scissors/assets/cat.jpg"))
        self.picture.setScaledContents(True)
        self.submit_button = QPushButton("Submit your name")
        
        self.current_player_name = QLabel("Current player is:")
        self.name_box = QLineEdit()

        self.name_box.setFixedSize(QSize(300,60))
        self.name_box.setPlaceholderText("Input your name here")

        self.submit_button.clicked.connect(self.submit_name)
        self.submit_button.setFixedSize(QSize(260,60))

        vertical_layout.addWidget(self.title,alignment=Qt.AlignHCenter)
        vertical_layout.addWidget(self.picture,alignment=Qt.AlignHCenter)
        vertical_layout.addSpacing(45)
        vertical_layout.addWidget(self.name_box,alignment=Qt.AlignHCenter)
        vertical_layout.addWidget(self.submit_button,alignment=Qt.AlignHCenter)
        vertical_layout.addWidget(self.current_player_name,alignment=Qt.AlignHCenter)
    

    def submit_name(self):
        self.player_name = self.name_box.text()
        if not self.player_name:
            pass
        elif self.validate_name(self.player_name):
            self.main_window.player.name = self.player_name
            self.current_player_name.setText(f"Current player is: {self.main_window.player.name}")
            self.name_is_filled = True
            # print(f"{self.main_window.player_name}")

    def validate_name(self,player_name:str)->bool:
        if re.fullmatch(r".{,5}",player_name):
            self.error_dialog("Name's too short\nProvide a name 6-12 symbols long")
            return False
        if re.fullmatch(r".{13,}",player_name):
            self.error_dialog("Name's too long\nProvide a name 6-12 symbols long")
            return False
        if not re.search(r"\d",player_name):
            self.error_dialog("Provide a name containing at least one digit")
            return False
        if not re.search(r"[a-z]",player_name):
            self.error_dialog("Provide a name containing at least one lowercase letter")
            return False
        if not re.search(r"[A-Z]",player_name):
            self.error_dialog("Provide a name containing at least one upppercase letter")
            return False
        if re.fullmatch(r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,12}",player_name):
            return True
        else:
            self.error_dialog("Generic error")
            return False

    def start_game(self):
        if self.name_filled_check():
            self.main_window.switch_to_page_2()
            # print(self.main_window.player_name)
        else:
            self.error_dialog("Please enter a correct name!")

    def name_filled_check(self):
        if self.name_is_filled:
            return True
        else:
            return False

    def error_dialog(self,message:str)->None:
        dlg = CustomDialog(message=message)
        dlg.exec_()
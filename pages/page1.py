import re

from PyQt5.QtWidgets import QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QPixmap

from widgets.custom_dialog import CustomDialog

class Page1(QWidget):
    def __init__(self,switch_to_page_2,close_window):
        super().__init__()

        page_1_horizontal_layout = QHBoxLayout()
        page_1_main_layout = QVBoxLayout()

        self.initUI_page_1_horizontal_layout(page_1_horizontal_layout,switch_to_page_2,close_window)

        self.initUI_page_1_vertical_layout(page_1_main_layout)

        page_1_main_layout.addLayout(page_1_horizontal_layout)
        page_1_main_layout.addSpacing(20)

        self.page_1_title.setObjectName("page_1_title")
        self.setStyleSheet("""
                                QWidget{
                                font-size: 25px;
                                font-family: Garamond;
                                            }
                                QLabel#page_1_title{
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

        self.setLayout(page_1_main_layout)

    def initUI_page_1_horizontal_layout(self,page_1_horizontal_layout:QHBoxLayout,switch_to_page_2,close_window)->None:
        self.page_1_start_button = QPushButton("Start the game")
        self.page_1_quit_button = QPushButton("Exit")

        self.page_1_start_button.setFixedSize(200,60)
        self.page_1_start_button.clicked.connect(switch_to_page_2)

        self.page_1_quit_button.setFixedSize(200,60)
        self.page_1_quit_button.clicked.connect(close_window)

        page_1_horizontal_layout.addWidget(self.page_1_start_button)
        page_1_horizontal_layout.addWidget(self.page_1_quit_button)

    def initUI_page_1_vertical_layout(self,page_1_main_layout:QVBoxLayout)->None:
        self.page_1_title = QLabel("Rock paper scissors")
        self.page_1_picture = QLabel()
        self.page_1_picture.setPixmap(QPixmap("assets/cat.jpg"))
        self.page_1_picture.setScaledContents(True)
        self.page_1_submit_button = QPushButton("Submit your name")
        
        self.page_1_current_player_name = QLabel("Current player is:")
        self.page_1_name_box = QLineEdit()

        self.page_1_name_box.setFixedSize(QSize(300,60))
        self.page_1_name_box.setPlaceholderText("Input your name here")

        self.page_1_submit_button.clicked.connect(self.submit_name)
        self.page_1_submit_button.setFixedSize(QSize(260,60))

        page_1_main_layout.addWidget(self.page_1_title,alignment=Qt.AlignHCenter)
        page_1_main_layout.addWidget(self.page_1_picture,alignment=Qt.AlignHCenter)
        page_1_main_layout.addSpacing(45)
        page_1_main_layout.addWidget(self.page_1_name_box,alignment=Qt.AlignHCenter)
        page_1_main_layout.addWidget(self.page_1_submit_button,alignment=Qt.AlignHCenter)
        page_1_main_layout.addWidget(self.page_1_current_player_name,alignment=Qt.AlignHCenter)
    

    def submit_name(self):
        self.player_name = self.page_1_name_box.text()
        if not self.player_name:
            pass
        elif self.validate_name(self.player_name):
            self.page_1_current_player_name.setText(f"Current player is: {self.player_name}")

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

    def error_dialog(self,message:str)->None:
        dlg = CustomDialog(message=message)
        dlg.exec_()
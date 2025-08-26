import re

from PyQt5.QtWidgets import (
    QPushButton,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QLabel,
)
from PyQt5.QtCore import Qt, QSize

from widgets.custom_dialog import CustomDialog
from utility.service import resource_path


class Page1(QWidget):
    def __init__(self, main_window):
        super().__init__()
        # main_window is created to use it's methods
        self.main_window = main_window

        self.name_is_filled = False

        # creating and initializing layouts
        horizontal_layout = QHBoxLayout()
        vertical_layout = QVBoxLayout()

        self.initUI_horizontal_layout(horizontal_layout=horizontal_layout)
        self.initUI_vertical_layout(vertical_layout)

        vertical_layout.addLayout(horizontal_layout)
        vertical_layout.addSpacing(20)

        self.title.setObjectName("title")
        self.setStyleSheet(
            """
                                QWidget{
                                color: #e6b47b;
                                font-size: 17px;
                                font-family: Press Start 2P;

                                            }
                                QLabel#title{
                                font-size: 28px;
                                
                                            }
                                QLineEdit{
                                padding: 15px;
                                color: #546345;
                                font-size: 15px;
                                border-radius: 15px;
                                            }
                                QPushButton{
                                background-color: #893f36;
                                border-radius: 15px;
                                            }
                                QPushButton:hover{
                                font-size: 18px;
                                background-color: #d0928a;
                                border-radius: 15px;
                                            }
                                                """
        )

        self.setLayout(vertical_layout)

    def initUI_horizontal_layout(self, horizontal_layout: QHBoxLayout) -> None:
        self.start_button = QPushButton("Start the game")
        self.quit_button = QPushButton("Exit")

        self.start_button.setFixedSize(300, 80)
        self.start_button.clicked.connect(self.start_game)

        self.quit_button.setFixedSize(300, 80)
        self.quit_button.clicked.connect(self.main_window.close)

        horizontal_layout.addWidget(self.start_button)
        horizontal_layout.addWidget(self.quit_button)

    def initUI_vertical_layout(self, vertical_layout: QVBoxLayout) -> None:
        self.title = QLabel("Rock paper scissors")

        self.picture = QLabel()
        pic = resource_path("assets/picture_1.jpg")
        pic = pic.replace("\\", "/")
        self.picture.setStyleSheet(
            f"""
            color: grey;
            border-image: url({pic});
            border-radius: 35px;
            """
        )
        self.picture.setFixedSize(QSize(350, 350))

        self.submit_button = QPushButton("Submit your name")
        self.submit_button.clicked.connect(self.submit_name)
        self.submit_button.setFixedSize(QSize(350, 80))

        self.current_player_name = QLabel("Current player is:")

        self.name_box = QLineEdit()
        self.name_box.setFixedSize(QSize(350, 80))
        self.name_box.setPlaceholderText("Input your name here")

        vertical_layout.setSpacing(25)
        vertical_layout.addSpacing(15)
        vertical_layout.addWidget(self.title, alignment=Qt.AlignHCenter)
        vertical_layout.addWidget(self.picture, alignment=Qt.AlignHCenter)
        vertical_layout.addWidget(self.current_player_name, alignment=Qt.AlignHCenter)
        vertical_layout.addWidget(self.name_box, alignment=Qt.AlignHCenter)
        vertical_layout.addWidget(self.submit_button, alignment=Qt.AlignHCenter)

    def submit_name(self) -> None:
        """
        get's the name from the lineedit widget, validates it\n
        updates it's value in player class object and sets it's value in the label\n
        sets name_is_filled True to allow proceeding to the next page
        """
        self.player_name = self.name_box.text()
        if not self.player_name:
            pass
        elif self.validate_name(self.player_name):
            self.main_window.player.name = self.player_name
            self.current_player_name.setText(
                f"Current player is: {self.main_window.player.name}"
            )
            self.name_is_filled = True

    def validate_name(self, player_name: str) -> bool:
        if re.fullmatch(r".{,2}", player_name):
            CustomDialog.error_dialog(
                "Name's too short\nProvide a name 3-12 symbols long"
            )
            return False
        if re.fullmatch(r".{13,}", player_name):
            CustomDialog.error_dialog(
                "Name's too long\nProvide a name 6-12 symbols long"
            )
            return False
        if re.search(r"\d", player_name):
            CustomDialog.error_dialog("Name can't contain digits")
            return False
        if re.search(r" ", player_name):
            CustomDialog.error_dialog("Name can't have whitespace in it")
            return False
        if not re.search(r"[a-z]", player_name):
            CustomDialog.error_dialog(
                "Provide a name containing at least one lowercase letter"
            )
            return False
        if not re.search(r"[A-Z]", player_name):
            CustomDialog.error_dialog(
                "Provide a name containing at least one upppercase letter"
            )
            return False
        if re.fullmatch(r"(?=.*[a-z])(?=.*[A-Z])[a-zA-Z_]{3,12}", player_name):
            return True
        else:
            CustomDialog.error_dialog("Generic error")
            return False

    def start_game(self):
        if self.name_filled_check():
            self.main_window.switch_to_page_2()
        else:
            CustomDialog.error_dialog("Please enter a correct name!")

    def name_filled_check(self):
        if self.name_is_filled:
            return True
        else:
            return False

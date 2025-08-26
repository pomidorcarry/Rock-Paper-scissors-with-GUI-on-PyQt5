from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QFontDatabase
from utility.service import resource_path


class CustomDialog(QDialog):
    def __init__(self, message):
        super().__init__()
        self.setMinimumSize(200, 110)
        custom_font = resource_path("assets/PressStart2P-Regular.ttf")
        custom_font = custom_font.replace("\\", "/")
        id = QFontDatabase.addApplicationFont(custom_font)

        famlies = QFontDatabase.applicationFontFamilies(id)
        # print(famlies[0])
        self.setWindowTitle("Error")
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        button_box.accepted.connect(self.accept)
        message_label = QLabel(f"{message}")
        v_layout = QVBoxLayout()
        v_layout.addWidget(message_label)
        v_layout.addWidget(button_box, alignment=Qt.AlignHCenter)

        self.setLayout(v_layout)
        self.setStyleSheet(
            """
                        QWidget{
                        font-size: 10px;
                        font-family: Press Start 2P;
                                    }
                        QPushButton{
                        font-size: 10px;
                        padding: 10px;
                        background-color: #893f36;
                        border-radius: 10px;
                                    }
                        QPushButton:hover{
                        font-size: 10px;
                        padding: 10px;
                        background-color: #d0928a;
                        border-radius: 10px;
                                    }
                                        """
        )
        self.show()

    @classmethod
    def error_dialog(cls, message: str) -> None:
        dlg = CustomDialog(message=message)
        dlg.exec_()

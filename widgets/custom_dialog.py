from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QLabel,QVBoxLayout
from PyQt5.QtCore import Qt

class CustomDialog(QDialog):
    def __init__(self, message):
        super().__init__()
        self.setWindowTitle("Error")
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        button_box.setMaximumSize(200,200)
        button_box.accepted.connect(self.accept)
        message_label =QLabel(f"{message}")
        v_layout = QVBoxLayout()
        v_layout.addWidget(message_label)
        v_layout.addWidget(button_box,alignment=Qt.AlignHCenter)

        self.setLayout(v_layout)
        self.setStyleSheet("""
                        QWidget{
                        font-size: 25px;
                        font-family: Garamond;
                                    }
                        QPushButton{
                        font-size: 20px;
                        padding: 15px 15px;
                        background-color: #f0a860;
                        border-radius: 10px;
                                    }
                        QPushButton:hover{
                        font-size: 20px;
                        padding: 15px 15px;
                        background-color: #faddc0;
                        border-radius: 10px;
                                    }
                                        """)
        self.show()
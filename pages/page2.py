from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMainWindow, QPushButton,  QDesktopWidget, QButtonGroup, QWidget, QVBoxLayout, QHBoxLayout, QStackedLayout, QLineEdit, QLabel, QApplication, QMessageBox, QDialog, QDialogButtonBox

from PyQt5.QtCore import Qt, QSize



class Page2(QWidget):
    def __init__(self,switch_to_page_1):
        super().__init__()
        page_2_layout = QVBoxLayout()
        page_2_button = QPushButton("Go to page 1")
        page_2_title = QLabel("This is page 2")
        page_2_button.clicked.connect(switch_to_page_1)
        page_2_layout.addWidget(page_2_title,alignment=Qt.AlignHCenter)
        page_2_layout.addWidget(page_2_button,alignment=Qt.AlignHCenter)
        self.setLayout(page_2_layout)
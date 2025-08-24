
from PyQt5.QtWidgets import QMainWindow, QPushButton,  QDesktopWidget, QButtonGroup, QWidget, QVBoxLayout, QHBoxLayout, QStackedLayout, QLineEdit, QLabel, QApplication, QMessageBox, QDialog, QDialogButtonBox
from PyQt5.QtGui import QIcon, QFont, QPixmap, QGuiApplication
from PyQt5.QtCore import Qt, QSize

from pages.page1 import Page1 
from pages.page2 import Page2
from pages.page3 import Page3
from utility.player import Player

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        #shared data
        self.player = Player()
        self.cpu = Player()
        self.game_result = None


        self.setWindowTitle("Rock Paper Scissors")
        self.setWindowIcon(QIcon("rock_paper_scissors/assets/test.jpg"))

        self.page_1_size = QSize(750,750)
        self.page_2_size = QSize(750,750)
        self.setFixedSize(self.page_1_size)
        self.page_1_widget = Page1(self)
        self.page_2_widget = Page2(self)
        self.page_3_widget = Page3(self)

        self.stacked_layout = QStackedLayout()

        self.stacked_layout.addWidget(self.page_1_widget)
        self.stacked_layout.addWidget(self.page_2_widget)
        self.stacked_layout.addWidget(self.page_3_widget)


        #set the initial page
        self.stacked_layout.setCurrentIndex(0)

        self.setStyleSheet("""
                        QMainWindow{
                        background-color: #7591d2;
                           }
                        """)

        #set the central widget
        central_widget = QWidget()
        central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(central_widget)

    def center_window(self)->None:
        window_resolution_rectangle = self.frameGeometry()
        screen_resolution_rectangle = self.screen().availableGeometry()
        center_point = screen_resolution_rectangle.center()
        window_resolution_rectangle.moveCenter(center_point)
        self.move(window_resolution_rectangle.topLeft())

   
    def closeEvent(self,event):
        reply = QMessageBox.question(self,"Message","Are you sure you wanna quit?",QMessageBox.Yes| QMessageBox.No,QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def close_window(self):
        self.close()

    def switch_to_page_2(self)->None:
        # self.page_2_widget = Page2(self)
        # self.stacked_layout.addWidget(self.page_2_widget)
        self.page_2_widget.update_values()
        self.setFixedSize(self.page_2_size)
        self.center_window()
        self.stacked_layout.setCurrentIndex(1)

    def switch_to_page_3(self)->None:
        # self.page_3_widget = Page3(self)
        # self.stacked_layout.addWidget(self.page_3_widget)
        self.page_3_widget.update_values()
        self.setFixedSize(self.page_2_size)
        self.center_window()
        self.stacked_layout.setCurrentIndex(2)
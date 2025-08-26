from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QStackedLayout,
    QMessageBox,
)
from PyQt5.QtGui import QIcon, QFontDatabase
from PyQt5.QtCore import QSize

from pages.page1 import Page1
from pages.page2 import Page2
from pages.page3 import Page3
from pages.page4 import Page4
from utility.player import Player

from widgets.custom_dialog import CustomDialog
from utility.service import resource_path


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # shared data
        self.player = Player()
        self.cpu = Player()
        self.game_result = None

        custom_font = resource_path("assets/PressStart2P-Regular.ttf")
        custom_font = custom_font.replace("\\", "/")
        id = QFontDatabase.addApplicationFont(custom_font)

        famlies = QFontDatabase.applicationFontFamilies(id)
        # print(famlies[0])

        self.setWindowTitle("Rock Paper Scissors")
        self.setWindowIcon(QIcon(resource_path("assets/icon.jpg")))
        self.setFixedSize(QSize(850, 850))

        # creating pages for stacked widget
        self.page_1_widget = Page1(self)
        self.page_2_widget = Page2(self)
        self.page_3_widget = Page3(self)
        self.page_4_widget = Page4(self)

        self.stacked_layout = QStackedLayout()

        # adding widgets to the stacked layout
        self.stacked_layout.addWidget(self.page_1_widget)
        self.stacked_layout.addWidget(self.page_2_widget)
        self.stacked_layout.addWidget(self.page_3_widget)
        self.stacked_layout.addWidget(self.page_4_widget)

        # set the initial page
        self.stacked_layout.setCurrentIndex(0)

        self.setStyleSheet(
            """
                        QMainWindow{
                        background-color: #1f1514;
                           }
                        """
        )

        # set the central widget
        central_widget = QWidget()
        central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(central_widget)

    def center_window(self) -> None:
        """
        Centers the window on the screen using abstract Qt rectangle object and dragging actual window by top left corner
        """
        window_resolution_rectangle = self.frameGeometry()
        screen_resolution_rectangle = self.screen().availableGeometry()
        center_point = screen_resolution_rectangle.center()
        window_resolution_rectangle.moveCenter(center_point)
        self.move(window_resolution_rectangle.topLeft())

    def closeEvent(self, event):
        """
        customizes the reaction of the window on the event of closing the window\n
        confirming that the user indeed wanted to close it
        """
        reply = QMessageBox.question(
            self,
            "Message",
            "Are you sure you wanna quit?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def switch_to_page_2(self) -> None:
        """
        switches widget to the second page widget in the stacked main window layout\n
        while at the same time updating specified values in some labels
        """
        self.page_2_widget.update_values()
        self.center_window()
        self.stacked_layout.setCurrentIndex(1)

    def switch_to_page_3(self) -> None:
        """
        switches widget to the third page widget in the stacked main window layout\n
        while at the same time updating specified values in some labels
        """
        self.setFixedSize(QSize(400, 300))
        self.page_3_widget.open_page()
        self.center_window()
        self.stacked_layout.setCurrentIndex(2)

    def switch_to_page_4(self) -> None:
        """
        switches widget to the third page widget in the stacked main window layout\n
        while at the same time updating specified values in some labels
        """
        self.setFixedSize(QSize(750, 750))
        self.page_4_widget.update_values()
        self.center_window()
        self.stacked_layout.setCurrentIndex(3)

    def error_dialog(self, message: str) -> None:
        """
        creates the error dialog window with the message passed to it
        """
        dlg = CustomDialog(message=message)
        dlg.exec_()

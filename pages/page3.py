from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
)

from PyQt5.QtCore import Qt, QSize, QTimer
from PyQt5.QtGui import QMovie
from utility.service import resource_path


class Page3(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.v_layout = QVBoxLayout()

        self.label_animation = QLabel()
        self.gif = QMovie(resource_path("assets/loading.gif"))
        self.gif.setScaledSize(QSize(400, 300))
        self.label_animation.setMovie(self.gif)

        self.v_layout.addWidget(self.label_animation)
        self.setLayout(self.v_layout)

    def open_page(self):
        timer = QTimer(self)
        self.start_animation()
        timer.singleShot(2000, self.stop_animation)

    def start_animation(self):
        self.gif.start()

    def stop_animation(self):
        self.gif.stop()
        self.main_window.switch_to_page_4()

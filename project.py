import sys
import os

from main_window import MainWindow
from PyQt5.QtWidgets import QApplication


def main():
    create_window()


def create_window():
    app = QApplication(sys.argv)
    window = MainWindow(resource_path=resource_path)
    window.show()
    sys.exit(app.exec_())


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


if __name__ == "__main__":
    main()

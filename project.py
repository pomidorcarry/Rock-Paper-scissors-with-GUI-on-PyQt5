import sys

from main_window import MainWindow
from PyQt5.QtWidgets import QApplication

from utility.service import resource_path


def main():
    create_window()


def create_window():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

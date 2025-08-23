import sys

from main_window import MainWindow
from PyQt5.QtWidgets import QApplication


def main():
    ...
    function_1_create_window()


def function_1_create_window():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


def function_2(): ...
def function_n(): ...


if __name__ == "__main__":
    main()

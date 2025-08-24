import sys
import os
import sys


from main_window import MainWindow
from PyQt5.QtWidgets import QApplication


def main():
    ...
    function_1_create_window()


def function_1_create_window():
    app = QApplication(sys.argv)
    window = MainWindow(rpath=resource_path)
    window.show()
    sys.exit(app.exec_())


def function_2(): ...
def function_n(): ...

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    main()

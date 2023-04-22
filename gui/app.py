import sys

from PySide6.QtWidgets import QApplication
from qt_material import apply_stylesheet

from ui import MainWidget


class App(MainWidget):
    def __init__(self) -> None:
        super().__init__()


if __name__ == '__main__':
    q_app = QApplication()
    apply_stylesheet(q_app, 'light_purple.xml')

    app = App()
    app.show()
    sys.exit(q_app.exec())
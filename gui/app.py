import sys

from PySide6.QtWidgets import QApplication, QFileDialog
from qt_material import apply_stylesheet

from ui import MainWidget


class App(MainWidget):
    def __init__(self) -> None:
        super().__init__()
        self._src_dir = None
        self._dest_dir = None

    def on_compress_btn_click(self):
        pass

    def on_src_btn_click(self):
        if (path := QFileDialog.getExistingDirectory()) is not None:
            self._src_dir = path
            self._te_source_dir.setText(path)

    def on_dest_btn_click(self):
        if (path := QFileDialog.getExistingDirectory()) is not None:
            self._dest_dir = path
            self._te_dest_dir.setText(path)


if __name__ == '__main__':
    q_app = QApplication()
    apply_stylesheet(q_app, 'light_purple.xml')

    app = App()
    app.show()
    sys.exit(q_app.exec())

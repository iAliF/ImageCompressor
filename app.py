import sys

from PySide6.QtWidgets import QApplication, QFileDialog, QMessageBox
from qt_material import apply_stylesheet

from lib import ImageCompressor, CompressionResult
from ui import MainWidget


class App(MainWidget):
    def __init__(self) -> None:
        super().__init__()
        self._src_dir = None
        self._dest_dir = None

    def on_compress_btn_click(self) -> None:
        obj = ImageCompressor(
            self._src_dir, self._dest_dir,
            self._check_optimize.isChecked(),
            self._slider_quality.value()
        )
        result = obj.compress_images()
        self.show_message(result)

    def on_src_btn_click(self) -> None:
        if (path := QFileDialog.getExistingDirectory()) is not None:
            self._src_dir = path
            self._te_source_dir.setText(path)

    def on_dest_btn_click(self) -> None:
        if (path := QFileDialog.getExistingDirectory()) is not None:
            self._dest_dir = path
            self._te_dest_dir.setText(path)

    def show_message(self, result: CompressionResult) -> None:
        QMessageBox(
            QMessageBox.Icon.Information,
            "Done",
            f"{result.count} Image{'s' if result.count > 1 else ''} were compressed in {round(result.time, 2)}"
            f" second{'s' if result.time > 1 else ''}",
            parent=self
        ).exec()


if __name__ == '__main__':
    q_app = QApplication()
    apply_stylesheet(q_app, 'light_purple.xml')

    app = App()
    app.show()
    sys.exit(q_app.exec())

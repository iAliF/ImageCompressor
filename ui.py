from typing import Optional

from PySide6.QtCore import Qt, QRect
from PySide6.QtWidgets import QWidget, QLabel, QTextEdit, QPushButton, QCheckBox, QSlider


class MainWidget(QWidget):
    WIDTH = 600
    HEIGHT = 480
    LEFT_MARGIN = 20

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

        self.setFixedSize(self.WIDTH, self.HEIGHT)

        self._te_source_dir = QTextEdit(self)
        self._btn_source_select = QPushButton("Select", self)

        self._te_dest_dir = QTextEdit(self)
        self._btn_dest_select = QPushButton("Select", self)

        self._check_optimize = QCheckBox("Optimize", self)
        self._slider_quality = QSlider(Qt.Orientation.Horizontal, self)
        self._text_quality = QLabel("100%", self)

        self.btn_compress = QPushButton("Compress Images", self)

        self._setup_ui()

    def _setup_ui(self):
        self._setup_labels()
        self._setup_checkbox()
        self._setup_slider()
        self._setup_compress_button()

        self.setWindowTitle("Image Compressor")

    def _setup_labels(self):
        v_space = 30  # Space between label & text edit
        h_space = 20  # Space between text edit & button
        te_width = 400
        btn_width = 140
        height = 40

        views = (
            (
                "Image Compressor",  # Text
                (0, 0, self.WIDTH, 60),  # Geometry (left, top, width, height)
                26,  # Size
                Qt.AlignCenter
            ),
            (
                # Label
                "Source Directory",
                (self.LEFT_MARGIN, 80, self.WIDTH, height),
                16,
                Qt.AlignLeft,
                # Text Edit & Btn
                self._te_source_dir,
                self._btn_source_select
            ),
            (
                # Label
                "Destination Directory",
                (self.LEFT_MARGIN, 170, self.WIDTH, height),
                16,
                Qt.AlignmentFlag.AlignLeft,
                # Text Edit & Btn
                self._te_dest_dir,
                self._btn_dest_select
            ),
            (
                "Quality",
                (self.LEFT_MARGIN, 260, self.WIDTH, 40),
                16,
                Qt.AlignmentFlag.AlignLeft,
            )
        )
        for (text, geo, size, alignment, *extra) in views:
            lbl = QLabel(text, self)
            lbl.setGeometry(QRect(*geo))
            lbl.setAlignment(alignment)
            lbl.setStyleSheet(f'font-size: {size}px; font-weight: bold')

            if len(extra):
                te, btn = extra  # type: QTextEdit, QPushButton
                top = geo[1] + v_space
                te.setGeometry(QRect(self.LEFT_MARGIN, top, te_width, height))
                te.setReadOnly(True)
                btn.setGeometry(
                    te_width + self.LEFT_MARGIN + h_space,
                    top, btn_width, height
                )

    def _setup_checkbox(self):
        self._check_optimize.setGeometry(self.LEFT_MARGIN, 320, 100, 40)

    def _setup_slider(self):
        self._slider_quality.setGeometry(self.LEFT_MARGIN, 290, 400, 40)
        self._slider_quality.setMinimum(1)
        self._slider_quality.setMaximum(100)

        self._text_quality.setGeometry(self.WIDTH - self.LEFT_MARGIN - 40, 280, 30, 40)
        self._text_quality.setStyleSheet(f'font-size: 18px; font-weight: bold')
        self._text_quality.setAlignment(Qt.AlignmentFlag.AlignVCenter)

    def _setup_compress_button(self):
        self.btn_compress.setGeometry(
            self.LEFT_MARGIN,
            self.HEIGHT - self.LEFT_MARGIN - 40,
            self.WIDTH - (2 * self.LEFT_MARGIN),
            40
        )

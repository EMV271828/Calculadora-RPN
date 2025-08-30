from PySide6.QtCore import QSize
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit


class VisorStack(QWidget):
    def __init__(self, valor_inicial):
        super().__init__()

        layout = QVBoxLayout()

        self.screen = QLineEdit()

        font_size = self.screen.font()

        font_size.setPointSize(15)

        self.screen.setFont(font_size)

        self.screen.setText(valor_inicial)

        self.screen.setReadOnly(True)

        self.screen.setFixedSize(QSize(500, 40))

        layout.addWidget(self.screen)

        self.setLayout(layout)

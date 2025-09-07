from PySide6.QtCore import QSize
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit


class Visor(QWidget):
    def __init__(self, valor_inicial, fonte_tamanho, tela_tamanho):
        super().__init__()

        layout = QVBoxLayout()

        self.screen = QLineEdit()

        font_size = self.screen.font()

        font_size.setPointSize(fonte_tamanho)

        self.screen.setFont(font_size)

        self.screen.setText(valor_inicial)

        self.screen.setReadOnly(True)

        self.screen.setFixedSize(QSize(tela_tamanho[0], tela_tamanho[1]))

        layout.addWidget(self.screen)

        self.setLayout(layout)

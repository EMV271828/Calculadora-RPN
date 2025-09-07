from PySide6.QtCore import QSize
from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QApplication, QLabel, QVBoxLayout, QWidget


class CalculadoraParteGrafica(QMainWindow):
    def __init__(self, visor, visor_stack, painel1, painel2):
        super().__init__()

        self.visor = visor

        self.visor_stack = visor_stack

        self.painel1 = painel1

        self.painel2 = painel2

        self.setWindowTitle('Calculadora RPN')

        self.setFixedSize(QSize(800, 650))

        self.stack_label = QLabel("STACK")

        layout = QVBoxLayout()

        layout_menu = QHBoxLayout()

        layout_visor_stack = QHBoxLayout()

        layout_visor_stack.addWidget(self.stack_label)

        layout_visor_stack.addWidget(self.visor_stack)

        layout_menu.addWidget(self.painel2)

        layout_menu.addWidget(self.painel1)

        layout.addLayout(layout_visor_stack)

        layout.addWidget(self.visor)

        layout.addLayout(layout_menu)

        widget = QWidget()

        widget.setLayout(layout)

        self.setCentralWidget(widget)

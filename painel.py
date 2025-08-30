from PySide6.QtCore import QSize
from PySide6.QtWidgets import QWidget, QButtonGroup, QGridLayout, QPushButton


class Painel(QWidget):
    def __init__(self, valores, calculadora):

        super().__init__()

        self.calculadora = calculadora

        self.valores = valores

        self.botoes = QButtonGroup()

        self.botoes.idClicked.connect(self.button_input)

        layout = QGridLayout()

        self.setFixedSize(QSize(400, 400))

        for i in range(4):
            for j in range(4):
                b = QPushButton(f"{valores[i * 4 + j]}")
                b.setFixedSize(QSize(90, 90))
                if valores[i * 4 + j] == 'Inv':
                    b.setStyleSheet("background-color: red")
                self.botoes.addButton(b, i * 4 + j)
                layout.addWidget(b, i, j)

        self.setLayout(layout)

    def button_input(self, idt):
        self.calculadora.operacao(self.botoes.button(idt).text())

    def inv_function(self, valores):
        for i,j in enumerate(self.botoes.buttons()):
            j.setText(valores[i])

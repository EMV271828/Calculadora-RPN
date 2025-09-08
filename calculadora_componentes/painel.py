from PySide6.QtCore import QSize, QEvent, QTimer
from PySide6.QtWidgets import QWidget, QButtonGroup, QGridLayout, QPushButton


class Painel(QWidget):
    def __init__(self, valores, calculadora):

        super().__init__()

        self.calculadora = calculadora

        self.valores = valores

        self.clique_duplo = False

        self.botoes = QButtonGroup()

        self.botoes.idClicked.connect(self.button_input)

        self.timer = QTimer()

        self.timer.setSingleShot(True)

        self.timer.timeout.connect(self.clique_simples)

        layout = QGridLayout()

        self.setFixedSize(QSize(400, 400))

        for i in range(4):
            for j in range(4):
                b = QPushButton(f"{valores[i * 4 + j]}")
                b.setFixedSize(QSize(90, 90))
                font_size = b.font()
                font_size.setPointSize(18)
                b.setFont(font_size)
                b.installEventFilter(self)

                if valores[i * 4 + j] == 'Inv':
                    b.setStyleSheet("background-color: red")

                if valores[i * 4 + j] == 'Deg':
                    b.setStyleSheet("background-color: yellow")

                self.botoes.addButton(b, i * 4 + j)

                layout.addWidget(b, i, j)

        self.setLayout(layout)

    def clique_simples(self):
        if self.clique_duplo:
            self.clique_duplo = False

    def eventFilter(self, obj, e):
        if isinstance(obj, QPushButton):

            if e.type() == QEvent.MouseButtonPress and obj.text() == 'DEL':
                self.timer.start(100)


            elif e.type() == QEvent.MouseButtonDblClick and obj.text() == 'DEL':
                self.clique_duplo = True
                self.timer.stop()

        return super().eventFilter(obj, e)

    def button_input(self, idt):
        self.calculadora.parte_logica.iniciar_operacao(self.botoes.button(idt).text(), idt)

    def inv_function(self, valores):
        for i, j in enumerate(self.botoes.buttons()):
            j.setText(valores[i])

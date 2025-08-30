import sys
from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QApplication
from visor import *
from visor_stack import *
from painel import *
from stack import *
import variaveis


class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculadora RPN')

        self.setFixedSize(QSize(800, 650))

        self.registrador = '0.0'

        self.over_write = True

        self.inv_button = False

        self.stack = Stack(50)

        self.operators = variaveis.operadores

        self.visor = Visor(str(self.stack.ultimo_elemento()))

        self.visor_stack = VisorStack(self.stack.ultimos_quatro_elementos())

        self.painel1 = Painel(variaveis.botoes1, self)

        self.painel2 = Painel(variaveis.botoes2, self)

        layout = QVBoxLayout()

        layout_menu = QHBoxLayout()

        layout_visores = QVBoxLayout()

        layout_visores.addWidget(self.visor_stack)

        layout_visores.addWidget(self.visor)

        layout_menu.addWidget(self.painel2)

        layout_menu.addWidget(self.painel1)

        layout.addLayout(layout_visores)

        layout.addLayout(layout_menu)

        widget = QWidget()

        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def solver(self, operador, tipo):

        if tipo == 'binary':
            self.stack.push(self.operators[tipo][operador](self.stack.pop(), self.stack.pop()))
        else:
            self.stack.push(self.operators[tipo][operador](self.stack.pop()))

        return str(self.stack.ultimo_elemento())

    def avaliar_registrador(self):
        if self.registrador == 'e':
            return '2.71828182846'

        if self.registrador == 'π':
            return '3.14159265359'

        return self.registrador

    def operacao(self, signal):

        if signal == "ENTER":
            self.over_write = True

            self.stack.push(np.float64(self.avaliar_registrador()))

            self.registrador = str(self.stack.ultimo_elemento())

        elif signal == "Inv":
            if not self.inv_button:
                self.inv_button = True
                self.painel2.inv_function(variaveis.botoes3)
            else:
                self.inv_button = False
                self.painel2.inv_function(variaveis.botoes2)

        elif len(signal.split(" ")) > 1:

            if self.registrador.isdigit():
                self.stack.push(np.float64(self.avaliar_registrador()))

            if signal.split(" ")[1] in self.operators['binary']:
                self.registrador = self.solver(signal.split(" ")[1], 'binary')
            else:
                self.registrador = self.solver(signal.split(" ")[1], 'unary')

            self.over_write = True

        elif signal == "DEL":
            self.registrador = self.registrador[: len(self.registrador) - 1]

        elif signal == "CLR":
            self.stack.clear()

        elif self.over_write:
            self.registrador = signal
            self.over_write = False

        else:
            self.registrador = self.registrador + signal

        self.visor.screen.setText(self.registrador)
        self.visor_stack.screen.setText(self.stack.ultimos_quatro_elementos())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculadora()
    window.show()
    app.exec()

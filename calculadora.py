import sys
import re
from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QApplication

from visor import *
from painel import *
from stack import *
import variaveis
from excecoes_customizadas import *


class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Calculadora RPN')

        self.setFixedSize(QSize(800, 650))

        self.registrador = '0.0'

        self.mensagem_de_erro = False

        self.over_write = True

        self.inv_button = False

        self.stack = Stack(50)

        self.operators = variaveis.operadores

        self.visor = Visor(str(self.stack.ultimo_elemento()), 27, [900, 150])

        self.visor_stack = Visor(self.stack.ultimos_elementos(), 15, [500, 40])

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

    def avaliar_registrador(self):
        if self.registrador == 'e':
            return '2.71828182846'

        if self.registrador == 'π':
            return '3.14159265359'

        return self.registrador

    def solver(self, operador, tipo):

        if tipo == 'binary':
            if self.stack.tamanho < 2:
                raise PrecisaDeDoisOperandos(operador)

            self.stack.push(self.operators[tipo][operador](self.stack.pop(), self.stack.pop()))

        else:
            if self.stack.tamanho < 1:
                raise PrecisaDeUmOperando(operador)

            self.stack.push(self.operators[tipo][operador](self.stack.pop()))

        return str(self.stack.ultimo_elemento())

    def operacao(self, signal, idt):

        if self.mensagem_de_erro and signal != 'DEL':
            self.registrador = "Clique em DEL para retomar operacoes"

        else:
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

            elif signal == "DEL":
                if self.painel1.clique_duplo or len(self.registrador) == 1 or self.mensagem_de_erro:
                    self.mensagem_de_erro = False
                    self.registrador = '0.0'
                    self.over_write = True
                else:
                    self.registrador = self.registrador[: len(self.registrador) - 1]

            elif signal == "CLR":
                self.stack.clear()

            elif signal == "Deg" or signal == "Rad":
                if signal == "Deg":
                    self.painel2.botoes.button(idt).setText("Rad")
                else:
                    self.painel2.botoes.button(idt).setText("Deg")

            elif len(signal.split(" ")) > 1:

                if self.over_write and (signal.split(" ")[1] == '+' or signal.split(" ")[1] == '-'):
                    self.registrador = signal.split(" ")[1]
                    self.over_write = False

                else:

                    if bool(re.match(r"^-?\d+(\.\d+)?$", self.registrador)):
                        self.stack.push(np.float64(self.avaliar_registrador()))

                    if signal.split(" ")[1] in self.operators['binary']:
                        try:
                            self.registrador = self.solver(signal.split(" ")[1], 'binary')
                        except PrecisaDeDoisOperandos as e:
                            self.mensagem_de_erro = True
                            self.stack.pop()
                            self.registrador = str(e)
                    else:
                        try:
                            self.registrador = self.solver(signal.split(" ")[1], 'unary')
                        except PrecisaDeUmOperando as e:
                            self.mensagem_de_erro = True
                            self.stack.pop()
                            self.registrador = str(e)

                    self.over_write = True

            elif self.over_write:
                self.registrador = signal
                self.over_write = False

            else:
                self.registrador = self.registrador + signal

        self.visor.screen.setText(self.registrador)
        self.visor_stack.screen.setText(self.stack.ultimos_elementos())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculadora()
    window.show()
    sys.exit(app.exec())

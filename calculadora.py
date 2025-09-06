import sys
from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QApplication, QLabel

from visor import *
from painel import *
from stack import *
import constantes
import operacoes
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

        self.deg_button = True

        self.stack = Stack(50)

        self.operadores = operacoes.operadores

        self.constantes = constantes

        self.stack_label = QLabel("STACK")

        self.visor = Visor(str(self.stack.ultimo_elemento()), 27, [900, 150])

        self.visor_stack = Visor(self.stack.ultimos_elementos(), 15, [500, 40])

        self.painel1 = Painel(constantes.botoes1, self)

        self.painel2 = Painel(constantes.botoes2, self)

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

    def avaliar_registrador(self):
        if self.registrador == 'e':
            return np.e

        if self.registrador == 'π':
            return np.pi

        return self.registrador

    def solver(self, operador, tipo):

        if tipo == 'binary':
            if self.stack.tamanho < 2:
                raise PrecisaDeDoisOperandos(operador)

            self.stack.push(self.operadores[tipo][operador](self.stack.pop(), self.stack.pop()))

        elif tipo == 'trigonometric':
            if self.stack.tamanho < 1:
                raise PrecisaDeUmOperando(operador)

            self.stack.push(self.operadores[tipo][operador](self.stack.pop(), self.deg_button))
        else:
            if self.stack.tamanho < 1:
                raise PrecisaDeUmOperando(operador)

            self.stack.push(self.operadores[tipo][operador](self.stack.pop()))

        return str(self.stack.ultimo_elemento())

    def operacao(self, signal, idt):

        if self.mensagem_de_erro and signal != 'DEL':
            self.registrador = "Clique em DEL para retomar operacoes"

        else:

            if signal == "ENTER":
                try:
                    self.over_write = True
                    self.stack.push(np.float64(self.avaliar_registrador()))
                    self.registrador = str(self.stack.ultimo_elemento())

                except StackOverflow as e:
                    self.mensagem_de_erro = True
                    self.registrador = str(e)

            elif signal == "Inv":
                if not self.inv_button:
                    self.inv_button = True
                    self.painel2.inv_function(constantes.botoes3)
                else:
                    self.inv_button = False
                    self.painel2.inv_function(constantes.botoes2)

                if not self.deg_button:
                    self.painel2.botoes.button(4).setText("Rad")

            elif signal == "DEL":
                if self.painel1.clique_duplo or len(self.registrador) == 1 or self.mensagem_de_erro:
                    self.mensagem_de_erro = False
                    self.registrador = '0.0'
                    self.over_write = True
                else:
                    self.registrador = self.registrador[: len(self.registrador) - 1]

            elif signal == "CLR":
                self.stack.clear()
                self.registrador = str(self.stack.ultimo_elemento())

            elif signal == "Deg" or signal == "Rad":
                if self.deg_button:
                    self.deg_button = False
                    self.painel2.botoes.button(idt).setText("Rad")
                else:
                    self.deg_button = True
                    self.painel2.botoes.button(idt).setText("Deg")

            elif len(signal.split(" ")) > 1:

                if self.registrador.isdigit() or self.registrador == 'e' or self.registrador == 'π':
                    try:
                        self.stack.push(np.float64(self.avaliar_registrador()))
                    except StackOverflow as e:
                        self.mensagem_de_erro = True
                        self.registrador = str(e)

                if signal.split(" ")[1] in self.operadores['binary']:

                    try:
                        self.registrador = self.solver(signal.split(" ")[1], 'binary')
                    except (PrecisaDeDoisOperandos, DivisaoPorZero) as e:
                        self.mensagem_de_erro = True
                        self.registrador = str(e)

                        if self.stack.idx == 1 and self.stack.stack[self.stack.idx - 1] != 0.0:
                            self.stack.pop()

                elif signal.split(" ")[1] in self.operadores['trigonometric']:
                    try:
                        self.registrador = self.solver(signal.split(" ")[1], 'trigonometric')
                    except (PrecisaDeUmOperando, ForaDoDominio) as e:
                        self.mensagem_de_erro = True
                        self.registrador = str(e)

                else:
                    try:
                        self.registrador = self.solver(signal.split(" ")[1], 'unary')
                    except (PrecisaDeUmOperando, ForaDoDominio) as e:
                        self.mensagem_de_erro = True
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

import re

import numpy as np
from calculadora_pyside_rpn.calculadora_componentes_secundarios import operacoes
from calculadora_pyside_rpn.calculadora_componentes_secundarios import constantes
from calculadora_pyside_rpn.calculadora_componentes_secundarios.excecoes_customizadas import *


class CalculadoraParteLogica:
    def __init__(self, painel1, painel2, visor, visor_stack, stack):

        self.painel1 = painel1

        self.painel2 = painel2

        self.visor = visor

        self.stack = stack

        self.visor_stack = visor_stack

        self.registrador = '0.0'

        self.mensagem_de_erro = False

        self.over_write = True

        self.inv_button = False

        self.deg_button = True

        self.operadores = operacoes.operadores

    def avaliar_registrador(self):
        if self.registrador == 'e':
            return np.e

        if self.registrador == 'π':
            return np.pi

        return self.registrador

    def solver(self, operador, tipo):

        if self.over_write and str(self.stack.ultimo_elemento()) == self.registrador:
            self.stack.pop()

        if tipo == 'binary':

            if operador == '-' and self.stack.tamanho == 1:
                self.stack.push(-1)
                operador = '×'

            if operador != '-' and self.stack.tamanho == 1:
                self.stack.pop()

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

    def iniciar_operacao(self, signal, idt):

        if self.mensagem_de_erro and signal != 'DEL':
            self.registrador = "Clique em DEL para retomar operacoes"

        else:
            match signal:
                case "ENTER":
                    try:
                        self.over_write = True
                        self.stack.push(np.float64(self.avaliar_registrador()))
                        self.registrador = str(self.stack.ultimo_elemento())

                    except StackOverflow as e:
                        self.mensagem_de_erro = True
                        self.registrador = str(e)

                case "Inv":
                    if not self.inv_button:
                        self.inv_button = True
                        self.painel2.inv_function(constantes.botoes3)
                    else:
                        self.inv_button = False
                        self.painel2.inv_function(constantes.botoes2)

                    if not self.deg_button:
                        self.painel2.botoes.button(4).setText("Rad")

                case "DEL":
                    if self.painel1.clique_duplo or len(self.registrador) == 1 or self.mensagem_de_erro:
                        self.mensagem_de_erro = False
                        self.registrador = '0.0'
                        self.over_write = True
                    else:
                        self.registrador = self.registrador[: len(self.registrador) - 1]

                case "CLR":
                    self.stack.clear()
                    self.registrador = str(self.stack.ultimo_elemento())

                case "Deg" | "Rad":
                    if self.deg_button:
                        self.deg_button = False
                        self.painel2.botoes.button(idt).setText("Rad")
                    else:
                        self.deg_button = True
                        self.painel2.botoes.button(idt).setText("Deg")

                case _ if len(signal.split(" ")) > 1:

                    if bool(re.match(r'^[-+]?(?:\d+(?:\.\d*)?|\.\d+)$', self.registrador)
                            or self.registrador in ['e', 'π']):
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

                            if self.stack.idx == 1 and self.stack.stack[self.stack.idx] != 0.0 and self.stack.stack[
                                self.stack.idx - 1] != 0.0:
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

                case _ if self.over_write:
                    self.registrador = signal
                    self.over_write = False

                case _:
                    self.registrador = self.registrador + signal

        self.visor.screen.setText(self.registrador)
        self.visor_stack.screen.setText(self.stack.ultimos_elementos())

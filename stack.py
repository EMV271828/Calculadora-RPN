import numpy as np
from excecoes_customizadas import *


class Stack:
    def __init__(self, n):
        self.n = n
        self.stack = np.zeros(n, np.float64)
        self.idx = 0
        self.tamanho = 0

    def pop(self):

        value = self.stack[self.idx - 1]
        self.stack[self.idx - 1] = 0.0
        self.idx -= 1
        self.tamanho -= 1
        return value

    def push(self, valor):
        if self.tamanho < self.n:
            self.stack[self.idx] = valor
            self.idx += 1
            self.tamanho += 1
        else:
            raise StackOverflow()

    def ultimo_elemento(self):
        return self.stack[self.idx - 1]

    def ultimos_elementos(self):
        if self.idx == 0:
            return ''
        if 0 < self.idx < 10:
            return " ".join("{:.3f}".format(i) for i in self.stack[:self.idx])
        return " ".join("{:.3f}".format(i) for i in self.stack[self.idx - 10:self.idx])

    def clear(self):
        self.idx = 0
        self.tamanho = 0
        self.stack = np.zeros(self.n, np.float64)

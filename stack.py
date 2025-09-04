import numpy as np


class Stack:
    def __init__(self, n):
        self.n = n
        self.stack = np.zeros(n, np.float64)
        self.idx = 0
        self.tamanho = 0

    def pop(self):
        if self.tamanho > 0:
            value = self.stack[self.idx - 1]
            self.stack[self.idx - 1] = 0.0
            self.idx -= 1
            self.tamanho -= 1
            return value
        else:
            return None

    def push(self, valor):
        if self.tamanho < self.n:
            self.stack[self.idx] = valor
            self.idx += 1
            self.tamanho += 1

    def ultimo_elemento(self):
        return self.stack[self.idx - 1]

    def ultimos_elementos(self):
        if self.idx == 0:
            return str(self.stack[0])
        if 1 <= self.idx < 10:
            return " ".join(str(i) for i in self.stack[:self.idx])
        return " ".join(str(i) for i in self.stack[self.idx - 10:self.idx])

    def clear(self):
        self.idx = 0
        self.tamanho = 0
        self.stack = np.zeros(self.n, np.float64)

import numpy as np
from scipy.special import factorial
from excecoes_customizadas import *


def div(x, y):
    if x == 0:
        raise DivisaoPorZero()
    return y / x


def modulo(x, y):
    if x == 0:
        raise DivisaoPorZero()
    return y % x


def fat(op, x):
    if x < 0:
        raise ForaDoDominio(op, 'x >= 0')
    return factorial(x)


def sin(x, grau):
    return np.sin([x])[0] if grau else np.sin([x * np.pi])[0]


def cos(x, grau):
    return np.cos([x])[0] if grau else np.cos([x * np.pi])[0]


def tan(op, x, grau):
    if (x - np.pi / 2) % np.pi == 0:
        raise ForaDoDominio(op, 'x = n*π/2, n = 1,2,...')

    return np.tan([x])[0] if grau else np.cos([x * np.pi])[0]


def arcsin(op, x, grau):
    if x > 1 or x < -1:
        raise ForaDoDominio(op, '-1 < x < 1')

    return np.arcsin([x])[0] if grau else np.arcsin([x * np.pi])[0]


def arccos(op, x, grau):
    if x > 1 or x < -1:
        raise ForaDoDominio(op, '-1 < x < 1')

    return np.arccos([x])[0] if grau else np.arccos([x * np.pi])[0]


def arctan(x, grau):
    return np.arctan([x])[0] if grau else np.arccos([x * np.pi])[0]


def root(op, x):
    if x < 0:
        raise ForaDoDominio(op, 'x >= 0')
    return np.sqrt([x])[0]


def log(op, x):
    if x < 1:
        raise ForaDoDominio(op, 'x > 0')
    return np.log10([x])[0]


def ln(op, x):
    if x < 1:
        raise ForaDoDominio(op, 'x > 0')
    return np.log([x])[0]


operadores = {
    'binary': {'×': lambda x, y: x * y, '-': lambda x, y: y - x, '÷': lambda x, y: div(x, y),
               '+': lambda x, y: x + y, '%': lambda x, y: modulo(x, y), 'xʸ': lambda x, y: y ** x
               },
    'unary': {'10ˣ': lambda x: 10 ** x, 'Abs': lambda x: np.abs(x), 'eˣ': lambda x: np.exp([x])[0],
              '!': lambda x: fat('!', x), 'log': lambda x: log('log', x), '2ˣ': lambda x: np.exp2([x])[0],
              'ln': lambda x: log('ln', x), '√': lambda x: root('√', x),
              },

    'trigonometric': {
        'sin': lambda x, grau: sin(x, grau), 'cos': lambda x, grau: cos(x, grau),
        'tan': lambda x, grau: tan('tan', x, grau), 'sin⁻¹': lambda x, grau: arcsin('sin⁻¹', x, grau),
        'cos⁻¹': lambda x, grau: arccos('cos⁻¹', x, grau), 'tan⁻¹': lambda x, grau: arctan(x, grau)
    }
}

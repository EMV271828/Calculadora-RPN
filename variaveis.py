import numpy as np
from scipy.special import factorial
from excecoes_customizadas import *


def fat(op, x):
    if x < 0:
        raise ForaDoDominio(op, 'x >= 0')
    return factorial(x)


def tan(op, x):
    if x % 90 == 0:
        raise ForaDoDominio(op, 'x')
    return np.tan([x])[0]


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
    'binary': {'×': lambda x, y: x * y, '-': lambda x, y: y - x, '÷': lambda x, y: y / x,
               '+': lambda x, y: x + y, '%': lambda x, y: y % x, 'xʸ': lambda x, y: x ** y
               },
    'unary': {'10ˣ': lambda x: 10 ** x, 'Abs': lambda x: np.abs(x), 'eˣ': lambda x: np.exp([x])[0],
              '!': lambda x: fat('!', x), 'log': lambda x: log('log', x), '2ˣ': lambda x: np.exp2([x])[0],
              'ln': lambda x: log('ln', x), 'sin': lambda x: np.sin([x])[0], 'cos': lambda x: np.cos([x])[0],
              'tan': lambda x: tan('tan', x), '√': lambda x: root('√', x), 'sin⁻¹': lambda x: np.arcsin([x])[0],
              'cos⁻¹': lambda x: np.arccos([x])[0], 'tan⁻¹': lambda x: np.arctan([x])[0]
              }
}

botoes1 = [
    '7', '8', '9', ' ×'
    , '4', '5', '6', ' -'
    , '1', '2', '3', ' +'
    , '0', '.', 'DEL', 'ENTER'
]

botoes2 = [
    'Inv', ' Abs', ' xʸ', ' !'
    , 'Deg', ' log', ' ln', 'e'
    , ' sin', ' cos', ' tan', 'π'
    , 'CLR', ' %', ' ÷', ' √'
]

botoes3 = [
    'Inv', ' Abs', ' xʸ', ' !'
    , 'Deg', ' 10ˣ', ' eˣ', 'e'
    , ' sin⁻¹', ' cos⁻¹', ' tan⁻¹', 'π'
    , 'CLR', ' %', ' ÷', ' 2ˣ'
]

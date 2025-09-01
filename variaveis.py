import numpy as np
from scipy.special import factorial

operadores = {
    'binary': {'×': lambda x, y: x * y, '-': lambda x, y: y - x, '÷': lambda x, y: y / x,
               '+': lambda x, y: x + y, '%': lambda x, y: y % x, '^': lambda x, y: x ** y
               },
    'unary': {'10^(x)': lambda x: 10 ** x, 'Abs': lambda x: x * -1, 'e^x': lambda x: np.exp([x])[0],
              '!': lambda x: factorial(x), 'log': lambda x: np.log10([x])[0], '2^x': lambda x: np.exp2([x])[0],
              'ln': lambda x: np.log([x])[0], 'sin': lambda x: np.sin([x])[0], 'cos': lambda x: np.cos([x])[0],
              'tan': lambda x: np.tan([x])[0], '√': lambda x: np.sqrt([x])[0], 'sin-1': lambda x: np.arcsin([x])[0],
              'cos-1': lambda x: np.arccos([x])[0], 'tan-1': lambda x: np.arctan([x])[0]
              }
}

botoes1 = [
    '7', '8', '9', ' ×'
    , '4', '5', '6', ' -'
    , '1', '2', '3', ' +'
    , '0', '.', 'DEL', 'ENTER'
]

botoes2 = [
    'Inv', ' Abs', ' ^', ' !'
    , ' log', ' ln', ' RAD', 'e'
    , ' sin', ' cos', ' tan', 'π'
    , 'CLR', ' %', ' ÷', ' √'
]

botoes3 = [
    'Inv', ' Abs', ' ^', ' !'
    , ' 10^x', ' e^x', ' RAD', 'e'
    , ' sin-1', ' cos-1', ' tan-1', 'π'
    , 'CLR', ' %', ' ÷', ' 2^x'
]

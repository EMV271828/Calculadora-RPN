import numpy as np
from scipy.special import factorial

operadores = {
    'binary': {'×': lambda x, y: x * y, '-': lambda x, y: y - x, '÷': lambda x, y: y / x,
               '+': lambda x, y: x + y, '%': lambda x, y: y % x, 'xʸ': lambda x, y: x ** y
               },
    'unary': {'10ˣ': lambda x: 10 ** x, 'Abs': lambda x: np.abs(x), 'eˣ': lambda x: np.exp([x])[0],
              '!': lambda x: factorial(x), 'log': lambda x: np.log10([x])[0], '2ˣ': lambda x: np.exp2([x])[0],
              'ln': lambda x: np.log([x])[0], 'sin': lambda x: np.sin([x])[0], 'cos': lambda x: np.cos([x])[0],
              'tan': lambda x: np.tan([x])[0], '√': lambda x: np.sqrt([x])[0], 'sin⁻¹': lambda x: np.arcsin([x])[0],
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
    , ' log', ' ln', ' RAD', 'e'
    , ' sin', ' cos', ' tan', 'π'
    , 'CLR', ' %', ' ÷', ' √'
]

botoes3 = [
    'Inv', ' Abs', ' xʸ', ' !'
    , ' 10ˣ', ' eˣ', ' RAD', 'e'
    , ' sin⁻¹', ' cos⁻¹', ' tan⁻¹', 'π'
    , 'CLR', ' %', ' ÷', ' 2ˣ'
]

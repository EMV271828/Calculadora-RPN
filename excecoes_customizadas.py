class PrecisaDeDoisOperandos(Exception):
    def __init__(self, op):
        super().__init__()
        self.op = op

    def __str__(self):
        return f"'{self.op}' precisa de dois operandos"


class PrecisaDeUmOperando(Exception):
    def __init__(self, op):
        super().__init__()
        self.op = op

    def __str__(self):
        return f"'{self.op}' precisa de um operando"

class ForaDoDominio(Exception):
    def __init__(self, op, dominio):
        super().__init__()
        self.op = op
        self.dominio = dominio

    def __str__(self):
        return f"Use valores {self.dominio} para '{self.op}'"

class DivisaoPorZero(Exception):
    def __str__(self):
        return "Divisão por zero"
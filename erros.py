class PrecisaDeDoisOperandos(Exception):
    def __init__(self, op):
        super().__init__()
        self.op = op

    def __str__(self):
        return f"A operacao {self.op} precisa de dois operandos"

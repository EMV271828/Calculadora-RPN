import sys
from visor import *
from painel import *
from calculadora_parte_logica import *
from calculadora_parte_grafica import *
from stack import *
import constantes


class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()

        self.stack = Stack(50)

        self.visor = Visor(str(self.stack.ultimo_elemento()), 27, [900, 150])

        self.visor_stack = Visor(self.stack.ultimos_elementos(), 15, [500, 40])

        self.painel1 = Painel(constantes.botoes1, self)

        self.painel2 = Painel(constantes.botoes2, self)

        self.parte_logica = CalculadoraParteLogica(self.painel1, self.painel2, self.visor,
                                                               self.visor_stack, self.stack)

        self.parte_grafica = CalculadoraParteGrafica(self.visor, self.visor_stack, self.painel1,
                                                                 self.painel2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculadora()
    window.parte_grafica.show()
    sys.exit(app.exec())

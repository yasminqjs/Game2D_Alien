from desconto import Desconto


class Pedido:
    def __init__(self, desconto: Desconto) -> None:
        self.desconto = desconto

    def total(self, valor: float) -> float:
        return valor - self.desconto.calcular(valor)

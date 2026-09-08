from pedido import Pedido
from cupom import CupomVIP

from desconto import (
    DescontoNormal,
    DescontoVIP,
    DescontoPremium
)

def aplicar_desconto(desconto, valor: float) -> float:
    return desconto.calcular(valor)


def aplicar_cupom(cupom, codigo: str, desconto, valor: float) -> float:
    if cupom.aplicar(codigo):
        return desconto.calcular(valor)

    return 0.0


if __name__ == "__main__":

    valor = 100

    pedido_normal = Pedido(DescontoNormal())
    pedido_vip = Pedido(DescontoVIP())
    pedido_premium = Pedido(DescontoPremium())

    print(f"Valor final Normal: R$ {pedido_normal.total(valor):.2f}")
    print(f"Valor final VIP: R$ {pedido_vip.total(valor):.2f}")
    print(f"Valor final Premium: R$ {pedido_premium.total(valor):.2f}")

    cupom = CupomVIP()

    desconto_cupom = aplicar_cupom(cupom, "DESC10", DescontoVIP(), valor)

    print(f"Desconto com cupom: R$ {desconto_cupom:.2f}")
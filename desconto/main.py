from desconto import (
    Desconto,
    DescontoNormal,
    DescontoVIP,
    DescontoPremium
)

def aplicar_desconto(desconto: Desconto, valor: float) -> float:
    return desconto.calcular(valor)


def aplicar_cupom(desconto: DescontoVIP, codigo: str) -> float:
    if desconto.aplicarCupom(codigo):
        return desconto.calcular(100)
    else:
        return 0.0


if __name__ == "__main__":

    valor = 100

    normal = DescontoNormal()
    vip = DescontoVIP()
    premium = DescontoPremium()

    print(f"Desconto Normal: R$ {aplicar_desconto(normal, valor):.2f}")
    print(f"Desconto VIP: R$ {aplicar_desconto(vip, valor):.2f}")
    print(f"Desconto Premium: R$ {aplicar_desconto(premium, valor):.2f}\n")

    print(f"Cupom VIP: R$ {aplicar_cupom(vip, 'DESC10'):.2f}")
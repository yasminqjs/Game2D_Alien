from .desconto import Desconto, DescontoNormal, DescontoVIP, DescontoPremium
from .pedido import Pedido
from .cupom import Cupom, CupomVIP

IDesconto = Desconto
DescontoVip = DescontoVIP

__all__ = [
    "Desconto",
    "IDesconto",
    "DescontoNormal",
    "DescontoVIP",
    "DescontoVip",
    "DescontoPremium",
    "Pedido",
    "Cupom",
    "CupomVIP",
]


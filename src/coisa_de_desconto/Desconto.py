from desconto.desconto import Desconto, DescontoNormal, DescontoVIP, DescontoPremium
from desconto.pedido import Pedido

IDesconto = Desconto
DescontoVip = DescontoVIP

__all__ = ["Desconto", "IDesconto", "DescontoNormal", "DescontoVIP", "DescontoVip", "DescontoPremium", "Pedido"]

from desconto import DescontoNormal, DescontoVip, DescontoPremium

if __name__ == "__main__":
    desconto_normal = DescontoNormal()
    desconto_vip = DescontoVip()
    desconto_premium = DescontoPremium()

    valor = 100
    print(f"Desconto Normal: R$ {desconto_normal.calcular(valor):.2f}")
    print(f"Desconto VIP: R$ {desconto_vip.calcular(valor):.2f}")
    print(f"Desconto Premium: R$ {desconto_premium.calcular(valor):.2f}")





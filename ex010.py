saldo=float(input("Digite qual é o valor em sua carteira? R$ "))
dolar=float(saldo/5.18)
euro=float(saldo/6.11)
print(f"Seu saldo é {saldo}R$, esse valor na cotação do dolar é:\n {dolar:2.2f}U$ \n {euro:2.2f}€")
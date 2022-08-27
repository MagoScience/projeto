print("Bem-vindo à calculadora de gorjetas!")
conta = float(input("Qual foi o valor total da conta? R$"))
dica = int(input("Quanta gorjeta você gostaria de dar? 10, 12 ou 15?"))
pessoas = int(input("Quantas pessoas dividir a conta?"))

gorjeta_como_percentual = dica / 100
quantia_total_gorjeta = conta * gorjeta_como_percentual
total_conta = conta + quantia_total_gorjeta
conta_por_pessoa = total_conta / pessoas
quantia_final = round(conta_por_pessoa, 2)
print(f"Sua conta deu R${conta} reais, e a gorjeta escolhida foi de {dica} %, divido por {pessoas} pessoa(s) e, cada um irá pagar {quantia_final} reais.")

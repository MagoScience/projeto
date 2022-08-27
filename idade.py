# 🚨 Não altere o código abaixo 👇
idade = input("Qual a sua idade atual?")
# 🚨 Não altere o código acima 👆

# Escreva seu código abaixo desta linha 👇
anos = 90 - int(idade)
meses = round(anos * 12)
semanas = round(anos * 52)
dias = round(anos * 365)

print(f"Você tem {dias} dias, {semanas} semanas e {meses} meses restantes.")

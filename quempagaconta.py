# Método de string dividida
import random

names_string = input("Dê-me os nomes de todos, separados por uma vírgula. ")
nomes = names_string.split(", ")
# 🚨 Não altere o código acima 👆

# Escreva seu código abaixo desta linha 👇
num_itens = len(nomes)
num_escolhido = random.randint(0, num_itens - 1)
escolhido = nomes[num_escolhido]

print(f"{escolhido} vai comprar a refeição hoje!")

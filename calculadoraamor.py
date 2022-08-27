# 🚨 Não altere o código abaixo 👇
print("Bem vindo a Calculadora do Amor!")
nome1 = input("Qual é o seu nome? \n")
nome2 = input("Qual é o nome do par? \n")
# 🚨 Não altere o código acima 👆

# Escreva seu código abaixo desta linha 👇

combinando_nomes = nome1 + nome2
lower_nomes = combinando_nomes.lower()
t = lower_nomes.count("t")
r = lower_nomes.count("r")
u = lower_nomes.count("u")
e = lower_nomes.count("e")


primeira_conta = t + r + u + e

l = lower_nomes.count("l")
o = lower_nomes.count("o")
v = lower_nomes.count("v")
e = lower_nomes.count("e")

segunda_conta = l + o + v + e

ScoreLove = int(str(primeira_conta) + str(segunda_conta))

if (ScoreLove < 10) or (ScoreLove > 90):
    print(f"Sua pontuação é {ScoreLove}, vocês combinam como coca e mentos.")

elif (ScoreLove >= 40) and (ScoreLove <= 50):
    print(f"Sua pontuação é {ScoreLove}, vocês estão bem juntos.")
else:
    print(f"Sua pontuação é {ScoreLove}.")

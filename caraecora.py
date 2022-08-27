import random

escolha = int(
    input("Você escolhe 'Cara' ou 'Coroa'? Sendo 0 para Cara e 1 para Coroa\n"))

if escolha == 0:
    escolha = "Cara"
else:
    escolha = "Coroa"

cara_coroa = random.randint(0, 1)

if cara_coroa == 0:
    cara_coroa = "Cara"

elif cara_coroa == 1:
    cara_coroa = "Coroa"

print(f"Você escolheu {escolha}, e deu {cara_coroa}")

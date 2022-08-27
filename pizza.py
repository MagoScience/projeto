conta = 0

tamanho = input("Qual o tamanho de pizza que você quer? P, M ou G ")
if tamanho == "p":
    conta += 15
elif tamanho == "m":
    conta += 20
else:
    conta += 25

add_pepperoni = input("Você quer calabresa? S ou N ")
if add_pepperoni == "s":
    if tamanho == "p":
        conta += 2
    else:
        conta += 3
extra_queijo = input("Você quer queijo extra? S ou N ")
if extra_queijo == "s":
    conta += 1
print(f"Sua conta final é: ${conta}.")

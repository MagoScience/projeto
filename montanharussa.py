print("Bem vindo a Montanha Russa")
altura = int(input("Qual sua altura em cm? "))

conta = 0

if altura >= 120:
    print("Você pode subir na montanha russa!")
    idade = int(input("Qual sua idade?"))
    if idade < 12:
        conta = 5
        print("ingressos para crianças custam US$ 5.")

    elif idade <= 18:
        conta = 7
        print("ingressos para jovens custam US$ 7.")
    elif idade >= 45 and idade <= 55:
        print("Tudo vai ficar bem, receba um ingresso gratuito de nós")

    else:
        conta = 12
        print("ingressos para adultos custam US$ 12.")

    foto = (input("você quer uma foto tirada? S ou N."))
    if foto == "s":
        conta += 3
    print(f"sua conta final é {conta}.")


else:
    print("Desculpe, Você não tem altura para subir na Montanha Russa!")

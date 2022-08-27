ano = int(input("Qual o ano quer saber se é bissexto?"))


if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print("É um ano bissexto!")
        else:
            print("Não é um ano bissexto")
    else:
        print("É um ano Bissexto")
else:
    print("Não é um ano bissexto!")

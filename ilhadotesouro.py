print("Bem-vindo à Ilha do Tesouro.")
print("Sua missão é encontrar o tesouro.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇

direcao = input(
    'Você\' está em uma encruzilhada. Onde você quer ir? Digite "esquerda" ou "direita".\n').lower()


if direcao == "esquerda":
    acao = input('Você\'veio a um lago. Há uma ilha no meio do lago. Digite "esperar" para esperar por um barco. Digite "nadar" para nadar.\n').lower()
    if acao == "esperar":
        portas = input(
            'Você\'chega ileso à ilha. Há uma casa com 3 portas. Uma "vermelha", uma "amarela" e uma "azul". Qual cor você escolhe?\n').lower()
        if portas == "amarela":
            print("Parabéns você achou o tesouro")
            print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
        elif portas == "vermelha":
            print("É uma sala cheia de fogo. Fim de jogo.")
        elif portas == "azul":
            print("comido por feras. fim de jogo")
        else:
            print("Fim de Jogo!")

    else:
        print("Você é atacado por uma truta furiosa. Fim de jogo.")

else:
    print("caiu em um buraco. fim de jogo")

# 🚨 Não altere o código abaixo 👇
linha1 = ["⬜️", "⬜️", "⬜️"]
linha2 = ["⬜️", "⬜️", "⬜️"]
linha3 = ["⬜️", "⬜️", "⬜️"]
mapa = [linha1, linha2, linha3]
print(f"{linha1}\n{linha2}\n{linha3}")
position = input("Onde você quer colocar o tesouro?")
# 🚨 Não altere o código acima 👆

# Escreva seu código abaixo desta linha 👇

horizontal = int(position[0])
vertical = int(position[1])

linha_selecionada = mapa[vertical - 1]
linha_selecionada[horizontal - 1] = "X"
# Escreva seu código acima desta linha 👆

# 🚨 Não altere o código abaixo 👇

print(f"{linha1}\n{linha2}\n{linha3}")

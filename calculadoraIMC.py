# 🚨 Não altere o código abaixo 👇
altura = float(input("digite sua altura em m: "))
peso = float(input("digite seu peso em kg: "))
# 🚨 Não altere o código acima 👆

# Escreva seu código abaixo desta linha 👇

bmi = round(peso/altura ** 2)
if bmi < 18.5:
    print(f"Seu IMC é {bmi}, você está abaixo do peso.")
elif bmi < 25:
    print(f"Seu IMC é {bmi}, você tem um peso normal.")
elif bmi < 30:
    print(f"Seu IMC é {bmi}, você está um pouco acima do peso.")
elif bmi < 35:
    print(f"Seu IMC é {bmi}, você é obeso.")
else:
    print(f"Seu IMC é {bmi}, você é clinicamente obeso.")

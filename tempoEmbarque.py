from datetime import datetime

# Data final
d2 = datetime.strptime('2017-05-05', '%Y-%m-%d')

# Data inicial
d1 = datetime.strptime('2017-05-01', '%Y-%m-%d')

# Realizamos o calculo da quantidade de dias
quantidade_dias = abs((d2 - d1).days)
print(quantidade_dias)

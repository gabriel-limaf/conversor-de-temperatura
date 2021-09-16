"""
Conversor de temperatura by Gabriel Lima

"""

print("Bem-vindo ao conversor de temperatura em Python! ")
print("Deseja converter uma nova temperatura?")
new_temp = int(input("SIM: Digite 1 \n"
                     "NÃO: Digite 2 \n"))

while new_temp < 1 or new_temp > 2:
    print("Digite um valor válido")
    print("Deseja converter uma nova temperatura?")
    new_temp = int(input("SIM: Digite 1 \n"
                         "NÃO: Digite 2 \n"))

if new_temp == 2:
    exit()

while new_temp == 1:

    esc1 = int(input("Qual escala deseja converter?: \n"
                     "Celsius: Digite 1 \n"
                     "Kelvin: Digite 2 \n"
                     "Fahrenheit: Digite 3 \n"
                     "Encerrar Programa: Digite 4 \n"))

    if esc1 == 4:
        exit()

    while esc1 < 1 or esc1 > 4:
        print("Escolha um valor válido \n")
        esc1 = int(input("Qual escala deseja converter?: \n"
                         "Celsius: Digite 1 \n"
                         "Kelvin: Digite 2 \n"
                         "Fahrenheit: Digite 3 \n"
                         "Para Encerrar Programa: Digite 4 \n"))
        if esc1 == 4:
            exit()

    esc2 = int(input("Para qual escala deseja converter?: \n"
                     "Celsius: Digite 1 \n"
                     "Kelvin: Digite 2 \n"
                     "Fahrenheit: Digite 3 \n"
                     "Para Encerrar Programa: Digite 4 \n"))

    if esc2 == 4:
        exit()

    while esc2 < 1 or esc2 > 4:
        print("Escolha um valor válido \n")
        esc2 = int(input("Para qual escala deseja converter?: \n"
                         "Celsius: Digite 1 \n"
                         "Kelvin: Digite 2 \n"
                         "Fahrenheit: Digite 3 \n"
                         "Encerrar Programa: Digite 4 \n"))

    if esc1 == esc2:
        print('A escala é a mesma, não há conversão')

    # Celsius para Kelvin
    elif esc1 == 1 and esc2 == 2:
        celsius_temp = float(input('Qual a temperatura em grau Celsius?: '))
        kelvin_temp = celsius_temp + 273.15
        print(f'A temperatura de {celsius_temp} grau Celsius é de {kelvin_temp} Kelvin \n')

    # Celsius para Fahrenheit
    elif esc1 == 1 and esc2 == 3:
        celsius_temp = float(input('Qual a temperatura em grau Celsius?: '))
        fah_temp = (celsius_temp * (9 / 5) + 32)
        print(f'A temperatura de {celsius_temp} grau Celsius é de {fah_temp} Grau Fahrenheit \n')

    # Kelvin para Celsius
    elif esc1 == 2 and esc2 == 1:
        kelvin_temp = float(input('Qual a temperatura em Kelvin?: '))
        celsius_temp = kelvin_temp - 273.15
        print(f'A temperatura de {kelvin_temp} grau Kelvin é de {celsius_temp} Grau Celsius \n')

    # Kelvin para Fahrenheit
    elif esc1 == 2 and esc2 == 3:
        kelvin_temp = float(input('Qual a temperatura em Kelvin?: '))
        fah_temp = ((kelvin_temp - 273.15) * 1.8) + 32
        print(f'A temperatura de {kelvin_temp} grau Kelvin é de {fah_temp} Grau Fahrenheit \n')

    # Fahrenheit para Celsius
    elif esc1 == 3 and esc2 == 1:
        fah_temp = float(input('Qual a temperatura em grau Fahrenheit?: '))
        celsius_temp = (5 * (fah_temp - 32) / 9)
        print(f'A temperatura de {fah_temp} grau Fahrenheit é de {celsius_temp} Grau Celsius \n')

    # Fahrenheit para Kelvin
    elif esc1 == 3 and esc2 == 2:
        fah_temp = float(input('Qual a temperatura em grau Fahrenheit?: '))
        kelvin_temp = (fah_temp-32)*5/9+273
        print(f'A temperatura de {fah_temp} grau Fahrenheit é de {kelvin_temp} Kelvin \n')

    print("Deseja converter uma nova temperatura? ")
    new_temp = int(input("SIM: Digite 1 \n"
                         "NÃO: Digite 2 \n"))

    while new_temp < 1 or new_temp > 2:
        print("Digite um valor válido")
        print("Deseja converter uma nova temperatura? ")
        new_temp = int(input("SIM: Digite 1 \n"
                             "NÃO: Digite 2 \n"))

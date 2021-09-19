"""
Conversor de temperatura by Gabriel Lima

"""

print("Bem-vindo ao conversor de temperatura em Python! ")


def inicio():

    print("Deseja converter uma temperatura?")
    new_temp = int(input("SIM: Digite 1 \n"
                         "NÃO: Digite 2 \n"))
    if new_temp < 1 or new_temp > 2:
        print("Escolha um valor válido \n")
        inicio()
    if new_temp == 2:
        exit()
    if new_temp == 1:
        escala_conversao()


def inicio2():

    print("Deseja converter uma nova temperatura?")
    new_temp = int(input("SIM: Digite 1 \n"
                         "NÃO: Digite 2 \n"))
    if new_temp < 1 or new_temp > 2:
        print("Escolha um valor válido \n")
        inicio()
    if new_temp == 2:
        exit()
    if new_temp == 1:
        escala_conversao()


def escala_conversao():

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
        if esc2 == 4:
            exit()

    if esc1 == esc2:
        print('A escala é a mesma, não há conversão')
        inicio()
    if esc1 == 1 and esc2 == 2:
        celsius_kelvin()
    if esc1 == 1 and esc2 == 3:
        celsius_fahrenheit()
    if esc1 == 2 and esc2 == 1:
        kelvin_celsius()
    if esc1 == 2 and esc2 == 3:
        kelvin_fahrenheit()
    if esc1 == 3 and esc2 == 1:
        fahrenheit_celsius()
    if esc1 == 3 and esc2 == 2:
        fahrenheit_kelvin()


# converter celsius para kelvin
def celsius_kelvin():
    celsius_temp = float(input('Qual a temperatura em grau Celsius?: '))
    kelvin_temp = celsius_temp + 273.15
    print(f'A temperatura de {celsius_temp} grau Celsius é de {kelvin_temp} Kelvin \n')
    inicio2()


# converter celsius para fahrenheit
def celsius_fahrenheit():
    celsius_temp = float(input('Qual a temperatura em grau Celsius?: '))
    fah_temp = (celsius_temp * (9 / 5) + 32)
    print(f'A temperatura de {celsius_temp} grau Celsius é de {fah_temp} Grau Fahrenheit \n')
    inicio2()


# converter kelvin para celsius
def kelvin_celsius():
    kelvin_temp = float(input('Qual a temperatura em Kelvin?: '))
    celsius_temp = kelvin_temp - 273.15
    print(f'A temperatura de {kelvin_temp} grau Kelvin é de {celsius_temp} Grau Celsius \n')
    inicio2()


# converter kelvin para fahrenheit
def kelvin_fahrenheit():
    kelvin_temp = float(input('Qual a temperatura em Kelvin?: '))
    fah_temp = ((kelvin_temp - 273.15) * 1.8) + 32
    print(f'A temperatura de {kelvin_temp} grau Kelvin é de {fah_temp} Grau Fahrenheit \n')
    inicio2()


# converter fahrenheit para celsius
def fahrenheit_celsius():
    fah_temp = float(input('Qual a temperatura em grau Fahrenheit?: '))
    celsius_temp = (5 * (fah_temp - 32) / 9)
    print(f'A temperatura de {fah_temp} grau Fahrenheit é de {celsius_temp} Grau Celsius \n')
    inicio2()


# converter fahrenheit para kelvin
def fahrenheit_kelvin():
    fah_temp = float(input('Qual a temperatura em grau Fahrenheit?: '))
    kelvin_temp = (fah_temp - 32) * 5 / 9 + 273
    print(f'A temperatura de {fah_temp} grau Fahrenheit é de {kelvin_temp} Kelvin \n')
    inicio2()


inicio()

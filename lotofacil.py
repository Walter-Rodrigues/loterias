from random import randint
from time import sleep

def lotofacil():
    lista_numeros = list()
    lista_jogos = list()

    print('-='*32)
    print("                     JOGO DA LOTOFÁCIL")
    print('-='*32)

    print('\nObs: uma aposta normal possui 15 números.\n')
    numeros_jogados = int(input("Quantos números deseja jogar? "))
    quantidade_de_jogos = int(input("Quantos jogos deseja fazer? "))
    total = 1

    while total <= quantidade_de_jogos:
        contador = 0

        while True:
            numero = randint(1, 25)

            if numero not in lista_numeros:
                lista_numeros.append(numero)
                contador += 1

            if contador == numeros_jogados:
                break

        lista_numeros.sort()
        lista_jogos.append(lista_numeros[:])
        lista_numeros.clear()
        total += 1

    print('-='*11, f"SORTEANDO {quantidade_de_jogos} JOGOS", '-='*11)

    for i, l in enumerate(lista_jogos):
        print(f"JOGO {i+1}: {l}")
        sleep(1)

    print('-='*13, "BOA SORTE", '-='*13)
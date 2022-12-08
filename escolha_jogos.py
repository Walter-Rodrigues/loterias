from lotofacil import lotofacil
from mega_sena import mega_sena
from quina import quina

print('-='*20, 'BEM VINDO', '-='*20)

loop = False
while loop == False:
    jogo = int(input("\nEm qual jogo deseja apostar? Digite 1- MEGA_SENA 2- LOTOFÁCIL 3- QUINA "))

    if jogo == 1:
        mega_sena()
        loop = True
    elif jogo == 2:
        lotofacil()
        loop = True
    elif jogo == 3:
        quina()
        loop = True
    else:
        print("Digite novamente")
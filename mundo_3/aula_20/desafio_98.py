from time import sleep

"""
Faça um programa que tenha uma função chamada contador(), que recebe três parâmetros:
início, fim e passo
E realize a contagem

Seu programa tem que realizar três contagens através da função criada

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) Uma contagem personalizada

--> print(f"{valor} ", end="")  # Exemplo de print espaçado
"""

def contador():
    # print("Contagem de 1 até 10 de 1 em 1:")
    # for i in range(1, 11, 1):
    #     print(f"{i} ", end="")
    #     sleep(0.3)
    
    # print(" ", end="\n")
    
    # print("Contagem de 10 até 0 de 2 em 2:")
    # for j in range(10, 0, -2):
    #     print(f"{j} ", end="")
    #     sleep(0.2)
    
    print("Agora é a sua vez: \n")
    inicio = int(input("Início: \n"))
    fim = int(input("Fim: \n"))
    passo = int(input("Passo: \n"))

    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    if inicio < fim:
        for k in range(inicio, fim, passo):
            print(f"{k} ", end="")
            sleep(0.1)
    else:
        for k in range(fim, inicio, passo):
            print(f"{k} ", end="")
            sleep(0.1)

contador()
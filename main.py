from time import sleep
from poke import *
from os import system

system('cls')

print("Bem vindo ao mundo de pokemon")
nome = input('Qual o seu nome?: ').title().strip()

print(f"Ah! Como vai \033[1;33m{nome}\033[m" )
sleep(1)
print("Você vai precisar de um pokemon se quiser sobreviver",end='')
for c in range(0,3):
    sleep(0.6)
    print(".",end='')
print("\nAH")
sleep(0.4)
print("JÁ")
sleep(0.3)
print("SEI!!!")
sleep(0.4)
print("Eu 'catei' uns pokemon de um lixão!")

sleep(1)
print("Vai servir")
print("Escolhe um ae:")
iniciais()






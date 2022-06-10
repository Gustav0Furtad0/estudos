'''
   -- EXEC IN TERMINAL --
pip install pyinstaller
pyinstaller --onefile list2.py
'''

import subprocess
subprocess.call('', shell=True)
from sys import stdout
from time import sleep

def addpessoa(nome, idade):
    pessoas.append(list((nome, idade)))

def escreve(texto, time = .08):
    for i in texto:
        systemout(time, i)

def systemout(time, i):
    stdout.write(i)
    stdout.flush()
    sleep(time)

pessoas = list()

addpessoa("Teci", 52)
addpessoa("Laura", 41)
addpessoa("João Pedro", 11)
addpessoa("Sarah", 6)
addpessoa("João, pai dos meus irmãos,", 46)
addpessoa("Tairine", 31)
addpessoa("Duda", 18)
addpessoa("Sávio", 21)
addpessoa("Matheus, meu tio,", 26)
addpessoa("Rita, minha sogra", "?")
addpessoa("Pedro", 18)
addpessoa("Paulo Márcio, pai do pedro,", "?")
addpessoa("Cristina, mãe do pedro,", "?")

text = list()

for pessoa in pessoas:
    sleep(1)
    if pessoa[0].upper() == "TECI":
        text = f"\033[1m\033[34m{pessoa[0]}", f" \033[0mtem {pessoa[1]} anos e é meu melhor amigo e pai.\n"
        for i in text:
            escreve(i)
    elif pessoa[0].upper() == "LAURA":
        text = f"\033[1m\033[35m{pessoa[0]}", f" \033[0mtem {pessoa[1]} anos e é minha melhor amiga e mãe.\n"
        for i in text:
            escreve(i)
    elif pessoa[0].upper() == "DUDA":
        text = f"\033[1m\033[95m{pessoa[0]}", f" \033[0mtem {pessoa[1]} anos e é minha melhor amiga e namorada.", " E é gatinha viu!\n"
        for i in text:
            escreve(i)
    elif pessoa[0].upper() == "JOÃO PEDRO":
        text = f"\033[1m\033[33m{pessoa[0]}", f" \033[0mtem {pessoa[1]} anos e é meu irmão.", " Eu tenho muito orgulho dele!\n"
        for i in text:
            escreve(i)
    elif pessoa[0].upper() == "SARAH":
        text = f"\033[1m\033[33m{pessoa[0]}", f" \033[0mtem {pessoa[1]} anos e é minha irmã, a mais fofa que conheço!\n"
        for i in text:
            escreve(i)
    else:
        text = f"\033[31m{pessoa[0]}", f" \033[0mtem {pessoa[1]} anos e é meu amigo(a).\n"
        for i in text:
            escreve(i)

sleep(1)    
print("")
sleep(1)
print("")
    
type = f'''\033[96m Estas são as pessoas da minha vida. Amo essas pessoas!
 Com certeza é uma grande responsabilidade viver ao lado de pessoas tão magníficas como
vocês, tento sempre ser uma pessoa boa a partir da melhor parte e dos erros de vocês. 
Aprendo todos os dias e vou continuar aprendendo com as particularidades de cada um.
 A vida é difícil e injusta, mas se fosse fácil não teria graça. Bem ou mal,
estamos aqui, então temos de aprender a fazer o melhor possível com o que temos. Estas
pessoas me ensinaram isso.
 Para os meus pais eu devo uma vida, para os meus amigos e namorada eu devo o mundo...
 Obrigado por tornarem as coias mais leves e felizes! 
 Admiro todos vocês!
 
 ''', '''Ass: Gustavo Furtado, 09/06/22'''

for text in type:
    if text[0:4] == 'Ass:':
        sleep(2)
        escreve(text, .2)
    else:
        for word in text:
            stdout.write(word)
            stdout.flush()
            if word in '.!':
                sleep(.7)
            elif word == ',':
                sleep(.3)
            else:
                sleep(.05)

sleep(1)
print("")
sleep(1)
print("")
sleep(1)
escreve("\033[0mFIM", .5)
sleep(1)

# -*- coding: utf-8 -*-
import os
from time import sleep
import time
from random import randint
import modules.config as con


# work with OS
def end():
    print('Сыграем ещё?:', end=' ')
    
    stat = input().lower()
    if stat == 'да':
        os.system('cls')
        os.system('run.bat')
    elif stat == 'нет':
        print('Тогда пока!')
        sleep(1)
        path_parent = os.getcwd()
        os.system(path_parent + "/exit.bat")

    else:
        print(con.name + ', я тебя не понял!(((')
        end()

def recording():
    coins = 0
    if con.d == 'легкая' and con.status == 'Win':
        coins = 10
    elif con.d == 'средняя' and con.status == 'Win':
        coins = 20
    elif con.d == 'тяжелая' and con.status == 'Win':
        coins = 60
    bcoins = str(bin(coins))
    idp = str(randint(400000, 900000))
    fud = 'user_data.txt'
    f = open(fud, 'w')
    f.write("Game over in " + t + "\n")
    f.write("ID player: " + idp + "\n")
    f.write("Your name: " + con.name + "\n")
    f.write("Chosen difficulty: " + con.d + "\n")
    f.write("Game result: " + con.status + "\n")
    if con.d == 'песочница':
        f = open(fud, 'a')
        f.write("Cheats: " + con.cheats + "\n")
    f.write("Coins: " + bcoins + "\n")
    f.close()

def statistic():
    global t
    t = time.asctime(time.localtime(time.time()))
    print('Хотите просмотреть свою статистику по текущей игре?:', end=' ')
    stat = input().lower()
    if stat == 'да':
        recording()
        os.system('run_file.bat')
        os.system('CLS')
        end()
    elif stat == 'нет':
        os.system('CLS')
        end()
    else:
        print(con.name + ', я тебя не понял!(((')
        print()
        statistic()

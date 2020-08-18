# -*- coding: utf-8 -*-
from random import randint
from modules.work_with_OS import *
import modules.config as con
from modules.sound import *
from os import system


# Logics game
def check_number_for_trollMod():
    
    while(con.count > 0):
        try:
            print('Твой ход:', end=' ')
            usnu = input()
            if usnu == 'o': #чит в тролль моде
                print('begin')
                screamer()
                system('pause')
                print('end')
            usnum = int(usnu)
            cpu_num = randint(5, 10)
            if (usnum < cpu_num):
                con.count -= 1
                print('Недолёт!!!')
                print('Осталось попыток: ' + str(con.count))
                print('==================================')
                print()
                if con.count == 0:
                    print(con.name, ' ты проиграл :(')
                    con.status = 'Lose'
                    statistic()

            elif (usnum > cpu_num):
                con.count -= 1
                print('Перелёт!!!')
                print('Осталось попыток: ' + str(con.count))
                print('==================================')
                print()
                if con.count == 0:
                    print(con.name, ' ты проиграл :(')
                    con.status = 'Lose'
                    statistic()

        except ValueError:
            print("Введены непонятные символы. Повторите попытку сново!")


def check_number():
    cpu = 0
    if con.d == 'легкая':
        cpu = randint(0, 10)
    elif con.d == 'средняя':
        cpu = randint(0, 20)
    elif con.d == 'сложная':
        cpu = randint(0, 40)
    
    cpu_num = cpu

    while(con.count > 0):
        try:
            print('Твой ход:', end=' ')
            usnum = int(input())

            if (usnum < cpu_num):
                con.count -= 1
                print('Недолёт!!! Число находится ближе к ', cpu_num + 2)
                print('Осталось попыток: ' + str(con.count))
                print('==================================')
                print()
                if con.count == 0:
                    print(con.name, ' ты проиграл :(')
                    print('Я загадал число ', cpu_num)
                    con.status = 'Lose'
                    break

            elif (usnum > cpu_num):
                con.count -= 1
                print('Перелёт!!!  Число находится ближе к ', cpu_num + 2)
                print('Осталось попыток: ' + str(con.count))
                print('==================================')
                print()
                if con.count == 0:
                    print(con.name, ' ты проиграл :(')
                    print('Я загадал число ', cpu_num)
                    con.status = 'Lose'
                    break

            else:
                print(con.name, ' ты победил')
                con.status = 'Win'
                break
        except ValueError:
            print("Введены непонятные символы. Повторите попытку сново!")

    statistic()
    exit

def check_number_for_sandbox():
    global cpu_num
    while True:
        try:
            print('Введите кол-во попыток:', end=' ')
            count = input()
            con.count = int(count)
            break
        except ValueError:
            print(con.name + ', я тебя не понял!(((')

    while True:
        try:
            print('Введите интервал загадывания чисел через символ "..." :', end=' ')
            b, e = map(int, input().split("..."))
            cpu_num = randint(b, e)
            break
        except ValueError:
            print(con.name + ', я тебя не понял!(((')

    print('Хотите играть с читами:', end=' ')
    ch = input().lower()
    if ch == 'да':
        con.cheats = 'On'
        print(cpu_num)
    if ch == 'нет':
        con.cheats = 'Off'
        
    check_number()
    exit

def check_count():
    while True:
        try:
            print('Введите кол-во попыток:', end=' ')
            count = input()
            con.count = int(count)
            if not (1 <= con.count <= 4):
                print('Обмащик!')
                check_count()
            else:
                print('Начинаем...')
                print('--------------------------------------------------------------------')
                check_number_for_trollMod()

        except ValueError:
            print(con.name + ', я тебя не понял!(((')
    exit

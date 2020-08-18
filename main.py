# -*- coding: utf-8 -*-
from random import randint
from time import sleep
from modules.dwferent import *
import modules.config as con


def lobby():
    print('Выберите сложность игры: 1-песочница, 2-легкая, 3-средняя, 4-тяжёлая, 5-trollMod')
    vd = input()
    if vd == '1':
        d_sandbox()
    elif vd == '2':
        d_easy()
    elif vd == '3':
        d_middle()
    elif vd == '4':
        d_hard()
    elif vd == '5':
        d_trollMod()
    else:
        print(con.name + ', я тебя не понял!(((')
        lobby()

# monolog №1
def monolog():
    print('Чтобы пропустить кадсцену нажмите клавишу С. Иначе, жмите ENTER :', end='')
    skip = input().lower()
    if skip == 'c' or skip == 'с':
        lobby()
    elif skip == '':
        print('Итак, ' + con.name + ', ты попал в игру "Угадай число"...')
        sleep(2)
        print('Стой! Стой! Стой!')
        sleep(2)
        print('Я знаю, что ты играл в подобные игры...')
        sleep(2)
        print('Стоп. Я что-то забыл...')
        sleep(2)
        print('Ах да... Забыл представиться!')
        sleep(2)
        print('Меня зовут:')
        sleep(2)
        print('''
    █▄░█ █░░█ ██▄██ █▀▄ █▀▀ █▀▄ █▀▄ ▄▀▀▄ ▀█▀
    █▀██ █░░█ █░▀░█ █▀▄ █▀▀ █▀▄ █▀▄ █░░█ ░█░
    ▀░░▀ ░▀▀░ ▀░░░▀ ▀▀░ ▀▀▀ ▀░▀ ▀▀░ ░▀▀░ ░▀░''')
        print('Мощно?')
        print('Ладно... Иди уже играть')
        lobby()
        
def begin():
    print('Привет! Как тебя зовут?:', end=' ')
    con.name = input()
    monolog()

begin()
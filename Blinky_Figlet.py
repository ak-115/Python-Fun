import pyfiglet
import os
import time


End = '\33[0m'
Red = '\33[31m'
Green = '\33[32m'
Yellow = '\33[33m'
Blue = '\33[34m'
Violet = '\33[35m'
Beige = '\33[34m'
White = '\33[37m'
Black = '\33[30m'

print(Green)
text = str(input('Enter the text:'))
figlet = pyfiglet.figlet_format((text))

def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')

screen_clear()

def blinky_figlet():

    while True:
        print(figlet)
        screen_clear()
        print(Red)
        print(figlet)
        screen_clear()
        print(Green)
        print(figlet)
        screen_clear()
        print(Yellow)
        print(figlet)
        screen_clear()
        print(Blue)
        print(figlet)
        screen_clear()
        print(Violet)
        print(figlet)
        screen_clear()
        print(Beige)
        print(figlet)
        screen_clear()
        print(White)
        print(figlet)
        screen_clear()
        print(Black)

blinky_figlet()

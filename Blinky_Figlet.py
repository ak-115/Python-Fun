import pyfiglet
import os

# Colours = [Red, Green, Yellow, Blue, Violet, White, Black]
Colours = ['\33[31m', '\33[32m', '\33[33m', '\33[34m', '\33[35m', '\33[37', '\33[30m']
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
      X = 0
      while True:
          if X <= 6:
             print(Colours[X] + figlet)
             X = X + 1
             screen_clear()
          else: break

blinky_figlet()

import colorama
from colorama import Fore, Back, Style
from colorama import init
init()
from variables import *
from defintions import *
for game in range(1, 7):
  displayBoard()
  inputword()
  from defintions import win
  from defintions import playerword
  if win == 1 :
    break
  print("\n")
  
if win == 1 :
  displayBoard()
  print(Style.RESET_ALL + "Congratulations you guessed the word")
else :
  print(Fore.RED + "GAME OVER")
  displayBoard()
  print(Style.RESET_ALL + "You have run out of trys!")
  for x in range(0,5) :
    word[x] = Fore.BLUE + word[x]
  print("The word is :",*word)

input(Back.BLACK + "press enter to exit: ") 

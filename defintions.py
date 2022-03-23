from variables import *
import colorama
from colorama import Fore, Back, Style

import random
word = (random.choice(open("words.txt").read().split()))
word = list(word.strip(" "))

def displayBoard() :
  global loop 
  print(Back.BLACK + "This is your current table")
  loop = loop + 1
  print(end= Style.RESET_ALL + "")
  print(*line1)
  print(*line2)
  print(*line3)
  print(*line4)
  print(*line5)
  print(*line6)



def wordchecker() :
  global loop
  global word
  global playerword
  for i in range(0,5) :
    if playerword[i] in word :
      multi = word.count(playerword[i])
      if playerword[i] == word[i] :
        playerword[i] = Back.GREEN + playerword[i]
      elif Back.YELLOW + playerword[i] in playerword and multi == 1 :
        playerword[i] = Back.BLACK + playerword[i]
      elif Back.YELLOW + playerword[i] in playerword and multi > 1 :
        playerword[i] = Back.YELLOW + playerword[i]
      elif Back.GREEN + playerword[i] in playerword and multi == 1 :
        playerword[i] = Back.BLACK + playerword[i]
      elif Back.GREEN + playerword[i] in playerword and multi > 1 :
        playerword[i] = Back.YELLOW + playerword[i]
      else :
        playerword[i] = Back.YELLOW + playerword[i]
    else : 
      playerword[i] = Back.BLACK + playerword[i]
  for i in range(0,5) :
    x = word[i]
    multi1 = word.count(x)
    multi2 = playerword.count(Back.GREEN + x) + playerword.count(Back.YELLOW + x)

    if multi2 > multi1 :
      index = playerword.index(Back.YELLOW + x)
      playerword[index] = Back.BLACK + x
    


def inputword() :
  global playerword
  global game
  global word
  global win
  global loop
  global line1
  global line2
  global pword
  global line3
  global line4
  global line5
  global line6
  playerword = (input("Write a 5 letter word: "))  
  if type(playerword) != str or len(playerword) != 5 :
      print(Back.RED + "Your word length is not 5 letters, try again")
      print(Style.RESET_ALL + "")
      inputword()
  else :
    playerword = str(playerword)
    playerword = list(playerword.strip(" "))
    if playerword == word :
      win = 1
      
    if len(playerword) == 5 :
      if loop == 1 :
        wordchecker()
        playerword.insert(5,Back.BLACK + " ")
        line1 = playerword
      if loop == 2 :
        wordchecker()
        playerword.insert(5,Back.BLACK + " ")
        line2 = playerword
      if loop == 3 :
        wordchecker()
        playerword.insert(5,Back.BLACK + " ")
        line3 = playerword
      if loop == 4 :
        wordchecker()
        playerword.insert(5,Back.BLACK + " ")
        line4 = playerword
      if loop == 5 :
        wordchecker()
        playerword.insert(5,Back.BLACK + " ")
        line5 = playerword
      if loop == 6 :
        wordchecker()
        playerword.insert(5,Back.BLACK + " ")
        line6 = playerword
      



 

    

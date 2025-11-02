import random
import time
import pickle
import curses

print("H A N G M A N\n")

hanged = ['''
  +---+
      |
      |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

try:
  playname = pickle.load(open("nom.p", "rb"))
  highscores = pickle.load(open("scores.p", "rb"))
  hangstate = pickle.load(open("open.p", "rb"))
  print(hanged[1]) if hangstate == True else print(hanged[7])
  print("Welcome back, " + playname + "!")
except OSError:
  highscores = [0, 0, 0]
  print(hanged[0])
  print("Welcome, [GUEST]!")

def badinp():
  print("Invalid input. Try again.")

def select(string):
 rand = []
 w = open(string+"words.txt", "r")
 for line in w:
   rand.append(line.strip())
 word = random.choice(rand)
 return word

def freshscreen(lis1, lis2, num1, num2, lis3, guessfirst):
  stdscr = curses.initscr()
  stdscr.erase()
  for n in range(len(lis1)):
    stdscr.addstr(lis1[n])
  stdscr.addstr("\n"+lis2[num2])
  stdscr.addstr("\nYou have "+ str(num1)+ " guesses left.\n")
  if guessfirst:
    stdscr.addstr("Letters guessed so far: ")
    for i in range(len(lis3)):
      stdscr.addstr(lis3[i]+" ")
    stdscr.addstr("\n")
  stdscr.refresh()

def win(second, guessesleft):
  stdscr = curses.initscr()
  stdscr.erase()
  stdscr.addstr("V I C T O R Y ! ! !\n")
  stdscr.refresh()
  time.sleep(2)
  stdscr.addstr("\nTime taken: " + str(second))
  stdscr.refresh()
  time.sleep(1)
  stdscr.addstr("\nGuesses remaining: " + str(guessesleft) + "\n")
  stdscr.refresh()
  


def game():
  difselect = input("\nWhich mode would you like to play on? (Easy, Normal, Hard)\n").lower()
  word = select(difselect)
  endgame = False
  firstguess = False
  guesses = 7
  hangednum = 0
  hidword = []
  guessedchar = []
  guess = ""
  for x in range(len(word)):
      hidword.append("_ ")
  start = time.time()
  stdscr = curses.initscr()
  while endgame == False and hangednum != 8:
    freshscreen(hidword, hanged, guesses, hangednum, guessedchar, firstguess)
    stdscr.addstr("Enter your guess: ")
    guess = stdscr.getkey().lower()
    firstguess = True
    if guess.isalpha() == True and guess not in guessedchar:
      guessedchar.append(guess)
    elif guess in guessedchar and guess not in word:
      guesses += 1
      hangednum -= 1
    freshscreen(hidword, hanged, guesses, hangednum, guessedchar, firstguess)
    if guess.isalpha() == False or len(guess) > 1:
      badinp()
      freshscreen(hidword, hanged, guesses, hangednum, guessedchar, firstguess)
    elif guess in word:
      for num in range(len(word)):
        if guess == word[num]:
          hidword[num] = guess+" " 
    elif guess not in word:
      guesses -= 1 
      hangednum += 1
    if hangednum == 7 or "_ " not in hidword:
      end = time.time()
      freshscreen(hidword, hanged, guesses, hangednum, guessedchar, firstguess)
      endgame = True
  totime = end - start
  if hangednum == 7:
    print("kys")
  elif "_ " not in hidword:
    win(totime, guesses)




 


 #actual contents of game
  
  '''start -= end
  score = (start*guesses)'''

def scoreload():
 print('''\nHIGH SCORES:\n
EASY MODE:''', highscores[0],
'''\nNORMAL MODE:''', highscores[1],
'''\nHARD MODE:''', highscores[2], "\n")
 menu()
 #subroutine that loads the player's high score for each difficulty

def end():
  print("\nBYE-BYE!")
  quit()

def menu():
 menuchoice = False
 print('''What would you like to do?
 1. Play
 2. Check score
 3. Exit''')
 opt = {
   1: game,
   2: scoreload,
   3: end
 }
 while not menuchoice:
  run = input()
  menuchoice = True
  if run.isnumeric() == False:
    badinp()
    menuchoice = False
  elif int(run) > 3 or int(run) < 1:
    badinp()
    menuchoice = False
  else:
    opt.get(int(run))()




 

 
 
menu()

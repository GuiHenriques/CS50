# Hangman Game

from random import randint
from time import sleep

# Board Sequence
board = ["""
 -=-=-=-=-=- Hangman -=-=-=-=-=-

 +---+
     |
     |
     |
     |
 ========= """, '''

 +---+
 |   |
 o   |
     |
     |
     |
 ========= ''', '''

 +---+
 |   |
 o   |
 |   |
     |
     |
 ========= ''', '''

  +---+
  |   |
  o   |
 /|   |
      |
      |
  ========= ''', """

  +---+
  |   |
  o   |
 /|\  |
      |
      |
  ========= """, """
  +---+
  |   |
  o   |
 /|\  |
 /    |
      |
  ========= """, """
    +---+
  |   |
  o   |
 /|\  |
 / \  |
      |
  ========= """]

# Classe
class Hangman():
    # Construtor
    def __init__(self, word):
        self.word = word

    # Guess letter
    def guess(self, letter):
        if letter in self.word:
            return True
        else:
            return False
            
    # Check win
    def hang_win(self, right):
        for i in self.word:
            if i in right:
                pass
            else:
                return False
        return True

    # Hide word
    def hide_word(self, right):
        print('Palavra: ', end='')
        for i in self.word:
            if i in right:
                print(i, end="")
            else:
                print("_", end="")
                
        print()
        # Check win

    # Print Game Status
    def status(self, wrong):
        # Wordsrong words
        print('Wrong words: ', end="")
        for i in wrong:
            print(i, end=" ")
        print()

def rand_word():
    with open("words.txt", "r") as w:
        bank = w.readlines()
    return bank[randint(0, len(bank) - 1)].strip()

# Execução
def main():
    # Words list
    right = []
    wrong = []
    
    # Objeto
    game = Hangman(rand_word())

    win = False
    for k, i in enumerate(board):
        if win:
            break
        # Board Game
        print(i)
        if k == 6:
            break 
                
        # Ask letter
        while True:
            # Word status
            game.hide_word(right)
            game.status(wrong)
            print()
            letter = input("Type a word: ").lower()
            if game.guess(letter):
                right.append(letter)
                
                # Check win
                if game.hang_win(right):
                    print("\033[32mWell Done. You Won\033[m")
                    win = True
                    break
            else:
                wrong.append(letter)
                break
    
    # If not hang_win an loop ended, you lost
    if not win:
        print("\033[31mGame Over. You Lost\033[m")
        print("The word was", game.word)

# Execute Program
if __name__ == "__main__":
    main()

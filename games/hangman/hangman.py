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
        # Words list
        self.right = []
        self.wrong = []
    
    def board(self):
        print(board[len(self.wrong)])

    # Guess letter
    def guess(self, letter):
        if letter in self.word:
            self.right.append(letter)
            return True
        else:
            self.wrong.append(letter)
            return False
            
    # Check win
    def hang_win(self):
        for letter in self.word:
            if letter not in self.right:
                return False
        return True
    
    def hang_over(self):
        if len(self.wrong) == 6:
            return True

    def hide_word(self):
        print('Palavra: ', end='')
        for letter in self.word:
            if letter in self.right:
                print(letter, end="")
            else:
                print("_", end="")
        print()

    def status(self):
        print('Wrong words: ', end="")
        for letter in self.wrong:
            print(letter, end=" ")
        print()

def rand_word():
    with open(".\words.txt", "r") as w:
        bank = w.readlines()
    return bank[randint(0, len(bank) - 1)].strip()
    

# Execução
def main():
    # Objeto
    game = Hangman(rand_word())
    
    # Word status
    while True:
        game.board()
        game.hide_word()
        game.status()
        letter = input("Type a word: ").lower()
        game.guess(letter)
        if game.hang_win():
            game.hide_word()
            print("\033[32mWell Done\033[m")
            break
        if game.hang_over():
            print("\033[31mGame Over.\033[m. The word was", game.word)
            break
        
# Execute Program
if __name__ == "__main__":
    main()

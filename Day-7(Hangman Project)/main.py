word_list = ["lemon","camel","nylon"]

import random
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = 6
display=[]
for _ in range(word_length):
    display.append("_")
    
print(display)

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter:").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_word:
        lives = lives -1
        if lives == 0:
            end_of_game = True
            print("You lose!")
                    
    print(display)   
    if "_" not in display:
        end_of_game = True
        print("You win.")
        

print(stages[lives])
print(f"The chosen word wass {chosen_word}") 
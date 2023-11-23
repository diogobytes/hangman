import random
import hangman_art
import hangman_words
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
display = []
word_length = len(chosen_word)
stages = hangman_art.stages

print(hangman_art.logo)
lives = 6
for _ in range(word_length):
    display += "_"

end_of_game = False
print(chosen_word)
while not end_of_game:
  guess = input("Guess a letter: ").lower()
  for pos in range(word_length):
    letter = chosen_word[pos]
    if guess == letter:
      display[pos] = letter
  print(f"{' '.join(display)}")
  print(f"{stages[lives]}")
  
  if guess not in display:
    lives -= 1
  if "_" not in display:
    end_of_game = True
    print("You win.")
  if lives == 0:
    end_of_game = True
    print("You lose.")
    
  
import random 
from hangman_words import word_list
from hangman_arts import stages, logo

print(logo)

lives = 6 
chosen_word = random.choice(word_list)

placeholder = ""
for position in chosen_word :
    placeholder += "_"

print("Word to Guess : " + placeholder)
game_over =False

while not game_over :
    print(f"*************************{lives} / 6 lives left *************************")
    guess = input("Guess a letter:").lower()

    display = ""
    correct_letters = []

    for letter in chosen_word :

        if guess == letter :
            display += letter
            correct_letters.append(guess)

        elif letter in correct_letters :
             display += letter

        else:
            display += "_"

    print ("Word to Guess : " + display)

    if guess not in chosen_word :
        lives -= 1
        
        if lives == 0 :
          game_over = True
          print(F"*************************IT WAS {chosen_word} YOU LOSE************************")
        print(stages[lives])

    if "_" not in display :
        game_over = True
        print("*************************YOU WIN*************************")
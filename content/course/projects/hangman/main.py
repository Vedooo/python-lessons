import random as rd
import functions as func

chosen_word = rd.choice(func.word_list)
word_lenght = len(chosen_word)
end_of_game = False
display = []
lives = 6

print(func.logo)
print(chosen_word)
for _ in range(word_lenght):
    display += "_"

while not end_of_game:
    guess = input("\n\nGuess a letter: \n").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print("Current letter: {}".format(letter))

    
    print(f"{' '.join(display)}")
    
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = 0
            print("\nGame over..")
            print(func.stages[lives])
            break
    
    
    if "_" not in display:
        end_of_game = True
        print("\nYou win..")          

    print(func.stages[lives])

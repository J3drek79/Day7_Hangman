#Step 3

import random
word_list = ["telefon", "kuchnia", "banan", "pomidor"]
chosen_word = random.choice(word_list)

#Testing code
print(chosen_word)

#Create blanks
display = []
for letter in chosen_word:
    display.append("_")
print(display)

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
end_of_game = False

while not end_of_game:
    guess = input("Podaj literę: \n").lower()
        
    #Check guessed letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    print(display)

    if "_" not in display:
        end_of_game = True
        print("Wygrałeś")
    

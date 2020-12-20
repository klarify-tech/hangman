#Creating the code for the hangman game
import random
import string
from words import words

selected_word = words[random.randint(0,len(words)-1)].upper()
#print(selected_word) If you want to see the word to debug your logic
guess_word = ""
for x in selected_word:
    guess_word= guess_word + "-"

print(f"Starting the game {guess_word}")
   
def fill_char(letter,word_in_selection,current_guess):
    temp_list = list(word_in_selection)
    temp_guess = list(current_guess)
    count=0
    for x in temp_list:
        if x == letter:
            temp_guess[count]=letter
        count +=1
        
    current_guess = "".join(temp_guess)
    print(current_guess)
    return current_guess    


#No of times a user can guess wrong letters
lives = 5
used_letters = []
while(guess_word != selected_word) and lives >0:
    input_char = input(f"Enter a letter. You have already guessed {used_letters} ").upper()
    used_letters.append(input_char)
    if input_char in selected_word:
        print(input_char)
        guess_word = fill_char(input_char,selected_word,guess_word)
        
        
    else:
         lives = lives-1
         print(f" Sorry the letter {input_char} is not in the word")
         print("You lost a chance remaining lives ",lives)
         print(guess_word)
         
    
    
    
if lives > 0:
    print(f"You guessed correctly {guess_word} ")
else:
    print(f"Sorry you lost. The word was {selected_word}") 




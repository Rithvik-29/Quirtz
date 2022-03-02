from flask import Flask, render_template
import random
from colorama import Fore

app=Flask(__name__)

from words import five_letter_words as final_list

answer = random.choice(final_list)

guesses = 0
failed = True

while guesses < 6:
    print(Fore.WHITE + '')
    guess = input('Enter a guess: ')

    if len(guess) == 5:
        guesses += 1
        correctletters = 0
        for letter in guess:
            letterindexguess = guess.find(letter)

            letterindextarget = answer.find(letter)

            if letterindextarget > -1:
                if letterindexguess == letterindextarget:
                    print(Fore.GREEN + letter, end=" ")
                    correctletters += 1
                else:
                    print(Fore.YELLOW + letter, end=" ")
            else:
                print(Fore.WHITE + letter, end=" ")

            if correctletters == 5:
                print('')
                print('YOU WIN!!')
                print(Fore.WHITE + '')
                guesses = 6
                failed = False

    else:
        print("It has to be 5 letter you dumbass")

if failed == True:
    print('')
    print(Fore.RED + 'You ran out of tries')
    print(Fore.WHITE + 'The word was: ' + answer)

@app.route('/')
def home():
    return render_template('home.html', answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
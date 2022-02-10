
import random

list_of_words =  open("secret_words.txt").readlines()
#print(list_of_words)
secret_word = list_of_words[random.randrange(len(list_of_words))]
print(secret_word)

number_of_letters = len(secret_word)-1
first_letter = secret_word[0]
last_letter = secret_word[-2]
print(last_letter)

def hint_word():
    number_of_hid_letters = number_of_letters - 2
    hidden = number_of_hid_letters * " _ "
    hint_word = f"{first_letter+hidden+last_letter}"
    return hint_word

guess = input(f"Guess word. {number_of_letters} letters? {hint_word()} \n ")


if guess == secret_word:
    print("Well done")
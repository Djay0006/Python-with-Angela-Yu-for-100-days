# def my_function():
#     print("Hello")
#     print("world")
# my_function()

import random
word_list=["camel","money","bridge","road"]
chosen_word=random.choice(word_list)
print(chosen_word)
placeholder=""
for i in range(len(chosen_word)):
    placeholder+="_"
print(placeholder)
while
User_guess=input("Guess the word: ").lower()
display=""
for letter in chosen_word:
    if letter==User_guess:
        display+=letter
    else:
        display+="_"
display==display
print(display)



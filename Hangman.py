# Making of game hangman
import random
# creating a list of various words
words_list= ["beekeaper","indepandent","house","master","oathbreaker","giveup","speaker"]
# selecting a random word from the list
random_word= random.choice(words_list)
# creating an empty list for storing the latters of selected random words_list
new_list=[]
for i in random_word:
    new_list.append("_")
print(random_word)
print(new_list)
# asking the user to guess the letter
# checking the guessed letter in the random word and replacing it in the new_list
life= 6
letter= ""
win= False
while win!=True:
    guessed_letter= input("guess a letter. ")
    for position in range(len(random_word)):
        letter=random_word[position]
        if letter==guessed_letter:
            new_list[position]= letter
    print(new_list)
        
    if "".join(new_list)== random_word:
        print("you won.")
        win= True
    
    if guessed_letter not in random_word:
        life-=1
        print("you loose a life.")

    if life==0:
        print("you loose.")
        break
            







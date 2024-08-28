
import random

max_no = input("Please insert your maximum number: ")

if max_no.isdigit():
    max_no=int(max_no)
    
    if max_no <= 0: 
        print("PLease enter a number greater than 0")
        quit()
guess = 0
while True:
    guess += 1
    user_guess = input("Please make a guess: ")
    if user_guess.isdigit():
     user_guess=int(user_guess)
    else:
        print("please enter a digit next time")
        continue

    rand_no = random.randint(0,max_no)
    

    if(rand_no == user_guess):
     print("you got it right in ",guess,"guesses!")
     break
    else:
     print("you got it wrong")
     print(rand_no)



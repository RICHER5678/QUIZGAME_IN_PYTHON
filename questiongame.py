print("welcome to my game!","please read instructions before starting")
score=0
response = input("Do you want to play this game? ").lower()
hello=0
if(response != "yes"):
    quit()
else:
    print("Starting the game now!!.......................")

question=input("question1: What is CPU in full?? ").lower()
if(question) == "central processing unit":
    score +=1
    print("You got it right")
else:
    print("you fucked up")

question=input("question1: What is GPU in full?? ").lower()
if(question) == "graphical processing unit":
    score +=1
    print("You got it right")
else:
    print("you fucked up!")


print("You got",score,"questions right")
print("Finally, you scored",float(score/2*100),"%")
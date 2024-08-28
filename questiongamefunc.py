
#question game using functions

def question(qn1, qn2, qn3):
    print("Welcome to my game!!!")
    response=input("Do you want to play this game?? ").lower()
    if(response != "YES"):
        quit()
    answer=input("what is JB in full?? ")
    question()
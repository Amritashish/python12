from random import import randint

#create a list of play options
t=["Rock", "Paper","Scissors"]

#assign a random play to the computer
computer=t[randint(0,2)]

#set player to FALSE
player=false

while player==False:
#set playerto true
    player=input("Rock,Paper,scissors?")
    if player==computer:
        print("Tie!")
    elif player=="Rock":
        if computer=="paper"
            print("You lose!",computer,"covers",player)
            else:
                print("You win!",player ,"smashes",computer)
    elif player=="paper"
       if computer=="Scissors":
           print("you lose!",computer,"cut",player)
           else:
               print("you win!"player,"smashes",computer) 

import random
def game():
    value=int(input("Press 1 for ROCK\nPress 2 for PAPER\nPress 3 for SCISSORS\n"))
    x=random.randint(1,3)
    if x==1:
        print("Computer chose: ROCK")
        print("*********************")
    elif x==2:
        print("Computer chose: PAPER")
        print("*********************")
    else:
        print("Computer chose: SCISSORS")
        print("*********************")
    if value==x:   #rock,rock/paper,paper/scissor,scissor
        print("Tie...")
        print("*********************")
    elif value==1 and x==2:      #you=rock me=paper
        print("Computer Wins!")
        print("*********************")
    elif value==1 and x==3:      #you=rock me=scissor
        print("You Win!")
        print("*********************")
    elif value==2 and x==1:      #you=paper me=rock
        print("You Win!") 
        print("*********************")
    elif value==2 and x==3:      #you=paper me=scissors
        print("Computer Wins!")
        print("*********************")
    elif value==3 and x==1:      #you=scissor me=rock
        print("Computer Wins!")
        print("*********************")
    elif value==3 and x==2:      #you=scissors me=paper
        print("You Win!")
        print("*********************")
    else:
        print("Invalid Input")
        print("*********************")
while True:
    play=input("Press y to play\nPress n to exit\n")
    if play=='y' or play=='Y':
        game()
    elif play=='n' or play=="N":
        print("Game Over")
        exit()
    else:
        print("Invalid Input")



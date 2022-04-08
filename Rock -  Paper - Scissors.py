import random
while True:
 selection = ["rock","paper","scissors"]
 computer = random.choice(selection)
 player = input("Enter your choice: rock, paper or scissor?: ").lower()
 print("--------------------")
 print("Your choice:",player)
 print("The computer:",computer)
#-----------------------------
 if player == computer:
    print("Both of us are the same",player,".Tie!")
 elif player == "rock":
    if computer == " paper":
        print("Paper covers the rock. You lose")
    else:
        print("Rock smashes the scissors. You win")
 elif player == "paper":
    if computer == "rock":
        print("Paper covers the rock. You win")
    else:
        print(" Scissors cut the paper. You lose")
 elif player == " Scissors":
    if computer == "paper":
        print("Scissors cut the paper. You win")
    else:
        print("Rock smashes the scissors. You lose")
 else:
    print("It is an invalid value. Please kindly check it again")

 play_again= input("Do you want to play again? (y/n):").lower()
 if play_again !="y":
    break
print("Bye. Thank you for playing")




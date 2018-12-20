#Rock beats scissors
#Scissors beats paper
#Paper beats rock

player_1= input(str("Player One : Choose rock/paper/scissor "))
player_2= input(str("Player two : Choose rock/paper/scissor "))

if player_1 == player_2:
    print("It is a tie")
elif player_1 == "rock":
    if player_2 == "scissors":
        print("Player One wins")
    else:
        print("player two wins")
elif player_1 == "scissors":
    if player_2 == "paper":
        print("Player One wins")
    else:
        print ( "player two wins" )
elif player_1 == "paper":
    if player_2 == "rock":
        print("Player one wins")
    else:
        print("Player two wins")

else:
    print("Incorrect option")
from random import randint
options = ('rock','paper','scissors')

# rand_num = randint(0,2)
# if rand_num == 0:
#     player2='rock'
# elif rand_num == 1:
#     player2='paper'
# else:
#     player2='scissors'

playercounter=0
computer=0


while playercounter or computer != 3:
    rand_num = randint(0, 2)
    if rand_num == 0:
        player2 = 'rock'
    elif rand_num == 1:
        player2 = 'paper'
    else:
        player2 = 'scissors'

    print("...rock...")
    print("...paper...")
    print("...scissors...")

    player1 = input("Pick an option: ")

    print ("Computer chose " + player2)

    if player1 == player2:
        print ("Try again")
    elif player1 == "rock" and player2 != "paper":
        print("You win this round!")
        playercounter+=1
        print(playercounter)
    elif player1 =="paper" and player2 != "scissors":
        print("You win this round!")
        playercounter+=1
        print(playercounter)
    elif player1 =="scissors" and player2 != "rock":
        print ("You win this round!")
        playercounter+=1
        print(playercounter)
    else:
        print ("Computer wins!")
        computer+=1
        print(computer)
    if playercounter == 3 or computer ==3:
        if playercounter ==3:
            print("YOU WON!! GAME OVER!")
        else:
            print("BOO WHORE, THE COMPUTER BEAT YOU")
        break


print("...rock...")
print("...paper...")
print("...scissors...")

player1 = input("Player 1, pick an option: ")

print("NO CHEATING!!!! \n" *50)

player2 = input("Player 2, pick an option: ")

if player1 == player2:
    print ("Try again")
elif player1 == "rock" and player2 != "paper":
    print("Player 1 wins!")
elif player1 =="paper" and player2 != "scissors":
    print("Player 1 wins!")
elif player1 =="scissors" and player2 != "rock":
    print ("Player1 wins!")
else:
    print ("Player2 wins!")



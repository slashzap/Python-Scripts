import random

# Option 1 for RPS

def rock_paper_scissors():
    user_choice = input("Choose 'rock', 'paper', or 'scissors': ").lower()
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print(f"\nYou chose {user_choice}, computer chose {computer_choice}")
    
    if user_choice == computer_choice: 
        print("It's a tie!")
        return ""
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
         print( "You won!")
         return "player"
    else:
         print( "You lost!")
         return "computer"
    
#print(rock_paper_scissors())


# Option 2 for RPS
def rps():
	options = ["rock", "paper", "scissors"]
	computer_choice = random.choice(options)
	player_choice = input("Rock, paper, or scissors? ")
	
	winner = "player"
	
	if player_choice == computer_choice:
	    print("Tie!")
	    winner = ""
	elif player_choice == "rock" and computer_choice == "scissors":
	    print("You win!")
	elif player_choice == "paper" and computer_choice == "rock":
	    print("You win!")
	elif player_choice == "scissors" and computer_choice == "paper":
	    print("You win!")
	else:
	    print("You lose!")
	    winner = "computer"
	
	return winner

round = 1
end_round = 5
player = 0
computer = 0

while(round <= end_round):
	winner = ""
	
	if round % 2 == 0:
		winner = rps()
	else:
		winner = rock_paper_scissors()

	if winner == "player":
		player += 1
	elif winner == "computer":
		computer += 1

	print(f"\nAfter {round} rounds, the score is Player {player} vs Computer {computer}")
	print("*" * 20 + "\n")
	round += 1


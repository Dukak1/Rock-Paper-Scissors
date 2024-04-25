import random
import time

options = {"r": "rock", "p": "paper", "s": "scissors"}

def game():
    wins = 0
    losses = 0
    print("Game starts! (Press 'q' to exit anytime)")

    while True:
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)

        opponent = random.choice(list(options.values()))
        move = input("Rock, paper, scissors? ('q' to exit): ").lower()

        if move == 'q':
            print("Exiting...")
            time.sleep(1)
            print("You finished with {} wins and {} losses against the computer".format(wins, losses))
            break        
        elif move in options.keys():
            move = options[move]
        elif move.startswith(tuple(options.keys())):
            move = options[move[0]]
        else:
            print("Invalid choice!!")
            continue

        if move == opponent:
            print("Draw!")
        elif (move == "rock" and opponent == "paper") or \
             (move == "paper" and opponent == "scissors") or \
             (move == "scissors" and opponent == "rock"):
            print("You lose!")
            losses += 1
        else:
            print("You win!")
            wins += 1

        print("Score: You {} - Computer {}".format(wins, losses))

game()

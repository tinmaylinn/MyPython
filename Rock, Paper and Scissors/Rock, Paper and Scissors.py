import random

print "Welcome Python! Play Rock, Paper and Scissors"

player = raw_input("Are you choose Rock or Paper or Scissors?")


def playGame(player):
    options = ('Rock', 'Paper', 'Scissors')
    computer = random.choice(options)
    if player == computer:
        print "Same point!"
    elif player == "Rock":
        if computer == "Paper":
            print "Computer win!"
        else:
            print "You win!"
    elif player == "Paper":
        if computer == "Scissors":
            print "Computer win!"
        else:
            print "You win!"
    elif player == "Scissors":
        if computer == "Rock":
            print "Computer win!"
        else:
            print "You win!"
    else:
        print "System Error!"

def playAgain(play):
    if play == "Y":
        playGame(player)
    elif play == "N":
        print "Thank You!"
        exit(-1)

if player:
    playGame(player)
    play = raw_input("Are you play again? Y or N")

if play:
    playAgain(play)




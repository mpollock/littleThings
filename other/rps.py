import random

done = False
comp = 0
user_in = ""
usernum = 0
throw = ["rock", "paper", "scissors"]
wins = 0
draws = 0
losses = 0

print("This is rock, paper, scissors. Enter 'q' to quit or 'w' to see your score.")

while not done:
  user_in = raw_input("Make your move [r,p,s or q,w]: ")
  if user_in == "q":
    done = True
    break
  elif user_in == "w":
    print("Wins:" + str(wins) + " Losses:" + str(losses) + " Draws:" + str(draws))
  elif user_in == "r" or user_in == "p" or user_in == "s":
    comp = random.randrange(3)
    print("The computer throws " + throw[comp])
    
    if user_in == "r":
      usernum = 0
    elif user_in == "p":
      usernum = 1
    elif user_in == "s":
      usernum = 2
    
    if (comp == 0 and usernum == 1) or (comp == 1 and usernum == 2) or (comp == 2 and usernum == 0):
      print("You win")
      wins += 1
    elif (comp == usernum):
      print("Draw")
      draws += 1
    else:
      print("You lose")
      losses += 1
  else:
    print("Please enter a proper command")

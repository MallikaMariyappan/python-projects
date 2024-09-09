import random
import sys

print("")
playerchoice=input("Enter...\n 1 for rock\n 2  for paper\n 3 for scissors:\n\n")
player=int(playerchoice)
if player<1 | player>3:
    sys.exit("You must enter 1,2 or 3")
computerchoice=random.choice("123")
choice=int(computerchoice)

print("")
print("You chose: "+ playerchoice)
print("python chose: "+ computerchoice)
print("")

if player==1 and choice==3:
    print("you win")
elif player==2 and choice==1:
    print("you win")
elif player == 3 and choice == 2:
    print("you win")
elif player==choice:
    print("Tie game")
else:
    print("Python win!!!!")





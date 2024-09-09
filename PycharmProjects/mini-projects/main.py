print("welcome to my computer quiz!")
player = input("do you want to play? ")
if player.lower() != "yes":
    quit()

print("Okey Let's Play")
score = 0
answer = input("CPU Stands for: ")
if answer.lower() == "central processing unit":
    print("correct")
    score += 1
else:
    print("Incorrect")

# print("You must enter the answer in camelcase method!!!Each word first letter would be capital")
answer = input("GPU Stands for: ")
if answer.lower() == "graphics processing unit":
    print("correct")
    score += 1
else:
    print("Incorrect")

# print("You must enter the answer in camelcase method!!!Each word first letter would be capital")
answer = input("RAM Stands for: ")
if answer.lower() == "random access memory":
    print("correct")
    score += 1
else:
    print("Incorrect")

# print("You must enter the answer in camelcase method!!!Each word first letter would be capital")
answer = input("ROM Stands for: ")
if answer.lower() == "read only memory":
    print("correct")
    score += 1
else:
    print("Incorrect")

# print("You must enter the answer in camelcase method!!!Each word first letter would be capital")
answer = input("PSU Stands for: ")
if answer.lower() == "power supply unit":
    print("correct")
    score += 1
else:
    print("Incorrect")
print("Your Score is: " + str(score))
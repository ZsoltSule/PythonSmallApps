import random

running = True
options = ["Rock", "Paper", "Scissors"]

while running:
    myChoice = input("Choose Rock, Paper or Scissors or type Exit to quit: ").capitalize()
    
    if myChoice == "Exit":
        running = False
        print("Thanks for playing!")
        continue
    
    if myChoice not in options:
        print("Invalid option, try again.")
        continue

    compChoice = random.choice(options)
    print(f"The computer chose {compChoice}")

    if myChoice == compChoice:
        print("Draw!")
    elif (myChoice == "Rock" and compChoice == "Scissors") or \
         (myChoice == "Paper" and compChoice == "Rock") or \
         (myChoice == "Scissors" and compChoice == "Paper"):
        print("You won!")
    else:
        print("You lost!")

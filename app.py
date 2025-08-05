import random

num = random.randint(1, 100)
print("Guess the number between 1 and 100")

guess = int(input())

guessCount = 1

while guess != num and guessCount <= 10:
    if guess < num:
        print ("Your guess is to low")
        print ("You have ", 10 - guessCount, "guess left")
    elif guess > num:
        print ("Your guess is to high")
        print ("You have ", 10 - guessCount, "guess left")
        
    guessCount += 1
    guess = int(input())

print ("Your guess is correct")





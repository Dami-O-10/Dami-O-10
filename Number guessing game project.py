import random

score = 0
attempts = 0

print("Welcome to the Number Guessing Game!")

mode = input("""There are 4 modes:
             Easy: Range is 1 - 20 - unlimited attempts.
             Medium: Range is 1- 50 - 20 Attempts.
             Hard: Range is 1 - 100 - 10 Attempts.
             Custom: Set your own range, the amount of points taken off, added & Number of Attempts.
             : """)

if mode == "Easy":
    number = random.randint(1,20)
    while True:
        try:
            Guess = int(input("Guess the Number: "))
        except ValueError:
                print("Please put in a valid attempt: ")
                continue
            
        if Guess > number:
            print("Too High!")
            score = score - 1
            attempts = attempts + 1
        elif Guess < number:
            print("Too Low!")
            attempts = attempts + 1
            score = score - 1
        elif Guess == number:
            print("Right on the Mon$y!")
            attempts = attempts + 1
            score = score + 10

            print("Your score is: ", score)
            print("You tried: ", attempts, " times.")
            break

elif mode == "Medium":
    number = random.randint(1,50)
    while attempts < 20:
        try:
            Guess = int(input("Guess the Number: "))
        except ValueError:
            print("Please Put in a valid attempt: ")
            continue

        if Guess > number:
            print("Too High!")
            score = score - 3
            attempts = attempts + 1
        elif Guess < number:
            print("Too Low!")
            attempts = attempts + 1
            score = score - 3
        elif Guess == number:
            print("Right on the Mon$y!")
            attempts = attempts + 1
            score = score + 30

            print("Your score is: ", score)
            print("You tried: ", attempts, " times.")
            break

elif mode == "Hard":
    number = random.randint(1,50)
    while attempts < 10:
        try:
            Guess = int(input("Guess the Number: "))
        except ValueError:
            print("Please Put in a valid attempt: ")
            continue

        if Guess > number:
            print("Too High!")
            score = score - 5
            attempts = attempts + 1
        elif Guess < number:
            print("Too Low!")
            attempts = attempts + 1
            score = score - 5
        elif Guess == number:
            print("Right on the Mon$y!")
            attempts = attempts + 1
            score = score + 50

            print("Your score is: ", score)
            print("You tried: ", attempts, " times.")
            break

elif mode == "Custom":
    minrange = int(input("Enter your Minimum Range: "))
    maxrange = int(input("Enter your Maximum Range: "))
    scoreminus = int(input("How many points would you like to take off for every incorrect guess? "))
    scoreplus = int(input("How many points would you like to add when the guess is correct? "))
    number = random.randint(minrange,maxrange)
    numattempts = int(input("How many attempts do you want? "))
    while attempts < numattempts:
        try:
            Guess = int(input("Guess the Number: "))
        except ValueError:
            print("Please Put in a valid attempt: ")
            continue

        if Guess > number:
            print("Too High!")
            score = score - scoreminus
            attempts = attempts + 1
        elif Guess < number:
            print("Too Low!")
            attempts = attempts + 1
            score = score - scoreminus
        elif Guess == number:
            print("Right on the Mon$y!")
            attempts = attempts + 1
            score = score + scoreplus

            print("Your score is: ", score)
            print("You tried: ", attempts, " times.")
            break
            
    
            

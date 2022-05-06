import random as rand

print("Welcome To The Best Number Guessing Game On The Internet!")

while True:
    guessedNumber = input("Please Guess A Number_")
    secretNumber = rand.randint(1, 5)

    if int(guessedNumber) != secretNumber:
        print(f"sorry,😅 The correct number is {secretNumber}")
        continue
    else:
        print("Congratulations!!")
        quit()
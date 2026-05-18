import random

num = input("Level: ")

answer = random.randint(1, int(num))

while True:
    try:
        guess = int(input("Guess: "))
        if guess < answer:
            print("Too small!")
        elif guess > answer:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass
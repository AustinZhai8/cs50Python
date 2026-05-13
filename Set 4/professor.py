import random


def main():
    Level = get_level()
    questions = 10
    score = 0
    while questions > 0:
        x = generate_integer(Level)
        y = generate_integer(Level)
        lives = 3
        while lives >= 0:
            if lives == 0:
                print(f"{x} + {y} = {x + y}")
                break
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == x + y:
                    score += 1
                    break
                else:
                    print("EEE")
                    lives -= 1
            except ValueError:
                print("EEE")
                lives -= 1
        questions -= 1
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1 or level > 3:
                continue
            else:
                break
        except ValueError:
            pass
    return level


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
from datetime import date
import inflect
p = inflect.engine()

def main():
    try:
        birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
        today = date.today()
        birthdate = date.fromisoformat(birthdate)
        time = abs(today - birthdate)
        time = time.days * 24 * 60
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
    word = p.number_to_words(time)
    print(word.capitalize)


if __name__ == "__main__":
    main()
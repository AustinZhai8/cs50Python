def main():
    time = input("What time is it? ")
    decimal_time = convert(time)

    if 7 <= decimal_time <= 8:
        print("breakfast time")
    elif 12 <= decimal_time <= 13:
        print("lunch time")
    elif 18 <= decimal_time <= 19:
        print("dinner time")


def convert(time):
    hour, minute = time.split(":")
    hour = int(hour)
    minute = float(minute)
    decimal_time = hour + minute / 60
    return decimal_time




if __name__ == "__main__":
    main()
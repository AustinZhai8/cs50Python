months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")

    try:
        month, day, year = date.split("/")
        month = int(month)
        day = int(day)
        year = int(year)
        print(f"{year}-{month:02}-{day:02}")
        break

    except ValueError:
        pass

    try:
        dayMonth, year = date.split(",")
        month, day = dayMonth.split()
        year = year.strip()

        day = int(day)
        year = int(year)

        numMonth = months.index(month) + 1

        print(f"{year}-{numMonth:02}-{day:02}")
        break

    except (ValueError, IndexError):
        pass
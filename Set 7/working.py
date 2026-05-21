import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Pattern: H:MM AM/PM to H:MM AM/PM or H AM/PM to H AM/PM, etc.
    pattern = r"^(\d{1,2})(?::(\d{2}))?\s(AM|PM)\sto\s(\d{1,2})(?::(\d{2}))?\s(AM|PM)$"
    match = re.match(pattern, s)
    
    if not match:
        raise ValueError("Invalid format")
    
    hour1 = int(match.group(1))
    minute1 = int(match.group(2)) if match.group(2) else 0
    period1 = match.group(3)
    
    hour2 = int(match.group(4))
    minute2 = int(match.group(5)) if match.group(5) else 0
    period2 = match.group(6)
    
    # Validate hours and minutes
    if hour1 < 1 or hour1 > 12 or minute1 < 0 or minute1 > 59:
        raise ValueError("Invalid time")
    if hour2 < 1 or hour2 > 12 or minute2 < 0 or minute2 > 59:
        raise ValueError("Invalid time")
    
    # Convert to 24-hour format
    def to_24hour(hour, minute, period):
        if period == "AM":
            if hour == 12:
                hour = 0
        else:  # PM
            if hour != 12:
                hour += 12
        return f"{hour}:{minute:02d}"
    
    time1_24 = to_24hour(hour1, minute1, period1)
    time2_24 = to_24hour(hour2, minute2, period2)
    
    return f"{time1_24} to {time2_24}"




if __name__ == "__main__":
    main()
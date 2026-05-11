while True:
    try:
        fuel = input("Fraction: ")
        x, y = fuel.split("/")
        x = int(x)
        y = int(y)
        
        if x > y:
            continue
        
        percentage = (x / y) * 100
        
        if percentage <= 1:
            print("E")
        elif percentage >= 99:
            print("F")
        else:
            print(f"{percentage}%")
        
        break
    except (ValueError, ZeroDivisionError):
        continue
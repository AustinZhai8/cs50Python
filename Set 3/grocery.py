groceryList = {}

while True:
    try:
        item = input("").upper()
        if item in groceryList:
            groceryList[item] += 1
        else:
            groceryList[item] = 1
    
    except (EOFError):
        sorted_dict = dict(sorted(groceryList.items()))
        for key, value in sorted_dict.items():
            print(f"{value} {key}")
        
        break
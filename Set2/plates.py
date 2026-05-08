def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    isValid = True
    seenDigits = False
    
    if len (s) < 2 or len(s) > 6:
        isValid = False
    elif not s[0].isalpha() or not s[1].isalpha():
        isValid = False
    elif s[-1].isalpha():
        isValid = False
    for i in s: 
        if i in [".", " ", "!", "?"]:
            isValid = False
    for i in range(len(s)):
        if s[i] =="0" and not seenDigits:
            isValid = False
        if s[i].isdigit():
            seenDigits = True
    return isValid
    

main()
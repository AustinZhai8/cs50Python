input = input("Input: ")

for i in input:
    if i in ["a", "e", "i", "o", "u"]:
        input = input.replace(i, "")
print("Output:", input)
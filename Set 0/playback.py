input = input("Enter a prompt: ")
newInput = ""
for i in input:
    if (i == " "):
        i = "..."
    newInput += i
print(newInput)
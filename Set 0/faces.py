def convert (text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

text = input("Enter a prompt: ")
print(convert(text))
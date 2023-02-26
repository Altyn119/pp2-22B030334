import re
text = input("Enter a string: ")
x = re.sub(r"(\w)([A-Z])", r"\1 \2", text)

print(x)
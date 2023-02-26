import re
text = input("Enter a string: ")
print(re.findall('[A-Z][^A-Z]*', text))
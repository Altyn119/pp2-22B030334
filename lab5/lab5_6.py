import re

txt = str(input("Enter a string: "))
x = re.sub('[ ,.]', ":", txt)
print(x)
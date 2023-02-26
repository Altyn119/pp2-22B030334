import re


def checka(text):
    begin = "^a(b{3})$"
    if re.search(begin, text):
        return ("Yes")
    else:
        return ("No")


print(checka('abbb'))
print(checka('ass'))

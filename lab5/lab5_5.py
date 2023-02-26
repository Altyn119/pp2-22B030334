import re

def chekupper(text):
        symbols = 'a.*?b$'
        if re.search(symbols, text):
            return 'Yes'
        else:
            return ('No')

print(chekupper("accddbbjjjb"))

import re

def chekupper(text):
        symbols = '^[A-Z]+[A-Z]+$'
        if re.search(symbols, text):
            return 'Yes'
        else:
            return ('No')

print(chekupper("AaBbGg"))

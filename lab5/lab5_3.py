import re

def cheklouer(text):
        symbols = '^[a-z]+_[a-z]+$'
        if re.search(symbols, text):
            return 'Yes'
        else:
            return ('No')

print(cheklouer("aab_cbbbc"))

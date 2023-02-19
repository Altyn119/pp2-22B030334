import math

a = int(input())
print((a * math.pi) / 180)

# 2
h = int(input())
a = int(input())
b = int(input())
print(((a + b) * h) / 2)

# 3
n = int(input())
l = int(input())
d = 180 / n
c = (l * l * n) / (4 * int(math.tan(d)))
print(c)

# 4
a = int(input())
b = int(input())
print(a * b)

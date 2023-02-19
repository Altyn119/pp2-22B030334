# 1
import datetime
a = datetime.datetime.today()
print(a)

print(a + datetime.timedelta(days=-5))

#2
x = datetime.datetime.today()
print(x + datetime.timedelta(days=-1))
print(x)
print(x + datetime.timedelta(days=1))

#3
withoutmictosec = datetime.datetime.today().replace(microsecond=0)
print(withoutmictosec)

#4
'''
a = datetime.datetime.today()
b = a + datetime.timedelta(days=-1)
print((b - a).microseconds)
'''
y, m, d = int(input()), int(input()), int(input())
y2, m2, d2 = int(input()), int(input()), int(input())
first = datetime(y, m, d)
second = datetime(y2, m2, d2)
print((second - first).total_seconds)
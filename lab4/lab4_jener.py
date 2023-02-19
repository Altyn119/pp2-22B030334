# 1
def nsqrt(N):
    for i in range(N):
        yield i ** 2


# 2
'''n = int(input())
for i in range(0, n+1, 2):
  if i < n - 1:
    print(i, end = ',' )
  else:
    print(i)'''


def even():
    for i in range(0, n + 1, 2):
        yield i


n = int(input())
res = []
for x in even():
    res.append(str(x))
print(",".join(res))


# 3
def thirdfour():
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


n = int(input())
for x in thirdfour():
    print(x)


# 4
def absqrt():
    for i in range(a, b + 1):
        yield i ** 2


a = int(input())
b = int(input())
for x in absqrt():
    print(x)

#5
def rev():
    for i in range(n, -1, -1):
        yield i
n = int(input())
for x in rev():
    print(x)


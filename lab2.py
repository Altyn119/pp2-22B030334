# list
fruits = ['apple', 'banana', 'cherry']
print(fruits[1])

fruits = ['apple', 'banana', 'cherry']
fruits[0] = 'kiwi'

fruits = ['kiwi', 'banana', 'cherry']
fruits.append('orange')

fruits = ['kiwi', 'banana', 'cherry']
fruits.insert(1, 'lemon')

fruits = ['kiwi', 'banana', 'cherry']
fruits.remove("banana")

fruits = ['kiwi', 'banana', 'cherry']
print(fruits[-1])

fruits = ['kiwi', 'banana', 'cherry', 'kiwi', 'lemon', 'mango']
print(fruits[2:5])

fruits = ['kiwi', 'banana', 'cherry']
print(len(fruits))

# turples
fruits = ['kiwi', 'banana', 'cherry']
print(fruits[0])

fruits = ['kiwi', 'banana', 'cherry']
print(len(fruits))

fruits = ['kiwi', 'banana', 'cherry']
print(len(fruits))

fruits = ['kiwi', 'banana', 'cherry', 'kiwi', 'lemon', 'mango']
print(fruits[2:5])

# sets
fruits = {'kiwi', 'banana', 'cherry', 'kiwi', 'lemon', 'mango'}
if "kiwi" in fruits:
    print("Yes, kiwi is a fruit")

fruits1 = {'kiwi', 'banana', 'cherry'}
fruits1.add("asdfg")

asdf = {'asd', 'cvbn', 'uiop'}
asdfg = {'vbnm', 'vbnm', 'qwer'}
asdf.update("asdfg")

asdf = {'kiwi', 'banana', 'cherry'}
asdf.remove('banana')

asdf = {'kiwi', 'banana', 'cherry'}
asdf.discard('banana')

# dicts
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964}
print(car.get("model"))

car["year"] = 2020
print(car)

car["color"] = "red"
print(car)

car.pop("model")
print(car)

car.clear()
print(car)


# while loops
i = 1
while i < 6:
    print(i)
    i += 1

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")


# for loops

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

for x in range(0, 6):
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)
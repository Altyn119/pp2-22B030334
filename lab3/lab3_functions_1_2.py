# 1
def gramblabla(grams):
    ounces = 28.3495231 * grams
    return ounces


grams = int(input())
print(gramblabla(grams))


# 2
def temprat(f):
    c = (5 / 9) * (f - 32)
    return c


fff = int(input())
print(temprat(fff))


# 4
def isPrime(nums):
    for i in nums:
        if nums[i] == 1 or nums[i] == 2 or nums[i] == 3:
            return True
        elif nums[i] % 2 == 0:
            return False
        for n in range(2, len(nums)):
            if nums[i] % n == 0:
                return False
        return True


nums = list(map(int, input().split()))
if isPrime(nums) == True:
    print(nums)


# 5
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


permut = str(input())
print(factorial(len(permut)))


# 6
def reverse(w):
    rev = w.split()
    return ' '.join(reversed(rev))


w = str(input())
print(reverse(w))


# 7
# 7
def has_33(nums):
    return any(nums[i + 1] == nums[i] == 3 for i in range(len(nums) - 1))


nums = list(map(int, input().split()))
print(has_33(nums))


# 8
# 8
def spy_game(nums1):
    a = ''.join(nums1)
    for i in nums1:
        if '007' in a:
            return True
    return False


nums1 = list(map(str, input().split()))
print(spy_game(nums1))

# 9
import math


def volume(r):  # V = 4pir^3/3
    vol = (4 * math.pi * r ** 3) / 3
    return vol


r = float(input())
print(volume(r))


# 10
def unique_list(l):
    empty = []
    for a in l:
        if a not in empty:
            empty.append(a)
    return empty


list1 = list(map(int, input().split()))
print(unique_list(list1))


# 11
# 11
def palindrome(w):
    if w == w[::-1]:
        return "Yes, it is palindrome"
    else:
        return "Not palindrome"


w = str(input())
print(palindrome(w))


# 12
def histogram(list):
    for i in range(0, len(list)):
        print('*' * list[i])
    return


list2 = list(map(int, input().split()))
print(histogram(list2))

# 13
import random

number = random.randrange(1, 20)
cnt = 1
name = str(input("Hello! What is your name?\n"))
print('Well', name, "I am thinking of a number between 1 and 20. Take a guess.", sep=", ")
UserNum = int(input())

while UserNum != number:
    if UserNum > number:
        print("Your guess is too high.")
        cnt += 1
    elif UserNum < number:
        print("Your guess is too low.")
        cnt += 1
    UserNum = int(input("Take a guess.\n"))
print("Good job,", name, "You guessed my number in", cnt, "guesses!")


# function 2

def single_movie(movies):
    for m in movies:
        if m["name"] == movies and m["imdb"] > 5.5:
            return True
        elif m["name"] == movies and m["imdb"] < 5.5:
            return "Sorry, imdb less than 5.5"


def above_5dot5(movies):
    movies_above = []
    for m in movies:
        if m["imdb"] > 5.5:
            movies_above.append(m["name"])
    return movies_above


above_5dot5(movies)


def m_category(category):
    m_category = []
    for m in movies:
        if m["category"] == category:
            m_category.append(m["name"])
    return m_category


thriller_movies = m_category("Thriller")
print(thriller_movies)


def movies_average_score(movies_list):
    movies_scores = []
    for m in movies_list:
        score = m["imdb"]
        movies_scores.append(score)
    average_score = sum(movies_scores) / len(movies_scores)
    return average_score


average = movies_average_score(movies)
print(average)

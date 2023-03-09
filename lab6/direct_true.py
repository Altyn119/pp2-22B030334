# 1
import os

p = os.listdir("c:\\Users\\Windous\\Onedrive\\pp2-B30334")
for i in p:
    if os.path.isdir(i):
        print(i)
for i in p:
    if os.path.isdir(i) or os.path.isfile(i):
        print(i)
for i in p:
    if os.path.isfile(i):
        print(i)

# 2
import os

p = os.listdir("c:\\Users\\Windous\\Onedrive\\pp2-B30334")

print('Exists:', os.access(__file__, os.F_OK))
print('Readable:', os.access(__file__, os.R_OK))
print('Writable:', os.access(__file__, os.W_OK))
print('Executable:', os.access(__file__, os.X_OK))

# 3
import os

p = ("\\Users\\Windous\\Onedrive\\pp2-B30334")
if os.path.exists(p):
    print("file and dir portions of the path")
    print(os.path.basename(p))
    print(os.path.dirname(p))
else:
    print("pass doesnt exist!")

# 4
f = open("c:\\Users\\Windous\\Onedrive\\pp2-B30334lab6\\dir_and_files\\sometext.txt")
cnt = 0
for lines in f:
    cnt += 1
print("files has {} lines".format(cnt))

# 5
f = open("c:\\Users\\Windous\\Onedrive\\pp2-B30334\\lab6\\dir_and_files\\iwrotelisthere.txt", "a")
a = ["i", "wrote", "some", "stuff"]
for i in a:
    f.write(i)

# 6
f1 = open("icopiedfromhere.txt", "r")
f2 = open("tohere.txt", "w")
for line in f1:
    f2.write(line)

# 7
f1 = open("icopiedfromhere.txt", "r")
f2 = open("tohere.txt", "w")
for line in f1:
    f2.write(line)

# 8
import os

p = ("c:\\Users\\Windous\\Onedrive\\pp2-B30334\\lab6\dir_and_files\\thisfieiswillbedeleted.txt")
if os.path.exists(p):
    os.remove(p)
else:
    print("this file doesnt exist")

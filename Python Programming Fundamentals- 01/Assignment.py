#Sum all the odd numbers from 0 to 100 and print it to the screen

num = 100
s = 0
i = 0
while i < num:
    if i % 2 != 0:
        s += i
    i += 1
print(s)

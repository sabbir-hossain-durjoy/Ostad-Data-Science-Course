original = [1, 5, 6, 5, 1, 2, 3]
duplicates = []

for i in range(len(original)):
    if original.count(original[i]) > 1:
        duplicates.append(original[i])

x = set(duplicates)
print(list(x))


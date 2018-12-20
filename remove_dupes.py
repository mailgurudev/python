a = [1, 4, 9, 16, 4, 36, 4, 64, 81, 100]
b = [1, 4, 27, 16, 25, 36, 49, 64, 99, 101]
for i in a:
    if i not in b :
        b.append(i)
print(b)
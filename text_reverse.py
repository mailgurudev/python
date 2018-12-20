string = input("Enter your statement")
result = string.split(" ")
print(result)
new_result = []
for i in reversed(result):
    new_result.append(i)

final_result = " ".join(new_result)
print(final_result)



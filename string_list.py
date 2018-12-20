word = input(str("Enter a word  "))
new_word = []
for c in word:
     new_word.append(c)
     
print(new_word)
print(list(reversed(new_word)))

if new_word == list(reversed(new_word)):
    print("Its is a pallindrome")
else:
    print("it is not a pallindrome")
import random

option = input("enter what level of password you want : ")

def random_word(passlen):
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    password = "".join(random.sample(s,passlen))
    print(password)

if option == "high":
    random_word(8)
elif option == "medium":
    random_word(6)
else:
    random_word(4)



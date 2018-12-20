number = int(input(" please enter a number "))

listrange = list(range(1,number+1))
divisorlist = []

for num  in listrange:
    if number % num == 0:
        divisorlist.append(num)

print(divisorlist)
print("Welcome to my calulator")
num1 = float(input( "Enter your 1st number : " ))
num2 = float(input ( "Enter your second number : " ))
operator = input ( "Choose + - * / " )

def calculator(operator):
    if operator == "+":
        add = num1+num2
        return add
    elif operator == "*":
        product = num1*num2
        return product
    elif operator == "/":
        quotient = num1/num2
        return quotient
    elif operator == "-":
        difference = num1-num2
        return difference

print(calculator(operator))



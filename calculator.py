num1 = float(input("Enter first number: "))
symbol = input("Enter symbol: ")
num2 = float(input("Enter second number: "))

if(symbol == '+'):
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif(symbol == '-'):
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif(symbol == '*'):
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif(symbol == '/'):
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")

else:
    print(f"{symbol} is not a valid operator.")
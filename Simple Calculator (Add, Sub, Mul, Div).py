print("Simple Calculator (Add, Sub, Mul, Div)")

num1 = float(input("enter the first Number: "))
num2 = float(input("enter the Second Number: "))

print("Select Calculator operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("enter choice (1/2/3/4):  ")

if choice == '1':
    print("result",num1+num2)
elif choice == '2':
    print("result",num1-num2)
elif choice == '3':
    print("result",num1*num2)
elif choice == '4':
    if num2 != 0:
        print("result",num1/num2)
    else: 
        print("error: division by zero")
else:
    print("Invalid Choice")

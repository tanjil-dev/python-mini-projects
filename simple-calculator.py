# Addition
def add(a,b):
    return a+b

# Subtraction
def sub(a,b):
    return a-b

# Multiplication
def mul(a,b):
    return a*b

#Division
def div(a,b):
    if b == 0:
        return "division by 0 is infinity"
    return a/b

print("A Simple Calculator")
print("Please select an operation(+, -, *, /):")
operator = input("Operation: ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if operator == "+":
    print("Result: ", add(num1, num2))
elif operator == "-":
    print("Result: ", sub(num1, num2))
elif operator == "*":
    print("Result: ", mul(num1, num2))
elif operator == "/":
    print("Result: ", div(num1, num2))
else:
    print("Invalid operation!")
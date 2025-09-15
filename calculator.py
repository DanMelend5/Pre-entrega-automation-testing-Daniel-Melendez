input1 = int(input("enter number 1: "))
math_operation = input(("enter operator:  "))
input2 = int(input("enter number 2: "))

def sum(input1, input2):
        return input1 + input2
def substract(input1, input2):
        return input1 - input2
def multiply(input1, input2):
        return input1 * input2
def divide(input1, input2):
        return input1 / input2


if math_operation == "+":
    print(sum(input1, input2))
elif math_operation == "-":
    print(substract(input1, input2))
elif math_operation == "*":
    print(multiply(input1, input2))
elif math_operation == "/":
    try:
        print(divide(input1, input2))
    except:
        print("cannot divide by 0")
else:
    print("invalid")
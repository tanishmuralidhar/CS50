expression = input("Expression: ")

x , y, z = expression.split(" ")
new_x = float(x)
new_z = float(z)

if y == "+":
    result = new_x + new_z
    print(result)

elif y == "-":
    result = new_x - new_z
    print(result)

elif y == "*":
    result = new_x * new_z
    print(result)

elif y == "/":
    result = new_x / new_z
    print(result)

elif y != "+" or "-" or "*" or "/":
    print("Not Valid Operater, Ex) Type + or - or * or /")
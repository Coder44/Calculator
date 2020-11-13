print("Welcome! This is my very first python project and calculator. I hope you enjoy!")
print("Please type in: Add, Subtract, Multiply, Divide")
instruction = str(input("Your choice: "))
if instruction == "Add" or instruction == "add":
    num_1 = int(input("Number: "))
    num_2 = int(input("Number: "))
    add = num_1 + num_2
    print("Result: ", add)
elif instruction == "Subtract" or instruction == "subtract":
    num_1 = int(input("Number: "))
    num_2 = int(input("Number: "))
    subtract = num_1 - num_2
    print("Result: ", subtract)
elif instruction == "Multiply" or instruction == "multiply":
    num_1 = int(input("Number: "))
    num_2 = int(input("Number: "))
    multiply = num_1 * num_2
    print("Result: ", multiply)
elif instruction == "Divide" or instruction == "divide":
    num_1 = int(input("Number: "))
    num_2 = int(input("Number: "))
    division_quotient = num_1 // num_2
    division_remainder = num_1 % num_2
    print("Quotient: ", division_quotient)
    print("Remainder: ", division_remainder)
else:
    print("Please make a correct choice.")
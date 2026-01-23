while True:
    num_a = float(input("\nEnter your first number (or type 0 to exit): "))
    ope = input("What you want to do (+ , - , * , /): ")
    num_b = float(input("Enter your second number: "))

    if ope == "+":
        print("The Addition is =", num_a + num_b)
    elif ope == "-":
        print("The Subtraction is =", num_a - num_b)
    elif ope == "*":
        print("The Multiplication is =", num_a * num_b)
    elif ope == "/" and num_b == 0:
        print("0 can't be in denominator")
    elif ope == "/":
        print("The Division is =", num_a / num_b)
    else:
        print("Something Error Occurred! Use only +, -, *, /")

    # Exit condition
    cont = input("\nDo you want to continue? (yes/no): ")
    if cont.lower() == "no":
        print("Calculator stopped. Goodbye!")
        break
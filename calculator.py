def calculator():
    print("Welcome to the calculator!")
    print("Options:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    try:
        choice = int(input("Choose an operation (1-4): "))

        if choice in [1, 2, 3, 4]:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            if choice == 1:
                print("Result:", num1 + num2)
            elif choice == 2:
                print("Result:", num1 - num2)
            elif choice == 3:
                print("Result:", num1 * num2)
            elif choice == 4:
                if num2 != 0:
                    print("Result:", num1 / num2)
                else:
                    print("Error: Division by zero is not allowed.")
        else:
            print("Invalid choice. Please select a number between 1 and 4.")
    except ValueError:
        print("Error: Please enter valid numbers.")

calculator()

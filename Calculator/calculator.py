
# calculator.py
def run_calculator():
    while True:
        print("Menu for Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Return to the menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\n")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 + num2
            print(f"Result: {result}")
            print("\n")
        elif choice == '2':
            print("\n")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 - num2
            print(f"Result: {result}")
            print("\n")
        elif choice == '3':
            print("\n")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 * num2
            print(f"Result: {result}")
            print("\n")
        elif choice == '4':
            print("\n")
            num1 = float(input("Enter the dividend: "))
            num2 = float(input("Enter the divisor: "))
            print("\n")
            if num2 != 0:
                result = num1 / num2
                print(f"Result: {result}")
                print("\n")
            else:
                print("\n")
                print("Division by zero is not allowed.")
                print("\n")
        elif choice == '5':
            break
        else:
            print("\n")
            print("Invalid choice. Please enter a valid option.")
            print("\n")

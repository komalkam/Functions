class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

if __name__ == "__main__":
    calculator = Calculator()

    while True:
        print("Select an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Goodbye!")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = calculator.add(num1, num2)
            elif choice == '2':
                result = calculator.subtract(num1, num2)
            elif choice == '3':
                result = calculator.multiply(num1, num2)
            elif choice == '4':
                result = calculator.divide(num1, num2)
            else:
                print("Invalid input. Please select a valid operation.")
                continue

            print("Result:", result)

        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except ZeroDivisionError as e:
            print(e)
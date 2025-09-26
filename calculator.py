class SafeCalculator:
    def _init_(self):  
        self.history = []

    def add(self, num1, num2):
        result = num1 + num2
        self.history.append(f"Added {num1} and {num2}. Result = {result}")
        return result

    def subtract(self, num1, num2):
        result = num1 - num2
        self.history.append(f"Subtracted {num2} from {num1}. Result = {result}")
        return result

    def multiply(self, num1, num2):
        result = num1 * num2
        self.history.append(f"Multiplied {num1} and {num2}. Result = {result}")
        return result

    def divide(self, num1, num2):
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        result = num1 / num2
        self.history.append(f"Divided {num1} by {num2}. Result = {result}")
        return result

    def view_history(self):
        if not self.history:
            print("No history yet.")
        else:
            for record in self.history:  # ✅ renamed variable
                print(record)


def main():
    calculator = SafeCalculator()
    while True:
        print("\n--- Safe Calculator ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. View History")
        print("6. Exit")

        choice = input("Enter your choice: ")
        try:
            if choice == "1":
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(f"Result: {calculator.add(num1, num2)}")

            elif choice == "2":
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(f"Result: {calculator.subtract(num1, num2)}")

            elif choice == "3":
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(f"Result: {calculator.multiply(num1, num2)}")

            elif choice == "4":
                num1 = float(input("Enter dividend: "))
                num2 = float(input("Enter divisor: "))
                print(f"Result: {calculator.divide(num1, num2)}")

            elif choice == "5":
                calculator.view_history()

            elif choice == "6":
                print("Exiting Safe Calculator. Goodbye!")
                break

            else:
                print("Invalid choice. Please choose a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except ZeroDivisionError as e:
            print(str(e))


if __name__ == "_main_":  
    main()
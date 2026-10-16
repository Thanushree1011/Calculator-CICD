
def validate_inputs(num1, num2):
    for num in (num1, num2):
        if isinstance(num, bool) or not isinstance(num, int):
            raise ValueError("Inputs must be integers.")


def add(num1, num2):
    validate_inputs(num1, num2)
    if num1 < 0 or num2 < 0:
        raise ValueError("Inputs cannot be negative.")
    return num1 + num2


def subtract(num1, num2):
    validate_inputs(num1, num2)
    if num1 <= 0 or num2 <= 0:
        raise ValueError("Inputs must be positive integers.")
    return num1 - num2


def multiply(num1, num2):
    validate_inputs(num1, num2)
    if num1 <= 0 or num2 <= 0:
        raise ValueError("Inputs must be positive integers.")
    return num1 * num2


def divide(num1, num2):
    validate_inputs(num1, num2)

    if num1 <= 0:
        raise ValueError("First number must be a positive integer.")

    if num2 == 0:
        return "Error: Division by zero is not allowed."

    if num2 < 0:
        raise ValueError("Second number must be a positive integer.")

    return num1 / num2


def main():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Choose an operation (1/2/3/4): ")

    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
    except ValueError:
        print("Please enter valid integers.")
        return

    try:
        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = subtract(num1, num2)
        elif choice == "3":
            result = multiply(num1, num2)
        elif choice == "4":
            result = divide(num1, num2)
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")
            return

        print("Result:", result)

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()

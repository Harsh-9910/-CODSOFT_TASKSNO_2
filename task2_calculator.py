"""Task 2: Simple calculator with basic arithmetic operations."""


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def calculate(a, b, op):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            return "Error: division by zero is not allowed"
        return a / b
    if op == "%":
        if b == 0:
            return "Error: modulus by zero is not allowed"
        return a % b
    if op == "**":
        return a ** b
    return None


def main():
    print("===== SIMPLE CALCULATOR =====")
    print("Operations: +  -  *  /  %  **")
    while True:
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")
        op = input("Choose operation (+, -, *, /, %, **): ").strip()
        result = calculate(a, b, op)
        if result is None:
            print("Invalid operation.")
        else:
            print(f"Result: {a:g} {op} {b:g} = {result:g}" if not isinstance(result, str) else result)
        if input("\nCalculate again? (y/n): ").strip().lower() != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()

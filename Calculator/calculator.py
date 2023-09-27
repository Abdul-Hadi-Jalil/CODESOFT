calculation_history = []


def calculator():
    print('\n'+"Welcome to the digital calculator".center(120,'*'))
    print('\n'+'='*100)
    print("Here you can perform operations like, 'Addition', 'Subtraction', Multiplication', 'Division' etc\n")
    print("Press 1 to see the demonstration on how to use this calculator")
    print("Press 2 to start the calculator if you already know how to use it")
    print("Press 3 to see previous calculations")
    print("Press 0 to exit")
    print('_'*100)

    user_choice = get_choice()

    if user_choice == 0:
        exit(1)
    elif user_choice == 2:
        start_calculator()
    elif user_choice == 1:
        demonstration()
        perform_calculation = input("Do you want to perform calculations now? (yes/no): ").strip().lower()
        if perform_calculation == "yes":
            start_calculator()
        elif perform_calculation == "no":
            print("Thank you for using the calculator.")
        else:
            print("Invalid choice. Exiting...")
    elif user_choice == 3:
        display_history()
    else:
        print("Invalid choice. Exiting...")


def start_calculator():
    while True:
        expression = input("Enter your expression here (or 'quit' to exit): ").strip()

        if expression.lower() == "quit":
            break

        try:
            result = eval(expression)
            print("Result:", result)
            # Store the calculation in history
            calculation_history.append((expression, result))
        except Exception as e:
            print("Error:", e)


def demonstration():
    print("\nCalculator Demonstration:")
    print("Here are some example expressions and their results:")

    examples = [
        ("2 + 3 + 4 + 5", 2 + 3 + 4 + 5),
        ("5 - 1 + 3 + 4", 5 - 1 + 3 + 4),
        ("4 * 6 + 2 - 1",4 * 6 + 2 - 1),
        ("8 / 2", 8 / 2),
    ]

    for example, result in examples:
        print(f"Example: {example} => Result: {result}")


def display_history():
    print("\nCalculation History:")
    for i, (expression, result) in enumerate(calculation_history, start=1):
        print(f"{i}. Expression: {expression} => Result: {result}")


def get_choice():
    while True:
        try:
            user_choice = int(input("Enter your choice here: "))
        except:
            print("Please enter an integer")
        else:
            if 0 <= user_choice <= 3:
                return user_choice


if __name__ == "__main__":
    calculator()
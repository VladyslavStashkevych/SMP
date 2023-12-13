def calculate(num1: float, num2: float, operation) -> float:
    try:
        if operation == "+":
            return num1 + num2
        elif operation == "-":
            return num1 - num2
        elif operation == "*":
            return num1 * num2
        elif operation == "/":
            if num2 != 0:
                return num1 / num2
            else:
                raise ZeroDivisionError()
        elif operation == "^":
            return pow(num1, num2)
        elif operation == "%":
            return num1 % num2
        else:
            raise ValueError()
    except ValueError as err:
        raise err
    except ZeroDivisionError as err:
        raise err


def end_menu(result_history, number_of_zero, res):
    choice = input("1. Do one more calculation \n"
                   "2. Save the result \n"
                   "3. See the history of results \n"
                   "4. Change an accuracy (number of zeros after the decimal point) \n"
                   "5. Exit \n"
                   "  >> ")

    if not choice.isnumeric():
        print("Wrong choice, try again")
        return end_menu(result_history, number_of_zero, res)

    if choice == "1":
        return number_of_zero
    elif choice == "2":
        history.append(res)
    elif choice == "3":
        if isinstance(result_history, list):
            for num in result_history:
                print(format(num, ".{0}f".format(accuracy)))
    elif choice == "4":
        while True:
            number_of_zero = input("enter new zero_number: ")
            if number_of_zero.isnumeric():
                print("This should be a number, try again")
            else:
                break
    elif choice == "5":
        quit()
    else:
        print("Wrong choice, try again.")

    return end_menu(result_history, number_of_zero, res)


history = []
accuracy = 0

while True:
    try:
        number1 = input("enter first number: ")
        number2 = input("enter second number: ")
        operator = input("enter operation to perform: ")
        result = calculate(float(number1), float(number2), operator)

        if result is not None:
            result = float(result)
            print(number1, operator, number2, "=", format(result, ".{0}f".format(accuracy)))

        accuracy = int(end_menu(history, accuracy, result))
    except ValueError:
        print("Value should be a number, try again")
    except ZeroDivisionError:
        print("Number cannot be divided by zero, try again")

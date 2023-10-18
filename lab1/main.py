def calculate(num1, num2, operation):
    num1 = float(num1)
    num2 = float(num2)
    
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
            print("You cannot divide by 0, try again")
            return "error"
    elif operation == "^":
        return pow(num1, num2)
    elif operation == "%":
        return num1 % num2
    else:
        print("wrong operation, try again")
        return "error"


def end_menu(result_history, number_of_zero, res):
    choice = int(input("1. Do one more calculation \n"
                       "2. Save the result \n"
                       "3. See the history of results \n"
                       "4. Change an accuracy (number of zeros after the decimal point) \n"
                       "5. Exit \n"
                       "  >> "))

    if choice == 1:
        return number_of_zero
    elif choice == 2:
        history.append(res)
    elif choice == 3:
        if isinstance(result_history, list):
            for num in result_history:
                print(format(num, ".{0}f".format(accuracy)))
    elif choice == 4:
        number_of_zero = int(input("enter new zero_number: "))
    elif choice == 5:
        return "end"
    else:
        print("Wrong choice, try again.")

    return end_menu(result_history, number_of_zero, res)


history = []
accuracy = 0

while True:
    number1 = float(input("enter first number: "))
    number2 = float(input("enter second number: "))
    operator = input("enter operation to perform: ")

    result = calculate(number1, number2, operator)

    if result != "error":
        result = float(result)
        print(number1, operator, number2, "=", format(result, ".{0}f".format(accuracy)))

    end_result = end_menu(history, accuracy, result)

    if end_result == "end":
        break
    else:
        accuracy = int(end_result)

class Calculator:
    def __init__(self, number1: float, number2: float, operator: object):
        self.number1 = number1
        self.number2 = number2
        self.operator = operator

    def input(self):
        self.number1 = float(input("enter first number: "))
        self.number2 = float(input("enter second number: "))
        self.operator = input("enter operation to perform: ")

        if not self.verify():
            self.input()

    def check_operator(self):
        return (self.operator == "+" or
                self.operator == "-" or
                self.operator == "*" or
                self.operator == "/" or
                self.operator == "^" or
                self.operator == "%")

    def calculate(self) -> float:
        num1 = float(self.number1)
        num2 = float(self.number2)

        if self.operator == "+":
            return num1 + num2
        elif self.operator == "-":
            return num1 - num2
        elif self.operator == "*":
            return num1 * num2
        elif self.operator == "/":
            if num2 != 0:
                return num1 / num2
        elif self.operator == "^":
            return pow(num1, num2)
        elif self.operator == "%":
            return num1 % num2

    def verify(self):
        if not self.check_operator():
            print("you've entered the wrong operator, please try again.")
            return False

        if self.operator == "/" and float(self.number2) == 0:
            print("number cannot be divided by zero, please try again.")
            return False

        return True

    def output(self, result: float):
        print(self.number1, self.operator, self.number2, "=", result)

    def ask_to_repeat(self):
        choice = input("For one more calculation, type Y: ")

        if choice == "Y" or choice == "y":
            self.start()

    def start(self):
        self.input()
        result = self.calculate()
        self.output(result)
        self.ask_to_repeat()

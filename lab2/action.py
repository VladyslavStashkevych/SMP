class Action:
    def __init__(self):
        self.result = 0.0

    def input(self):
        self.result = input()

    def output(self):
        print(self.result)

    def verify(self):
        return self.result is float

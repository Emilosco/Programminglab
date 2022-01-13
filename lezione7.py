class Example:
    def __init__ (self, numbers):
       self.numbers = numbers

    def somma(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        return self.num1 + self.num2

somma1 = Example(None)
print(somma1.somma(2,3))

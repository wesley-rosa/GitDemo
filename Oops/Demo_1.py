class Calculator:
    num = 100

    def __init__(self):
        print("Eu apareço sozinho")

    def getData(self):
        return "Executing method in class"


obj = Calculator()
obj.getData()
print(obj.num)
# print()

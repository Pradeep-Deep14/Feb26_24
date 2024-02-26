class sum:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        return sum(self.num + num2.num)

x = sum(1)
y = sum(2)
z = x + y
print(z.num)
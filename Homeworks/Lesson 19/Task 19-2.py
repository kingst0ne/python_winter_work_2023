'''
Реализуйте класс Fibonacci, который реализует итератор, генерирующий
бесконечную последовательность чисел Фибоначчи


'''

class Fibonacci:
    def __init__(self):
        self.x1 = 0
        self.x2 = 1
    def __iter__(self):
        return self
    def __next__(self):
        self.x1, self.x2 = self.x2,self.x2+self.x1

        return self.x1

a = Fibonacci()

for i in range(15):
    print(next(a), end=' ')
'''
Напечатайте ряд чисел Фибоначчи до введенного номера n:
'''

n = int(input())

fib = [1, 1]
for i in range(2,n+1):
    fib.append(fib[i-2] + fib[i-1])

print(', '.join(str(j) for j in fib))
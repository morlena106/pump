# функция вычисления n-ого члена последовательности фибоначчи
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# 1
n = 1
sum_chet = 0
while fib(n) < 10000000:
    if fib(n) % 2 == 0:
        print(fib(n), end=' ')
        sum_chet += fib(n)
    n += 1
print()

print(f'{n-1} - количество элементов в последовательности')
print(f'{sum_chet} - сумма всех четных элементов')
print(f'{fib(n-2)} ближайший к 10 миллионам член последовательности')

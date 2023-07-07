"""Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных 
чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя 
использовать циклы.
2 2
    4 """
a = int (input("vvedite chislo "))
b = int(input("vvedite vtoroe chislo "))
def summa(m, n):
    if n == 0 & m == 0:
        return 0
    else:
        return m + summa (m, n - 1)
    
print(summa(a, b))
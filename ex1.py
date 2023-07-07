"""Напишите программу, которая на вход принимает два числа A и B, и возводит число А 
в целую степень B с помощью рекурсии.

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 """
a = int (input("vvedite chislo "))
b = int(input("vvedite stepen "))
def stepen(m, n):
    if n == 0:
        return 1
    else:
        return m * stepen (m, n - 1)
    
print(stepen(a, b))
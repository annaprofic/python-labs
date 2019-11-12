from lab5 import recur, recur as rec  # 1
from lab5.recur import fibonacci_rec as fib  # 2
from lab5.recur import factorial_rec as fact  # 3
from lab5.recur import *  # 4

print(rec.fibonacci_rec(2))  # 1
print(rec.factorial_rec(3))  # 1
print(recur.factorial_rec(1))  # 1
print(recur.fibonacci_rec(4))  # 1

print(fib(1))  # 2
print(fact(2))  # 3

print(factorial_rec(2))  # 4
print(fibonacci_rec(1))  # 4

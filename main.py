from task1 import kwargsAcceptFun
from task2 import typeBasedTransformer
from task3 import decorator_1
import random
import time

@decorator_1
def func():
    print("I am ready to Start")
    result = 0
    n =  random.randint(10,751)
    for i in range(n):
        result += (i**2)
        
@decorator_1
def funx(n=2, m=5):
    print("I am ready to do serious stuff")
    max_val = float('-inf')
    n =  random.randint(10,751)
    res = [pow(i,2) for i in range(n)]
    for i in res:
        if i > max_val: 
            max_val = i

if __name__ == "__main__":
    print("Task 1")
    kwargsAcceptFun(Mary='apple', Alex='pizza', Elizabeth='chocolate cake')
    print()
    print("Task 2")
    print(typeBasedTransformer(a=4, b=0.15, c='Hello', d=True, e=[1, 2, 3], f={1: "a", 2: "b", 3:"c"}))
    print()
    print("Task 3")
    func()
    funx()
    func()
    funx()
    func()

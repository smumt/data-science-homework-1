import time
import random

def decorator_1(func):
    def timer(*args, **kwargs):
        start = time.time()  
        result = func(*args, **kwargs)
        end = time.time() 
        execution = end - start 
        print(f"{func.__name__} call executed in {execution:.4f} sec")
        return result
    return timer

@decorator_1
def func():
    print("I am ready to Start")
    result = 0
    n = random.randint(10, 751)
    for i in range(n):
        result += (i ** 2)

@decorator_1
def funx(n=2, m=5):
    print("I am ready to do serious stuff")
    max_val = float('-inf')
    n = random.randint(10, 751)
    res = [pow(i, 2) for i in range(n)]
    for i in res:
        if i > max_val: 
            max_val = i

if __name__ == "__main__": 
    func()
    funx()
    func()
    funx()
    func()

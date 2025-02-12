from typing import Callable #, Dict

def caching_fibonacci() -> Callable[[int], int]:
    cache = {}
    def fibonacci(n: int) -> int:
#        print(cache)  
        for i in range(n+1):
            if i in cache:
                pass
            else: 
                if i == 0:
                   cache[i] = 0
                elif i == 1:   
                   cache[i] = 1
                else:   
                   cache[i] = cache[i-2] + cache[i-1]

        return cache[n]

    return fibonacci

fib = caching_fibonacci()
# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
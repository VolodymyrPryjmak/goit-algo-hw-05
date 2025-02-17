from typing import Callable #, Dict

def caching_fibonacci() -> Callable[[int], int]:
    cache = {}

    def fibonacci(n: int) -> int:
        if n in cache:
           return cache[n]
        
        if n == 0:
           cache[n] = n
           return cache[n]
        elif n == 1:
           cache[n] = n
           return cache[n]
        else:    
            cache[n] = fibonacci(n-2) + fibonacci(n-1)
            return cache[n]  

    return fibonacci

fib = caching_fibonacci()
# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
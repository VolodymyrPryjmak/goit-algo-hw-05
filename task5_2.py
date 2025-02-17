from typing import Callable
import re

def generator_numbers(text: str):
    list_txt_dig = re.findall(r"\d+\.\d+", text) # числа з точкою (float)
    list_txt2 = re.split(" ",text)            
    list_txt2 = [elem for elem in list_txt2 if elem.isdigit()] # числа без точки
    list_txt_dig.extend(list_txt2)
    for el in list_txt_dig:
        yield float(el)    
    return 

def sum_profit(text: str, func: Callable):
    total_income = 0
    for el in func(text):
        total_income += el

    return total_income

text = "Загальний дохід працівника складається з декількох частин: 1000 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.0 доларів."
total_income = sum_profit(text , generator_numbers)
print(f"Загальний дохід: {total_income}")

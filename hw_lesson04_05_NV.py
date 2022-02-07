# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

num_list = [i for i in range(100,1001) if i % 2 == 0]
# print(num_list)

def sum_func(prev_el, el):
    return prev_el * el

print(reduce(sum_func, num_list))

# print(reduce((lambda x,y: x * y), num_list)) # Альтернативное решение

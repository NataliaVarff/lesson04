# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

import sys
from hw_lesson04_01_func import salary_calc

print(sys.argv)

try:
    file, hours, rate, bonus = sys.argv
except ValueError:
    print("Invalid args")
    exit()

print(f"Заработная плата {salary_calc(int(hours), int(rate), float(bonus))} рублей")

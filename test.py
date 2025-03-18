def find_max_even_number(a: list):
 """
 Ищет максимальное чётное значение в списке положительных целых значений, переданном в параметр функции.
 """
 CurrentMax: int = 0
 for b in a:
     if b % 2 == 0:
        CurrentMax = max(b)
 return CurrentMax

max_even = find_max_even_number([2, 12, 85, 0, 6])
# Попробуйте передать в find_max_even_number() другие списки:
# [10, 8, 6, 4, 2]
# [2, 12, 85, 0, 6]
print(f"Максимальное чётное число: {max_even}")
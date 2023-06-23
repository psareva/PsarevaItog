def division (first):
    if first == 0:
        return 0
    if isinstance(first, int) == False and isinstance(first, float) == False:
        return 'Несоответствующий тип данных'
    if first < 0:
        return 'Число должно быть положительным'
    return first**2

print(division(8))
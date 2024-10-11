numbers = []
while True:
    a = input("Введите число (или 'stop' или 'end' для завершения): ").replace(',','.')
    if a.lower() == 'stop' or a.lower() == 'end':
        break
    elif a.isalpha()==True:
        print('Ошибка! Введите число')
    elif a.lower() != 'stop' or a.lower() != 'end':
        number = float(a)
        numbers.append(number)
    else:
        print('Некорректный ввод')

total = sum(numbers)
print(f"Сумма чисел: {total}")
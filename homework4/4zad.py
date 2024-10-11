a = input("Введите первое число: ").replace(',','.')
b = input("Введите второе число: ").replace(',','.')
if a.isalpha()==True or b.isalpha()==True:
    print('ошибка!')
elif a.isnumeric()==True or b.isnumeric()==True:
    a = float(a); b = float(b)
    if a==b or a<1 or b<1:
        print("Целые числа отсутствуют")
    elif a<b and a!=b:
        while a<b and a!=b:
            a+=1
            print(int(a))
    elif b<a and b!=a:
        while b<a and b!=a:
            b+=1
            print(int(b))
else:
    print("Целые числа отсутствуют")

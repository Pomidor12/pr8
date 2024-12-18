a = input("Введите первое число, желательно целое: ").replace(',','.')
b = input("Введите второе число, желательно целое: ").replace(',','.')
if a.isalpha()==True or b.isalpha()==True:
    print('ошибка!')
elif a.isnumeric()==True or b.isnumeric()==True:
    a = float(a); b = float(b)
    if type(a)==float and type(b)==float:
        if a<b and a!=b:
            a=int(a+1); b = int(b)
            while a<b and a!=b-1:
                a+=1
                print(int(a-1))
            print(b-1)
        elif b<a and b!=a:
            b=int(b+1); a = int(a)
            while b<a and b!=a-1:
                b+=1
                print(int(b-1))
            print(a-1)
else:
    print('Это невозможно')

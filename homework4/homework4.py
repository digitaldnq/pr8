while True:
    try:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        break
    except ValueError:
        print("Ошибка: пожалуйста, введите целые числа.")

if a < b:
    for i in range(a+1, b):
        print(i, end=' ')
elif a > b:
    for i in range(b+1, a):
        print(i, end=' ')
else:
    print(a)

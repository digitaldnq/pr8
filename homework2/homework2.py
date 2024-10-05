while True:
    try:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        print(f"Сумма: {a + b}")
    except ValueError:
        print("Пожалуйста, введите корректные целые числа")

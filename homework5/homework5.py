total = 0

while True:
    user_input = input("Введите число или 'stop либо end' для завершения программы: ")
    
    if user_input.lower() in ['stop', 'end']:
        break
    
    try:
        number = float(user_input)
        total += number
    except ValueError:
        print("Необходимо ввести корректное число.")

print(f"Сумма всех введенных чисел равняется: {total}")

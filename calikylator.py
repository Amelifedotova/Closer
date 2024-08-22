# функция получения числа от пользователя
def get_number(prompt):
    while True:
        try:
            number = float(input(prompt)) # проверяем, является ли число дробным
            if number.is_integer():
                return int(number) # проверяем, является ли число целым
            return number
        except ValueError:
            print("Это не число! Пожалуйста, введите число.") # если пользователь ввел не число, то выводим это сообщение


# функция получения математического оператора
def get_operation():
    message = '''
Выберете математическую операцию:

+ : Сложение
- : Вычитание
/ : Деление
* : Умножение
Ваш выбор:
'''

    correct_operations = '+-/*' # строка корректных операций
    # спрашиваем у пользователя, какую операцию он хочет выбрать
    operation = input(message)

    while operation not in correct_operations:
        # выводим выбранную операцию; если операция отсутствует в строке корректных операций, то выводим сообщение об ошибке
        print('Такая операция недоступна. Повторите попытку.')
        operation = input(message)
    return operation


# функция расчета
def calculate(num1, num2, operation):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '/':
        try:
            result = num1 / num2
        except ZeroDivisionError:
            result = "Деление на ноль запрещено"
    elif operation == '*':
        result = num1 * num2
    return result


# главная функция, которая вызывает все функции написанные выше
def main():
    num1 = get_number("Введите первое число: ") # ввод первого числа
    num2 = get_number("Введите второе число: ") # ввод второго числа
    operation = get_operation() # ввод операции
    result = calculate(num1, num2, operation) # результат
    print("Результат:", result) # вывод результата


# вызываем основую функцию main
main()
# после выполнения main() запускаем бесконечный цикл (while True)
while True:
    # спрашиваем пользвователя, желает ли он дальше пользоваться калькулятором
    decision = (input('Продолжить? (да/нет) ')).lower()
    # если да, то опять вызываем main()
    if decision == 'да':
        main()
    # если нет, выходим из бесконечного цикла (break)
    elif decision == 'нет':
        break



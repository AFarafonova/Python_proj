import sys

result = 0
while True:
     line = input("Введите число: ")
     tokens = line.split(" ")
     for token in tokens:
         try:
             number = float(token)
             result += number
         except:
             if token == 'q':
                 print(f"Сумма ваших чисел {result}. Программа завершена")
                 exit(0)
             else:
                 print(f"Сумма ваших чисел {result}. Ошибка ввода", file=sys.stderr)
                 exit(1)
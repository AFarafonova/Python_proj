firm = {'Иванов': 18, 'Петров': 10, 'Сидоров': 10, 'Смирнов': 50}
try:
    file_obj = open("test_3.txt", 'w')
    for last_name, salary in firm.items():
        file_obj.write(last_name + ':' + str(salary) + "\n")
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file_obj.close()
summa = 0
count = 0
persons = []
with open("test_3.txt", "r") as file_obj:
    for line in file_obj:
        print(line, end="")
        tokens = line.split(':')
        if int(tokens[1]) <= 20:
            persons.append(tokens[0])
        summa += int(tokens[1])
        count += 1
result = summa / count
print(f"зарплата ниже 20 тр у: {persons}")
print(f"средняя зарплата: {result}")
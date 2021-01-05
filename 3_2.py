name = input('Введите имя ')
surname = input('Введите фамилию ')
year = int(input('Введите год рождения '))
city = input('Введите город проживания ')
email = input('Введите e-mail')
phone = input('Введите телефон')
def my_func(name, surname, year, city, email, phone):
    print(name, surname, year, city, email, phone)
print(my_func(name, surname, year, city, email, phone))
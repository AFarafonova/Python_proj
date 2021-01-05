def my_func(x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return "Y не может быть 0 "
    except ValueError:
        return "Вводите только числа "


print(my_func(int(input("Enter x = ")), int(input("Enter y = "))))
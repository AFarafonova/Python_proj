class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} машина поехала'

    def stop(self):
        return f'{self.name} машина остановилась'

    def turn_right(self):
        return f'{self.name} машина повернула направо'

    def turn_left(self):
        return f'{self.name} машина повернула налево'

    def show_speed(self):
        return f'Скорость {self.name} составляет {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость {self.name} составляет {self.speed}')

        if self.speed > 60:
            return f'Машина {self.name} превышает скорость'

        else:
            return f'Скорость {self.name} не превышает допустимую'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость {self.name} составляет {self.speed}')

        if self.speed > 40:
            return f'Машина {self.name} превышает скорость'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} из полицейского отделения'
        else:
            return f'{self.name} не из полицейского отделения'


audi = SportCar(100, 'Red', 'Audi', False)
oka = TownCar(30, 'White', 'Oka', False)
lada = WorkCar(70, 'Rose', 'Lada', True)
ford = PoliceCar(110, 'Blue', 'Ford', True)
print(lada.turn_left())
print(f'Когда {oka.turn_right()}, {audi.stop()}')
print(f'{lada.go()} со скоростью {lada.show_speed()}')
print(f'{lada.name} цвета {lada.color}')
print(f'{audi.name} полицейская машина? {audi.is_police}')
print(f'{lada.name} полицейская машина? {lada.is_police}')
print(audi.show_speed())
print(oka.show_speed())
print(ford.police())
print(ford.show_speed())
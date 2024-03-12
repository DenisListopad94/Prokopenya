"""
2.	Создать базовый класс «Грузоперевозчик» и производные классы «Самолет», «Поезд», «Автомобиль».
Определить время и стоимость перевозки для указанных городов и расстояний
"""


class CargoCarrier:
    def __init__(self, rate=0, speed=0, distance=0):
        self.rate = rate
        self.speed = speed
        self.distance = distance

    def compute_time(self):
        print(f'Время затраченное на транспортировку - {round(self.distance / self.speed, 2)}ч ')

    def compute_cost(self):
        print(
            f'Стоимость транспортировки: тариф {self.rate} руб/км, расстояние {self.distance}, стоимость - {self.rate * self.distance}руб')


class Plain(CargoCarrier):
    def __init__(self, rate, speed):
        super().__init__(rate=rate, speed=speed)

    def compute_cost(self):
        city1 = input("Введите город отправления ")
        city2 = input("Введите город назначения ")
        distance = float(input("Введите расстояние между городами "))
        self.distance = distance
        print(f'Средняя скорость самолета {self.speed} км/ч')
        print(f'Стоимость транспортировки между городами {city1} - {city2}: '
              f'тариф {self.rate} руб/км, расстояние {self.distance}, стоимость - {self.rate * self.distance}руб')


plain = Plain(25, 850)
plain.compute_cost()
plain.compute_time()


class Train(CargoCarrier):
    def __init__(self, rate, speed):
        super().__init__(rate=rate, speed=speed)

    def compute_cost(self):
        city1 = input("Введите город отправления ")
        city2 = input("Введите город назначения ")
        distance = float(input("Введите расстояние между городами "))
        self.distance = distance
        print(f'Средняя скорость поезда {self.speed} км/ч')
        print(f'Стоимость транспортировки между городами {city1} - {city2}: '
              f'тариф {self.rate} руб/км, расстояние {self.distance}, стоимость - {self.rate * self.distance}руб')


# train = Train(15, 111)
# train.compute_cost()
# train.compute_time()

class Car(CargoCarrier):
    def __init__(self, rate, speed):
        super().__init__(rate=rate, speed=speed)

    def compute_cost(self):
        city1 = input("Введите город отправления ")
        city2 = input("Введите город назначения ")
        distance = float(input("Введите расстояние между городами "))
        self.distance = distance
        print(f'Средняя скорость автомобиля {self.speed} км/ч')
        print(f'Стоимость транспортировки между городами {city1} - {city2}: '
              f'тариф {self.rate} руб/км, расстояние {self.distance}, стоимость - {self.rate * self.distance}руб')

# car = Car(15, 111)
# car.compute_cost()
# car.compute_time()

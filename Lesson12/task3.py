"""
3.	Создать класс «Живое». Определить наследуемые классы – «лиса», «кролик» и «растение». Лиса ест кролика.
Кролик ест растения. Растение поглощает солнечный свет. Представитель каждого класса может умереть,
если достигнет определенного возраста или для него не будет еды. Напишите виртуальные методы поедания и
определения состояния живого существа (живой или нет, в зависимости от достижения предельного возраста и
наличия еды (входной параметр)).
"""
import random


class Alive:
    def __init__(self, age=random.randint(1, 10)):
        self.age = age

    def __str__(self):
        return f'{self.__class__.__name__}'

    def eat(self, food=None):
        if food:
            print(f'{self.__str__()}, съел {food}')
        else:
            print(f'{self.__str__()}, остался голодным, съел - {food}')

    def get_sate(self):
        if self.age == 10:
            print(f'Не живой')
        else:
            print(f'Живой')


class Fox(Alive):
    def __init__(self, age=random.randint(1, 8)):
        # средняя продол-ть жизни лисы 7 лет
        super().__init__()
        self.age = age

    def get_sate(self):
        if self.age > 7:
            print(f'Животное {self.__str__()} - Не живая возраст - {self.age}')
        else:
            print(f'Животное {self.__str__()} -  живая, возраст - {self.age}')


# fox = Fox()
# fox.get_sate()
# fox.eat()


class Rabbit(Alive):
    def __init__(self, age=random.randint(1, 10)):
        # средняя продол-ть жизни кролика 9 лет
        self.age = age
        super().__init__()

    def get_sate(self):
        if self.age > 9:
            print(f'{self.__str__()} - Не живой возраст - {self.age}')
        else:
            print(f'{self.__str__()} - живой, возраст - {self.age}')


# rabbit = Rabbit()
# rabbit.get_sate()
# rabbit.eat('Морковка')


class Plant(Alive):
    def __init__(self, age=random.randint(1, 6)):
        # средняя продол-ть жизни растения (взято рандомно)
        self.age = age
        super().__init__()

    def get_sate(self):
        if self.age > 5:
            print(f'{self.__str__()} - Не живой возраст - {self.age}')
        else:
            print(f'{self.__str__()} - живой, возраст - {self.age}')

    def eat(self, food=None):
        if food:
            print(f'{self.__str__()}, поглотил {food}')
        else:
            print(f'{self.__str__()}, остался без солнечного света')


plant = Plant()
plant.get_sate()
plant.eat()

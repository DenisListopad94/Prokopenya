"""
4.	Разработайте программу, имитирующую работу транспортного агентства.
Транспортное агентство имеет сеть филиалов в нескольких городах.
Транспортировка грузов осуществляется между этими городами тремя видами транспорта: автомобильным, железнодорожным и
воздушным. Любой вид транспортировки имеет стоимость единицы веса на единицу пути и скорость доставки.
Воздушный транспорт можно использовать только между крупными городами, этот вид самый скоростной и самый дорогой.
Железнодорожный транспорт можно использовать между крупными и средними городами, этот вид самый дешевый.
Автомобильный транспорт можно использовать между любыми городами. Заказчики через случайные промежутки времени
обращаются в один из филиалов транспортного агентства с заказом на перевозку определенной массы груза и возможным
пожеланием о скорости/цене доставки. Транспортное агентство организует отправку грузов одним из видов
транспорта с учетом пожеланий клиента.

-Доход транспортного агентства, в том числе с разбивкой по видам транспорта и городам.
-Среднее время доставки груза, в том числе с разбивкой по видам транспорта и городам.
-Список исполняемых заказов с возможность сортировки по городам, видам транспорта, стоимости перевозки.
"""


class Transit:
    def __init__(self, speed_of_transport={}, pricing={}, cities_and_citizens={}):
        self.speed_of_transport = speed_of_transport
        self.pricing = pricing
        self.cities_and_citizens = cities_and_citizens

    def menu(self):
        answer = None
        while answer != 4:
            print('\nВыберите действие:\n'
                  '1 - Посмотреть Доступные города для доставки грузов\n'
                  '2 - Посмотреть расценки\n'
                  '3 - Сделать заказ на транспортировку груза\n'
                  '4 - Выход\n')
            action = int(input())
            if action == 1:
                self.get_cities()
            elif action == 2:
                self.get_price()
            elif action == 3:
                self.get_order()
            elif action == 4:
                break

    def get_cities(self):
        if self.cities_and_citizens:
            print(f'##################################################################################################')
            print(f'Обращаем ваше внимание, доставка самолетом осуществляется в города с населением больше 1млн.чел\n'
                  f'Доставка поездом осуществляется в города с населением от 100тыс.чел и больше\n'
                  f'Автомобильный транспорт можно использовать между любыми городами')
            print(f'##################################################################################################')
            print(f'Доступные города: ')
            for city in self.cities_and_citizens.keys():
                print(f'{city}')
        else:
            print(f'В данный момент агентво не осуществляет грузоперевозки')

    def get_price(self):
        if self.pricing:
            print("Цена доставки в рублях за 1кг/км:")
            for transport, price in self.pricing.items():
                print(f'{transport} - {price}')

    def get_bill_by_car(self, city_one, citi_two):
        distance = float(input(f"Введите расстояние от {city_one} до {citi_two} в км\n"))
        weight = float(input(f"Введите вес груза в кг\n"))
        return (f'Итоговая цена для доставки между {city_one} до {citi_two}:\n'
                f'{distance * self.pricing['Автомобиль'] * weight} руб')

    def get_bill_by_train(self, city_one, citi_two):
        distance = float(input(f"Введите расстояние от {city_one} до {citi_two} в км\n"))
        weight = float(input(f"Введите вес груза в кг\n"))
        return (f'Итоговая цена для доставки между {city_one} до {citi_two}:\n'
                f'{distance * self.pricing['Поезд'] * weight} руб')

    def get_bill_by_plain(self, city_one, citi_two):
        distance = float(input(f"Введите расстояние от {city_one} до {citi_two} в км\n"))
        weight = float(input(f"Введите вес груза в кг\n"))
        return (f'Итоговая цена для доставки между {city_one} до {citi_two}:\n'
                f'{distance * self.pricing['Самолет'] * weight} руб')

    def get_order(self):
        self.get_cities()
        city1 = input("Введите город отправления ")
        city2 = input("Введите город назначения ")
        if city1 not in self.cities_and_citizens.keys() or city2 not in self.cities_and_citizens.keys():
            print(f'Маршрут невозможен, 1 из введенных вами город отсутствует в списке доступных')
        elif 0 < self.cities_and_citizens[city1] <= 150000 or 0 < self.cities_and_citizens[city2] <= 150000:
            print(f'Доставка по маршруту из города {city1} в город {city2} доступна только автомобилем\n'
                  f'т.к. население в одном из городов меньше 100 тыс.')
            print(self.get_bill_by_car(city1, city2))

        elif 300000 < self.cities_and_citizens[city1] < 999999 or 300000 < self.cities_and_citizens[city2] < 999999:
            print(f'Доставка по маршруту из города {city1} в город {city2} доступна автомобилем или поездом\n'
                  f'т.к. население в одном из городов меньше 100 тыс.')
            choose_transport = int(input("Выберите транспорт 1- автомобиль, 2 - поезд "))
            if choose_transport == 1:
                print(self.get_bill_by_car(city1, city2))
            else:
                print(self.get_bill_by_train(city1, city2))

        elif self.cities_and_citizens[city1] and self.cities_and_citizens[city2] > 1000000:
            print(f'Доставка по маршруту из города {city1} в город {city2} доступна любым видом транспорта')
            choose_transport = int(input("Выберите транспорт 1- автомобиль, 2 - поезд, 3 - самолет "))
            if choose_transport == 1:
                print(self.get_bill_by_car(city1, city2))
            elif choose_transport == 2:
                print(self.get_bill_by_train(city1, city2))
            else:
                print(self.get_bill_by_plain(city1, city2))


cities = {'Минск': 2000000, 'Москва': 10000000, 'Пинск': 150000, 'Брест': 342000, 'Ивацевичи': 30000}
cost = {'Автомобиль': 0.15, 'Самолет': 1, 'Поезд': 0.25}
speed = {'Автомобиль': 15, 'Самолет': 1500, 'Поезд': 25}


obj = Transit(speed, cost, cities)
obj.menu()



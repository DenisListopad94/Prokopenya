"""
4.	Реализуйте класс MoneyBox, для работы с виртуальной копилкой. Каждая копилка имеет ограниченную вместимость,
которая выражается целым числом – количеством монет(capacity -вместимость), которые можно положить в копилку.
Класс должен поддерживать информацию о количестве монет в копилке, предоставлять возможность добавлять монеты в
копилку и узнавать, можно ли добавить в копилку ещё какое-то количество монет, не превышая ее вместимость.
При создании копилки, число монет в ней равно 0.
Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True.
"""


class MoneyBox:
    def __init__(self, capacity=100, current_cnt_of_coin=0):
        self.capacity = capacity
        self.current_cnt_of_coin = current_cnt_of_coin

    def state_of_monyebox(self):
        print(f'Текущее состояние копилки (кол-во монет) - {self.current_cnt_of_coin}')

    def can_add(self):
        if self.current_cnt_of_coin <= 100:
            return True
        else:
            return False

    def add(self):
        if self.can_add:
            plus_coins = int(input("Введите кол-во монет которое хотите добавить в копилку "))

            if self.current_cnt_of_coin + plus_coins > 100:
                print(f'Слишком много монет, вместимость копилки - {self.capacity}')
                print(f'Можно добавить только {100 - self.current_cnt_of_coin}')
            else:
                self.current_cnt_of_coin += plus_coins


obj = MoneyBox()
obj.state_of_monyebox()
obj.add()
obj.state_of_monyebox()
obj.add()
obj.state_of_monyebox()



"""
2.	Описать класс, реализующий десятичный счетчик, который может увеличивать или уменьшать свое значение на единицу в
заданном диапазоне. Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями.
Счетчик имеет два метода: увеличения и уменьшения, — и свойство, позволяющее получить его текущее состояние.
Написать программу, демонстрирующую все возможности класса.
"""


class Counter:
    def __init__(self, default=10, range_for_default=1):
        self.default = default
        self.range_for_default = range_for_default

    def increase(self):
        return f'Значение увеличино на {range}, значение счетчика {self.default + self.range_for_default}'

    def decrease(self):
        return f'Значение уменьшено на {range}, значение счетчика {self.default - self.range_for_default}'

    def get_sate(self):
        return f'Текущее состояние счетчика {self.default - self.range_for_default}'

